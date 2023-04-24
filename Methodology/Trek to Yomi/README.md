# Trek to Yomi

> Game info

TitleID: `0100D77019324000`<br>
Explanation based on:
- Internal version: `0.4`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `A52C9938956331C9`
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
.text:00000071026F3DCC                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071026F3DD0                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071026F3DD4                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:00000071026F3DD8                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071026F3DDC                 LDR             X8, [X8,#0x10]
.text:00000071026F3DE0                 MOV             W3, #0x20
.text:00000071026F3DE4                 BLR             X8
.text:00000071026F3DE8                 ADRP            X19, #qword_71073F93E8@PAGE
.text:00000071026F3DEC                 ADD             X19, X19, #qword_71073F93E8@PAGEOFF
.text:00000071026F3DF0                 STP             X24, X0, [X19]
.text:00000071026F3DF4                 LDR             X8, [X0]
.text:00000071026F3DF8                 LDR             X8, [X8,#0x68]
.text:00000071026F3DFC                 BLR             X8
.text:00000071026F3E00                 STR             X0, [X19,#(qword_71073F93F8 - 0x71073F93E8)]
```

So first final address is stored at 0x73F93F8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102C05C24                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102C05C28                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102C05C2C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102C05C30                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102C05C34                 LDR             X8, [X8,#0x10]
.text:0000007102C05C38                 MOV             W3, WZR
.text:0000007102C05C3C                 BLR             X8
.text:0000007102C05C40                 ADRP            X19, #qword_7107426A08@PAGE
.text:0000007102C05C44                 ADD             X19, X19, #qword_7107426A08@PAGEOFF
.text:0000007102C05C48                 ADRP            X8, #off_7105F168A8@PAGE
.text:0000007102C05C4C                 ADD             X8, X8, #off_7105F168A8@PAGEOFF
.text:0000007102C05C50                 STP             X8, X0, [X19]
.text:0000007102C05C54                 LDR             X8, [X0]
.text:0000007102C05C58                 LDR             X8, [X8,#0x68]
.text:0000007102C05C5C                 BLR             X8
.text:0000007102C05C60                 STR             X0, [X19,#(qword_7107426A18 - 0x7107426A08)]
```
So our second final address is 0x7426A18.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x73F93F8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7426A18, 0]
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
    address: [MAIN, 0x73F93F8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7426A18, 0]
    value_type: float
    value: [0, 0]

```
