# No Man's Sky

> Game info

TitleID: `0100853015E86000`<br>
Explanation based on:
- Internal version: `1.1.0`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `DA7D68D91AB5FA3C`
- Engine: Proprietary

> Details

Game can be set up to 60 FPS with FPSLocker alone, but because of dynamic resolution introduced at some point with FSR2, performance is subpar and we need to tweak its target framerate.

# How to find offsets

We need to use disassembler in this case. I will be using IDA since it calculates offsets for us.

After finishing disassembling main, we need to find those bytes:
```
A8 AA 8A 52 A8 40 A8 72
```

There should be only one result. Above that offset you have

```arm
CMP             W8, #0
```

You need to NOP it.

Below our result offset we should have

```arm
FMOV            S1, W8
LDR             W8, [X0,#4]
FCSEL           S10, S1, S0, EQ
```

We need to patch first and third line to point game to some .bss offset not used by game, in version of game I had we can use 0x71049ACD00.
ADRP doesn't accept last 3 numbers other than 0, so we patch first line with
```arm
ADRP X18,0x71049AC000
```

Third line we are patching with LDR, which will load from X18 register which is 0x71049AC000 + we add to idd 0xD00, so in the end we will get our offset 0x71049ACD00
```arm
LDR S10, [x18,#0xD00]
```

So in the result whole block should look like this
```arm
.text:0000007101D927B0                 NOP
.text:0000007101D927B4                 MOV             W8, #0x5555
.text:0000007101D927B8                 MOVK            W8, #0x4205,LSL#16
.text:0000007101D927BC                 ADRP            X18,0x71049AC000
.text:0000007101D927C0                 LDR             W8, [X0,#4]
.text:0000007101D927C4                 LDR             S10, [x18,#0xD00]
```

And we are writing it to our patch, remembering to write to 0x71049ACD00 default value 1000/30 as float, so game wouldn't crash because it can try to access it before first frame is pushed to display.

Example:
```yaml
MASTER_WRITE:
# Redirect DR frametime target to MAIN+0x49ACD00
  -
    type: bytes
    main_offset: 0x1D927B0
    value_type: uint32
    value: 0xD503201F
  -
    type: bytes
    main_offset: 0x1D927BC
    value_type: uint32
    value: 
      - 0xD00160D2
      - 0xB9400408
      - 0xBD4D024A
  # default value
  -
    type: bytes
    main_offset: 0x49ACD00
    value_type: float
    value: 33.3333333333
15FPS:
  -
    type: write
    address: [MAIN, 0x49ACD00]
    value_type: float
    value: 66.6666666666
```