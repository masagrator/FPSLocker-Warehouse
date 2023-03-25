# 英雄伝説 閃の軌跡I：改 -THORS MILITARY ACADEMY 1204-
The Legend of Heroes: Trails of Cold Steel (Sen on Kiseki) Kai -THORS MILITARY ACADEMY 1204-

> Game info

TitleID: `0100AD0014AB4000`<br>
Explanation based on:
- Internal version: `1.0.3`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `AC8C8EC9DB1A8EF4`
- Engine: Heavily modified `Phyre` engine

> Details

Game is using internal FPS locker. We need to patch it.<br>
**WARNING**: Game has issues with slow-motion cutscenes when FPS is set above 30 FPS. It will make them up to several times longer than they should. Use Turbo mode when that happens.

---

# How to find offsets

We need to use disassembler in this case. 

After finishing disassembling `main` we need to find those bytes:
```
21 00 23 1E 00 10 2E 1E 00 18 21 1E
```

It should return a function that looks something like this:
```asm
.text:0000007100022CA0 sub_7100022CA0                          ; CODE XREF: sub_7100127780+90↓j
.text:0000007100022CA0                                         ; sub_7100127780+158↓p ...
.text:0000007100022CA0                 UCVTF           S1, W1
.text:0000007100022CA4                 FMOV            S0, #1.0
.text:0000007100022CA8                 FDIV            S0, S0, S1
.text:0000007100022CAC                 ADRP            X8, #dword_710080C9F0@PAGE
.text:0000007100022CB0                 CMP             W1, #0x3C
.text:0000007100022CB4                 STR             S0, [X8,#dword_710080C9F0@PAGEOFF]
.text:0000007100022CB8                 MOV             W8, #0x1E
.text:0000007100022CBC                 CSEL            W8, W1, W8, EQ
.text:0000007100022CC0                 STR             W8, [X0,#0x40]
.text:0000007100022CC4                 RET
.text:0000007100022CC4 ; End of function sub_7100022CA0
```

`dword_710080C9F0` is our pointer where it's stored frame time in seconds that is used as FPS lock.

So for 15 FPS it will look like this:
```yaml
15FPS:
  -
    type: write
    address: [MAIN, 0x80C9F0]
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
    address: [MAIN, 0x80C9F0]
    value_type: float
    value: 0.03333333333

```
