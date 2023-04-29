# Oceanhorn 2: Knights of the Lost Realm

> Game info

TitleID: `01007FB010DC8000`<br>
Explanation based on:
- Internal version: `1.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `9F2F187D1C6E44EC`
- Engine: `Unreal Engine 4.23.1`

> Details

Plugin alone can set FPS above 30, but because of dynamic resolution set to 32.1 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710198C744                 ADRP            X1, #aRDynamicresFra_0@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710198C748                 ADD             X1, X1, #aRDynamicresFra_0@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710198C74C                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710198C750                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710198C754                 LDR             X8, [X8,#8]
.text:000000710198C758                 MOV             W3, #0x20
.text:000000710198C75C                 BLR             X8
.text:000000710198C760                 ADRP            X19, #qword_71051E80C8@PAGE
.text:000000710198C764                 ADD             X19, X19, #qword_71051E80C8@PAGEOFF
.text:000000710198C768                 STP             X23, X0, [X19]
.text:000000710198C76C                 LDR             X8, [X0]
.text:000000710198C770                 LDR             X8, [X8,#0x58]
.text:000000710198C774                 BLR             X8
.text:000000710198C778                 STR             X0, [X19,#(qword_71051E80D8 - 0x71051E80C8)]
```

So first final address is stored at 0x51E80D8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101E79D48                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101E79D4C                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101E79D50                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E79D54                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E79D58                 LDR             X8, [X8,#8]
.text:0000007101E79D5C                 MOV             W3, WZR
.text:0000007101E79D60                 BLR             X8
.text:0000007101E79D64                 ADRP            X19, #qword_71052122D0@PAGE
.text:0000007101E79D68                 ADD             X19, X19, #qword_71052122D0@PAGEOFF
.text:0000007101E79D6C                 ADRP            X8, #off_710409C1B0@PAGE
.text:0000007101E79D70                 ADD             X8, X8, #off_710409C1B0@PAGEOFF
.text:0000007101E79D74                 STP             X8, X0, [X19]
.text:0000007101E79D78                 LDR             X8, [X0]
.text:0000007101E79D7C                 LDR             X8, [X8,#0x58]
.text:0000007101E79D80                 BLR             X8
.text:0000007101E79D84                 STR             X0, [X19,#(qword_71052122E0 - 0x71052122D0)]
```
So our second final address is 0x52122E0.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 32.1.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimal - 1.2
  -
    type: write
    address: [MAIN, 0x51E80D8, 0]
    value_type: float
    value: [65.4, 65.4]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x52122E0, 0]
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
    address: [MAIN, 0x51E80D8, 0]
    value_type: float
    value: [32.1, 32.1]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x52122E0, 0]
    value_type: float
    value: [0, 0]

```