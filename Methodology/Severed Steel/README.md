# Severed Steel

> Game info

TitleID: `0100E1C0148F8000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `77C053D779EE97F6`
- Engine: `Unreal Engine 4.27.2`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 30 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:00000071030B614C                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:00000071030B6150                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:00000071030B6154                 ADRP            X2, #aF_666@PAGE ; "F"
.text:00000071030B6158                 ADD             X2, X2, #aF_666@PAGEOFF ; "F"
.text:00000071030B615C                 LDR             X8, [X8,#0x10]
.text:00000071030B6160                 MOV             W3, #0x20
.text:00000071030B6164                 BLR             X8
.text:00000071030B6168                 ADRP            X19, #qword_71075EE898@PAGE
.text:00000071030B616C                 ADD             X19, X19, #qword_71075EE898@PAGEOFF
.text:00000071030B6170                 STP             X24, X0, [X19]
.text:00000071030B6174                 LDR             X8, [X0]
.text:00000071030B6178                 LDR             X8, [X8,#0x68]
.text:00000071030B617C                 BLR             X8
.text:00000071030B6180                 STR             X0, [X19,#(qword_71075EE8A8 - 0x71075EE898)]
```

So first final address is stored at 0x75EE8A8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071035E045C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071035E0460                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071035E0464                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071035E0468                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071035E046C                 LDR             X8, [X8,#0x10]
.text:00000071035E0470                 MOV             W3, WZR
.text:00000071035E0474                 BLR             X8
.text:00000071035E0478                 ADRP            X19, #qword_710761C468@PAGE
.text:00000071035E047C                 ADD             X19, X19, #qword_710761C468@PAGEOFF
.text:00000071035E0480                 ADRP            X8, #off_71060788B8@PAGE
.text:00000071035E0484                 ADD             X8, X8, #off_71060788B8@PAGEOFF
.text:00000071035E0488                 STP             X8, X0, [X19]
.text:00000071035E048C                 LDR             X8, [X0]
.text:00000071035E0490                 LDR             X8, [X8,#0x68]
.text:00000071035E0494                 BLR             X8
.text:00000071035E0498                 STR             X0, [X19,#(qword_710761C478 - 0x710761C468)]
```
So our second final address is 0x761C478.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 30.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = 0.9 * (1000/FPS)
  -
    type: write
    address: [MAIN, 0x75EE8A8, 0]
    value_type: float
    value: [60, 60]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x761C478, 0]
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
    address: [MAIN, 0x75EE8A8, 0]
    value_type: float
    value: [30, 30]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x761C478, 0]
    value_type: float
    value: [0, 0]

```