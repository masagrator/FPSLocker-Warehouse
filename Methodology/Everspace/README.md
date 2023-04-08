# Everspace™ - Stellar Edition

> Game info

TitleID: `0100DCF0093EC000`<br>
Explanation based on:
- Internal version: `1.0.5`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `71873FEB4648FA39`
- Engine: `Unreal Engine 4.20.2`

> Details

Game is using internal FPS lock, and dynamic resolution set to 33.33 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101B81914                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B81918                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B8191C                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007101B81920                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007101B81924                 MOV             W3, #0x20
.text:0000007101B81928                 BLR             X8
.text:0000007101B8192C                 ADD             X20, X21, #0x10
.text:0000007101B81930                 STR             X0, [X27,#(qword_7105FAB538 - 0x7105FAAAC0)]
.text:0000007101B81934                 ADD             X19, X27, #0xA70
.text:0000007101B81938                 STR             X20, [X27,#(qword_7105FAB530 - 0x7105FAAAC0)]
.text:0000007101B8193C                 LDR             X8, [X0]
.text:0000007101B81940                 LDR             X8, [X8,#0x48]
.text:0000007101B81944                 BLR             X8
.text:0000007101B81948                 STR             X0, [X27,#(qword_7105FAB540 - 0x7105FAAAC0)]
```

So first final address is stored at 0x5FAB540.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102129264                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102129268                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:000000710212926C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102129270                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102129274                 MOV             W3, WZR
.text:0000007102129278                 BLR             X8
.text:000000710212927C                 ADRP            X8, #qword_7105193798@PAGE
.text:0000007102129280                 ADD             X8, X8, #qword_7105193798@PAGEOFF
.text:0000007102129284                 ADD             X8, X8, #0x10
.text:0000007102129288                 STR             X0, [X23,#(qword_7105FD00A0 - 0x7105FCF930)]
.text:000000710212928C                 ADD             X19, X23, #0x768
.text:0000007102129290                 STR             X8, [X23,#(qword_7105FD0098 - 0x7105FCF930)]
.text:0000007102129294                 LDR             X8, [X0]
.text:0000007102129298                 LDR             X8, [X8,#0x48]
.text:000000710212929C                 BLR             X8
.text:00000071021292A0                 STR             X0, [X23,#(qword_7105FD00A8 - 0x7105FCF930)]
```
So our second final address is 0x5FD00A8.

Each of our final address stores pointer that points to two floats. t.MaxFPS is set to 32. r.DynamicRes.FrameTimeBudget is 33.33.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x5FAB540, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x5FD00A8, 0]
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
    address: [MAIN, 0x5FAB540, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x5FD00A8, 0]
    value_type: float
    value: [32, 32]

```
