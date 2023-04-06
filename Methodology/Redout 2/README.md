# Redout 2

> Game info

TitleID: `0100664016D5C000`<br>
Explanation based on:
- Internal version: `1.0.6`, 
- Nintendo version ID: `v6`/`v393216`
- BID: `D45B9332B5742A70`
- Engine: `Unreal Engine 4.27.2`

> Details

Game is using internal FPS lock, and dynamic resolution set to 32.3 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007102ED9AC0                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102ED9AC4                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102ED9AC8                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102ED9ACC                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102ED9AD0                 LDR             X8, [X8,#0x10]
.text:0000007102ED9AD4                 MOV             W3, #0x20
.text:0000007102ED9AD8                 BLR             X8
.text:0000007102ED9ADC                 ADRP            X19, #qword_7108549638@PAGE
.text:0000007102ED9AE0                 ADD             X19, X19, #qword_7108549638@PAGEOFF
.text:0000007102ED9AE4                 STP             X24, X0, [X19]
.text:0000007102ED9AE8                 LDR             X8, [X0]
.text:0000007102ED9AEC                 LDR             X8, [X8,#0x68]
.text:0000007102ED9AF0                 BLR             X8
.text:0000007102ED9AF4                 STR             X0, [X19,#(qword_7108549648 - 0x7108549638)]
```

So first final address is stored at 0x8549648.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710340338C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007103403390                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007103403394                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103403398                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710340339C                 LDR             X8, [X8,#0x10]
.text:00000071034033A0                 MOV             W3, WZR
.text:00000071034033A4                 BLR             X8
.text:00000071034033A8                 ADRP            X19, #qword_7108577208@PAGE
.text:00000071034033AC                 ADD             X19, X19, #qword_7108577208@PAGEOFF
.text:00000071034033B0                 ADRP            X8, #off_7106E758B8@PAGE
.text:00000071034033B4                 ADD             X8, X8, #off_7106E758B8@PAGEOFF
.text:00000071034033B8                 STP             X8, X0, [X19]
.text:00000071034033BC                 LDR             X8, [X0]
.text:00000071034033C0                 LDR             X8, [X8,#0x68]
.text:00000071034033C4                 BLR             X8
.text:00000071034033C8                 STR             X0, [X19,#(qword_7108577218 - 0x7108577208)]
```
So our second final address is 0x8577218.

Each of our final address stores pointer that points to two floats. Game is swapping t.MaxFPS between 30 and 0. r.DynamicRes.FrameTimeBudget via config is 32.3.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget ((1000/FPS) * 0.969)
  -
    type: write
    address: [MAIN, 0x8549648, 0]
    value_type: float
    value: [64.6, 64.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x8577218, 0]
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
    address: [MAIN, 0x8549648, 0]
    value_type: float
    value: [32.3, 32.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x8577218, 0]
    value_type: float
    value: [30, 30]

```
