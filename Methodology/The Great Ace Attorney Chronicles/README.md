# The Great Ace Attorney Chronicles

> Game info

TitleID: `010036E00FB20000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `1DA748FC9499882F`
- Engine: `MT Framework`

> Details

Game is using internal FPS Lock. We need to patch it.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find those bytes:
```
08 3E A8 D2 08 3E E8 F2
```
We need to find where X8 register is written by searching for first `STR X8` instruction.
```
.text:00000071002EA2F0                 LDR             X0, [X20]
.text:00000071002EA2F4                 MOV             X8, #0x41F00000
.text:00000071002EA2F8                 MOVK            X8, #0x41F0,LSL#48
.text:00000071002EA2FC                 MOV             W9, #0x83C8
.text:00000071002EA300                 MOVK            W9, #5,LSL#16
.text:00000071002EA304                 STR             X8, [X0,#0x48]
```
So in our case it's X0+0x48. X8 consists of two floats and we are interested in second one, so offset we need is 0x4C.
Now we need to find what X0 is, so we are looking before for instruction that loads pointer to it.

We see that to X0 it's loaded pointer from X20, so we need to find what loads into X20.

```
.text:00000071002EA270                 ADRP            X20, #off_7100BD6C78@PAGE
.text:00000071002EA274                 LDR             X20, [X20,#off_7100BD6C78@PAGEOFF]
```
We have hardcoded pointer loaded from `off_7100BD6C78` which is `qword_7100CF90F8`.
So our final address is `[MAIN+0xCF90F8]+0x4C`.

Our entry for 30 FPS will look like this (add block timing for anythine else than 30 and 60):
```yaml
30FPS:
  # FPS lock (default)
  -
    type: write
    address: [MAIN, 0xCF90F8, 0x4C]
    value_type: float
    value: 30
```