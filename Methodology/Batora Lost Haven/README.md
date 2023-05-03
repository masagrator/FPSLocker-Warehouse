# Batora: Lost Haven

> Game info

TitleID: `0100A93016BF4000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `770A07C35E631CB2`
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
.text:000000710286F32C                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710286F330                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710286F334                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710286F338                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710286F33C                 LDR             X8, [X8,#0x10]
.text:000000710286F340                 MOV             W3, #0x20
.text:000000710286F344                 BLR             X8
.text:000000710286F348                 ADRP            X19, #qword_71074F84B8@PAGE
.text:000000710286F34C                 ADD             X19, X19, #qword_71074F84B8@PAGEOFF
.text:000000710286F350                 STP             X24, X0, [X19]
.text:000000710286F354                 LDR             X8, [X0]
.text:000000710286F358                 LDR             X8, [X8,#0x68]
.text:000000710286F35C                 BLR             X8
.text:000000710286F360                 STR             X0, [X19,#(qword_71074F84C8 - 0x71074F84B8)]
```

So first final address is stored at 0x74F84C8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102D8F97C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102D8F980                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102D8F984                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D8F988                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D8F98C                 LDR             X8, [X8,#0x10]
.text:0000007102D8F990                 MOV             W3, WZR
.text:0000007102D8F994                 BLR             X8
.text:0000007102D8F998                 ADRP            X19, #qword_7107526048@PAGE
.text:0000007102D8F99C                 ADD             X19, X19, #qword_7107526048@PAGEOFF
.text:0000007102D8F9A0                 ADRP            X8, #off_7105FF88B8@PAGE
.text:0000007102D8F9A4                 ADD             X8, X8, #off_7105FF88B8@PAGEOFF
.text:0000007102D8F9A8                 STP             X8, X0, [X19]
.text:0000007102D8F9AC                 LDR             X8, [X0]
.text:0000007102D8F9B0                 LDR             X8, [X8,#0x68]
.text:0000007102D8F9B4                 BLR             X8
.text:0000007102D8F9B8                 STR             X0, [X19,#(qword_7107526058 - 0x7107526048)]
```
So our second final address is 0x7526058.

Each of our final address stores pointer that points to two floats. After game will go to main menu t.MaxFPS is set to 30. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimal
  -
    type: write
    address: [MAIN, 0x74F84C8, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7526058, 0]
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
    address: [MAIN, 0x74F84C8, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7526058, 0]
    value_type: float
    value: [0, 0]

```