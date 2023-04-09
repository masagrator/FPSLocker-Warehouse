# ABZU

> Game info

TitleID: `0100C1300BBC6000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `59719CFCD1671B98`
- Engine: `Unreal Engine 4.18.1`

> Details

Game is using SmoothFrameRateRange that blocks setting FPS above 40. We will be using another function to overwrite this limitation.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
t.MaxFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101FA30E0                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101FA30E4                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101FA30E8                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101FA30EC                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101FA30F0                 MOV             W3, WZR
.text:0000007101FA30F4                 BLR             X8
.text:0000007101FA30F8                 ADD             X8, X25, #0x10
.text:0000007101FA30FC                 STR             X0, [X22,#(qword_7106228ED8 - 0x71062288F0)]
.text:0000007101FA3100                 ADD             X19, X22, #0x5E0
.text:0000007101FA3104                 STR             X8, [X22,#(qword_7106228ED0 - 0x71062288F0)]
.text:0000007101FA3108                 LDR             X8, [X0]
.text:0000007101FA310C                 LDR             X8, [X8,#0x48]
.text:0000007101FA3110                 BLR             X8
.text:0000007101FA3114                 STR             X0, [X22,#(qword_7106228EE0 - 0x71062288F0)]
```

So final address is stored at 0x6228EE0.

Our final address stores pointer that points to two floats. t.MaxFPS is set to 0.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x6228EE0, 0]
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
    address: [MAIN, 0x6228EE0, 0]
    value_type: float
    value: [0, 0]

```
