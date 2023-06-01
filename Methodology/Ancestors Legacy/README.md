#  Ancestors Legacy

> Game info

TitleID: `01009EE0111CC000`<br>
Explanation based on:
- Internal version: `1.1.0`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `EE20B8DD92B8F9B4`
- Engine: `Unreal Engine 4.17.2`

> Details

Game is using internal FPS Lock + double buffer. They must be patched.<br>
To disable double buffer just find `nvn.NumBufferedFrames` stored as UTF-32-LE and change at least one character to something else before game initializes.

# How to find offsets

We need to use disassembler in this case. I will be using IDA since it calculates offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
t.MaxFPS
```

It will have few xrefs, we are going to one which includes also description of this setting.

Below after second BLR we have our final address
```asm
.text:0000007101FABAC0                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101FABAC4                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101FABAC8                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101FABACC                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101FABAD0                 MOV             W3, WZR
.text:0000007101FABAD4                 BLR             X8
.text:0000007101FABAD8                 ADRP            X19, #unk_7105075DA0@PAGE
.text:0000007101FABADC                 ADD             X19, X19, #unk_7105075DA0@PAGEOFF
.text:0000007101FABAE0                 STP             X24, X0, [X19]
.text:0000007101FABAE4                 LDR             X8, [X0]
.text:0000007101FABAE8                 LDR             X8, [X8,#0x48]
.text:0000007101FABAEC                 BLR             X8
.text:0000007101FABAF0                 STR             X0, [X19,#(qword_7105075DB0 - 0x7105075DA0)]
```

Our final address is 0x5075DB0.

The final address stores pointer that points to two floats. By config t.MaxFPS is 30.<br>
Our entry for 15 FPS will look like this:
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x5075DB0, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x5075DB0, 0]
    value_type: float
    value: [30, 30]

```
