# The Stretchers

> Game info

TitleID: `0100AA400A238000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `14D7D1537BD5A986`
- Engine: `Unreal Engine 4.20.2`

> Details

Game is using internal FPS lock, and dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101B312D4                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B312D8                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101B312DC                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007101B312E0                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007101B312E4                 MOV             W3, #0x20
.text:0000007101B312E8                 BLR             X8
.text:0000007101B312EC                 ADD             X20, X21, #0x10
.text:0000007101B312F0                 STR             X0, [X27,#(qword_7105C63548 - 0x7105C62AD0)]
.text:0000007101B312F4                 ADD             X19, X27, #0xA70
.text:0000007101B312F8                 STR             X20, [X27,#(qword_7105C63540 - 0x7105C62AD0)]
.text:0000007101B312FC                 LDR             X8, [X0]
.text:0000007101B31300                 LDR             X8, [X8,#0x48]
.text:0000007101B31304                 BLR             X8
.text:0000007101B31308                 STR             X0, [X27,#(qword_7105C63550 - 0x7105C62AD0)]
```

So first final address is stored at 0x5C63550.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071020DE614                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071020DE618                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071020DE61C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071020DE620                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071020DE624                 MOV             W3, WZR
.text:00000071020DE628                 BLR             X8
.text:00000071020DE62C                 ADRP            X8, #unk_7104DCE7E0@PAGE
.text:00000071020DE630                 ADD             X8, X8, #unk_7104DCE7E0@PAGEOFF
.text:00000071020DE634                 ADD             X8, X8, #0x10
.text:00000071020DE638                 STR             X0, [X23,#(qword_7105C880D0 - 0x7105C87960)]
.text:00000071020DE63C                 ADD             X19, X23, #0x768
.text:00000071020DE640                 STR             X8, [X23,#(qword_7105C880C8 - 0x7105C87960)]
.text:00000071020DE644                 LDR             X8, [X0]
.text:00000071020DE648                 LDR             X8, [X8,#0x48]
.text:00000071020DE64C                 BLR             X8
.text:00000071020DE650                 STR             X0, [X23,#(qword_7105C880D8 - 0x7105C87960)]
```
So our second final address is 0x5C880D8.

Each of our final address stores pointer that points to two floats. t.MaxFPS is set to 30. r.DynamicRes.FrameTimeBudget is 33.3.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to 1 decimals
  -
    type: write
    address: [MAIN, 0x5C63550, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x5C880D8, 0]
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
    address: [MAIN, 0x5C63550, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x5C880D8, 0]
    value_type: float
    value: [30, 30]

```
