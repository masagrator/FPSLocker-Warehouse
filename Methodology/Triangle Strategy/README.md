# Triangle Strategy

> Game info

TitleID: `0100CC80140F8000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `2AA7F33234696651`
- Engine: `Unreal Engine 4.27.0`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution in battles that is set to 33.33 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below after first BLR we have base address
```asm
.text:0000007102A217F0                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102A217F4                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102A217F8                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102A217FC                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102A21800                 LDR             X8, [X8,#0x10]
.text:0000007102A21804                 MOV             W3, #0x20
.text:0000007102A21808                 BLR             X8
.text:0000007102A2180C                 ADRP            X19, #unk_710745D828@PAGE
.text:0000007102A21810                 ADD             X19, X19, #unk_710745D828@PAGEOFF
.text:0000007102A21814                 STP             X24, X0, [X19]
.text:0000007102A21818                 LDR             X8, [X0]
.text:0000007102A2181C                 LDR             X8, [X8,#0x68]
.text:0000007102A21820                 BLR             X8
```

Our base address is 0x745D828.

After next BLR we have an offset:
```asm
STR x0, [x19, #0x10]
```
so our final address is 0x745D828 + 0x10 = 0x745D838.<br>
If you use IDA, you will have already calculated pointer
```asm
.text:0000007102A21824                 STR             X0, [X19,#(qword_710745D838 - 0x710745D828)]
```

The same way we're searching for 
```
t.MaxFPS
```
It should have 2 xrefs. We are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102F4B02C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102F4B030                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102F4B034                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102F4B038                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102F4B03C                 LDR             X8, [X8,#0x10]
.text:0000007102F4B040                 MOV             W3, WZR
.text:0000007102F4B044                 BLR             X8
.text:0000007102F4B048                 ADRP            X19, #unk_710748B3F8@PAGE
.text:0000007102F4B04C                 ADD             X19, X19, #unk_710748B3F8@PAGEOFF
.text:0000007102F4B050                 ADRP            X8, #off_7105F8F8B8@PAGE
.text:0000007102F4B054                 ADD             X8, X8, #off_7105F8F8B8@PAGEOFF
.text:0000007102F4B058                 STP             X8, X0, [X19]
.text:0000007102F4B05C                 LDR             X8, [X0]
.text:0000007102F4B060                 LDR             X8, [X8,#0x68]
.text:0000007102F4B064                 BLR             X8
.text:0000007102F4B068                 STR             X0, [X19,#(qword_710748B408 - 0x710748B3F8)]
```
So our second final address is 0x748B408.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget via config file is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget ((1000/FPS) * 0.945)
  -
    type: write
    address: [MAIN, 0x745D838, 0]
    value_type: float
    value: [63, 63]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x748B408, 0]
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
    address: [MAIN, 0x745D838, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x748B408, 0]
    value_type: float
    value: [0, 0]

```
