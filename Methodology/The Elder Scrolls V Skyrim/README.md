# The Elder Scrolls V: Skyrim

> Game info

TitleID: `01000A10041EA000`<br>
Explanation based on:
- Internal version: `1.1.177.3285177`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `771BDFB65F8D0AF7`
- Engine: `Creation Engine`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to range 30-33 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find those bytes:
```
48 33 93 52 28 D3 A7 72 01 01 27 1E
```

It will show us function that looks like this:

```asm
.text:0000007100BE06F8 sub_7100BE06F8                          ; CODE XREF: sub_71005E16A4+6A0↑p
.text:0000007100BE06F8                 MOV             W8, #0x999A
.text:0000007100BE06FC                 MOVK            W8, #0x3E99,LSL#16
.text:0000007100BE0700                 FMOV            S1, W8
.text:0000007100BE0704                 MOV             W8, #0x3333
.text:0000007100BE0708                 MOVK            W8, #0x3F33,LSL#16
.text:0000007100BE070C                 FMOV            S2, W8
.text:0000007100BE0710                 ADRP            X8, #off_710215DA08@PAGE
.text:0000007100BE0714                 FMUL            S3, S0, S1
.text:0000007100BE0718                 LDR             S1, [X0,#0xFC]
.text:0000007100BE071C                 LDR             X8, [X8,#off_710215DA08@PAGEOFF]
.text:0000007100BE0720                 FMADD           S1, S1, S2, S3
.text:0000007100BE0724                 STR             S1, [X0,#0xFC]
.text:0000007100BE0728                 LDR             S2, [X8,#(dword_71033178C8 - 0x71033178C0)]
.text:0000007100BE072C                 FCMP            S1, S2
.text:0000007100BE0730                 B.GE            loc_7100BE0758
.text:0000007100BE0734                 ADRP            X9, #off_710215DA10@PAGE
.text:0000007100BE0738                 LDR             X9, [X9,#off_710215DA10@PAGEOFF]
.text:0000007100BE073C                 MOV             W8, #1
.text:0000007100BE0740                 STRH            W8, [X0,#0x11C]
.text:0000007100BE0744                 LDR             S0, [X9,#(dword_71033178B0 - 0x71033178A8)]
.text:0000007100BE0748                 FCMP            S1, S0
.text:0000007100BE074C                 B.LE            loc_7100BE0778
.text:0000007100BE0750                 STR             S0, [X0,#0xFC]
.text:0000007100BE0754                 RET
```

First LDR S2 provides us an address to float with dynamic resolution frame timing under which game increases resolution. It's 0x33178C8.
First LDR S0 provides us an address to float with dynamic resolution frame timing above which game decreases resolution. it's 0x33178B0.

So for 30 FPS it will look like this:
```yaml
30FPS:
  # Dynamic Resolution Frame Time Min (default value)
  -
    type: write
    address: [MAIN, 0x33178C8]
    value_type: float
    value: 30
  # Dynamic Resolution Frame Time Max (default value)
  -
    type: write
    address: [MAIN, 0x33178B0]
    value_type: float
    value: 33
```