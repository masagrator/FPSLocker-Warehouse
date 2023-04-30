# CRISIS CORE -FINAL FANTASY VII- REUNION

> Game info

TitleID: `01004BC0166CC000`<br>
Explanation based on:
- Internal version: `1.0.4`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `44D207EA6428E3F1`
- Engine: `Unreal Engine 4.27.2`

> Details

Game is using internal FPS lock + dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007102B0555C                 ADRP            X1, #aRDynamicresFra_1@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102B05560                 ADD             X1, X1, #aRDynamicresFra_1@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102B05564                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102B05568                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102B0556C                 LDR             X8, [X8,#0x10]
.text:0000007102B05570                 MOV             W3, #0x20
.text:0000007102B05574                 BLR             X8
.text:0000007102B05578                 ADRP            X19, #qword_71096CFD98@PAGE
.text:0000007102B0557C                 ADD             X19, X19, #qword_71096CFD98@PAGEOFF
.text:0000007102B05580                 STP             X24, X0, [X19]
.text:0000007102B05584                 LDR             X8, [X0]
.text:0000007102B05588                 LDR             X8, [X8,#0x68]
.text:0000007102B0558C                 BLR             X8
.text:0000007102B05590                 STR             X0, [X19,#(qword_71096CFDA8 - 0x71096CFD98)]
```

So first final address is stored at 0x96CFDA8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007103033B30                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007103033B34                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007103033B38                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103033B3C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103033B40                 LDR             X8, [X8,#0x10]
.text:0000007103033B44                 MOV             W3, WZR
.text:0000007103033B48                 BLR             X8
.text:0000007103033B4C                 ADRP            X19, #qword_71096FDCC0@PAGE
.text:0000007103033B50                 ADD             X19, X19, #qword_71096FDCC0@PAGEOFF
.text:0000007103033B54                 ADRP            X8, #off_710605A8B8@PAGE
.text:0000007103033B58                 ADD             X8, X8, #off_710605A8B8@PAGEOFF
.text:0000007103033B5C                 STP             X8, X0, [X19]
.text:0000007103033B60                 LDR             X8, [X0]
.text:0000007103033B64                 LDR             X8, [X8,#0x68]
.text:0000007103033B68                 BLR             X8
.text:0000007103033B6C                 STR             X0, [X19,#(qword_71096FDCD0 - 0x71096FDCC0)]
```
So our second final address is 0x96FDCD0.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimal
  -
    type: write
    address: [MAIN, 0x96CFDA8, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x96FDCD0, 0]
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
    address: [MAIN, 0x96CFDA8, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x96FDCD0, 0]
    value_type: float
    value: [0, 0]

```
