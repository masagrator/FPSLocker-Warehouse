# Bloodstained: Ritual of the Night

> Game info

TitleID: `0100BF500207C000`<br>
Explanation based on:
- Internal version: `1.4.0`
- Nintendo version ID: `v11`/`720896`
- BID: `12E0B62494B22F62`
- Engine: `Unreal Engine 4.22.3`

> Details

Plugin alone can set FPS above 30, but because of dynamic resolution set to 28 ms performance is subpar. It must be patched.<br>
Game also uses double buffer. To make game triple buffer you must find string `nvn.NumBufferedFrames` stored as UTF-16-LE and change at least one character to anything else before game initializes.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710693C990                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710693C994                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710693C998                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710693C99C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710693C9A0                 MOV             W3, #0x20
.text:000000710693C9A4                 BLR             X8
.text:000000710693C9A8                 ADRP            X19, #qword_710CF57E80@PAGE
.text:000000710693C9AC                 ADD             X19, X19, #qword_710CF57E80@PAGEOFF
.text:000000710693C9B0                 STP             X22, X0, [X19]
.text:000000710693C9B4                 LDR             X8, [X0]
.text:000000710693C9B8                 LDR             X8, [X8,#0x48]
.text:000000710693C9BC                 BLR             X8
.text:000000710693C9C0                 STR             X0, [X19,#(qword_710CF57E90 - 0x710CF57E80)]
```

So first final address is stored at 0xCF57E90.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007106E2DC00                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007106E2DC04                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007106E2DC08                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007106E2DC0C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007106E2DC10                 MOV             W3, WZR
.text:0000007106E2DC14                 BLR             X8
.text:0000007106E2DC18                 ADRP            X19, #qword_710CF7EC70@PAGE
.text:0000007106E2DC1C                 ADD             X19, X19, #qword_710CF7EC70@PAGEOFF
.text:0000007106E2DC20                 ADRP            X8, #off_710BB2C858@PAGE
.text:0000007106E2DC24                 ADD             X8, X8, #off_710BB2C858@PAGEOFF
.text:0000007106E2DC28                 STP             X8, X0, [X19]
.text:0000007106E2DC2C                 LDR             X8, [X0]
.text:0000007106E2DC30                 LDR             X8, [X8,#0x48]
.text:0000007106E2DC34                 BLR             X8
.text:0000007106E2DC38                 STR             X0, [X19,#(qword_710CF7EC80 - 0x710CF7EC70)]
```
So our second final address is 0xCF7EC80.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 28.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = 0.84 * (1000/FPS)
  -
    type: write
    address: [MAIN, 0xCF57E90, 0]
    value_type: float
    value: [56, 56]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0xCF7EC80, 0]
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
    address: [MAIN, 0xCF57E90, 0]
    value_type: float
    value: [28, 28]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0xCF7EC80, 0]
    value_type: float
    value: [0, 0]

```
