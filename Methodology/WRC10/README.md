# WRC10

> Game info

TitleID: `01003E3014AFE000`<br>
Explanation based on:
- Internal version: `1.1.0`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `69CACEEC5F01C418`
- Engine: `KTEngine`

> Details

Plugin can unlock 60 FPS alone, but we need to patch dynamic resolution frame time, it's set to 31.0 ms via config and because of that performance is subpar.

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
.text:0000007100B494E0                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:0000007100B494E4                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:0000007100B494E8                 MOV             X0, X28
.text:0000007100B494EC                 MOV             X2, X22
.text:0000007100B494F0                 MOV             W3, #3
.text:0000007100B494F4                 BL              sub_7100D53704
.text:0000007100B494F8                 MOV             X8, #0x3333333333333333
.text:0000007100B494FC                 MOVK            X8, #0x4205,LSL#16
.text:0000007100B49500                 MOVK            X8, #0x4205,LSL#48
.text:0000007100B49504                 MOV             W20, #0x3333
.text:0000007100B49508                 MOVK            W20, #0x4205,LSL#16
.text:0000007100B4950C                 MOV             X0, XZR
.text:0000007100B49510                 STR             X24, [X19,#(qword_7102A14940 - 0x7102A141C0)]
.text:0000007100B49514                 STUR            X8, [X28,#0x84]
.text:0000007100B49518                 STR             W20, [X19,#(dword_7102A149E0 - 0x7102A141C0)]
.text:0000007100B4951C                 STR             W23, [X28,#(dword_7102A149D4 - 0x7102A14940)]
.text:0000007100B49520                 STR             X21, [X19,#(qword_7102A149E8 - 0x7102A141C0)]
.text:0000007100B49524                 STR             X27, [X19,#(qword_7102A149F0 - 0x7102A141C0)]
.text:0000007100B49528                 BL              sub_7100D5AFD0
.text:0000007100B4952C                 LDR             X0, [X19,#(qword_7102A14948 - 0x7102A141C0)]
.text:0000007100B49530                 STR             XZR, [X19,#(qword_7102A14948 - 0x7102A141C0)]
.text:0000007100B49534                 BL              sub_7100D5B000
.text:0000007100B49538                 STRB            WZR, [X19,#(byte_7102A149F8 - 0x7102A141C0)]
.text:0000007100B4953C                 MOV             X0, X28
.text:0000007100B49540                 MOV             W1, WZR
.text:0000007100B49544                 STRB            WZR, [X28,#(byte_7102A149E6 - 0x7102A14940)]
.text:0000007100B49548                 MOV             W2, #1
.text:0000007100B4954C                 STR             W20, [X28,#(dword_7102A149BC - 0x7102A14940)]
```

So float we want is stored at MAIN+0x2A149BC.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = (1000/FPS) - (0.07 * (1000/30)
  -
    type: write
    address: [MAIN, 0x2A149BC]
    value_type: float
    value: 64.333333
```