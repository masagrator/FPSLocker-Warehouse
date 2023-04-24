# Ultra Age

> Game info

TitleID: `01008D4015904000`<br>
Explanation based on:
- Internal version: `2.0.4`, 
- Nintendo version ID: `v7`/`v458752`
- BID: `CA77083E259D87A2`
- Engine: `Unreal Engine 4.27.2`

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
.text:0000007102C0819C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102C081A0                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102C081A4                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102C081A8                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102C081AC                 LDR             X8, [X8,#0x10]
.text:0000007102C081B0                 MOV             W3, #0x20
.text:0000007102C081B4                 BLR             X8
.text:0000007102C081B8                 ADRP            X19, #qword_7107984A38@PAGE
.text:0000007102C081BC                 ADD             X19, X19, #qword_7107984A38@PAGEOFF
.text:0000007102C081C0                 STP             X24, X0, [X19]
.text:0000007102C081C4                 LDR             X8, [X0]
.text:0000007102C081C8                 LDR             X8, [X8,#0x68]
.text:0000007102C081CC                 BLR             X8
.text:0000007102C081D0                 STR             X0, [X19,#(qword_7107984A48 - 0x7107984A38)]
```

So first final address is stored at 0x7984A48.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710312F4DC                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:000000710312F4E0                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:000000710312F4E4                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:000000710312F4E8                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710312F4EC                 LDR             X8, [X8,#0x10]
.text:000000710312F4F0                 MOV             W3, WZR
.text:000000710312F4F4                 BLR             X8
.text:000000710312F4F8                 ADRP            X19, #qword_71079B22E8@PAGE
.text:000000710312F4FC                 ADD             X19, X19, #qword_71079B22E8@PAGEOFF
.text:000000710312F500                 ADRP            X8, #off_71063B18B8@PAGE
.text:000000710312F504                 ADD             X8, X8, #off_71063B18B8@PAGEOFF
.text:000000710312F508                 STP             X8, X0, [X19]
.text:000000710312F50C                 LDR             X8, [X0]
.text:000000710312F510                 LDR             X8, [X8,#0x68]
.text:000000710312F514                 BLR             X8
.text:000000710312F518                 STR             X0, [X19,#(qword_71079B22F8 - 0x71079B22E8)]
```
So our second final address is 0x79B22F8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x7984A48, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x79B22F8, 0]
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
    address: [MAIN, 0x7984A48, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x79B22F8, 0]
    value_type: float
    value: [0, 0]

```