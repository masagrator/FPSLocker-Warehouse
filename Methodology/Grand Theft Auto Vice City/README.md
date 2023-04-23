# Grand Theft Auto: Vice City - Definitive Edition

> Game info

TitleID: `0100182014022000`<br>
Explanation based on:
- Internal version: `1.0.7`, 
- Nintendo version ID: `v7`/`v458752`
- BID: `56EEFA704373BDB3`
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
.text:00000071036E9A78                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071036E9A7C                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071036E9A80                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:00000071036E9A84                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071036E9A88                 MOV             W3, #0x20
.text:00000071036E9A8C                 BLR             X8
.text:00000071036E9A90                 ADRP            X19, #qword_7107565288@PAGE
.text:00000071036E9A94                 ADD             X19, X19, #qword_7107565288@PAGEOFF
.text:00000071036E9A98                 STP             X24, X0, [X19]
.text:00000071036E9A9C                 LDR             X8, [X0]
.text:00000071036E9AA0                 LDR             X8, [X8,#0x68]
.text:00000071036E9AA4                 BLR             X8
.text:00000071036E9AA8                 STR             X0, [X19,#(qword_7107565298 - 0x7107565288)]
```

So first final address is stored at 0x7565298.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007103DADC30                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007103DADC34                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007103DADC38                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103DADC3C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103DADC40                 MOV             W3, WZR
.text:0000007103DADC44                 BLR             X8
.text:0000007103DADC48                 ADRP            X19, #qword_7107589FD0@PAGE
.text:0000007103DADC4C                 ADD             X19, X19, #qword_7107589FD0@PAGEOFF
.text:0000007103DADC50                 ADRP            X8, #off_7105E8A748@PAGE
.text:0000007103DADC54                 ADD             X8, X8, #off_7105E8A748@PAGEOFF
.text:0000007103DADC58                 STP             X8, X0, [X19]
.text:0000007103DADC5C                 LDR             X8, [X0]
.text:0000007103DADC60                 LDR             X8, [X8,#0x68]
.text:0000007103DADC64                 BLR             X8
.text:0000007103DADC68                 STR             X0, [X19,#(qword_7107589FE0 - 0x7107589FD0)]
```
So our second final address is 0x7589FE0.

Each of our final address stores pointer that points to two floats. t.MaxFPS via config is 30. r.DynamicRes.FrameTimeBudget via config is 36.5. Instead we will use a different calculation for each FPS.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to one decimal
  -
    type: write
    address: [MAIN, 0x7565298, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7589FE0, 0]
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
    address: [MAIN, 0x7565298, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7589FE0, 0]
    value_type: float
    value: [30, 30]

```
