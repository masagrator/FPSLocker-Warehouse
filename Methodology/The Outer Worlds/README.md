# The Outer Worlds

> Game info

TitleID: `0100626011656000`<br>
Explanation based on:
- Internal version: `1.0.5`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `761CD556AB357C87`
- Engine: `Unreal Engine 4.21.2`

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
.text:0000007100B580C8                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007100B580CC                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007100B580D0                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007100B580D4                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007100B580D8                 MOV             W3, #0x20
.text:0000007100B580DC                 BLR             X8
.text:0000007100B580E0                 ADRP            X19, #qword_7107A4AE38@PAGE
.text:0000007100B580E4                 ADD             X19, X19, #qword_7107A4AE38@PAGEOFF
.text:0000007100B580E8                 STP             X21, X0, [X19]
.text:0000007100B580EC                 LDR             X8, [X0]
.text:0000007100B580F0                 LDR             X8, [X8,#0x48]
.text:0000007100B580F4                 BLR             X8
.text:0000007100B580F8                 STR             X0, [X19,#(qword_7107A4AE48 - 0x7107A4AE38)]
```

So first final address is stored at 0x7A4AE48.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007100B7F2A8                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007100B7F2AC                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007100B7F2B0                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007100B7F2B4                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007100B7F2B8                 MOV             W3, WZR
.text:0000007100B7F2BC                 BLR             X8
.text:0000007100B7F2C0                 ADRP            X19, #qword_7107A70070@PAGE
.text:0000007100B7F2C4                 ADD             X19, X19, #qword_7107A70070@PAGEOFF
.text:0000007100B7F2C8                 ADRP            X8, #off_71068E3A50@PAGE
.text:0000007100B7F2CC                 ADD             X8, X8, #off_71068E3A50@PAGEOFF
.text:0000007100B7F2D0                 STP             X8, X0, [X19]
.text:0000007100B7F2D4                 LDR             X8, [X0]
.text:0000007100B7F2D8                 LDR             X8, [X8,#0x48]
.text:0000007100B7F2DC                 BLR             X8
.text:0000007100B7F2E0                 STR             X0, [X19,#(qword_7107A70080 - 0x7107A70070)]
```
So our second final address is 0x7A70080.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x7A4AE48, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7A70080, 0]
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
    address: [MAIN, 0x7A4AE48, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7A70080, 0]
    value_type: float
    value: [0, 0]

```
