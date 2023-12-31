# Mortal Shell

> Game info

TitleID: `0100154019A7C000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `BE2D1A84420113EC`
- Engine: `Unreal Engine 4.25.0`

> Details

Game runs on unlocked framerate from main menu forward, but because of dynamic resolution set to 33.33 ms game is clearly targeting 30 FPS. Requires patch to make running at higher framerates easier. And since we are doing it, we will also search for internal FPS locker.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007102F2D514                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102F2D518                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102F2D51C                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102F2D520                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102F2D524                 LDR             X8, [X8,#0x10]
.text:0000007102F2D528                 MOV             W3, #0x20
.text:0000007102F2D52C                 BLR             X8
.text:0000007102F2D530                 ADRP            X19, #qword_7106ACCBC8@PAGE
.text:0000007102F2D534                 ADD             X19, X19, #qword_7106ACCBC8@PAGEOFF
.text:0000007102F2D538                 STP             X25, X0, [X19]
.text:0000007102F2D53C                 LDR             X8, [X0]
.text:0000007102F2D540                 LDR             X8, [X8,#0x68]
.text:0000007102F2D544                 BLR             X8
.text:0000007102F2D548                 STR             X0, [X19,#(qword_7106ACCBD8 - 0x7106ACCBC8)]
```

So first final address is stored at 0x6ACCBD8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071035C72D0                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071035C72D4                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071035C72D8                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071035C72DC                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071035C72E0                 LDR             X8, [X8,#0x10]
.text:00000071035C72E4                 MOV             W3, WZR
.text:00000071035C72E8                 BLR             X8
.text:00000071035C72EC                 ADRP            X19, #qword_7106AEF750@PAGE
.text:00000071035C72F0                 ADD             X19, X19, #qword_7106AEF750@PAGEOFF
.text:00000071035C72F4                 ADRP            X8, #off_710581C530@PAGE
.text:00000071035C72F8                 ADD             X8, X8, #off_710581C530@PAGEOFF
.text:00000071035C72FC                 STP             X8, X0, [X19]
.text:00000071035C7300                 LDR             X8, [X0]
.text:00000071035C7304                 LDR             X8, [X8,#0x68]
.text:00000071035C7308                 BLR             X8
.text:00000071035C730C                 STR             X0, [X19,#(qword_7106AEF760 - 0x7106AEF750)]
```
So our second final address is 0x6AEF760.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x6ACCBD8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x6AEF760, 0]
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
    address: [MAIN, 0x6ACCBD8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x6AEF760, 0]
    value_type: float
    value: [0, 0]

```
