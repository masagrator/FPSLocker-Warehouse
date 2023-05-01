# Gigantosaurus: Dino Kart

> Game info

TitleID: `01001890167FE000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `EF7B49570430043E`
- Engine: `Unreal Engine 4.26.1`

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
.text:00000071022CAD0C                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071022CAD10                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071022CAD14                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:00000071022CAD18                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071022CAD1C                 LDR             X8, [X8,#0x10]
.text:00000071022CAD20                 MOV             W3, #0x20
.text:00000071022CAD24                 BLR             X8
.text:00000071022CAD28                 ADRP            X19, #qword_7106D196B8@PAGE
.text:00000071022CAD2C                 ADD             X19, X19, #qword_7106D196B8@PAGEOFF
.text:00000071022CAD30                 STP             X24, X0, [X19]
.text:00000071022CAD34                 LDR             X8, [X0]
.text:00000071022CAD38                 LDR             X8, [X8,#0x68]
.text:00000071022CAD3C                 BLR             X8
.text:00000071022CAD40                 STR             X0, [X19,#(qword_7106D196C8 - 0x7106D196B8)]
```

So first final address is stored at 0x6D196C8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071027D2414                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071027D2418                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071027D241C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071027D2420                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071027D2424                 LDR             X8, [X8,#0x10]
.text:00000071027D2428                 MOV             W3, WZR
.text:00000071027D242C                 BLR             X8
.text:00000071027D2430                 ADRP            X19, #qword_7106D46C48@PAGE
.text:00000071027D2434                 ADD             X19, X19, #qword_7106D46C48@PAGEOFF
.text:00000071027D2438                 ADRP            X8, #off_71058EA8A8@PAGE
.text:00000071027D243C                 ADD             X8, X8, #off_71058EA8A8@PAGEOFF
.text:00000071027D2440                 STP             X8, X0, [X19]
.text:00000071027D2444                 LDR             X8, [X0]
.text:00000071027D2448                 LDR             X8, [X8,#0x68]
.text:00000071027D244C                 BLR             X8
.text:00000071027D2450                 STR             X0, [X19,#(qword_7106D46C58 - 0x7106D46C48)]
```
So our second final address is 0x6D46C58.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 30. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x6D196C8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x6D46C58, 0]
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
    address: [MAIN, 0x6D196C8, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value is 30)
  -
    type: write
    address: [MAIN, 0x6D46C58, 0]
    value_type: float
    value: [0, 0]

```