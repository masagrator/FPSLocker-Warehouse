# OCTOPATH TRAVELER

> Game info

TitleID: `010057D006492000`<br>
Explanation based on:
- Internal version: `1.0.4`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `B88A8D8E5516DDE9`
- Engine: `Unreal Engine 4.18.0`

> Details

Game is using internal FPS lock. Requires patch to fix that.
**WARNING**: Game has issues with properly synchronizing sprites of characters moving behind main character, which results in stuttering sprites. This happens only above 30 FPS.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
t.MaxFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101BFDB88                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101BFDB8C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101BFDB90                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101BFDB94                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101BFDB98                 MOV             W3, WZR
.text:0000007101BFDB9C                 BLR             X8
.text:0000007101BFDBA0                 ADD             X8, X25, #0x10
.text:0000007101BFDBA4                 STR             X0, [X22,#(qword_71050B5690 - 0x71050B50B0)]
.text:0000007101BFDBA8                 ADD             X19, X22, #0x5D8
.text:0000007101BFDBAC                 STR             X8, [X22,#(qword_71050B5688 - 0x71050B50B0)]
.text:0000007101BFDBB0                 LDR             X8, [X0]
.text:0000007101BFDBB4                 LDR             X8, [X8,#0x48]
.text:0000007101BFDBB8                 BLR             X8
.text:0000007101BFDBBC                 STR             X0, [X22,#(qword_71050B5698 - 0x71050B50B0)]
```

So final address is stored at 0x50B5698.

Our final address stores pointer that points to two floats. By default t.MaxFPS is always 30.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x50B5698, 0]
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
    address: [MAIN, 0x50B5698, 0]
    value_type: float
    value: [0, 0]

```