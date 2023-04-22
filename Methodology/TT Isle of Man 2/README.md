# TT Isle of Man 2

> Game info

TitleID: `010000400F582000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `02F2E5C8CBF5A92F`
- Engine: `KTEngine`

> Details

Game has broken vsync lock and that's why it's technically unlocked 60 FPS, but game graphically is targeting 30 FPS (dynamic resolution target is set to 32 ms), so it's hard to get 60 FPS without graphics tweaks. We will be patching that.

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
.text:000000710066BBA4                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:000000710066BBA8                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:000000710066BBAC                 MOV             W3, #3
.text:000000710066BBB0                 MOV             X0, X28
.text:000000710066BBB4                 MOV             X2, X24
.text:000000710066BBB8                 BL              sub_7100837C90
.text:000000710066BBBC                 MOV             X9, #0x3333333333333333
.text:000000710066BBC0                 MOVK            X9, #0x4205,LSL#16
.text:000000710066BBC4                 ADD             X8, X19, #0x634
.text:000000710066BBC8                 MOV             W20, #0x3333
.text:000000710066BBCC                 MOVK            W20, #0x4205,LSL#16
.text:000000710066BBD0                 STR             X22, [X19,#(qword_7102153C80 - 0x71021536D0)]
.text:000000710066BBD4                 MOVK            X9, #0x4205,LSL#48
.text:000000710066BBD8                 MOV             X0, XZR
.text:000000710066BBDC                 STR             X9, [X8]
.text:000000710066BBE0                 STR             W20, [X19,#(dword_7102153D20 - 0x71021536D0)]
.text:000000710066BBE4                 STR             W23, [X19,#(dword_7102153D14 - 0x71021536D0)]
.text:000000710066BBE8                 STR             X21, [X19,#(qword_7102153D28 - 0x71021536D0)]
.text:000000710066BBEC                 STR             X27, [X19,#(qword_7102153D30 - 0x71021536D0)]
.text:000000710066BBF0                 BL              sub_710083C9A0
.text:000000710066BBF4                 LDR             X0, [X19,#(qword_7102153C88 - 0x71021536D0)]
.text:000000710066BBF8                 STR             XZR, [X19,#(qword_7102153C88 - 0x71021536D0)]
.text:000000710066BBFC                 BL              sub_710083C9D0
.text:000000710066BC00                 LDR             X8, [X19,#(qword_7102153C80 - 0x71021536D0)]
.text:000000710066BC04                 STRB            WZR, [X19,#(byte_7102153D38 - 0x71021536D0)]
.text:000000710066BC08                 STRB            WZR, [X19,#(byte_7102153D26 - 0x71021536D0)]
.text:000000710066BC0C                 STR             W20, [X19,#(dword_7102153CFC - 0x71021536D0)]
```

So float we want is stored at MAIN+0x2153CFC.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = 0.96 * (1000/FPS)
  -
    type: write
    address: [MAIN, 0x2153CFC]
    value_type: float
    value: 64
```