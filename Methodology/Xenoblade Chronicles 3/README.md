# Xenoblade Chronicles 3

> Game info

TitleID: `010074F013262000`<br>
Explanation based on:
- Internal version: `1.3.0`, 
- Nintendo version ID: `v6`/`v393216`
- BID: `B76CD24AF02ACEA2`

> Details

This game is using internal vsync signal detection set to 2, which means it skips every second frame. <br>
We need to change it to 1 to unlock >30 FPS. <br>
2D animations are hardcoded to use 30 FPS, so above 30 FPS they are rendered faster than normal.<br>

Beside that cutscenes animations are hardcoded to 30 FPS and nobody figured out if it's even possible to render them above 30 FPS with correct speed.
That's why is is necessary to get an offset to determine if we are in cutscene or not to automatically lock to 30 FPS if cutscene is detected.

Thanks to `theboy181` for finding the most reliable offset to figure out when cutscene is played.

---

# How to find offsets

We need to use disassembler in this case. 

> First we determine how to enable 60 FPS.

After finishing disassembling `main`, we need to find those bytes (they may change after some invasive update, but for now it's reliable):
```
00 01 00 B9 2A 01 00 B9 C0 03 5F D6
```

Before them we will find instructions that are storing offsets to vsync signal detection values. Function looks something like this:
```asm
.text:0000007101157D18 sub_7101157D18                          ; CODE XREF: sub_7101192BC4+14↓p
.text:0000007101157D18                 ADRP            X8, #off_7101A2EC28@PAGE
.text:0000007101157D1C                 LDR             X8, [X8,#off_7101A2EC28@PAGEOFF]
.text:0000007101157D20                 ADRP            X9, #off_7101A2EC50@PAGE
.text:0000007101157D24                 LDR             X9, [X9,#off_7101A2EC50@PAGEOFF]
.text:0000007101157D28                 LDR             W10, [X8]
.text:0000007101157D2C                 STR             W0, [X8]
.text:0000007101157D30                 STR             W10, [X9]
.text:0000007101157D34                 RET
.text:0000007101157D34 ; End of function sub_7101157D18
```

`off_7101A2EC28` stores one pointer `dword_7101A08F98`, so our first offset is `[MAIN, 0x1A08F98]`.<br>
`off_7101A2EC50` stores another pointer `dword_7101A08F9C`, so our second offset is `[MAIN, 0x1A08F9C]`

As they are stored one after another at the same size, we can use patch format in this way to write default values for 30 FPS and below (they may change after some invasive update, but for now it's reliable):
```yaml
  -
    type: write
    address: [MAIN, 0x1A08F98]
    value_type: int32
    value: [2, 2]
```

> Cutscene detection offset

Now we need to find those bytes
```
09 01 00 39 FD 7B C3 A8 C0 03 5F D6
```

Fourth instruction above is LDR instruction that loads pointer. Piece of function looks like this:
```asm
.text:0000007100C3B824                 LDR             X8, [X8,#off_7101A28B40@PAGEOFF]
.text:0000007100C3B828                 STR             XZR, [X19,#0x8B0]
.text:0000007100C3B82C                 LDP             X20, X19, [SP,#var_s20]
.text:0000007100C3B830                 LDP             X22, X21, [SP,#var_s10]
.text:0000007100C3B834                 STRB            W9, [X8]
.text:0000007100C3B838                 LDP             X29, X30, [SP+var_s0],#0x30
.text:0000007100C3B83C                 RET
```


 Pointer is loaded from `off_7101A28B40`, which leads to `byte_7101A65958`.


So value is stored as 1 byte at `[MAIN,0x1A65958]`.<br>
If it's not equal to 0, cutscene is played. If it's not equal to 1, cutscene is not played.

So we can write patch like this for above 30 FPS:
```yaml
  -
    type: compare
    compare_address: [MAIN, 0x1A65958]
    compare_type: "!="
    compare_value_type: int8
    compare_value: 1
    address: [MAIN, 0x1A08F98]
    value_type: int32
    value: [1, 1]
  -
    type: compare
    compare_address: [MAIN, 0x1A65958]
    compare_type: "!="
    compare_value_type: int8
    compare_value: 0
    address: [MAIN, 0x1A08F98]
    value_type: int32
    value: [2, 2]
```
