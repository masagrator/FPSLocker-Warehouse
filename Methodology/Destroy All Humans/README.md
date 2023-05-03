# Destroy All Humans!

> Game info

TitleID: `01009E701356A000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `72E8F20EBBDBA296`
- Engine: `Unreal Engine 4.22.3`

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
.text:0000007102189F40                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102189F44                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:0000007102189F48                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:0000007102189F4C                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:0000007102189F50                 LDR             X8, [X8,#8]
.text:0000007102189F54                 MOV             W3, #0x20
.text:0000007102189F58                 BLR             X8
.text:0000007102189F5C                 ADRP            X19, #qword_71066C5390@PAGE
.text:0000007102189F60                 ADD             X19, X19, #qword_71066C5390@PAGEOFF
.text:0000007102189F64                 STP             X22, X0, [X19]
.text:0000007102189F68                 LDR             X8, [X0]
.text:0000007102189F6C                 LDR             X8, [X8,#0x48]
.text:0000007102189F70                 BLR             X8
.text:0000007102189F74                 STR             X0, [X19,#(qword_71066C53A0 - 0x71066C5390)]
```

So first final address is stored at 0x66C53A0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:000000710266A0A4                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:000000710266A0A8                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:000000710266A0AC                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:000000710266A0B0                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:000000710266A0B4                 LDR             X8, [X8,#8]
.text:000000710266A0B8                 MOV             W3, WZR
.text:000000710266A0BC                 BLR             X8
.text:000000710266A0C0                 ADRP            X19, #qword_71066ED310@PAGE
.text:000000710266A0C4                 ADD             X19, X19, #qword_71066ED310@PAGEOFF
.text:000000710266A0C8                 STP             X20, X0, [X19]
.text:000000710266A0CC                 LDR             X8, [X0]
.text:000000710266A0D0                 LDR             X8, [X8,#0x48]
.text:000000710266A0D4                 BLR             X8
.text:000000710266A0D8                 STR             X0, [X19,#(qword_71066ED320 - 0x71066ED310)]
```
So our second final address is 0x66ED320.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimal
  -
    type: write
    address: [MAIN, 0x66C53A0, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x66ED320, 0]
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
    address: [MAIN, 0x66C53A0, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x66ED320, 0]
    value_type: float
    value: [0, 0]

```