# Soundfall

> Game info

TitleID: `0100B7A01386E000`<br>
Explanation based on:
- Internal version: `1.3.17957`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `39F1BCCB912A12DF`
- Engine: `Unreal Engine 4.27.1`

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
.text:00000071027E7EFC                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071027E7F00                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071027E7F04                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:00000071027E7F08                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071027E7F0C                 LDR             X8, [X8,#0x10]
.text:00000071027E7F10                 MOV             W3, #0x20
.text:00000071027E7F14                 BLR             X8
.text:00000071027E7F18                 ADRP            X19, #qword_71075E5BE8@PAGE
.text:00000071027E7F1C                 ADD             X19, X19, #qword_71075E5BE8@PAGEOFF
.text:00000071027E7F20                 STP             X24, X0, [X19]
.text:00000071027E7F24                 LDR             X8, [X0]
.text:00000071027E7F28                 LDR             X8, [X8,#0x68]
.text:00000071027E7F2C                 BLR             X8
.text:00000071027E7F30                 STR             X0, [X19,#(qword_71075E5BF8 - 0x71075E5BE8)]
```

So first final address is stored at 0x75E5BF8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102D40C24                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102D40C28                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102D40C2C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D40C30                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102D40C34                 LDR             X8, [X8,#0x10]
.text:0000007102D40C38                 MOV             W3, WZR
.text:0000007102D40C3C                 BLR             X8
.text:0000007102D40C40                 ADRP            X19, #qword_7107613BE8@PAGE
.text:0000007102D40C44                 ADD             X19, X19, #qword_7107613BE8@PAGEOFF
.text:0000007102D40C48                 ADRP            X8, #off_71061968B8@PAGE
.text:0000007102D40C4C                 ADD             X8, X8, #off_71061968B8@PAGEOFF
.text:0000007102D40C50                 STP             X8, X0, [X19]
.text:0000007102D40C54                 LDR             X8, [X0]
.text:0000007102D40C58                 LDR             X8, [X8,#0x68]
.text:0000007102D40C5C                 BLR             X8
.text:0000007102D40C60                 STR             X0, [X19,#(qword_7107613BF8 - 0x7107613BE8)]
```
So our second final address is 0x7613BF8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x75E5BF8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7613BF8, 0]
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
    address: [MAIN, 0x75E5BF8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7613BF8, 0]
    value_type: float
    value: [0, 0]

```