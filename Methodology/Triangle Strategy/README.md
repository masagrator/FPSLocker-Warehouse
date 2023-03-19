# Triangle Strategy

> Game info

TitleID: `0100CC80140F8000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `2AA7F33234696651`

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

Our final address stores pointer that points to two floats. By default 30 FPS is 33.33, so our entry for 30 FPS will look like this:
```yaml
30FPS:
  -
    type: write
    address: [MAIN, 0x745D838, 0]
    value_type: float
    value: [33.33, 33.33]

```
