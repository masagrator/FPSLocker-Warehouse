# Little Nightmares II

> Game info

TitleID: `010097100EDD6000`<br>
Explanation based on:
- Internal version: `1.4`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `7F4216B6E784A4B2`
- Engine: `Unreal Engine 4.24.2`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 33.33 ms, performance is subpar. Requires patch to fix that.
Game has issues with going below 20 FPS by using t.MaxFPS alone, we must force it to run at 15 FPS. Below 20 FPS it slows down.

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below after first BLR we have base address
```asm
.text:000000710354FF5C                 ADRP            X1, #aRDynamicresFra@PAGE
.text:000000710354FF60                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710354FF64                 ADRP            X2, #aFrameSTimeBudg@PAGE
.text:000000710354FF68                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710354FF6C                 MOV             W3, #0x20
.text:000000710354FF70                 BLR             X8
.text:000000710354FF74                 ADRP            X19, #unk_71074A0360@PAGE
.text:000000710354FF78                 ADD             X19, X19, #unk_71074A0360@PAGEOFF
.text:000000710354FF7C                 STP             X23, X0, [X19]
.text:000000710354FF80                 LDR             X8, [X0]
.text:000000710354FF84                 LDR             X8, [X8,#0x68]
.text:000000710354FF88                 BLR             X8
```

Our base address is 0x74A0360.

After next BLR we have an offset:
```asm
STR x0, [x19, #0x10]
```
so our final address is 0x74A0360 + 0x10 = 0x74A0370.<br>
If you use IDA, you will have already calculated pointer
```asm
.text:000000710354FF8C                 STR             X0, [X19,#(qword_71074A0370 - 0x71074A0360)]
```

The same way we're searching for 
```
t.MaxFPS
```
It should have 2 xrefs. We are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007103C0DCD4                 ADRP            X1, #aTMaxfps@PAGE
.text:0000007103C0DCD8                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007103C0DCDC                 ADRP            X2, #aCapsFpsToTheGi@PAGE
.text:0000007103C0DCE0                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103C0DCE4                 MOV             W3, WZR
.text:0000007103C0DCE8                 BLR             X8
.text:0000007103C0DCEC                 ADRP            X19, #unk_71074CC700@PAGE
.text:0000007103C0DCF0                 ADD             X19, X19, #unk_71074CC700@PAGEOFF
.text:0000007103C0DCF4                 ADRP            X8, #off_710612B800@PAGE
.text:0000007103C0DCF8                 ADD             X8, X8, #off_710612B800@PAGEOFF
.text:0000007103C0DCFC                 STP             X8, X0, [X19]
.text:0000007103C0DD00                 LDR             X8, [X0]
.text:0000007103C0DD04                 LDR             X8, [X8,#0x68]
.text:0000007103C0DD08                 BLR             X8
.text:0000007103C0DD0C                 STR             X0, [X19,#(qword_71074CC710 - 0x71074CC700)]
```
So our second final address is 0x74CC710.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget via config file is 33.3333.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 20 FPS will look like this:
```yaml
20FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS)
  -
    type: write
    address: [MAIN, 0x745D838, 0]
    value_type: float
    value: [66.6666, 66.6666]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x74CC710, 0]
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
    address: [MAIN, 0x745D838, 0]
    value_type: float
    value: [33.3333, 33.3333]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x74CC710, 0]
    value_type: float
    value: [0, 0]

```
