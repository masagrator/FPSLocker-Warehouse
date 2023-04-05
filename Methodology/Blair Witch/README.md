# Blair Witch

> Game info

TitleID: `01006CC01182C000`<br>
Explanation based on:
- Internal version: `1.0.3`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `C31E59266A218855`
- Engine: `Unreal Engine 4.21.2`

> Details

Game is using internal FPS lock and is dynamic resolution set to 33 ms, performance is subpar. Requires patch to fix those.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101E7E930                 ADRP            X1, #aRDynamicresFra_1@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101E7E934                 ADD             X1, X1, #aRDynamicresFra_1@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007101E7E938                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007101E7E93C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007101E7E940                 MOV             W3, #0x20
.text:0000007101E7E944                 BLR             X8
.text:0000007101E7E948                 ADRP            X19, #unk_7105CC7300@PAGE
.text:0000007101E7E94C                 ADD             X19, X19, #unk_7105CC7300@PAGEOFF
.text:0000007101E7E950                 STP             X20, X0, [X19]
.text:0000007101E7E954                 LDR             X8, [X0]
.text:0000007101E7E958                 LDR             X8, [X8,#0x48]
.text:0000007101E7E95C                 BLR             X8
.text:0000007101E7E960                 STR             X0, [X19,#(qword_7105CC7310 - 0x7105CC7300)]
```

So first final address is stored at 0x5CC7310.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710243EC28                 ADRP            X2, #aCapsFpsToTheGi@PAGE
.text:000000710243EC2C                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710243EC30                 MOV             W3, WZR
.text:000000710243EC34                 BLR             X8
.text:000000710243EC38                 ADRP            X19, #unk_7105CEB9E8@PAGE
.text:000000710243EC3C                 ADD             X19, X19, #unk_7105CEB9E8@PAGEOFF
.text:000000710243EC40                 ADRP            X8, #off_7104E002F0@PAGE
.text:000000710243EC44                 ADD             X8, X8, #off_7104E002F0@PAGEOFF
.text:000000710243EC48                 STP             X8, X0, [X19]
.text:000000710243EC4C                 LDR             X8, [X0]
.text:000000710243EC50                 LDR             X8, [X8,#0x48]
.text:000000710243EC54                 BLR             X8
.text:000000710243EC58                 STR             X0, [X19,#(qword_7105CEB9F8 - 0x7105CEB9E8)]
```
So our second final address is 0x5CEB9F8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0, via config r.DynamicRes.FrameTimeBudget is 33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget (1000/FPS) without cutted decimals
  -
    type: write
    address: [MAIN, 0x5CC7310, 0]
    value_type: float
    value: [66, 66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x5CEB9F8, 0]
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
    address: [MAIN, 0x5CC7310, 0]
    value_type: float
    value: [33, 33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x5CEB9F8, 0]
    value_type: float
    value: [0, 0]

```
