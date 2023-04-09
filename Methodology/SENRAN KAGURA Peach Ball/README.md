# SENRAN KAGURA Peach Ball

> Game info

TitleID: `01004DC00D936000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `31CDAD67EA25CC16`
- Engine: proprietary

> Details

Game is locking game internally to 30 FPS when actual game is played and in main menu. We need to force game to allow going above 30 FPS.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find this string:
```
//=================================\n
//CRendSpanMgr:[SpanType_60FPS]\n
//=================================\n
\n
```

It will return for us function that swaps between 30 and 60 FPS lock. At the beginning of function we have an offset from which is loaded static pointer.
Whole function looks like this
```
.text:000000710003FA50 sub_710003FA50                          ; CODE XREF: sub_71000004C0+68↑p
.text:000000710003FA50                                         ; sub_71000D2FD0+48↓p ...
.text:000000710003FA50                 ADRP            X8, #off_7100497D48@PAGE
.text:000000710003FA54                 LDR             X8, [X8,#off_7100497D48@PAGEOFF]
.text:000000710003FA58                 ADRP            X10, #off_7100497D50@PAGE
.text:000000710003FA5C                 LDR             W9, [X8]
.text:000000710003FA60                 LDR             X10, [X10,#off_7100497D50@PAGEOFF]
.text:000000710003FA64                 LDRB            W10, [X10]
.text:000000710003FA68                 CMP             W9, W0
.text:000000710003FA6C                 CCMP            W10, #0, #0, NE
.text:000000710003FA70                 B.EQ            loc_710003FA78
.text:000000710003FA74                 RET
.text:000000710003FA78 ; ---------------------------------------------------------------------------
.text:000000710003FA78
.text:000000710003FA78 loc_710003FA78                          ; CODE XREF: sub_710003FA50+20↑j
.text:000000710003FA78                 STR             W0, [X8]
.text:000000710003FA7C                 CBZ             W0, loc_710003FA8C
.text:000000710003FA80                 ADRP            X0, #aCrendspanmgrSp@PAGE ; "//=================================\n//"...
.text:000000710003FA84                 ADD             X0, X0, #aCrendspanmgrSp@PAGEOFF ; "//=================================\n//"...
.text:000000710003FA88                 B               sub_71001DA840
.text:000000710003FA8C ; ---------------------------------------------------------------------------
.text:000000710003FA8C
.text:000000710003FA8C loc_710003FA8C                          ; CODE XREF: sub_710003FA50+2C↑j
.text:000000710003FA8C                 ADRP            X0, #aCrendspanmgrSp_0@PAGE ; "//=================================\n//"...
.text:000000710003FA90                 ADD             X0, X0, #aCrendspanmgrSp_0@PAGEOFF ; "//=================================\n//"...
.text:000000710003FA94                 B               sub_71001DA840
.text:000000710003FA94 ; End of function sub_710003FA50
```

At off_7100497D48 is stored a pointer leading to MAIN+0x62D8CC

So for anything above 30 FPS we will set:
```yaml
60FPS:
  # CRendSpanMgr:[SpanType_60FPS]
  -
    type: write
    address: [MAIN, 0x62D8CC]
    value_type: int32
    value: 0
```
For everything else:
```yaml
30FPS:
  # CRendSpanMgr:[SpanType_30FPS]
  -
    type: write
    address: [MAIN, 0x62D8CC]
    value_type: int32
    value: 1
```
