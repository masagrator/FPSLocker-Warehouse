# Monster Truck Championship

> Game info

TitleID: `0100D30010C42000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `682F4A502035678D`
- Engine: `Unreal Engine 4.25.0`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to 32.33 ms, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:000000710244E5E8                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710244E5EC                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710244E5F0                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710244E5F4                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710244E5F8                 MOV             W3, #0x20
.text:000000710244E5FC                 BLR             X8
.text:000000710244E600                 ADRP            X19, #qword_7106F8C6A0@PAGE
.text:000000710244E604                 ADD             X19, X19, #qword_7106F8C6A0@PAGEOFF
.text:000000710244E608                 STP             X24, X0, [X19]
.text:000000710244E60C                 LDR             X8, [X0]
.text:000000710244E610                 LDR             X8, [X8,#0x68]
.text:000000710244E614                 BLR             X8
.text:000000710244E618                 STR             X0, [X19,#(qword_7106F8C6B0 - 0x7106F8C6A0)]
```

So first final address is stored at 0x6F8C6B0.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071028A27FC                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071028A2800                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071028A2804                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071028A2808                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071028A280C                 MOV             W3, WZR
.text:00000071028A2810                 BLR             X8
.text:00000071028A2814                 ADRP            X19, #qword_7106FB45C8@PAGE
.text:00000071028A2818                 ADD             X19, X19, #qword_7106FB45C8@PAGEOFF
.text:00000071028A281C                 ADRP            X8, #off_7105B091B0@PAGE
.text:00000071028A2820                 ADD             X8, X8, #off_7105B091B0@PAGEOFF
.text:00000071028A2824                 STP             X8, X0, [X19]
.text:00000071028A2828                 LDR             X8, [X0]
.text:00000071028A282C                 LDR             X8, [X8,#0x68]
.text:00000071028A2830                 BLR             X8
.text:00000071028A2834                 STR             X0, [X19,#(qword_7106FB45D8 - 0x7106FB45C8)]
```
So our second final address is 0x6FB45D8.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. r.DynamicRes.FrameTimeBudget is 32.33.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = 0.97 * (1000/FPS) cutted to two decimals
  -
    type: write
    address: [MAIN, 0x6F8C6B0, 0]
    value_type: float
    value: [64.66, 64.66]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x6FB45D8, 0]
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
    address: [MAIN, 0x6F8C6B0, 0]
    value_type: float
    value: [32.33, 32.33]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x6FB45D8, 0]
    value_type: float
    value: [0, 0]

```
