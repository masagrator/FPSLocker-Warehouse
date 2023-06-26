# Sifu

> Game info

TitleID: `01007B5017A12000`<br>
Explanation based on:
- Internal version: `1.13_842`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `C56FA2C9627A26CF`
- Engine: `Unreal Engine 4.26.2`

> Details

Plugin alone can set FPS above 30, but some things downgrades possible FPS. One of it is Dynamic Resolution, so we need to patch it.
Performance improvement from changing it is so small that problably something else also is responsible for worse than expected performance, but I don't know what.
So we will focus only on Dynamic Resolution and finding internal FPS lock. 

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007105975148                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710597514C                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007105975150                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007105975154                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007105975158                 LDR             X8, [X8,#0x10]
.text:000000710597515C                 MOV             W3, #0x20
.text:0000007105975160                 BLR             X8
.text:0000007105975164                 ADRP            X19, #qword_71094CD838@PAGE
.text:0000007105975168                 ADD             X19, X19, #qword_71094CD838@PAGEOFF
.text:000000710597516C                 STP             X26, X0, [X19]
.text:0000007105975170                 LDR             X8, [X0]
.text:0000007105975174                 LDR             X8, [X8,#0x68]
.text:0000007105975178                 BLR             X8
.text:000000710597517C                 STR             X0, [X19,#(qword_71094CD848 - 0x71094CD838)]
```

So first final address is stored at 0x94CD848.

The same way we're searching for 
```
t.MaxFPS
r.VSync
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007105A29BE8                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007105A29BEC                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007105A29BF0                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007105A29BF4                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007105A29BF8                 LDR             X8, [X8,#0x10]
.text:0000007105A29BFC                 MOV             W3, WZR
.text:0000007105A29C00                 BLR             X8
.text:0000007105A29C04                 ADRP            X19, #qword_71094F2848@PAGE
.text:0000007105A29C08                 ADD             X19, X19, #qword_71094F2848@PAGEOFF
.text:0000007105A29C0C                 ADRP            X8, #off_71081B0B48@PAGE
.text:0000007105A29C10                 ADD             X8, X8, #off_71081B0B48@PAGEOFF
.text:0000007105A29C14                 STP             X8, X0, [X19]
.text:0000007105A29C18                 LDR             X8, [X0]
.text:0000007105A29C1C                 LDR             X8, [X8,#0x68]
.text:0000007105A29C20                 BLR             X8
.text:0000007105A29C24                 STR             X0, [X19,#(qword_71094F2858 - 0x71094F2848)]
```
So our second final address is 0x94F2858.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x94CD848, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x94F2858, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # r.DynamicRes.FrameTimeBudget (default value)
  -
    type: write
    address: [MAIN, 0x94CD848, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x94F2858, 0]
    value_type: float
    value: [0, 0]

```
