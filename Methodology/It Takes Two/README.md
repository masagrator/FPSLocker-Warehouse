# It Takes Two

> Game info

TitleID: `010092A0172E4000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `C4067E8CB3258656`
- Engine: `Unreal Engine 4.26.0`

> Details

Plugin alone can set FPS above 30, but game is using double buffer. We can disable it by finding string `nvn.NumBufferedFrames` stored as UTF-16-LE and changing at least one character to something else before game initializes.

Plus is using dynamic resolution which timing is adjusted per level. We need to tweak it.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007104F6227C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007104F62280                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007104F62284                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007104F62288                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007104F6228C                 LDR             X8, [X8,#0x10]
.text:0000007104F62290                 MOV             W3, #0x20
.text:0000007104F62294                 BLR             X8
.text:0000007104F62298                 ADRP            X19, #qword_710ACCB3C8@PAGE
.text:0000007104F6229C                 ADD             X19, X19, #qword_710ACCB3C8@PAGEOFF
.text:0000007104F622A0                 STP             X24, X0, [X19]
.text:0000007104F622A4                 LDR             X8, [X0]
.text:0000007104F622A8                 LDR             X8, [X8,#0x68]
.text:0000007104F622AC                 BLR             X8
.text:0000007104F622B0                 STR             X0, [X19,#(qword_710ACCB3D8 - 0x710ACCB3C8)]
```

So first final address is stored at 0xACCB3D8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710547F704                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:000000710547F708                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:000000710547F70C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:000000710547F710                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710547F714                 LDR             X8, [X8,#0x10]
.text:000000710547F718                 MOV             W3, WZR
.text:000000710547F71C                 BLR             X8
.text:000000710547F720                 ADRP            X19, #qword_710ACF9120@PAGE
.text:000000710547F724                 ADD             X19, X19, #qword_710ACF9120@PAGEOFF
.text:000000710547F728                 ADRP            X8, #off_71094F08A8@PAGE
.text:000000710547F72C                 ADD             X8, X8, #off_71094F08A8@PAGEOFF
.text:000000710547F730                 STP             X8, X0, [X19]
.text:000000710547F734                 LDR             X8, [X0]
.text:000000710547F738                 LDR             X8, [X8,#0x68]
.text:000000710547F73C                 BLR             X8
.text:000000710547F740                 STR             X0, [X19,#(qword_710ACF9130 - 0x710ACF9120)]
```
So our second final address is 0xACF9130.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget by default it's 29, but it's changing depending on level.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = 0.87 * (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0xACCB3D8, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0xACF9130, 0]
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
    address: [MAIN, 0xACCB3D8, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0xACF9130, 0]
    value_type: float
    value: [0, 0]

```
