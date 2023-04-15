# WRC Generations

> Game info

TitleID: `0100041018810000`<br>
Explanation based on:
- Internal version: `1.2.2`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `B8BE1CFAE53CAEBE`
- Engine: `KTEngine`

> Details

Game is causing some glitch in NVN that even if it blocks to interval 2, nvnGetPresentInterval returns 1. So NX-FPS update was required to workaround this issue. You must have at least NX-FPS 1.3.3 to unlock 60 FPS.

We need to patch dynamic resolution frame time, it's set to 31.0 ms via config and because of that performance is subpar.

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
.text:0000007100D4C23C                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:0000007100D4C240                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:0000007100D4C244                 MOV             X0, X28
.text:0000007100D4C248                 MOV             X2, X22
.text:0000007100D4C24C                 MOV             W3, #3
.text:0000007100D4C250                 BL              sub_7100F89EC4
.text:0000007100D4C254                 MOV             X8, #0x3333333333333333
.text:0000007100D4C258                 MOVK            X8, #0x4205,LSL#16
.text:0000007100D4C25C                 MOVK            X8, #0x4205,LSL#48
.text:0000007100D4C260                 MOV             W20, #0x3333
.text:0000007100D4C264                 MOVK            W20, #0x4205,LSL#16
.text:0000007100D4C268                 MOV             X0, XZR
.text:0000007100D4C26C                 STR             X26, [X19,#(qword_7102D5A7C0 - 0x7102D59F70)]
.text:0000007100D4C270                 STUR            X8, [X28,#0x84]
.text:0000007100D4C274                 STR             W20, [X19,#(dword_7102D5A860 - 0x7102D59F70)]
.text:0000007100D4C278                 STR             W23, [X28,#(dword_7102D5A854 - 0x7102D5A7C0)]
.text:0000007100D4C27C                 STR             X21, [X19,#(qword_7102D5A868 - 0x7102D59F70)]
.text:0000007100D4C280                 STR             X27, [X19,#(qword_7102D5A870 - 0x7102D59F70)]
.text:0000007100D4C284                 BL              sub_7100F93820
.text:0000007100D4C288                 LDR             X0, [X19,#(qword_7102D5A7C8 - 0x7102D59F70)]
.text:0000007100D4C28C                 STR             XZR, [X19,#(qword_7102D5A7C8 - 0x7102D59F70)]
.text:0000007100D4C290                 BL              sub_7100F93850
.text:0000007100D4C294                 STRB            WZR, [X19,#(byte_7102D5A878 - 0x7102D59F70)]
.text:0000007100D4C298                 MOV             X0, X28
.text:0000007100D4C29C                 MOV             W1, WZR
.text:0000007100D4C2A0                 STRB            WZR, [X28,#(byte_7102D5A866 - 0x7102D5A7C0)]
.text:0000007100D4C2A4                 MOV             W2, #1
.text:0000007100D4C2A8                 STR             W20, [X28,#(dword_7102D5A83C - 0x7102D5A7C0)]
```

So float we want is stored at MAIN+0x2D5A83C.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = (1000/FPS) - (0.07 * (1000/30)
  -
    type: write
    address: [MAIN, 0x2D5A83C]
    value_type: float
    value: 64.333333
```