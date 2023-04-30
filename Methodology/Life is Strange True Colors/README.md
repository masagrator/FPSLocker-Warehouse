# Life is Strange: True Colors

> Game info

TitleID: `0100500012AB4000`<br>
Explanation based on:
- Internal version: `1.0.4`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `118AA7B71E824B3B`
- Engine: `Unreal Engine 4.25.0`

> Details

Game is using internal FPS lock + dynamic resolution timing set to 33.33ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710282F018                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710282F01C                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710282F020                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710282F024                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710282F028                 MOV             W3, #0x20
.text:000000710282F02C                 BLR             X8
.text:000000710282F030                 ADRP            X19, #qword_7107426EE0@PAGE
.text:000000710282F034                 ADD             X19, X19, #qword_7107426EE0@PAGEOFF
.text:000000710282F038                 STP             X24, X0, [X19]
.text:000000710282F03C                 LDR             X8, [X0]
.text:000000710282F040                 LDR             X8, [X8,#0x68]
.text:000000710282F044                 BLR             X8
.text:000000710282F048                 STR             X0, [X19,#(qword_7107426EF0 - 0x7107426EE0)]
```

So first final address is stored at 0x7426EF0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102D41A98                 ADRP            X1, #aTMaxfps_0@PAGE ; "t.MaxFPS"
.text:0000007102D41A9C                 ADD             X1, X1, #aTMaxfps_0@PAGEOFF ; "t.MaxFPS"
.text:0000007102D41AA0                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D41AA4                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D41AA8                 MOV             W3, WZR
.text:0000007102D41AAC                 BLR             X8
.text:0000007102D41AB0                 ADRP            X19, #qword_7107451B68@PAGE
.text:0000007102D41AB4                 ADD             X19, X19, #qword_7107451B68@PAGEOFF
.text:0000007102D41AB8                 ADRP            X8, #off_7105D018B0@PAGE
.text:0000007102D41ABC                 ADD             X8, X8, #off_7105D018B0@PAGEOFF
.text:0000007102D41AC0                 STP             X8, X0, [X19]
.text:0000007102D41AC4                 LDR             X8, [X0]
.text:0000007102D41AC8                 LDR             X8, [X8,#0x68]
.text:0000007102D41ACC                 BLR             X8
.text:0000007102D41AD0                 STR             X0, [X19,#(qword_7107451B78 - 0x7107451B68)]
```
So our second final address is 0x7451B78.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x7426EF0, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7451B78, 0]
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
    address: [MAIN, 0x7426EF0, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7451B78, 0]
    value_type: float
    value: [0, 0]

```