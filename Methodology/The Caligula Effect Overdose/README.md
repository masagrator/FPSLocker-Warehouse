# The Caligula Effect: Overdose

> Game info

TitleID: `010069100B7F0000`<br>
Explanation based on:
- Internal version: `1.01`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `A953B35A45BEA33D`
- Engine: `Unreal Engine 4.20.3`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101B032B4                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B032B8                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B032BC                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007101B032C0                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007101B032C4                 MOV             W3, #0x20
.text:0000007101B032C8                 BLR             X8
.text:0000007101B032CC                 ADD             X20, X21, #0x10
.text:0000007101B032D0                 STR             X0, [X27,#(qword_7105CF2528 - 0x7105CF1AB0)]
.text:0000007101B032D4                 ADD             X19, X27, #0xA70
.text:0000007101B032D8                 STR             X20, [X27,#(qword_7105CF2520 - 0x7105CF1AB0)]
.text:0000007101B032DC                 LDR             X8, [X0]
.text:0000007101B032E0                 LDR             X8, [X8,#0x48]
.text:0000007101B032E4                 BLR             X8
.text:0000007101B032E8                 STR             X0, [X27,#(qword_7105CF2530 - 0x7105CF1AB0)]
```

So first final address is stored at 0x5CF2530.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071020AEC84                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071020AEC88                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071020AEC8C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071020AEC90                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071020AEC94                 MOV             W3, WZR
.text:00000071020AEC98                 BLR             X8
.text:00000071020AEC9C                 ADRP            X8, #qword_7104EB8108@PAGE
.text:00000071020AECA0                 ADD             X8, X8, #qword_7104EB8108@PAGEOFF
.text:00000071020AECA4                 ADD             X8, X8, #0x10
.text:00000071020AECA8                 STR             X0, [X23,#(qword_7105D170A0 - 0x7105D16930)]
.text:00000071020AECAC                 ADD             X19, X23, #0x768
.text:00000071020AECB0                 STR             X8, [X23,#(qword_7105D17098 - 0x7105D16930)]
.text:00000071020AECB4                 LDR             X8, [X0]
.text:00000071020AECB8                 LDR             X8, [X8,#0x48]
.text:00000071020AECBC                 BLR             X8
.text:00000071020AECC0                 STR             X0, [X23,#(qword_7105D170A8 - 0x7105D16930)]
```
So our second final address is 0x5D170A8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to one decimal
  -
    type: write
    address: [MAIN, 0x5CF2530, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x5D170A8, 0]
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
    address: [MAIN, 0x5CF2530, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x5D170A8, 0]
    value_type: float
    value: [0, 0]

```
