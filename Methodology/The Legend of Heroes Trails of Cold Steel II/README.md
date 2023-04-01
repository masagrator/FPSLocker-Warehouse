# 英雄伝説 閃の軌跡Ⅱ：改 -THE EREBONIAN CIVIL WAR-
The Legend of Heroes: Trails of Cold Steel (Sen on Kiseki) II Kai -THE EREBONIAN CIVIL WAR-

> Game info

TitleID: `0100906014C3C000`<br>
Explanation based on:
- Internal version: `1.0.5`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `EAB1DC1D53E319F9`
- Engine: Heavily modified `Phyre` engine

> Details

Game is using internal FPS locker. We need to patch it.<br>

---

# How to find offsets

We need to use disassembler in this case. 

After finishing disassembling `main` we need to find those bytes:
```
20 18 20 1E 48 55 00 90 00 71 0B BD
```

It should return a function that looks something like this:
```asm
.text:000000710005D100 sub_710005D100                          ; CODE XREF: sub_7100378760+AFC↓p
.text:000000710005D100                                         ; sub_71003A7910+C4↓p ...
.text:000000710005D100
.text:000000710005D100 var_20          = -0x20
.text:000000710005D100 var_18          = -0x18
.text:000000710005D100 var_10          = -0x10
.text:000000710005D100 var_C           = -0xC
.text:000000710005D100 var_8           = -8
.text:000000710005D100
.text:000000710005D100                 SUB             SP, SP, #0x20
.text:000000710005D104                 MOV             W2, W1
.text:000000710005D108                 MOV             X3, X0
.text:000000710005D10C                 STR             X0, [SP,#0x20+var_8]
.text:000000710005D110                 STR             W1, [SP,#0x20+var_C]
.text:000000710005D114                 LDR             X0, [SP,#0x20+var_8]
.text:000000710005D118                 LDR             S0, [SP,#0x20+var_C]
.text:000000710005D11C                 UCVTF           S0, S0
.text:000000710005D120                 FMOV            S1, #1.0
.text:000000710005D124                 FDIV            S0, S1, S0
.text:000000710005D128                 ADRP            X8, #dword_7100B05B70@PAGE
.text:000000710005D12C                 STR             S0, [X8,#dword_7100B05B70@PAGEOFF]
.text:000000710005D130                 STR             W2, [SP,#0x20+var_10]
.text:000000710005D134                 STR             X3, [SP,#0x20+var_18]
.text:000000710005D138                 STR             X0, [SP,#0x20+var_20]
.text:000000710005D13C                 ADD             SP, SP, #0x20
.text:000000710005D140                 RET
.text:000000710005D140 ; End of function sub_710005D100
```

`dword_7100B05B70` is our pointer where it's stored frame time in seconds that is used as FPS lock.

So for 15 FPS it will look like this:
```yaml
15FPS:
  -
    type: write
    address: [MAIN, 0xB05B70]
    value_type: float
    value: 0.06666666666
  -
    type: block
    what: timing

```
For 30 FPS like this:
```yaml
30FPS:
  -
    type: write
    address: [MAIN, 0xB05B70]
    value_type: float
    value: 0.03333333333

```
