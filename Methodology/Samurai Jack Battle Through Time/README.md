# Samurai Jack: Battle Through Time

> Game info

TitleID: `01006C600E46E000`<br>
Explanation based on:
- Internal version: `1.0.3`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `6D5DB3434CCF63F2`
- Engine: `Unreal Engine 4.22.3`

> Details

Game is using internal FPS lock + dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007100DC4F1C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007100DC4F20                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007100DC4F24                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007100DC4F28                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007100DC4F2C                 MOV             W3, #0x20
.text:0000007100DC4F30                 BLR             X8
.text:0000007100DC4F34                 ADRP            X19, #qword_7106FC5548@PAGE
.text:0000007100DC4F38                 ADD             X19, X19, #qword_7106FC5548@PAGEOFF
.text:0000007100DC4F3C                 STP             X21, X0, [X19]
.text:0000007100DC4F40                 LDR             X8, [X0]
.text:0000007100DC4F44                 LDR             X8, [X8,#0x48]
.text:0000007100DC4F48                 BLR             X8
.text:0000007100DC4F4C                 STR             X0, [X19,#(qword_7106FC5558 - 0x7106FC5548)]
```

So first final address is stored at 0x6FC5558.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007100DECDBC                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007100DECDC0                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007100DECDC4                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007100DECDC8                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007100DECDCC                 MOV             W3, WZR
.text:0000007100DECDD0                 BLR             X8
.text:0000007100DECDD4                 ADRP            X19, #qword_7106FEB018@PAGE
.text:0000007100DECDD8                 ADD             X19, X19, #qword_7106FEB018@PAGEOFF
.text:0000007100DECDDC                 ADRP            X8, #off_7105BBE580@PAGE
.text:0000007100DECDE0                 ADD             X8, X8, #off_7105BBE580@PAGEOFF
.text:0000007100DECDE4                 STP             X8, X0, [X19]
.text:0000007100DECDE8                 LDR             X8, [X0]
.text:0000007100DECDEC                 LDR             X8, [X8,#0x48]
.text:0000007100DECDF0                 BLR             X8
.text:0000007100DECDF4                 STR             X0, [X19,#(qword_7106FEB028 - 0x7106FEB018)]
```
So our second final address is 0x6FEB028.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimal
  -
    type: write
    address: [MAIN, 0x6FC5558, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x6FEB028, 0]
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
    address: [MAIN, 0x6FC5558, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value is 30)
  -
    type: write
    address: [MAIN, 0x6FEB028, 0]
    value_type: float
    value: [0, 0]

```