# Ruiner

> Game info

TitleID: `01006EC00F2CC000`<br>
Explanation based on:
- Internal version: `1.3`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `F199FFD7D83F399E`
- Engine: `Unreal Engine 4.22.3`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will be using IDA because it will calculate offset for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below after second BLR we have our first final address
```asm
.text:000000710185FFC0                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710185FFC4                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710185FFC8                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710185FFCC                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710185FFD0                 MOV             W3, #0x20
.text:000000710185FFD4                 BLR             X8
.text:000000710185FFD8                 ADD             X21, X22, #0x10
.text:000000710185FFDC                 STR             X0, [X19,#(qword_71055B1688 - 0x71055B0FC0)]
.text:000000710185FFE0                 ADD             X20, X19, #0x6C0
.text:000000710185FFE4                 STR             X21, [X19,#(qword_71055B1680 - 0x71055B0FC0)]
.text:000000710185FFE8                 LDR             X8, [X0]
.text:000000710185FFEC                 LDR             X8, [X8,#0x48]
.text:000000710185FFF0                 BLR             X8
.text:000000710185FFF4                 STR             X0, [X19,#(qword_71055B1690 - 0x71055B0FC0)]
```

Our final address is 0x55B1690.

The same way we're searching for 
```
t.MaxFPS
```

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101D5A640                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101D5A644                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101D5A648                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101D5A64C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101D5A650                 MOV             W3, WZR
.text:0000007101D5A654                 BLR             X8
.text:0000007101D5A658                 ADRP            X8, #qword_710473DC80@PAGE
.text:0000007101D5A65C                 ADD             X8, X8, #qword_710473DC80@PAGEOFF
.text:0000007101D5A660                 ADD             X8, X8, #0x10
.text:0000007101D5A664                 STR             X0, [X23,#(qword_71055D80F8 - 0x71055D7910)]
.text:0000007101D5A668                 ADD             X19, X23, #0x7E0
.text:0000007101D5A66C                 STR             X8, [X23,#(qword_71055D80F0 - 0x71055D7910)]
.text:0000007101D5A670                 LDR             X8, [X0]
.text:0000007101D5A674                 LDR             X8, [X8,#0x48]
.text:0000007101D5A678                 BLR             X8
.text:0000007101D5A67C                 STR             X0, [X23,#(qword_71055D8100 - 0x71055D7910)]
```
So our second final address is 0x55D8100.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget via config file is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to one decimal
   -
    type: write
    address: [MAIN, 0x55B1690, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x55D8100, 0]
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
    address: [MAIN, 0x55B1690, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x55D8100, 0]
    value_type: float
    value: [0, 0]

```
