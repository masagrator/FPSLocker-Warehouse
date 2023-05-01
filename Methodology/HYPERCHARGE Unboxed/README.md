# HYPERCHARGE: Unboxed

> Game info

TitleID: `0100A8B00F0B4000`<br>
Explanation based on:
- Internal version: `0.1.2341.233`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `92511355705EA8C5`
- Engine: `Unreal Engine 4.22.2`

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
.text:000000710211B6FC                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710211B700                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710211B704                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710211B708                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710211B70C                 MOV             W3, #0x20
.text:000000710211B710                 BLR             X8
.text:000000710211B714                 ADRP            X19, #qword_71066951A0@PAGE
.text:000000710211B718                 ADD             X19, X19, #qword_71066951A0@PAGEOFF
.text:000000710211B71C                 STP             X20, X0, [X19]
.text:000000710211B720                 LDR             X8, [X0]
.text:000000710211B724                 LDR             X8, [X8,#0x48]
.text:000000710211B728                 BLR             X8
.text:000000710211B72C                 STR             X0, [X19,#(qword_71066951B0 - 0x71066951A0)]
```

So first final address is stored at 0x66951B0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102603830                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102603834                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102603838                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:000000710260383C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102603840                 MOV             W3, WZR
.text:0000007102603844                 BLR             X8
.text:0000007102603848                 ADRP            X19, #qword_71066BBA20@PAGE
.text:000000710260384C                 ADD             X19, X19, #qword_71066BBA20@PAGEOFF
.text:0000007102603850                 ADRP            X8, #off_71055F6AB8@PAGE
.text:0000007102603854                 ADD             X8, X8, #off_71055F6AB8@PAGEOFF
.text:0000007102603858                 STP             X8, X0, [X19]
.text:000000710260385C                 LDR             X8, [X0]
.text:0000007102603860                 LDR             X8, [X8,#0x48]
.text:0000007102603864                 BLR             X8
.text:0000007102603868                 STR             X0, [X19,#(qword_71066BBA30 - 0x71066BBA20)]
```
So our second final address is 0x66BBA30.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x66951B0, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x66BBA30, 0]
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
    address: [MAIN, 0x66951B0, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x66BBA30, 0]
    value_type: float
    value: [0, 0]

```