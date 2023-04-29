# OCTOPATH TRAVELER II

> Game info

TitleID: `0100A3501946E000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `BB891294DA55675E`
- Engine: `Unreal Engine 4.27.2`

> Details

Game is using internal FPS lock. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
t.MaxFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007102E4006C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102E40070                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102E40074                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102E40078                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102E4007C                 LDR             X8, [X8,#0x10]
.text:0000007102E40080                 MOV             W3, WZR
.text:0000007102E40084                 BLR             X8
.text:0000007102E40088                 ADRP            X19, #qword_71076C9F58@PAGE
.text:0000007102E4008C                 ADD             X19, X19, #qword_71076C9F58@PAGEOFF
.text:0000007102E40090                 ADRP            X8, #off_710608E8B8@PAGE
.text:0000007102E40094                 ADD             X8, X8, #off_710608E8B8@PAGEOFF
.text:0000007102E40098                 STP             X8, X0, [X19]
.text:0000007102E4009C                 LDR             X8, [X0]
.text:0000007102E400A0                 LDR             X8, [X8,#0x68]
.text:0000007102E400A4                 BLR             X8
.text:0000007102E400A8                 STR             X0, [X19,#(qword_71076C9F68 - 0x71076C9F58)]
```

So final address is stored at 0x76C9F68.

Our final address stores pointer that points to two floats. By default t.MaxFPS is always 30.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x76C9F68, 0]
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
    address: [MAIN, 0x76C9F68, 0]
    value_type: float
    value: [0, 0]

```