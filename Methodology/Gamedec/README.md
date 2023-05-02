# Gamedec - Definitive Edition

> Game info

TitleID: `01002A501869E000`<br>
Explanation based on:
- Internal version: `1.3.0`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `BFA92380757EF97D`
- Engine: `Unreal Engine 4.26.2`

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
.text:0000007102C7099C                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102C709A0                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102C709A4                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102C709A8                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102C709AC                 LDR             X8, [X8,#0x10]
.text:0000007102C709B0                 MOV             W3, #0x20
.text:0000007102C709B4                 BLR             X8
.text:0000007102C709B8                 ADRP            X19, #unk_7108A9A428@PAGE
.text:0000007102C709BC                 ADD             X19, X19, #unk_7108A9A428@PAGEOFF
.text:0000007102C709C0                 STP             X24, X0, [X19]
.text:0000007102C709C4                 LDR             X8, [X0]
.text:0000007102C709C8                 LDR             X8, [X8,#0x68]
.text:0000007102C709CC                 BLR             X8
.text:0000007102C709D0                 STR             X0, [X19,#(qword_7108A9A438 - 0x7108A9A428)]
```

So first final address is stored at 0x8A9A438.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007103178314                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007103178318                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:000000710317831C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103178320                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103178324                 LDR             X8, [X8,#0x10]
.text:0000007103178328                 MOV             W3, WZR
.text:000000710317832C                 BLR             X8
.text:0000007103178330                 ADRP            X19, #unk_7108AC77F8@PAGE
.text:0000007103178334                 ADD             X19, X19, #unk_7108AC77F8@PAGEOFF
.text:0000007103178338                 ADRP            X8, #off_710760BB00@PAGE
.text:000000710317833C                 ADD             X8, X8, #off_710760BB00@PAGEOFF
.text:0000007103178340                 STP             X8, X0, [X19]
.text:0000007103178344                 LDR             X8, [X0]
.text:0000007103178348                 LDR             X8, [X8,#0x68]
.text:000000710317834C                 BLR             X8
.text:0000007103178350                 STR             X0, [X19,#(qword_7108AC7808 - 0x7108AC77F8)]
```
So our second final address is 0x8AC7808.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x8A9A438, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x8AC7808, 0]
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
    address: [MAIN, 0x8A9A438, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value is 30)
  -
    type: write
    address: [MAIN, 0x8AC7808, 0]
    value_type: float
    value: [0, 0]

```