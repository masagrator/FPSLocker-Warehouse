# TT Isle of Man

> Game info

TitleID: `010099900CAB2000`<br>
Explanation based on:
- Internal version: `1.1.0`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `F2F739A2F1CAFF72`
- Engine: `KTEngine`

> Details

Plugin can set FPS above 30 alone, but we need to patch dynamic resolution frame time, it's set to 31.0 ms via config and because of that performance is subpar.

---

# How to find offsets

We need to use disassembler in this case. I will be using IDA because it will calculate main offset for us.

We need to find string:
```
OptimalFrameDuration_ms
```

And go to its only xref.

Below xref at register X9 it stores an executable default value.
We need to search where this X9 is written. It will be first `STR X9`.

Piece of function looks like this:
```asm
.text:00000071004D8C50                 BL              sub_71000001C0
.text:00000071004D8C54                 ADD             X22, X23, #0x1A0
.text:00000071004D8C58                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:00000071004D8C5C                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:00000071004D8C60                 MOV             W3, #3
.text:00000071004D8C64                 MOV             X0, X22
.text:00000071004D8C68                 MOV             X2, X20
.text:00000071004D8C6C                 BL              loc_71005D1C10
.text:00000071004D8C70                 MOV             X9, #0x3333333333333333
.text:00000071004D8C74                 MOVK            X9, #0x4205,LSL#16
.text:00000071004D8C78                 ADD             X8, X23, #0x1FC
.text:00000071004D8C7C                 MOV             W0, #4  ; unsigned __int64
.text:00000071004D8C80                 MOVK            X9, #0x4205,LSL#48
.text:00000071004D8C84                 STR             X25, [X23,#(qword_710171DDD0 - 0x710171DC30)]
.text:00000071004D8C88                 STR             X9, [X8]
```

For some reason IDA didn't calculate offset for us, but it's pretty easy.<br>

X8 register is where it's stored our address.<br>
As we can see few instructions above, to X8 register is written X23+0x1FC.<br>
X23 is also used for second last instruction that is using it as base address. So X23 is 0x171DC30. <br>
To 0x171DC30 we add 0x1FC and we got 0x171DE2C.

So float we want is stored at MAIN+0x171DE2C.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = (1000/FPS) - (0.07 * (1000/30)
  -
    type: write
    address: [MAIN, 0x171DE2C]
    value_type: float
    value: 64.333333
```