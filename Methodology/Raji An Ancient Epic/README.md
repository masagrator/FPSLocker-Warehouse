# Raji: An Ancient Epic

> Game info

TitleID: `010010B00DDA2000`<br>
Explanation based on:
- Internal version: `1.0.4`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `8A39E660F956BB00`
- Engine: `Unreal Engine 4.26.2`

> Details

Plugin alone can set FPS above 30, but because of dynamic resolution set to 33.33 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007102350050                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102350054                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102350058                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710235005C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102350060                 MOV             W3, #0x20
.text:0000007102350064                 BLR             X8
.text:0000007102350068                 ADRP            X19, #qword_7106B461A8@PAGE
.text:000000710235006C                 ADD             X19, X19, #qword_7106B461A8@PAGEOFF
.text:0000007102350070                 STP             X24, X0, [X19]
.text:0000007102350074                 LDR             X8, [X0]
.text:0000007102350078                 LDR             X8, [X8,#0x68]
.text:000000710235007C                 BLR             X8
.text:0000007102350080                 STR             X0, [X19,#(qword_7106B461B8 - 0x7106B461A8)]
```

So first final address is stored at 0x6B461B8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710206A938                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:000000710206A93C                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:000000710206A940                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:000000710206A944                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710206A948                 MOV             W3, WZR
.text:000000710206A94C                 BLR             X8
.text:000000710206A950                 ADRP            X19, #qword_7106B3C320@PAGE
.text:000000710206A954                 ADD             X19, X19, #qword_7106B3C320@PAGEOFF
.text:000000710206A958                 ADRP            X8, #off_71057BE8A8@PAGE
.text:000000710206A95C                 ADD             X8, X8, #off_71057BE8A8@PAGEOFF
.text:000000710206A960                 STP             X8, X0, [X19]
.text:000000710206A964                 LDR             X8, [X0]
.text:000000710206A968                 LDR             X8, [X8,#0x68]
.text:000000710206A96C                 BLR             X8
.text:000000710206A970                 STR             X0, [X19,#(qword_7106B3C330 - 0x7106B3C320)]
```
So our second final address is 0x6B3C330.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x6B461B8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x6B3C330, 0]
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
    address: [MAIN, 0x6B461B8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x6B3C330, 0]
    value_type: float
    value: [0, 0]

```