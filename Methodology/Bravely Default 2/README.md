# Bravely Default II

> Game info

TitleID: `01006DC010326000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `05DE5A7F20BD1532`
- Engine: `Unreal Engine 4.23.0`

> Details

Game is using internal FPS lock, and dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:00000071028DA51C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071028DA520                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071028DA524                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:00000071028DA528                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071028DA52C                 MOV             W3, #0x20
.text:00000071028DA530                 BLR             X8
.text:00000071028DA534                 ADRP            X19, #qword_71072AEE80@PAGE
.text:00000071028DA538                 ADD             X19, X19, #qword_71072AEE80@PAGEOFF
.text:00000071028DA53C                 STP             X21, X0, [X19]
.text:00000071028DA540                 LDR             X8, [X0]
.text:00000071028DA544                 LDR             X8, [X8,#0x58]
.text:00000071028DA548                 BLR             X8
.text:00000071028DA54C                 STR             X0, [X19,#(qword_71072AEE90 - 0x71072AEE80)]
```

So first final address is stored at 0x72AEE90.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102C29D24                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102C29D28                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102C29D2C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102C29D30                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102C29D34                 MOV             W3, WZR
.text:0000007102C29D38                 BLR             X8
.text:0000007102C29D3C                 ADRP            X19, #qword_71073050E0@PAGE
.text:0000007102C29D40                 ADD             X19, X19, #qword_71073050E0@PAGEOFF
.text:0000007102C29D44                 ADRP            X8, #off_7105C879E0@PAGE
.text:0000007102C29D48                 ADD             X8, X8, #off_7105C879E0@PAGEOFF
.text:0000007102C29D4C                 STP             X8, X0, [X19]
.text:0000007102C29D50                 LDR             X8, [X0]
.text:0000007102C29D54                 LDR             X8, [X8,#0x58]
.text:0000007102C29D58                 BLR             X8
.text:0000007102C29D5C                 STR             X0, [X19,#(qword_71073050F0 - 0x71073050E0)]
```
So our second final address is 0x73050F0.

Each of our final address stores pointer that points to two floats. Game is swapping t.MaxFPS between 30 and 0. r.DynamicRes.FrameTimeBudget via config is 32.3.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to one decimal
  -
    type: write
    address: [MAIN, 0x72AEE90, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x73050F0, 0]
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
    address: [MAIN, 0x72AEE90, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x73050F0, 0]
    value_type: float
    value: [30, 30]

```
