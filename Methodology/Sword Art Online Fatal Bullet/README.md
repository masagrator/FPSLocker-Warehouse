# SWORD ART ONLINE: FATAL BULLET Complete Edition

> Game info

TitleID: `01005DF00DC26000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `029C2837B0EEE8A9`
- Engine: `Unreal Engine 4.20.3`

> Details

Game is using internal FPS lock, and dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix those.
**WARNING**: Game's AI is tied to framerate. Higher framerate means enemy AI's faster responses.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710296E414                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710296E418                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710296E41C                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710296E420                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710296E424                 MOV             W3, #0x20
.text:000000710296E428                 BLR             X8
.text:000000710296E42C                 ADD             X20, X21, #0x10
.text:000000710296E430                 STR             X0, [X27,#(qword_7107D78508 - 0x7107D77A90)]
.text:000000710296E434                 ADD             X19, X27, #0xA70
.text:000000710296E438                 STR             X20, [X27,#(qword_7107D78500 - 0x7107D77A90)]
.text:000000710296E43C                 LDR             X8, [X0]
.text:000000710296E440                 LDR             X8, [X8,#0x48]
.text:000000710296E444                 BLR             X8
.text:000000710296E448                 STR             X0, [X27,#(qword_7107D78510 - 0x7107D77A90)]
```

So first final address is stored at 0x7D78510.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102F17AD4                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102F17AD8                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102F17ADC                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102F17AE0                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102F17AE4                 MOV             W3, WZR
.text:0000007102F17AE8                 BLR             X8
.text:0000007102F17AEC                 ADRP            X8, #unk_7106C0A0A0@PAGE
.text:0000007102F17AF0                 ADD             X8, X8, #unk_7106C0A0A0@PAGEOFF
.text:0000007102F17AF4                 ADD             X8, X8, #0x10
.text:0000007102F17AF8                 STR             X0, [X23,#(qword_7107D9D170 - 0x7107D9CA00)]
.text:0000007102F17AFC                 ADD             X19, X23, #0x768
.text:0000007102F17B00                 STR             X8, [X23,#(qword_7107D9D168 - 0x7107D9CA00)]
.text:0000007102F17B04                 LDR             X8, [X0]
.text:0000007102F17B08                 LDR             X8, [X8,#0x48]
.text:0000007102F17B0C                 BLR             X8
.text:0000007102F17B10                 STR             X0, [X23,#(qword_7107D9D178 - 0x7107D9CA00)]
```
So our second final address is 0x7D9D178.

Each of our final address stores pointer that points to two floats. t.MaxFPS is set to 30. r.DynamicRes.FrameTimeBudget via config is 33.3.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to one decimal
  -
    type: write
    address: [MAIN, 0x7D78510, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7D9D178, 0]
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
    address: [MAIN, 0x7D78510, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7D9D178, 0]
    value_type: float
    value: [30, 30]

```
