# Fishing: North Atlantic

> Game info

TitleID: `0100A55019C38000`<br>
Explanation based on:
- Internal version: `1.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `B9DB6040F70BE58F`
- Engine: `Unreal Engine 4.27.2`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 33.33 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710211FD1C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710211FD20                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710211FD24                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710211FD28                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710211FD2C                 LDR             X8, [X8,#0x10]
.text:000000710211FD30                 MOV             W3, #0x20
.text:000000710211FD34                 BLR             X8
.text:000000710211FD38                 ADRP            X19, #qword_71069973B8@PAGE
.text:000000710211FD3C                 ADD             X19, X19, #qword_71069973B8@PAGEOFF
.text:000000710211FD40                 STP             X24, X0, [X19]
.text:000000710211FD44                 LDR             X8, [X0]
.text:000000710211FD48                 LDR             X8, [X8,#0x68]
.text:000000710211FD4C                 BLR             X8
.text:000000710211FD50                 STR             X0, [X19,#(qword_71069973C8 - 0x71069973B8)]
```

So first final address is stored at 0x69973C8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071026483DC                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071026483E0                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071026483E4                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071026483E8                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071026483EC                 LDR             X8, [X8,#0x10]
.text:00000071026483F0                 MOV             W3, WZR
.text:00000071026483F4                 BLR             X8
.text:00000071026483F8                 ADRP            X19, #qword_71069C4C58@PAGE
.text:00000071026483FC                 ADD             X19, X19, #qword_71069C4C58@PAGEOFF
.text:0000007102648400                 ADRP            X8, #off_710554D8B8@PAGE
.text:0000007102648404                 ADD             X8, X8, #off_710554D8B8@PAGEOFF
.text:0000007102648408                 STP             X8, X0, [X19]
.text:000000710264840C                 LDR             X8, [X0]
.text:0000007102648410                 LDR             X8, [X8,#0x68]
.text:0000007102648414                 BLR             X8
.text:0000007102648418                 STR             X0, [X19,#(qword_71069C4C68 - 0x71069C4C58)]
```
So our second final address is 0x69C4C68.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to =2 decimals
  -
    type: write
    address: [MAIN, 0x69973C8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x69C4C68, 0]
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
    address: [MAIN, 0x69973C8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x69C4C68, 0]
    value_type: float
    value: [0, 0]

```