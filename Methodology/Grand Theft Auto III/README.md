# Grand Theft Auto III - Definitive Edition

> Game info

TitleID: `0100C3C012718000`<br>
Explanation based on:
- Internal version: `1.0.7`, 
- Nintendo version ID: `v7`/`v458752`
- BID: `2CF52C8DA4468946`
- Engine: `Unreal Engine 4.26.1`

> Details

Game is using internal FPS lock, and dynamic resolution set to 36.5 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

If it has more than 1 xref, we are interested in the one that has description pointer loaded.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710368AFF8                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710368AFFC                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710368B000                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710368B004                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710368B008                 MOV             W3, #0x20
.text:000000710368B00C                 BLR             X8
.text:000000710368B010                 ADRP            X19, #qword_71074FD288@PAGE
.text:000000710368B014                 ADD             X19, X19, #qword_71074FD288@PAGEOFF
.text:000000710368B018                 STP             X24, X0, [X19]
.text:000000710368B01C                 LDR             X8, [X0]
.text:000000710368B020                 LDR             X8, [X8,#0x68]
.text:000000710368B024                 BLR             X8
.text:000000710368B028                 STR             X0, [X19,#(qword_71074FD298 - 0x71074FD288)]
```

So first final address is stored at 0x74FD298.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007103D4F1B0                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007103D4F1B4                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007103D4F1B8                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103D4F1BC                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103D4F1C0                 MOV             W3, WZR
.text:0000007103D4F1C4                 BLR             X8
.text:0000007103D4F1C8                 ADRP            X19, #qword_7107521FD0@PAGE
.text:0000007103D4F1CC                 ADD             X19, X19, #qword_7107521FD0@PAGEOFF
.text:0000007103D4F1D0                 ADRP            X8, #off_7105E2D748@PAGE
.text:0000007103D4F1D4                 ADD             X8, X8, #off_7105E2D748@PAGEOFF
.text:0000007103D4F1D8                 STP             X8, X0, [X19]
.text:0000007103D4F1DC                 LDR             X8, [X0]
.text:0000007103D4F1E0                 LDR             X8, [X8,#0x68]
.text:0000007103D4F1E4                 BLR             X8
.text:0000007103D4F1E8                 STR             X0, [X19,#(qword_7107521FE0 - 0x7107521FD0)]
```
So our second final address is 0x7521FE0.

Each of our final address stores pointer that points to two floats. t.MaxFPS via config is 30. r.DynamicRes.FrameTimeBudget via config is 36.5. Instead we will use a different calculation for each FPS.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to one decimal
  -
    type: write
    address: [MAIN, 0x74FD298, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7521FE0, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # r.DynamicRes.FrameTimeBudget (default value is 36.5)
  -
    type: write
    address: [MAIN, 0x74FD298, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7521FE0, 0]
    value_type: float
    value: [30, 30]

```
