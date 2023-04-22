# WRC8

> Game info

TitleID: `010087800DCEA000`<br>
Explanation based on:
- Internal version: `1.4.0`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `6B0B26802F0DAAAF`
- Engine: `KTEngine`

> Details

Game has broken vsync lock and that's why it's technically unlocked 60 FPS, but game graphically is targeting 30 FPS (dynamic resolution target is set to 31 ms), so it's hard to get 60 FPS without graphics tweaks. We will be patching that.

---

# How to find offsets

We need to use disassembler in this case. I will be using IDA that will calculate base address for us.

We need to find string:
```
OptimalFrameDuration_ms
```

And go to its only xref.

Below we search for first `STR X20, [X19]` instruction.

Piece of function looks like this:
```asm
.text:0000007100840D40                 ADRP            X1, #aOptimalframedu@PAGE ; "OptimalFrameDuration_ms"
.text:0000007100840D44                 ADD             X1, X1, #aOptimalframedu@PAGEOFF ; "OptimalFrameDuration_ms"
.text:0000007100840D48                 MOV             X0, X27
.text:0000007100840D4C                 MOV             X2, X23
.text:0000007100840D50                 MOV             W3, #3
.text:0000007100840D54                 BL              sub_71009F69F0
.text:0000007100840D58                 MOV             X9, #0x3333333333333333
.text:0000007100840D5C                 MOVK            X9, #0x4205,LSL#16
.text:0000007100840D60                 ADD             X8, X19, #0x664
.text:0000007100840D64                 MOV             W21, #0x3333
.text:0000007100840D68                 MOVK            W21, #0x4205,LSL#16
.text:0000007100840D6C                 STR             X20, [X19,#(qword_71022F5078 - 0x71022F4AA0)]
```

Our base address is 0x22F4AA0. By adding to it 0x65C we are getting offset at which dynamic resolution is set.

So float we want is stored at MAIN+0x22F50FC.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # OptimalFrameDuration_ms = (1000/FPS) - (0.07 * (1000/30)
  -
    type: write
    address: [MAIN, 0x22F50FC]
    value_type: float
    value: 64.333333
```