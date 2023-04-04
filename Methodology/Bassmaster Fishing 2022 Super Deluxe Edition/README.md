# Bassmaster Fishing 2022: Super Deluxe Edition

> Game info

TitleID: `0100B8501771A000`<br>
Explanation based on:
- Internal version: `1.02`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `78BF042012CF9EE8`
- Engine: `Unreal Engine 4.26.1`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 33.3333 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below after first BLR we have base address
```asm
.text:00000071028B5EFC                 ADRP            X1, #aRDynamicresFra@PAGE
.text:00000071028B5F00                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071028B5F04                 ADRP            X2, #aFrameSTimeBudg@PAGE
.text:00000071028B5F08                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071028B5F0C                 LDR             X8, [X8,#0x10]
.text:00000071028B5F10                 MOV             W3, #0x20
.text:00000071028B5F14                 BLR             X8
.text:00000071028B5F18                 ADRP            X19, #unk_710797AA88@PAGE
.text:00000071028B5F1C                 ADD             X19, X19, #unk_710797AA88@PAGEOFF
.text:00000071028B5F20                 STP             X24, X0, [X19]
.text:00000071028B5F24                 LDR             X8, [X0]
.text:00000071028B5F28                 LDR             X8, [X8,#0x68]
.text:00000071028B5F2C                 BLR             X8
```

Our base address is 0x797AA88.

After next BLR we have an offset:
```asm
STR x0, [x19, #0x10]
```
so our final address is 0x797AA88 + 0x10 = 0x797AA98.<br>
If you use IDA, you will have already calculated pointer
```asm
.text:00000071028B5F30                 STR             X0, [X19,#(qword_710797AA98 - 0x710797AA88)]
```

The same way we're searching for 
```
t.MaxFPS
```

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007102DDE924                 ADRP            X1, #aTMaxfps@PAGE
.text:0000007102DDE928                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007102DDE92C                 ADRP            X2, #aCapsFpsToTheGi@PAGE
.text:0000007102DDE930                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007102DDE934                 LDR             X8, [X8,#0x10]
.text:0000007102DDE938                 MOV             W3, WZR
.text:0000007102DDE93C                 BLR             X8
.text:0000007102DDE940                 ADRP            X19, #unk_71079A7F38@PAGE
.text:0000007102DDE944                 ADD             X19, X19, #unk_71079A7F38@PAGEOFF
.text:0000007102DDE948                 ADRP            X8, #off_71063078A8@PAGE
.text:0000007102DDE94C                 ADD             X8, X8, #off_71063078A8@PAGEOFF
.text:0000007102DDE950                 STP             X8, X0, [X19]
.text:0000007102DDE954                 LDR             X8, [X0]
.text:0000007102DDE958                 LDR             X8, [X8,#0x68]
.text:0000007102DDE95C                 BLR             X8
.text:0000007102DDE960                 STR             X0, [X19,#(qword_71079A7F48 - 0x71079A7F38)]
```
So our second final address is 0x79A7F48.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget via config file is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) rounded to two decimals
   -
    type: write
    address: [MAIN, 0x797AA98, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x79A7F48, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # r.DynamicRes.FrameTimeBudget (default value)
  -
    type: write
    address: [MAIN, 0x797AA98, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x79A7F48, 0]
    value_type: float
    value: [0, 0]

```
