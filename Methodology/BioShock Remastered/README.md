# BioShock Remastered

> Game info

TitleID: `0100AD10102B2000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `D89FFAA2062E373D`
- Engine: `Unreal Engine 2.5`

> Details

Game can go above 30 FPS with plugin alone, but we need to patch dynamic resolution frame timing to get better performance.
Thanks to `Kirby567Fan` for finding relevant instructions.

# How to find offsets

After analyzing main we need to find those bytes:
```
08 3E A8 D2 09 59 A8 D2
```

After going to result we need to find first instruction below that starts with
```asm
STR X0
```

This instruction stores pointer to dynamic resolution FPS factor in hardcoded offset in main. In IDA whole piece of code looks like this:
```asm
.text:000000710099D740                 MOV             X8, #0x41F00000
.text:000000710099D744                 MOV             X9, #0x42C80000
.text:000000710099D748                 MOV             X24, #0x42C80000
.text:000000710099D74C                 MOVK            X8, #0x4248,LSL#48
.text:000000710099D750                 MOVK            X9, #0x3F00,LSL#48
.text:000000710099D754                 MOVK            X24, #0x3F80,LSL#48
.text:000000710099D758                 STP             X8, X9, [X0]
.text:000000710099D75C                 MOV             X8, #0xC28F
.text:000000710099D760                 MOVK            X8, #0x4055,LSL#16
.text:000000710099D764                 MOV             X9, #0xCCCD
.text:000000710099D768                 MOVK            X9, #0x3DCC,LSL#16
.text:000000710099D76C                 MOVK            X8, #4,LSL#32
.text:000000710099D770                 STUR            X24, [X0,#0x2C]
.text:000000710099D774                 MOVK            X9, #0xCCCD,LSL#32
.text:000000710099D778                 MOVK            X9, #0x3DCC,LSL#48
.text:000000710099D77C                 STP             X8, X9, [X0,#0x10]
.text:000000710099D780                 MOV             X8, #0x40400000
.text:000000710099D784                 MOVK            X8, #0x4296,LSL#48
.text:000000710099D788                 STR             X8, [X0,#0x20]
.text:000000710099D78C                 MOV             W8, #1
.text:000000710099D790                 STR             W8, [X0,#0x28]
.text:000000710099D794                 ADRP            X26, #qword_71029B4BA0@PAGE
.text:000000710099D798                 STP             XZR, XZR, [X0,#0x38]
.text:000000710099D79C                 LDR             W8, [X25,#dword_71020C8244@PAGEOFF]
.text:000000710099D7A0                 STR             X0, [X26,#qword_71029B4BA0@PAGEOFF]
```

So pointer to our value is stored at MAIN+0x29B4BA0
Value is stored as float matching FPS target.

So for 30 FPS it will look like this:
```yaml
30FPS:
  # Dynamic resolution FPS factor (default)
  -
    type: write
    address: [MAIN, 0x29B4BA0, 0]
    value_type: float
    value: 30
```
