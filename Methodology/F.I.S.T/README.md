# F.I.S.T.: Forged in Shadow Torch

> Game info

TitleID: `01009F8017F48000`<br>
Explanation based on:
- Internal version: `1.0.4`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `69EE5F71F187EAA9`
- Engine: `Unreal Engine 4.27.1`

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
.text:0000007104ED09E0                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007104ED09E4                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007104ED09E8                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007104ED09EC                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007104ED09F0                 LDR             X8, [X8,#0x10]
.text:0000007104ED09F4                 MOV             W3, #0x20
.text:0000007104ED09F8                 BLR             X8
.text:0000007104ED09FC                 ADRP            X19, #qword_710AE271B8@PAGE
.text:0000007104ED0A00                 ADD             X19, X19, #qword_710AE271B8@PAGEOFF
.text:0000007104ED0A04                 STP             X24, X0, [X19]
.text:0000007104ED0A08                 LDR             X8, [X0]
.text:0000007104ED0A0C                 LDR             X8, [X8,#0x68]
.text:0000007104ED0A10                 BLR             X8
.text:0000007104ED0A14                 STR             X0, [X19,#(qword_710AE271C8 - 0x710AE271B8)]
```

So first final address is stored at 0xAE271C8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071053FCB8C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071053FCB90                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071053FCB94                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071053FCB98                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071053FCB9C                 LDR             X8, [X8,#0x10]
.text:00000071053FCBA0                 MOV             W3, WZR
.text:00000071053FCBA4                 BLR             X8
.text:00000071053FCBA8                 ADRP            X19, #qword_710AE54F48@PAGE
.text:00000071053FCBAC                 ADD             X19, X19, #qword_710AE54F48@PAGEOFF
.text:00000071053FCBB0                 ADRP            X8, #off_71093148B8@PAGE
.text:00000071053FCBB4                 ADD             X8, X8, #off_71093148B8@PAGEOFF
.text:00000071053FCBB8                 STP             X8, X0, [X19]
.text:00000071053FCBBC                 LDR             X8, [X0]
.text:00000071053FCBC0                 LDR             X8, [X8,#0x68]
.text:00000071053FCBC4                 BLR             X8
.text:00000071053FCBC8                 STR             X0, [X19,#(qword_710AE54F58 - 0x710AE54F48)]
```
So our second final address is 0xAE54F58.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0xAE271C8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0xAE54F58, 0]
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
    address: [MAIN, 0xAE271C8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0xAE54F58, 0]
    value_type: float
    value: [0, 0]

```