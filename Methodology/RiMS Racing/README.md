# RiMS Racing

> Game info

TitleID: `01003CD01299E000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `4232D493269475B2`
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
.text:0000007100BEB264                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:0000007100BEB268                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:0000007100BEB26C                 MOV             X0, X28
.text:0000007100BEB270                 MOV             X2, X24
.text:0000007100BEB274                 MOV             W3, #3
.text:0000007100BEB278                 BL              sub_7100E044D0
.text:0000007100BEB27C                 MOV             X9, #0x3333333333333333
.text:0000007100BEB280                 MOVK            X9, #0x4205,LSL#16
.text:0000007100BEB284                 ADD             X8, X19, #0x674
.text:0000007100BEB288                 MOV             W20, #0x3333
.text:0000007100BEB28C                 MOVK            W20, #0x4205,LSL#16
.text:0000007100BEB290                 STR             X22, [X19,#(qword_7102CDFC40 - 0x7102CDF650)]
.text:0000007100BEB294                 MOVK            X9, #0x4205,LSL#48
.text:0000007100BEB298                 MOV             X0, XZR
.text:0000007100BEB29C                 STR             X9, [X8]
.text:0000007100BEB2A0                 STR             W20, [X19,#(dword_7102CDFCE0 - 0x7102CDF650)]
.text:0000007100BEB2A4                 STR             W23, [X19,#(dword_7102CDFCD4 - 0x7102CDF650)]
.text:0000007100BEB2A8                 STR             X21, [X19,#(qword_7102CDFCE8 - 0x7102CDF650)]
.text:0000007100BEB2AC                 STR             X27, [X19,#(qword_7102CDFCF0 - 0x7102CDF650)]
.text:0000007100BEB2B0                 BL              sub_7100E0BA80
.text:0000007100BEB2B4                 LDR             X0, [X19,#(qword_7102CDFC48 - 0x7102CDF650)]
.text:0000007100BEB2B8                 STR             XZR, [X19,#(qword_7102CDFC48 - 0x7102CDF650)]
.text:0000007100BEB2BC                 BL              sub_7100E0BAB0
.text:0000007100BEB2C0                 LDR             X8, [X19,#(qword_7102CDFC40 - 0x7102CDF650)]
.text:0000007100BEB2C4                 STRB            WZR, [X19,#(byte_7102CDFCF8 - 0x7102CDF650)]
.text:0000007100BEB2C8                 STRB            WZR, [X19,#(byte_7102CDFCE6 - 0x7102CDF650)]
.text:0000007100BEB2CC                 STR             W20, [X19,#(dword_7102CDFCBC - 0x7102CDF650)]
```

So float we want is stored at MAIN+0x2CDFCBC.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = (1000/FPS) - (0.07 * (1000/30)
  -
    type: write
    address: [MAIN, 0x2CDFCBC]
    value_type: float
    value: 64.333333
```