# Tony Hawk's Pro Skater 1 + 2

> Game info

TitleID: `0100CC00102B4000`<br>
Explanation based on:
- Internal version: `1.0.3`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `8AFCBE6A930CD42E`
- Engine: `Unreal Engine 4.24.3`

> Details

Game is using internal FPS Lock, plus because game is using dynamic resolution set to 33.3333 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710354C540                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710354C544                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710354C548                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710354C54C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710354C550                 LDR             X8, [X8,#0x10]
.text:000000710354C554                 MOV             W3, #0x20
.text:000000710354C558                 BLR             X8
.text:000000710354C55C                 ADRP            X19, #qword_7107DB2AA0@PAGE
.text:000000710354C560                 ADD             X19, X19, #qword_7107DB2AA0@PAGEOFF
.text:000000710354C564                 STP             X20, X0, [X19]
.text:000000710354C568                 LDR             X8, [X0]
.text:000000710354C56C                 LDR             X8, [X8,#0x68]
.text:000000710354C570                 BLR             X8
.text:000000710354C574                 STR             X0, [X19,#(qword_7107DB2AB0 - 0x7107DB2AA0)]
```

So first final address is stored at 0x7DB2AB0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007103BEAA44                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007103BEAA48                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007103BEAA4C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103BEAA50                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103BEAA54                 LDR             X8, [X8,#0x10]
.text:0000007103BEAA58                 MOV             W3, WZR
.text:0000007103BEAA5C                 BLR             X8
.text:0000007103BEAA60                 ADRP            X19, #qword_7107DDEF80@PAGE
.text:0000007103BEAA64                 ADD             X19, X19, #qword_7107DDEF80@PAGEOFF
.text:0000007103BEAA68                 STP             X26, X0, [X19]
.text:0000007103BEAA6C                 LDR             X8, [X0]
.text:0000007103BEAA70                 LDR             X8, [X8,#0x68]
.text:0000007103BEAA74                 BLR             X8
.text:0000007103BEAA78                 STR             X0, [X19,#(qword_7107DDEF90 - 0x7107DDEF80)]
```
So our second final address is 0x7DDEF90.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.3333.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to 4 decimals
  -
    type: write
    address: [MAIN, 0x7DB2AB0, 0]
    value_type: float
    value: [66.6666, 66.6666]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7DDEF90, 0]
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
    address: [MAIN, 0x7DB2AB0, 0]
    value_type: float
    value: [33.3333, 33.3333]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7DDEF90, 0]
    value_type: float
    value: [30, 30]

```
