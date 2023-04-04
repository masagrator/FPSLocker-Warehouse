# What Remains of Edith Finch

> Game info

TitleID: `010038900DFE0000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `E9578A470B175851`
- Engine: `Unreal Engine 4.20.2`

> Details

Game is using internal FPS lock and is using dynamic resolution set to 33.3 ms. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below after first BLR we have base address
```asm
.text:00000071018AEFD8                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071018AEFDC                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071018AEFE0                 ADRP            X2, #aF_562@PAGE ; "F"
.text:00000071018AEFE4                 ADD             X2, X2, #aF_562@PAGEOFF ; "F"
.text:00000071018AEFE8                 MOV             W3, #0x20
.text:00000071018AEFEC                 BLR             X8
.text:00000071018AEFF0                 ADRP            X19, #unk_710532B390@PAGE
.text:00000071018AEFF4                 ADD             X19, X19, #unk_710532B390@PAGEOFF
.text:00000071018AEFF8                 STP             X20, X0, [X19]
.text:00000071018AEFFC                 LDR             X8, [X0]
.text:00000071018AF000                 LDR             X8, [X8,#0x48]
.text:00000071018AF004                 BLR             X8
```

Our base address is 0x532B390.

After next BLR we have an offset:
```asm
STR x0, [x19, #0x10]
```
so our final address is 0x532B390 + 0x10 = 0x532B3A0.<br>
If you use IDA, you will have already calculated pointer
```asm
.text:00000071018AF008                 STR             X0, [X19,#(qword_710532B3A0 - 0x710532B390)]
```

The same way we're searching for 
```
t.MaxFPS
```
It should have 2 xrefs. We are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101D55B34                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101D55B38                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101D55B3C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101D55B40                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101D55B44                 MOV             W3, WZR
.text:0000007101D55B48                 BLR             X8
.text:0000007101D55B4C                 ADRP            X19, #unk_7105350848@PAGE
.text:0000007101D55B50                 ADD             X19, X19, #unk_7105350848@PAGEOFF
.text:0000007101D55B54                 ADRP            X8, #off_7104328898@PAGE
.text:0000007101D55B58                 ADD             X8, X8, #off_7104328898@PAGEOFF
.text:0000007101D55B5C                 STP             X8, X0, [X19]
.text:0000007101D55B60                 LDR             X8, [X0]
.text:0000007101D55B64                 LDR             X8, [X8,#0x48]
.text:0000007101D55B68                 BLR             X8
.text:0000007101D55B6C                 STR             X0, [X19,#(qword_7105350858 - 0x7105350848)]
```
So our second final address is 0x5350858.

Each of our final address stores pointer that points to two floats. In config file t.MaxFPS is 30. r.DynamicRes.FrameTimeBudget by default is always 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget ((1000/FPS) * 0.945)
  -
    type: write
    address: [MAIN, 0x532B3A0, 0]
    value_type: float
    value: [63, 63]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x5350858, 0]
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
    address: [MAIN, 0x532B3A0, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x5350858, 0]
    value_type: float
    value: [30, 30]

```
