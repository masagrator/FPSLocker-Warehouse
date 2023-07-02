# Cassette Beasts

> Game info

TitleID: `010066F01A0E0000`<br>
Explanation based on:
- Internal version: `1.4.0`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `224357DED42E86ED`
- Engine: `Godot 3.5.1`

> Details
> 
Game is using internal FPS lock. It must be patched.

# How to find offsets

We need to use disassembler in this case.<br>
After finishing disassembling main, we need to find this string:
```
debug/settings/fps/force_fps
```

then we go to its first xref.

We are looking for first `free` call above referenced instruction, then for first instruction below `free` call. It should read from some register pointer address.
In our case it's X22.
```asm
.text:0000007100CDB264                 BL              free
.text:0000007100CDB268                 LDR             X19, [X22]
.text:0000007100CDB26C                 STUR            XZR, [X29,#var_10]
.text:0000007100CDB270                 ADRP            X1, #aDebugSettingsF@PAGE ; "debug/settings/fps/force_fps"
.text:0000007100CDB274                 ADD             X1, X1, #aDebugSettingsF@PAGEOFF ; "debug/settings/fps/force_fps"
.text:0000007100CDB278                 SUB             X0, X29, #-var_10
.text:0000007100CDB27C                 BL              sub_7100018E40
.text:0000007100CDB280                 MOV             W8, #2
```

So we need to find what X22 stores. We are doing that by searching for `LDR X22` instruction before our xref.

In our case it looks like this:
```asm
.text:0000007100CD9F68                 ADRP            X22, #off_71033C8370@PAGE
.text:0000007100CD9F6C                 LDUR            X8, [X29,#var_98]
.text:0000007100CD9F70                 LDR             X22, [X22,#off_71033C8370@PAGEOFF]
```

At `off_71033C8370` is stored fixed pointer `qword_71033DCB78`. This is where our pointer to FPS settings are stored -> `MAIN+0x33DCB78`.

FPS Lock is stored at offset 0x30 as int32.
We need to also tweak physics fps target that is stored at offset 0x24.

So our example entry will look like this
```yaml
15FPS:
  # physics/common/physics_fps
  -
    type: write
    address: [MAIN, 0x33DCB78, 0x24]
    value_type: int32
    value: 15
  # debug/settings/fps/force_fps
  -
    type: write
    address: [MAIN, 0x33DCB78, 0x30]
    value_type: int32
    value: 15
  -
    type: block
    what: timing
```
