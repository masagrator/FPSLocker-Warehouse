# New Tales from the Borderlands

> Game info

TitleID: `010051B0131F0000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `A19E113723E5C32E`
- Engine: `Unreal Engine 4.27.2`

> Details

Game is using internal FPS lock + dynamic resolution set to 33.33 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710284F520                 ADRP            X1, #aRDynamicresFra_1@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710284F524                 ADD             X1, X1, #aRDynamicresFra_1@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710284F528                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710284F52C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710284F530                 LDR             X8, [X8,#0x10]
.text:000000710284F534                 MOV             W3, #0x20
.text:000000710284F538                 BLR             X8
.text:000000710284F53C                 ADRP            X19, #qword_710A158EF8@PAGE
.text:000000710284F540                 ADD             X19, X19, #qword_710A158EF8@PAGEOFF
.text:000000710284F544                 STP             X24, X0, [X19]
.text:000000710284F548                 LDR             X8, [X0]
.text:000000710284F54C                 LDR             X8, [X8,#0x68]
.text:000000710284F550                 BLR             X8
.text:000000710284F554                 STR             X0, [X19,#(qword_710A158F08 - 0x710A158EF8)]
```

So first final address is stored at 0xA158F08.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102D95CEC                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102D95CF0                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102D95CF4                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D95CF8                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D95CFC                 LDR             X8, [X8,#0x10]
.text:0000007102D95D00                 MOV             W3, WZR
.text:0000007102D95D04                 BLR             X8
.text:0000007102D95D08                 ADRP            X19, #qword_710A1884C8@PAGE
.text:0000007102D95D0C                 ADD             X19, X19, #qword_710A1884C8@PAGEOFF
.text:0000007102D95D10                 ADRP            X8, #off_7108A608D8@PAGE
.text:0000007102D95D14                 ADD             X8, X8, #off_7108A608D8@PAGEOFF
.text:0000007102D95D18                 STP             X8, X0, [X19]
.text:0000007102D95D1C                 LDR             X8, [X0]
.text:0000007102D95D20                 LDR             X8, [X8,#0x68]
.text:0000007102D95D24                 BLR             X8
.text:0000007102D95D28                 STR             X0, [X19,#(qword_710A1884D8 - 0x710A1884C8)]
```
So our second final address is 0xA1884D8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0xA158F08, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0xA1884D8, 0]
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
    address: [MAIN, 0xA158F08, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0xA1884D8, 0]
    value_type: float
    value: [0, 0]

```