# Paradise Lost

> Game info

TitleID: `010077A012A5C000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `F5ECE696120B65B3`
- Engine: `Unreal Engine 4.23.1`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 30 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below after first BLR we have base address
```asm
.text:0000007101925068                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710192506C                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101925070                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007101925074                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007101925078                 LDR             X8, [X8,#8]
.text:000000710192507C                 MOV             W3, #0x20
.text:0000007101925080                 BLR             X8
.text:0000007101925084                 ADRP            X19, #unk_71056A9C68@PAGE
.text:0000007101925088                 ADD             X19, X19, #unk_71056A9C68@PAGEOFF
.text:000000710192508C                 STP             X23, X0, [X19]
.text:0000007101925090                 LDR             X8, [X0]
.text:0000007101925094                 LDR             X8, [X8,#0x58]
.text:0000007101925098                 BLR             X8
```

Our base address is 0x56A9C68.

After next BLR we have an offset:
```asm
STR x0, [x19, #0x10]
```
so our final address is 0x56A9C68 + 0x10 = 0x56A9C78.<br>
If you use IDA, you will have already calculated pointer
```asm
.text:000000710192509C                 STR             X0, [X19,#(qword_71056A9C78 - 0x71056A9C68)]
```

The same way we're searching for 
```
t.MaxFPS
```
It should have 2 xrefs. We are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101E1D1C0                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101E1D1C4                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101E1D1C8                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E1D1CC                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E1D1D0                 LDR             X8, [X8,#8]
.text:0000007101E1D1D4                 MOV             W3, WZR
.text:0000007101E1D1D8                 BLR             X8
.text:0000007101E1D1DC                 ADRP            X19, #unk_71056D3E90@PAGE
.text:0000007101E1D1E0                 ADD             X19, X19, #unk_71056D3E90@PAGEOFF
.text:0000007101E1D1E4                 ADRP            X8, #off_71044FE1B0@PAGE
.text:0000007101E1D1E8                 ADD             X8, X8, #off_71044FE1B0@PAGEOFF
.text:0000007101E1D1EC                 STP             X8, X0, [X19]
.text:0000007101E1D1F0                 LDR             X8, [X0]
.text:0000007101E1D1F4                 LDR             X8, [X8,#0x58]
.text:0000007101E1D1F8                 BLR             X8
.text:0000007101E1D1FC                 STR             X0, [X19,#(qword_71056D3EA0 - 0x71056D3E90)]
```
So our second final address is 0x56D3EA0.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget via config file is 30.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget ((1000/FPS) * 0.9)
  -
    type: write
    address: [MAIN, 0x56A9C78, 0]
    value_type: float
    value: [60, 60]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x56D3EA0, 0]
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
    address: [MAIN, 0x56A9C78, 0]
    value_type: float
    value: [30, 30]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x56D3EA0, 0]
    value_type: float
    value: [0, 0]

```
