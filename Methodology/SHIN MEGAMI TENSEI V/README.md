# SHIN MEGAMI TENSEI V

> Game info

TitleID: `0100B870126CE000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `019FBFE7738EA314`
- Engine: `Unreal Engine 4.23.1`

> Details

Plugin alone can set FPS above 30, but because of Dynamic Resolution set to 40ms performance is subpar. We need to patch that.
Also game uses internal FPS lock to 30 when cutscenes are played. We will need to patch this too.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007100C5B130                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007100C5B134                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007100C5B138                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007100C5B13C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007100C5B140                 MOV             W3, #0x20
.text:0000007100C5B144                 BLR             X8
.text:0000007100C5B148                 ADRP            X19, #qword_71075F81C0@PAGE
.text:0000007100C5B14C                 ADD             X19, X19, #qword_71075F81C0@PAGEOFF
.text:0000007100C5B150                 STP             X24, X0, [X19]
.text:0000007100C5B154                 LDR             X8, [X0]
.text:0000007100C5B158                 LDR             X8, [X8,#0x58]
.text:0000007100C5B15C                 BLR             X8
.text:0000007100C5B160                 STR             X0, [X19,#(qword_71075F81D0 - 0x71075F81C0)]
```

So first final address is stored at 0x75F81D0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007100C7BAD0                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007100C7BAD4                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007100C7BAD8                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007100C7BADC                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007100C7BAE0                 MOV             W3, WZR
.text:0000007100C7BAE4                 BLR             X8
.text:0000007100C7BAE8                 ADRP            X19, #qword_7107621D60@PAGE
.text:0000007100C7BAEC                 ADD             X19, X19, #qword_7107621D60@PAGEOFF
.text:0000007100C7BAF0                 ADRP            X8, #off_71055B5500@PAGE
.text:0000007100C7BAF4                 ADD             X8, X8, #off_71055B5500@PAGEOFF
.text:0000007100C7BAF8                 STP             X8, X0, [X19]
.text:0000007100C7BAFC                 LDR             X8, [X0]
.text:0000007100C7BB00                 LDR             X8, [X8,#0x58]
.text:0000007100C7BB04                 BLR             X8
.text:0000007100C7BB08                 STR             X0, [X19,#(qword_7107621D70 - 0x7107621D60)]
```
So our second final address is 0x7621D70.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is 30 in cutscenes and everywhere else 0. r.DynamicRes.FrameTimeBudget is 40.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 2 decimals
  -
    type: write
    address: [MAIN, 0x75F81D0, 0]
    value_type: float
    value: [66.66, 66.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7621D70, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # r.DynamicRes.FrameTimeBudget
  -
    type: write
    address: [MAIN, 0x75F81D0, 0]
    value_type: float
    value: [33.33, 33.33]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7621D70, 0]
    value_type: float
    value: [0, 0]

```