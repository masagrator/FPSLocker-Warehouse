# Xenoblade Chronicles: Definitive Edition

> Game info

TitleID: `010074F013262000`<br>
Explanation based on:
- Internal version: `1.1.2`, 
- Nintendo version ID: `v6`/`v393216`
- BID: `92C78BB3DCBBC3F7`
- Engine: Monolith Soft proprietary engine (Rendering pipeline is called `DrPixlMan`)

> Details

This game is using internal vsync signal detection set to 2, which means it skips every second frame. <br>
We need to change it to 1 to unlock >30 FPS. <br>
2D animations and particle effects are hardcoded to use 30 FPS, so above 30 FPS they are rendered faster than normal. We know offsets that must be used to patch their speed, but they are in read only section, so they cannot be patched via FPSLocker. You can find patch designed for 60 FPS [HERE](https://gbatemp.net/threads/mod-xenoblade-chronicles-definitive-edition-60fps.567921/post-10109178)<br>

Game is also using double buffer. To disable it, turn off `Sync Wait` in FPSLocker. Expect some small graphical glitches. Cutscenes even after that are still runinng using double buffer, and even if FPS counter shows that they're rendered in 60 FPS, that may not be the case with too low OC.

---

# How to find offsets

We need to use disassembler in this case. 

> First we determine how to enable 60 FPS.

After finishing disassembling `main`, we need to find function
```cpp
ml::DevGraph::setVSync
```

It has instructions that are loading pointers to vsync signal detection values. Whole function looks something like this:
```asm
text:0000007100683DF0 ; __int64 __fastcall ml::DevGraph::setVSync(ml::DevGraph *__hidden this, int)
.text:0000007100683DF0                 EXPORT _ZN2ml8DevGraph8setVSyncEi
.text:0000007100683DF0 _ZN2ml8DevGraph8setVSyncEi              ; CODE XREF: game::DevGuiSysConfig::DevGuiSysConfig(fw::Document const&)+EC↑p
.text:0000007100683DF0                                         ; game::DevGuiSysConfig::~DevGuiSysConfig()+30↑p ...
.text:0000007100683DF0                 ADRP            X8, #off_71013EFCD0@PAGE
.text:0000007100683DF4                 LDR             X8, [X8,#off_71013EFCD0@PAGEOFF]
.text:0000007100683DF8                 ADRP            X9, #off_71013EFD00@PAGE
.text:0000007100683DFC                 LDR             X9, [X9,#off_71013EFD00@PAGEOFF]
.text:0000007100683E00                 LDR             W10, [X8] ; ml::dg::s_nVSync
.text:0000007100683E04                 STR             W0, [X8] ; ml::dg::s_nVSync
.text:0000007100683E08                 STR             W10, [X9] ; ml::dg::s_nVSyncOld
.text:0000007100683E0C                 RET
.text:0000007100683E0C ; End of function ml::DevGraph::setVSync(int)
```

`off_71013EFCD0` stores one pointer named `_ZN2ml2dg8s_nVSyncE` which is 0x13BFDA0, so our first offset is `[MAIN, 0x13BFDA0]`.<br>
`off_71013EFD00` stores another pointer named `_ZN2ml2dg11s_nVSyncOldE` which is 0x13BFDA4, so our second offset is `[MAIN, 0x13BFDA4]`

As they are stored one after another at the same size, we can use patch format in this way to write default values for 30 FPS and below:
```yaml
  -
    type: write
    address: [MAIN, 0x13BFDA0]
    value_type: int32
    value: [2, 2]
```