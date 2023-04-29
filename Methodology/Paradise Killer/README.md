# Paradise Killer

> Game info

TitleID: `01007FB010DC8000`<br>
Explanation based on:
- Internal version: `1.2.1`, 
- Nintendo version ID: `v7`/`v458752`
- BID: `D3744AF2C376CDC4`
- Engine: `Unreal Engine 4.27.0`

> Details

Plugin alone can set FPS above 30, but because of dynamic resolution set to 33.33 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007102416550                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102416554                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102416558                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710241655C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102416560                 LDR             X8, [X8,#0x10]
.text:0000007102416564                 MOV             W3, #0x20
.text:0000007102416568                 BLR             X8
.text:000000710241656C                 ADRP            X19, #qword_710715EDA8@PAGE
.text:0000007102416570                 ADD             X19, X19, #qword_710715EDA8@PAGEOFF
.text:0000007102416574                 STP             X24, X0, [X19]
.text:0000007102416578                 LDR             X8, [X0]
.text:000000710241657C                 LDR             X8, [X8,#0x68]
.text:0000007102416580                 BLR             X8
.text:0000007102416584                 STR             X0, [X19,#(qword_710715EDB8 - 0x710715EDA8)]
```

So first final address is stored at 0x715EDB8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102942FFC                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007102943000                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102943004                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007102943008                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710294300C                 LDR             X8, [X8,#0x10]
.text:0000007102943010                 MOV             W3, WZR
.text:0000007102943014                 BLR             X8
.text:0000007102943018                 ADRP            X19, #qword_710718C9A8@PAGE
.text:000000710294301C                 ADD             X19, X19, #qword_710718C9A8@PAGEOFF
.text:0000007102943020                 ADRP            X8, #off_7105CAC8B8@PAGE
.text:0000007102943024                 ADD             X8, X8, #off_7105CAC8B8@PAGEOFF
.text:0000007102943028                 STP             X8, X0, [X19]
.text:000000710294302C                 LDR             X8, [X0]
.text:0000007102943030                 LDR             X8, [X8,#0x68]
.text:0000007102943034                 BLR             X8
.text:0000007102943038                 STR             X0, [X19,#(qword_710718C9B8 - 0x710718C9A8)]
```
So our second final address is 0x718C9B8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x715EDB8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x718C9B8, 0]
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
    address: [MAIN, 0x715EDB8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x718C9B8, 0]
    value_type: float
    value: [0, 0]

```