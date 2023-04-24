# The Sinking City

> Game info

TitleID: `010028D00BA1A000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `85E49C169A8B988A`
- Engine: `Unreal Engine 4.22.1`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 33.3 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:00000071019E2248                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071019E224C                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071019E2250                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:00000071019E2254                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:00000071019E2258                 MOV             W3, #0x20
.text:00000071019E225C                 BLR             X8
.text:00000071019E2260                 ADRP            X19, #qword_7105228DB0@PAGE
.text:00000071019E2264                 ADD             X19, X19, #qword_7105228DB0@PAGEOFF
.text:00000071019E2268                 STP             X22, X0, [X19]
.text:00000071019E226C                 LDR             X8, [X0]
.text:00000071019E2270                 LDR             X8, [X8,#0x48]
.text:00000071019E2274                 BLR             X8
.text:00000071019E2278                 STR             X0, [X19,#(qword_7105228DC0 - 0x7105228DB0)]
```

So first final address is stored at 0x5228DC0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101ED3D50                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101ED3D54                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101ED3D58                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101ED3D5C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101ED3D60                 MOV             W3, WZR
.text:0000007101ED3D64                 BLR             X8
.text:0000007101ED3D68                 ADRP            X19, #qword_710524F930@PAGE
.text:0000007101ED3D6C                 ADD             X19, X19, #qword_710524F930@PAGEOFF
.text:0000007101ED3D70                 ADRP            X8, #off_710438AF80@PAGE
.text:0000007101ED3D74                 ADD             X8, X8, #off_710438AF80@PAGEOFF
.text:0000007101ED3D78                 STP             X8, X0, [X19]
.text:0000007101ED3D7C                 LDR             X8, [X0]
.text:0000007101ED3D80                 LDR             X8, [X8,#0x48]
.text:0000007101ED3D84                 BLR             X8
.text:0000007101ED3D88                 STR             X0, [X19,#(qword_710524F940 - 0x710524F930)]
```
So our second final address is 0x524F940.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimals
  -
    type: write
    address: [MAIN, 0x5228DC0, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x524F940, 0]
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
    address: [MAIN, 0x5228DC0, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x524F940, 0]
    value_type: float
    value: [0, 0]

```
