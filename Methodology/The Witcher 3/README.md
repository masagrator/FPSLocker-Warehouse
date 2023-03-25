# The Witcher 3

> Game info

TitleID: `010039400E8D6000`<br>
Explanation based on:
- Internal version: `3.7`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `4FFB62F1CD9E17F8`
- Engine: `REDengine 3`

Base version of game is not compatible with SaltyNX, that's why ✝️ next to its version.

> Details

Game is using internal FPS lock that is set as integer 60, but because of NVN interval it's locked to 30. We will be using internal FPS lock to change our FPS target.<br>
Dynamic resolution frametime also affects maximum FPS because it delays frame if it was rendered faster than target, so we need to tweak it too.<br>
Game is using for gameplay 31.5 ms and 40.0 ms for cutscenes. Because 31.5/33.(3) = 0.945 we will be multiplying this by each frametime target for both gameplay and cutscenes.

That's why for each FPS entry except `30FPS` and `60FPS` in yaml file we want to add this entry
```yaml
  -
    type: block
    what: timing

```

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling `main`, we need to find this string:
```
DRGameTargetFrameTimeInMs
```

and go to it's only available xref.<br>
Above ADRP/ADD loading pointer to this string we have ADRP/ADD that loads base address we need
```asm
.text:000000710210D9DC                 ADRP            X21, #qword_7104FDA8C8@PAGE
.text:000000710210D9E0                 ADD             X21, X21, #qword_7104FDA8C8@PAGEOFF
.text:000000710210D9E4                 ADRP            X8, #aDrgametargetfr@PAGE ; "DRGameTargetFrameTimeInMs"
.text:000000710210D9E8                 ADD             X8, X8, #aDrgametargetfr@PAGEOFF ; "DRGameTargetFrameTimeInMs"
```
So we take 0x4FDA8C8.

Below ADRP/ADD loading pointer to string we need to find this instruction:
```asm
MOV             W26, #0x41FC0000
```
below it we have STR that looks like this
```asm
STR w26, [x21, #0x28]
```
So we need to do: 0x4FDA8C8 + 0x28 + 4 = 0x4FDA8F4<br>
if you use IDA, you should have already calculated 0x4FDA8C8 + 0x28 as
```asm
.text:000000710210DA10                 STR             W26, [X21,#(dword_7104FDA8F0 - 0x7104FDA8C8)]
```

This is our address for `DRGameTargetFrameTimeInMs`. Value is stored as float. By default it's 31.5

We need to go the same way to xref of string
```
DRCinematicTargetFrameTimeInMs
```

find base address above ADRP/ADD
```asm
.text:000000710210DA48                 ADRP            X21, #qword_7104FDA8F8@PAGE
.text:000000710210DA4C                 ADD             X21, X21, #qword_7104FDA8F8@PAGEOFF
.text:000000710210DA50                 ADRP            X8, #aDrcinematictar@PAGE ; "DRCinematicTargetFrameTimeInMs"
.text:000000710210DA54                 ADD             X8, X8, #aDrcinematictar@PAGEOFF ; "DRCinematicTargetFrameTimeInMs"
```
So we take 0x4FDA8F8.

Below ADRP/ADD loading pointer to string we need to find first `BL` instruction.<br>
Just above it we have
```asm
STR w27, [x21, #0x28]
```
So we need to do: 0x4FDA8F8 + 0x28 + 4 = 0x4FDA8F4<br>
if you use IDA, you should have already calculated 0x4FDA8F8 + 0x28 as
```asm
.text:000000710210DA74                 STR             W27, [X21,#(dword_7104FDA920 - 0x7104FDA8F8)]
```

This is our address for `DRCinematicTargetFrameTimeInMs`. Value is stored as float. By default it's 40.0

We need to go the same way to xref of string
```
LimitFPS
```

find base address above ADRP/ADD
```asm
.text:00000071005E978C                 ADRP            X21, #qword_7104C983C0@PAGE
.text:00000071005E9790                 ADD             X21, X21, #qword_7104C983C0@PAGEOFF
.text:00000071005E9794                 STR             W22, [X8,#dword_7104C983B8@PAGEOFF]
.text:00000071005E9798                 ADRP            X8, #aLimitfps@PAGE ; "LimitFPS"
.text:00000071005E979C                 ADD             X8, X8, #aLimitfps@PAGEOFF ; "LimitFPS"
```

So we take 0x4C983C0.

Below ADRP/ADD loading pointer to string we need to find first `BL` instruction.
Just above it we have
```asm
STR w20, [x21, #0x28]
```

So we need to do: 0x4C983C0 + 0x28 + 4 = 0x4C983EC<br>
if you use IDA, you should have already calculated 0x4C983C0 + 0x28 as
```asm
.text:00000071005E97D4                 STR             W20, [X21,#(dword_7104C983E8 - 0x7104C983C0)]
```

This is our address for `LimitFPS`. Value is stored as int32. By default it's 60

So for 15 FPS it will be looking like this
```yaml
15FPS:
  # DRGameTargetFrameTimeInMs
  -
    type: write
    address: [MAIN, 0x4FDA8F4]
    value_type: float
    value: 63
  # DRCinematicTargetFrameTimeInMs
  -
    type: write
    address: [MAIN, 0x4FDA924]
    value_type: float
    value: 63
  # LimitFPS
  -
    type: write
    address: [MAIN, 0x4C983EC]
    value_type: int32
    value: 15
  -
    type: block
    what: timing
```
