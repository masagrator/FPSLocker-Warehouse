# Grand Theft Auto: San Andreas - Definitive Edition

> Game info

TitleID: `010065A014024000`<br>
Explanation based on:
- Internal version: `1.0.7`, 
- Nintendo version ID: `v7`/`v458752`
- BID: `6FB56071CCB321B6`
- Engine: `Unreal Engine 4.26.1`

> Details

Game is using internal FPS lock, and dynamic resolution set to 36.5 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

If it has more than 1 xref, we are interested in the one that has description pointer loaded.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:00000071039C68F8                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071039C68FC                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071039C6900                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:00000071039C6904                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071039C6908                 MOV             W3, #0x20
.text:00000071039C690C                 BLR             X8
.text:00000071039C6910                 ADRP            X19, #qword_7107952288@PAGE
.text:00000071039C6914                 ADD             X19, X19, #qword_7107952288@PAGEOFF
.text:00000071039C6918                 STP             X24, X0, [X19]
.text:00000071039C691C                 LDR             X8, [X0]
.text:00000071039C6920                 LDR             X8, [X8,#0x68]
.text:00000071039C6924                 BLR             X8
.text:00000071039C6928                 STR             X0, [X19,#(qword_7107952298 - 0x7107952288)]
```

So first final address is stored at 0x7952298.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710408A820                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:000000710408A824                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:000000710408A828                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:000000710408A82C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710408A830                 MOV             W3, WZR
.text:000000710408A834                 BLR             X8
.text:000000710408A838                 ADRP            X19, #qword_7107976FD0@PAGE
.text:000000710408A83C                 ADD             X19, X19, #qword_7107976FD0@PAGEOFF
.text:000000710408A840                 ADRP            X8, #off_71061AC748@PAGE
.text:000000710408A844                 ADD             X8, X8, #off_71061AC748@PAGEOFF
.text:000000710408A848                 STP             X8, X0, [X19]
.text:000000710408A84C                 LDR             X8, [X0]
.text:000000710408A850                 LDR             X8, [X8,#0x68]
.text:000000710408A854                 BLR             X8
.text:000000710408A858                 STR             X0, [X19,#(qword_7107976FE0 - 0x7107976FD0)]
```
So our second final address is 0x7976FE0.

Each of our final address stores pointer that points to two floats. t.MaxFPS via config is 30. r.DynamicRes.FrameTimeBudget via config is 36.5. Instead we will use a different calculation for each FPS.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to one decimal
  -
    type: write
    address: [MAIN, 0x7952298, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7976FE0, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # r.DynamicRes.FrameTimeBudget (default value is 36.5)
  -
    type: write
    address: [MAIN, 0x7952298, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7976FE0, 0]
    value_type: float
    value: [30, 30]

```
