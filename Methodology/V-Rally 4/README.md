# V-Rally 4

> Game info

TitleID: `010064400B138000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `EB8A679B5DDD0060`
- Engine: `KTEngine`

> Details

Plugin alone can set FPS above 30, but dynamic resolution target is set to 31 ms, so it's hard to get 60 FPS without graphics tweaks. We will be patching that.

---

# How to find offsets

We need to use disassembler in this case. I will be using IDA that will calculate base address for us.

We need to find string:
```
OptimalFrameDuration_ms
```

And go to its only xref.

Below we search for first `STR X28, [X19]` instruction.

Piece of function looks like this:
```asm
.text:000000710072829C                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:00000071007282A0                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:00000071007282A4                 MOV             W3, #3
.text:00000071007282A8                 MOV             X0, X24
.text:00000071007282AC                 MOV             X2, X22
.text:00000071007282B0                 BL              sub_7100874C60
.text:00000071007282B4                 MOV             X9, #0x3333333333333333
.text:00000071007282B8                 MOVK            X9, #0x4205,LSL#16
.text:00000071007282BC                 ADD             X8, X19, #0x65C
.text:00000071007282C0                 MOV             W0, #4  ; unsigned __int64
.text:00000071007282C4                 MOVK            X9, #0x4205,LSL#48
.text:00000071007282C8                 STR             X28, [X19,#(qword_71020A0DD0 - 0x71020A07E8)]
```

Our base address is 0x20A07E8. By adding to it 0x65C we are getting offset at which dynamic resolution is set.

So float we want is stored at MAIN+0x20A0E44.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = (1000/FPS) - (0.07 * (1000/30)
  -
    type: write
    address: [MAIN, 0x20A0E44]
    value_type: float
    value: 64.333333
```