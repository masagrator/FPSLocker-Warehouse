# HOT WHEELS UNLEASHED

> Game info

TitleID: `0100AA60136D2000`<br>
Explanation based on:
- Internal version: `1.0.13`, 
- Nintendo version ID: `v13`/`v851968`
- BID: `F73C6504D378C38B`
- Engine: `Unreal Engine 4.26.2`

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
.text:0000007103937C88                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007103937C8C                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007103937C90                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007103937C94                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007103937C98                 MOV             W3, #0x20
.text:0000007103937C9C                 BLR             X8
.text:0000007103937CA0                 ADRP            X19, #qword_710978D978@PAGE
.text:0000007103937CA4                 ADD             X19, X19, #qword_710978D978@PAGEOFF
.text:0000007103937CA8                 STP             X24, X0, [X19]
.text:0000007103937CAC                 LDR             X8, [X0]
.text:0000007103937CB0                 LDR             X8, [X8,#0x68]
.text:0000007103937CB4                 BLR             X8
.text:0000007103937CB8                 STR             X0, [X19,#(qword_710978D988 - 0x710978D978)]
```

So first final address is stored at 0x978D988.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007103E78318                 ADRP            X1, #aTMaxfps_0@PAGE ; "t.MaxFPS"
.text:0000007103E7831C                 ADD             X1, X1, #aTMaxfps_0@PAGEOFF ; "t.MaxFPS"
.text:0000007103E78320                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103E78324                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103E78328                 MOV             W3, WZR
.text:0000007103E7832C                 BLR             X8
.text:0000007103E78330                 ADRP            X19, #qword_71097BB4D0@PAGE
.text:0000007103E78334                 ADD             X19, X19, #qword_71097BB4D0@PAGEOFF
.text:0000007103E78338                 ADRP            X8, #off_7107D398A8@PAGE
.text:0000007103E7833C                 ADD             X8, X8, #off_7107D398A8@PAGEOFF
.text:0000007103E78340                 STP             X8, X0, [X19]
.text:0000007103E78344                 LDR             X8, [X0]
.text:0000007103E78348                 LDR             X8, [X8,#0x68]
.text:0000007103E7834C                 BLR             X8
.text:0000007103E78350                 STR             X0, [X19,#(qword_71097BB4E0 - 0x71097BB4D0)]
```
So our second final address is 0x97BB4E0.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x978D988, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x97BB4E0, 0]
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
    address: [MAIN, 0x978D988, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x97BB4E0, 0]
    value_type: float
    value: [0, 0]

```