# WRC9

> Game info

TitleID: `01001A0011798000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `66B2DEA98B5CDF65`
- Engine: `KTEngine`

> Details

Game has broken vsync lock and that's why it's technically unlocked 60 FPS, but game graphically is targeting 30 FPS (dynamic resolution target is set to 31 ms), so it's hard to get 60 FPS without graphics tweaks. We will be patching that.

---

# How to find offsets

We need to use disassembler in this case. I will be using IDA because it will calculate offsets for us.

We need to find string:
```
OptimalFrameDuration_ms
```

And go to its only xref.

Below xref at register W20 it stores an executable default value.
We need to search where this W20 is written. It will be a second `STR W20`.

Piece of function looks like this:
```asm
.text:00000071009EE634                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:00000071009EE638                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:00000071009EE63C                 MOV             X0, X28
.text:00000071009EE640                 MOV             X2, X23
.text:00000071009EE644                 MOV             W3, #3
.text:00000071009EE648                 BL              sub_7100BE0450
.text:00000071009EE64C                 MOV             X9, #0x3333333333333333
.text:00000071009EE650                 MOVK            X9, #0x4205,LSL#16
.text:00000071009EE654                 ADD             X8, X19, #0x6F4
.text:00000071009EE658                 MOV             W20, #0x3333
.text:00000071009EE65C                 MOVK            W20, #0x4205,LSL#16
.text:00000071009EE660                 STR             X24, [X19,#(qword_71027C4A90 - 0x71027C4420)]
.text:00000071009EE664                 MOVK            X9, #0x4205,LSL#48
.text:00000071009EE668                 MOV             X0, XZR
.text:00000071009EE66C                 STR             X9, [X8]
.text:00000071009EE670                 STR             W20, [X19,#(dword_71027C4B30 - 0x71027C4420)]
.text:00000071009EE674                 STR             W22, [X19,#(dword_71027C4B24 - 0x71027C4420)]
.text:00000071009EE678                 STR             X21, [X19,#(qword_71027C4B38 - 0x71027C4420)]
.text:00000071009EE67C                 STR             X27, [X19,#(qword_71027C4B40 - 0x71027C4420)]
.text:00000071009EE680                 BL              sub_7100BE6E30
.text:00000071009EE684                 LDR             X0, [X19,#(qword_71027C4A98 - 0x71027C4420)]
.text:00000071009EE688                 STR             XZR, [X19,#(qword_71027C4A98 - 0x71027C4420)]
.text:00000071009EE68C                 BL              sub_7100BE6E60
.text:00000071009EE690                 LDR             X8, [X19,#(qword_71027C4A90 - 0x71027C4420)]
.text:00000071009EE694                 STRB            WZR, [X19,#(byte_71027C4B48 - 0x71027C4420)]
.text:00000071009EE698                 STRB            WZR, [X19,#(byte_71027C4B36 - 0x71027C4420)]
.text:00000071009EE69C                 STR             W20, [X19,#(dword_71027C4B0C - 0x71027C4420)]
```

So float we want is stored at MAIN+0x27C4B0C.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = (1000/FPS) - (0.07 * (1000/30)
  -
    type: write
    address: [MAIN, 0x27C4B0C]
    value_type: float
    value: 64.333333
```