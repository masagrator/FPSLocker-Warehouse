# Insomnis

> Game info

TitleID: `01001CF0190C2000`<br>
Explanation based on:
- Internal version: `1.01`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `4C6727375D877B90`
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
.text:000000710243CF4C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710243CF50                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710243CF54                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710243CF58                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710243CF5C                 LDR             X8, [X8,#0x10]
.text:000000710243CF60                 MOV             W3, #0x20
.text:000000710243CF64                 BLR             X8
.text:000000710243CF68                 ADRP            X19, #qword_710680CAA8@PAGE
.text:000000710243CF6C                 ADD             X19, X19, #qword_710680CAA8@PAGEOFF
.text:000000710243CF70                 STP             X24, X0, [X19]
.text:000000710243CF74                 LDR             X8, [X0]
.text:000000710243CF78                 LDR             X8, [X8,#0x68]
.text:000000710243CF7C                 BLR             X8
.text:000000710243CF80                 STR             X0, [X19,#(qword_710680CAB8 - 0x710680CAA8)]
```

So first final address is stored at 0x680CAB8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710296913C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102969140                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102969144                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102969148                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710296914C                 LDR             X8, [X8,#0x10]
.text:0000007102969150                 MOV             W3, WZR
.text:0000007102969154                 BLR             X8
.text:0000007102969158                 ADRP            X19, #qword_710683A348@PAGE
.text:000000710296915C                 ADD             X19, X19, #qword_710683A348@PAGEOFF
.text:0000007102969160                 ADRP            X8, #off_71054D68B8@PAGE
.text:0000007102969164                 ADD             X8, X8, #off_71054D68B8@PAGEOFF
.text:0000007102969168                 STP             X8, X0, [X19]
.text:000000710296916C                 LDR             X8, [X0]
.text:0000007102969170                 LDR             X8, [X8,#0x68]
.text:0000007102969174                 BLR             X8
.text:0000007102969178                 STR             X0, [X19,#(qword_710683A358 - 0x710683A348)]
```
So our second final address is 0x683A358.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x680CAB8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x683A358, 0]
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
    address: [MAIN, 0x680CAB8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x683A358, 0]
    value_type: float
    value: [0, 0]

```