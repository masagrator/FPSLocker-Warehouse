# It Takes Two

> Game info

TitleID: `0100956016464000`<br>
Explanation based on:
- Internal version: `1.5`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `F9C83728910E28A4`
- Engine: `Unreal Engine 4.26.1`

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
.text:0000007102550F10                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102550F14                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102550F18                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102550F1C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102550F20                 LDR             X8, [X8,#0x10]
.text:0000007102550F24                 MOV             W3, #0x20
.text:0000007102550F28                 BLR             X8
.text:0000007102550F2C                 ADRP            X19, #qword_71071160D0@PAGE
.text:0000007102550F30                 ADD             X19, X19, #qword_71071160D0@PAGEOFF
.text:0000007102550F34                 STP             X21, X0, [X19]
.text:0000007102550F38                 LDR             X8, [X0]
.text:0000007102550F3C                 LDR             X8, [X8,#0x68]
.text:0000007102550F40                 BLR             X8
.text:0000007102550F44                 STR             X0, [X19,#(qword_71071160E0 - 0x71071160D0)]
```

So first final address is stored at 0x71160E0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102B121C0                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102B121C4                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102B121C8                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102B121CC                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102B121D0                 LDR             X8, [X8,#0x10]
.text:0000007102B121D4                 MOV             W3, WZR
.text:0000007102B121D8                 BLR             X8
.text:0000007102B121DC                 ADRP            X19, #qword_71071C39E0@PAGE
.text:0000007102B121E0                 ADD             X19, X19, #qword_71071C39E0@PAGEOFF
.text:0000007102B121E4                 ADRP            X8, #off_7105C118A8@PAGE
.text:0000007102B121E8                 ADD             X8, X8, #off_7105C118A8@PAGEOFF
.text:0000007102B121EC                 STP             X8, X0, [X19]
.text:0000007102B121F0                 LDR             X8, [X0]
.text:0000007102B121F4                 LDR             X8, [X8,#0x68]
.text:0000007102B121F8                 BLR             X8
.text:0000007102B121FC                 STR             X0, [X19,#(qword_71071C39F0 - 0x71071C39E0)]
```
So our second final address is 0x71C39F0.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimal
  -
    type: write
    address: [MAIN, 0x71160E0, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x71C39F0, 0]
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
    address: [MAIN, 0x71160E0, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x71C39F0, 0]
    value_type: float
    value: [0, 0]

```