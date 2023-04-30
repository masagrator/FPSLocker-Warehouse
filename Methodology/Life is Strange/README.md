# Life is Strange Remastered

> Game info

TitleID: `0100DC301186A000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `EE295EAAEA7D31E4`
- Engine: `Unreal Engine 4.23.1`

> Details

Plugin alone can set FPS above 30, but because of dynamic resolution set to 33.33 ms performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101B9A254                 ADRP            X1, #aRDynamicresFra_1@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B9A258                 ADD             X1, X1, #aRDynamicresFra_1@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B9A25C                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007101B9A260                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007101B9A264                 MOV             W3, #0x20
.text:0000007101B9A268                 BLR             X8
.text:0000007101B9A26C                 ADRP            X19, #qword_710674AF08@PAGE
.text:0000007101B9A270                 ADD             X19, X19, #qword_710674AF08@PAGEOFF
.text:0000007101B9A274                 STP             X23, X0, [X19]
.text:0000007101B9A278                 LDR             X8, [X0]
.text:0000007101B9A27C                 LDR             X8, [X8,#0x58]
.text:0000007101B9A280                 BLR             X8
.text:0000007101B9A284                 STR             X0, [X19,#(qword_710674AF18 - 0x710674AF08)]
```

So first final address is stored at 0x674AF18.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071020CB824                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071020CB828                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071020CB82C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071020CB830                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071020CB834                 MOV             W3, WZR
.text:00000071020CB838                 BLR             X8
.text:00000071020CB83C                 ADRP            X19, #qword_71067758B0@PAGE
.text:00000071020CB840                 ADD             X19, X19, #qword_71067758B0@PAGEOFF
.text:00000071020CB844                 ADRP            X8, #off_7104CDE1B0@PAGE
.text:00000071020CB848                 ADD             X8, X8, #off_7104CDE1B0@PAGEOFF
.text:00000071020CB84C                 STP             X8, X0, [X19]
.text:00000071020CB850                 LDR             X8, [X0]
.text:00000071020CB854                 LDR             X8, [X8,#0x58]
.text:00000071020CB858                 BLR             X8
.text:00000071020CB85C                 STR             X0, [X19,#(qword_71067758C0 - 0x71067758B0)]
```
So our second final address is 0x67758C0.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x674AF18, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x67758C0, 0]
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
    address: [MAIN, 0x674AF18, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x67758C0, 0]
    value_type: float
    value: [0, 0]

```