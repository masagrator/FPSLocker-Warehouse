# DOOM® Eternal

> Game info

TitleID: `0100B1A00D8CE000`<br>
Explanation based on:
- Internal version: `1.13`, 
- Nintendo version ID: `v13`/`v851968`
- BID: `5AF6F31EAC42D8C0`
- Engine: `IdTech 7`

> Details

Game can be set above 30 FPS with plugin alone, but because of dynamic resolution target set to 32-33 ms we need to tweak it. Also we block adaptive GPU frequency for anything above 30 FPS.
There is also one setting `com_adaptiveTickMaxHz` that must be tweaked otherwise setting anything above 30 FPS results in wrong game speed.

# How to find offsets

We need to use disassembler in this case.

We need to find those strings:
```
rs_force460
rs_raiseThreshold
rs_dropThreshold
rs_raiseMilliseconds
rs_dropMilliseconds
com_adaptiveTickMaxHz
```

Each one should have only one xref.

Each xref for X0 register contains an address at which will be stored pointer related to our value.<br>
For example for our last string piece of function looks like this:
```asm
.text:0000007100CADC70                 ADRP            X0, #qword_7106A674F8@PAGE
.text:0000007100CADC74                 ADD             X0, X0, #qword_7106A674F8@PAGEOFF
.text:0000007100CADC78                 ADRP            X1, #aComAdaptivetic_1@PAGE ; "com_adaptiveTickMaxHz"
.text:0000007100CADC7C                 ADD             X1, X1, #aComAdaptivetic_1@PAGEOFF ; "com_adaptiveTickMaxHz"
.text:0000007100CADC80                 ADRP            X2, #a30_0@PAGE ; "30"
.text:0000007100CADC84                 ADD             X2, X2, #a30_0@PAGEOFF ; "30"
.text:0000007100CADC88                 ADRP            X4, #aMaxGameHz@PAGE ; "max game hz"
.text:0000007100CADC8C                 ADD             X4, X4, #aMaxGameHz@PAGEOFF ; "max game hz"
.text:0000007100CADC90                 MOV             W3, #2
.text:0000007100CADC94                 MOV             X5, XZR
.text:0000007100CADC98                 MOV             X6, XZR
```

So our pointer is stored at MAIN+0x6A674F8.

Those values are stored as int32 at offset 0x8
```
rs_force460
com_adaptiveTickMaxHz
```

- `rs_force460` - we want to set it to 1 for anything above 30 FPS to solve issues with game fighting with sys-clk and causing performance drops
- `com_adaptiveTickMaxHz` - we want to set it to 60 for anything above 30 FPS to solve issues with game speed


Those values are stored as float at offset 0xC
```
rs_raiseThreshold
rs_dropThreshold
rs_raiseMilliseconds
rs_dropMilliseconds
```

For 30 FPS it looks like this:
```yaml
30FPS:
  # rs_force460 (default)
  -
    type: write
    address: [MAIN, 0x792F238, 8]
    value_type: int32
    value: 0
  # rs_raiseThreshold (default)
  -
    type: write
    address: [MAIN, 0x792E9C8, 0xC]
    value_type: float
    value: 0.948
  # rs_dropThreshold (default)
  -
    type: write
    address: [MAIN, 0x792E950, 0xC]
    value_type: float
    value: 0.97
  # rs_raiseMilliseconds
  -
    type: write
    address: [MAIN, 0x792E578, 0xC]
    value_type: float
    value: 32
  # rs_dropMilliseconds
  -
    type: write
    address: [MAIN, 0x792E500, 0xC]
    value_type: float
    value: 33
  # com_adaptiveTickMaxHz (default)
  -
    type: write
    address: [MAIN, 0x6A674F8, 8]
    value_type: int32
    value: 30
```

For 45 FPS like this:
```yaml
45FPS:
  # rs_force460
  -
    type: write
    address: [MAIN, 0x792F238, 8]
    value_type: int32
    value: 1
  # rs_raiseThreshold
  -
    type: write
    address: [MAIN, 0x792E9C8, 0xC]
    value_type: float
    value: 0.63
  # rs_dropThreshold
  -
    type: write
    address: [MAIN, 0x792E950, 0xC]
    value_type: float
    value: 0.646
  # rs_raiseMilliseconds
  -
    type: write
    address: [MAIN, 0x792E578, 0xC]
    value_type: float
    value: 21.33
  # rs_dropMilliseconds
  -
    type: write
    address: [MAIN, 0x792E500, 0xC]
    value_type: float
    value: 22
  # com_adaptiveTickMaxHz
  -
    type: write
    address: [MAIN, 0x6A674F8, 8]
    value_type: int32
    value: 60
```
