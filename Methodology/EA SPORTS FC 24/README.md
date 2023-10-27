# EA SPORTS FC 24

> Game info

TitleID: `0100BDB01A0E6000`<br>
Explanation based on:
- Internal version: `1.54.6f8d`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `9C33602289E55F7A`
- Engine: `Frostbite`

> Details

Game is using internal FPS lock that must be patched.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA.

After finishing disassembling main, we need to find those bytes:
```
C1 F7 01 6F 08 00 26 1E
```

We should get only one result.

Above that we need to find first `LDR X8`:
```asm
.text:0000007104F40734                 ADRP            X8, #off_710B913F58@PAGE
.text:0000007104F40738                 LDR             X8, [X8,#off_710B913F58@PAGEOFF]
.text:0000007104F4073C                 FDIV            S0, S1, S0
.text:0000007104F40740                 LDR             X9, [X8]
.text:0000007104F40744                 FMOV            V1.2D, #30.0
.text:0000007104F40748                 FMOV            W8, S0
```

off_710B913F58 is storing hardcoded pointer, that in case of this version is qword_710CD45EC0. So our final address is MAIN + 0xCD45EC0

Our final address stores pointer that points to double storing FPS lock value. By default it's 30.<br>
Entry for 30 FPS will look like this:
```yaml
30FPS:
  # Internal FPS Lock (default value is 30)
  -
    type: write
    address: [MAIN, 0xCD45EC0, 8]
    value_type: double
    value: 30
```