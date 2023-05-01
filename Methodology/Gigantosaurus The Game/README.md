# Gigantosaurus The Game

> Game info

TitleID: `01002C400E526000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `EF7B49570430043E`
- Engine: `Unreal Engine 4.23.1`

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
.text:000000710172DE4C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710172DE50                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710172DE54                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710172DE58                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710172DE5C                 MOV             W3, #0x20
.text:000000710172DE60                 BLR             X8
.text:000000710172DE64                 ADRP            X19, #qword_71052F20D8@PAGE
.text:000000710172DE68                 ADD             X19, X19, #qword_71052F20D8@PAGEOFF
.text:000000710172DE6C                 STP             X23, X0, [X19]
.text:000000710172DE70                 LDR             X8, [X0]
.text:000000710172DE74                 LDR             X8, [X8,#0x58]
.text:000000710172DE78                 BLR             X8
.text:000000710172DE7C                 STR             X0, [X19,#(qword_71052F20E8 - 0x71052F20D8)]
```

So first final address is stored at 0x52F20E8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101C4345C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101C43460                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101C43464                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101C43468                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101C4346C                 MOV             W3, WZR
.text:0000007101C43470                 BLR             X8
.text:0000007101C43474                 ADRP            X19, #qword_710531C2F0@PAGE
.text:0000007101C43478                 ADD             X19, X19, #qword_710531C2F0@PAGEOFF
.text:0000007101C4347C                 ADRP            X8, #off_71041D1270@PAGE
.text:0000007101C43480                 ADD             X8, X8, #off_71041D1270@PAGEOFF
.text:0000007101C43484                 STP             X8, X0, [X19]
.text:0000007101C43488                 LDR             X8, [X0]
.text:0000007101C4348C                 LDR             X8, [X8,#0x58]
.text:0000007101C43490                 BLR             X8
.text:0000007101C43494                 STR             X0, [X19,#(qword_710531C300 - 0x710531C2F0)]
```
So our second final address is 0x531C300.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x52F20E8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x531C300, 0]
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
    address: [MAIN, 0x52F20E8, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value is 30)
  -
    type: write
    address: [MAIN, 0x531C300, 0]
    value_type: float
    value: [0, 0]

```