# Destiny Connect: Tick-Tock Travelers

> Game info

TitleID: `010069500DD86000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `5AD84EFD9D28FDDE`
- Engine: `Unreal Engine 4.20.2`

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
.text:000000710195E2B4                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710195E2B8                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710195E2BC                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710195E2C0                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710195E2C4                 MOV             W3, #0x20
.text:000000710195E2C8                 BLR             X8
.text:000000710195E2CC                 ADD             X20, X21, #0x10
.text:000000710195E2D0                 STR             X0, [X27,#(qword_7105934538 - 0x7105933AC0)]
.text:000000710195E2D4                 ADD             X19, X27, #0xA70
.text:000000710195E2D8                 STR             X20, [X27,#(qword_7105934530 - 0x7105933AC0)]
.text:000000710195E2DC                 LDR             X8, [X0]
.text:000000710195E2E0                 LDR             X8, [X8,#0x48]
.text:000000710195E2E4                 BLR             X8
.text:000000710195E2E8                 STR             X0, [X27,#(qword_7105934540 - 0x7105933AC0)]
```

So first final address is stored at 0x5934540.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101F055A4                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101F055A8                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101F055AC                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101F055B0                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101F055B4                 MOV             W3, WZR
.text:0000007101F055B8                 BLR             X8
.text:0000007101F055BC                 ADRP            X8, #unk_7104B73650@PAGE
.text:0000007101F055C0                 ADD             X8, X8, #unk_7104B73650@PAGEOFF
.text:0000007101F055C4                 ADD             X8, X8, #0x10
.text:0000007101F055C8                 STR             X0, [X23,#(qword_71059590A0 - 0x7105958930)]
.text:0000007101F055CC                 ADD             X19, X23, #0x768
.text:0000007101F055D0                 STR             X8, [X23,#(qword_7105959098 - 0x7105958930)]
.text:0000007101F055D4                 LDR             X8, [X0]
.text:0000007101F055D8                 LDR             X8, [X8,#0x48]
.text:0000007101F055DC                 BLR             X8
.text:0000007101F055E0                 STR             X0, [X23,#(qword_71059590A8 - 0x7105958930)]
```
So our second final address is 0x59590A8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) cutted to one decimal
  -
    type: write
    address: [MAIN, 0x5934540, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x59590A8, 0]
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
    address: [MAIN, 0x5934540, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x59590A8, 0]
    value_type: float
    value: [0, 0]
```
