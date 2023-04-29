# BioShock 2 Remastered

> Game info

TitleID: `01002620102C6000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `7D1714279435589C`
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
.text:000000710048D0A8                 MOV             X8, #0x41F00000
.text:000000710048D0AC                 MOV             X9, #0x42C80000
.text:000000710048D0B0                 MOVK            X8, #0x4248,LSL#48
.text:000000710048D0B4                 MOVK            X9, #0x3F00,LSL#48
.text:000000710048D0B8                 STP             X8, X9, [X0]
.text:000000710048D0BC                 MOV             X8, #0xC28F
.text:000000710048D0C0                 MOVK            X8, #0x4055,LSL#16
.text:000000710048D0C4                 MOV             X9, #0xCCCD
.text:000000710048D0C8                 MOVK            X9, #0x3DCC,LSL#16
.text:000000710048D0CC                 MOVK            X8, #4,LSL#32
.text:000000710048D0D0                 MOVK            X9, #0xCCCD,LSL#32
.text:000000710048D0D4                 MOVK            X9, #0x3DCC,LSL#48
.text:000000710048D0D8                 STP             X8, X9, [X0,#0x10]
.text:000000710048D0DC                 MOV             X8, #0x40400000
.text:000000710048D0E0                 MOVK            X8, #0x4296,LSL#48
.text:000000710048D0E4                 STR             X8, [X0,#0x20]
.text:000000710048D0E8                 MOV             W8, #1
.text:000000710048D0EC                 STR             W8, [X0,#0x28]
.text:000000710048D0F0                 MOV             X8, #0x42C80000
.text:000000710048D0F4                 STP             XZR, XZR, [X0,#0x38]
.text:000000710048D0F8                 MOVK            X8, #0x3F80,LSL#48
.text:000000710048D0FC                 STUR            X8, [X0,#0x2C]
.text:000000710048D100                 ADRP            X8, #qword_710212C138@PAGE
.text:000000710048D104                 STR             X0, [X8,#qword_710212C138@PAGEOFF]
```

So pointer to our value is stored at MAIN+0x212C138
Value is stored as float matching FPS target.

So for 30 FPS it will look like this:
```yaml
30FPS:
  # Dynamic resolution FPS factor (default)
  -
    type: write
    address: [MAIN, 0x212C138, 0]
    value_type: float
    value: 30
```
