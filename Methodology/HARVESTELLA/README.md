# HARVESTELLA

> Game info

TitleID: `0100521017B2A000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `249EAB9BF046C5EA`
- Engine: `Unreal Engine 4.27.2`

> Details

Game is using internal FPS lock + using dynamic resolution set to 33.33 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007102CC568C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102CC5690                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102CC5694                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102CC5698                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102CC569C                 LDR             X8, [X8,#0x10]
.text:0000007102CC56A0                 MOV             W3, #0x20
.text:0000007102CC56A4                 BLR             X8
.text:0000007102CC56A8                 ADRP            X19, #qword_7107B279D8@PAGE
.text:0000007102CC56AC                 ADD             X19, X19, #qword_7107B279D8@PAGEOFF
.text:0000007102CC56B0                 STP             X24, X0, [X19]
.text:0000007102CC56B4                 LDR             X8, [X0]
.text:0000007102CC56B8                 LDR             X8, [X8,#0x68]
.text:0000007102CC56BC                 BLR             X8
.text:0000007102CC56C0                 STR             X0, [X19,#(qword_7107B279E8 - 0x7107B279D8)]
```

So first final address is stored at 0x7B279E8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071031F417C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071031F4180                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071031F4184                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071031F4188                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071031F418C                 LDR             X8, [X8,#0x10]
.text:00000071031F4190                 MOV             W3, WZR
.text:00000071031F4194                 BLR             X8
.text:00000071031F4198                 ADRP            X19, #qword_7107B555D8@PAGE
.text:00000071031F419C                 ADD             X19, X19, #qword_7107B555D8@PAGEOFF
.text:00000071031F41A0                 ADRP            X8, #off_71065718B8@PAGE
.text:00000071031F41A4                 ADD             X8, X8, #off_71065718B8@PAGEOFF
.text:00000071031F41A8                 STP             X8, X0, [X19]
.text:00000071031F41AC                 LDR             X8, [X0]
.text:00000071031F41B0                 LDR             X8, [X8,#0x68]
.text:00000071031F41B4                 BLR             X8
.text:00000071031F41B8                 STR             X0, [X19,#(qword_7107B555E8 - 0x7107B555D8)]
```
So our second final address is 0x7B555E8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x7B279E8, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7B555E8, 0]
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
    address: [MAIN, 0x7B279E8, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x7B555E8, 0]
    value_type: float
    value: [0, 0]

```