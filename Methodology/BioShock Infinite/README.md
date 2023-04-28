# BioShock Infinite

> Game info

TitleID: `0100D560102C8000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `48681F1D90704F6C`
- Engine: `Unreal Engine 3`

> Details

Game can go above 30 FPS with plugin alone, but we need to patch dynamic resolution frame timing to get better performance.
Thanks to `Kirby567Fan` for finding relevant instructions.

# How to find offsets

After analyzing main we need to find those bytes:
```
00 00 FC 41 56 55 85 42
```
We need to go to xref of this data.

After going to result we need to find first instruction below that starts with
```asm
STR X0
```

This instruction stores pointer to dynamic resolution FPS factor in hardcoded offset in main. In IDA whole piece of code looks like this:
```asm
.text:0000007100A59000                 ADRP            X8, #xmmword_7102205030@PAGE
.text:0000007100A59004                 LDR             Q0, [X8,#xmmword_7102205030@PAGEOFF]
.text:0000007100A59008                 MOV             X8, #0x3FC00000
.text:0000007100A5900C                 STP             XZR, XZR, [X0,#0x38]
.text:0000007100A59010                 MOVK            X8, #4,LSL#32
.text:0000007100A59014                 STR             X8, [X0,#0x10]
.text:0000007100A59018                 ADRP            X8, #xmmword_7102204020@PAGE
.text:0000007100A5901C                 STR             Q0, [X0]
.text:0000007100A59020                 LDR             Q0, [X8,#xmmword_7102204020@PAGEOFF]
.text:0000007100A59024                 MOV             X8, #0x42960000
.text:0000007100A59028                 MOVK            X8, #1,LSL#32
.text:0000007100A5902C                 STR             X8, [X0,#0x28]
.text:0000007100A59030                 ADRP            X8, #qword_7102200CE8@PAGE
.text:0000007100A59034                 STUR            Q0, [X0,#0x18]
.text:0000007100A59038                 LDR             D0, [X8,#qword_7102200CE8@PAGEOFF]
.text:0000007100A5903C                 ADRP            X8, #qword_71028A8450@PAGE
.text:0000007100A59040                 STR             D0, [X0,#0x30]
.text:0000007100A59044                 STR             X0, [X8,#qword_71028A8450@PAGEOFF]
```

So pointer to our value is stored at MAIN+0x28A8450
Value is stored as float matching FPS target + 1.5

So for 30 FPS it will look like this:
```yaml
30FPS:
  # Dynamic resolution FPS factor (default)
  -
    type: write
    address: [MAIN, 0x28A8450, 0]
    value_type: float
    value: 31.5
```
