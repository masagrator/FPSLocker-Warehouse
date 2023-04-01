# Remnant: From the Ashes

> Game info

TitleID: `010010F01418E000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `49CF6B0B0A62F9E2`
- Engine: `Unreal Engine 4.25.4`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set for 30 FPS, performance is subpar. Requires patch to fix that.
Game has implemented custom dynamic resolution framebuffer manipulation that they called "r.DynamicRes.CrysisStyle". It's using GPU time to change resolution and enabled does not use FrameTimeBudget, but custom values.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.MaxGPUTime
```

then we go to its xref.

Below after first BLR we have base address
```asm
text:00000071041EF88C                 ADRP            X1, #aRDynamicresMax_1@PAGE ; "r.DynamicRes.MaxGPUTime"
.text:00000071041EF890                 ADD             X1, X1, #aRDynamicresMax_1@PAGEOFF ; "r.DynamicRes.MaxGPUTime"
.text:00000071041EF894                 ADRP            X2, #aIfGpuTimeExcee@PAGE ; "If GPU time exceeds this value, we star"...
.text:00000071041EF898                 ADD             X2, X2, #aIfGpuTimeExcee@PAGEOFF ; "If GPU time exceeds this value, we star"...
.text:00000071041EF89C                 LDR             X8, [X8,#0x10]
.text:00000071041EF8A0                 MOV             W3, #0x20
.text:00000071041EF8A4                 BLR             X8
.text:00000071041EF8A8                 ADRP            X19, #unk_7107E23AE0@PAGE
.text:00000071041EF8AC                 ADD             X19, X19, #unk_7107E23AE0@PAGEOFF
.text:00000071041EF8B0                 STP             X26, X0, [X19]
.text:00000071041EF8B4                 LDR             X8, [X0]
.text:00000071041EF8B8                 LDR             X8, [X8,#0x68]
.text:00000071041EF8BC                 BLR             X8
```

Our base address is 0x7E23AE0.

After next BLR we have an offset:
```asm
STR x0, [x19, #0x10]
```
so our final address is 0x7E23AE0 + 0x10 = 0x7E23AF0.<br>
If you use IDA, you will have already calculated pointer
```asm
.text:00000071041EF8C0                 STR             X0, [X19,#(qword_7107E23AF0 - 0x7107E23AE0)]
```

The same way we're searching for 
```
r.DynamicRes.MinGPUTime
r.DynamicRes.MaxGPUTimeStill
r.DynamicRes.MinGPUTimeStill
```
Also for
```
t.MaxFPS
```
but it should have 2 xrefs. We are interested in the one that has description pointer loaded.

Is should look like this in IDA:
```asm
.text:0000007104323260                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007104323264                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007104323268                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:000000710432326C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007104323270                 LDR             X8, [X8,#0x10]
.text:0000007104323274                 MOV             W3, WZR
.text:0000007104323278                 BLR             X8
.text:000000710432327C                 ADRP            X19, #unk_7107E46688@PAGE
.text:0000007104323280                 ADD             X19, X19, #unk_7107E46688@PAGEOFF
.text:0000007104323284                 ADRP            X8, #off_710636C960@PAGE
.text:0000007104323288                 ADD             X8, X8, #off_710636C960@PAGEOFF
.text:000000710432328C                 STP             X8, X0, [X19]
.text:0000007104323290                 LDR             X8, [X0]
.text:0000007104323294                 LDR             X8, [X8,#0x68]
.text:0000007104323298                 BLR             X8
.text:000000710432329C                 STR             X0, [X19,#(qword_7107E46698 - 0x7107E46688)]
```
So our `t.MaxFPS` final address is 0x7E46698.

Each of our final address stores pointer that points to two floats. <br>
By default t.MaxFPS is always 0. <br>
r.DynamicRes.MaxGPUTime is set in code as 31.0.<br>
r.DynamicRes.MinGPUTime is set in code as 29.0.<br>
r.DynamicRes.MaxGPUTimeStill is set in code as 31.5.<br>
r.DynamicRes.MinGPUTimeStill is set in code as 31.0.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.MaxGPUTime ((1000/FPS) * 0.93)
  -
    type: write
    address: [MAIN, 0x7E23AF0, 0]
    value_type: float
    value: [62, 62]
  # r.DynamicRes.MinGPUTime ((1000/FPS) * 0.87)
  -
    type: write
    address: [MAIN, 0x7E23B08, 0]
    value_type: float
    value: [58, 58]
  # r.DynamicRes.MaxGPUTimeStill ((1000/FPS) * 0.945)
  -
    type: write
    address: [MAIN, 0x7E23B20, 0]
    value_type: float
    value: [63, 63]
  # r.DynamicRes.MinGPUTimeStill ((1000/FPS) * 0.93)
  -
    type: write
    address: [MAIN, 0x7E23B38, 0]
    value_type: float
    value: [62, 62]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7E46698, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
  # r.DynamicRes.MaxGPUTime (default value)
  -
    type: write
    address: [MAIN, 0x7E23AF0, 0]
    value_type: float
    value: [31, 31]
  # r.DynamicRes.MinGPUTime (default value)
  -
    type: write
    address: [MAIN, 0x7E23B08, 0]
    value_type: float
    value: [29, 29]
  # r.DynamicRes.MaxGPUTimeStill (default value)
  -
    type: write
    address: [MAIN, 0x7E23B20, 0]
    value_type: float
    value: [31.5, 31.5]
  # r.DynamicRes.MinGPUTimeStill (default value)
  -
    type: write
    address: [MAIN, 0x7E23B38, 0]
    value_type: float
    value: [31, 31]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7E46698, 0]
    value_type: float
    value: [0, 0]

```
