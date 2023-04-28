# Rad Rogers: Radical Edition

> Game info

TitleID: `010000600CD54000`<br>
Explanation based on:
- Internal version: `1.2.0`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `78885A1CA987C04C`
- Engine: `Unreal Engine 4.17.2`

> Details

Game has broken NVN interval and is forced to use SmoothedFrameRateRange that is set to max 31. We will use different internal FPS lock that has higher priority to overwrite it. Beside that we need to tweak Dynamic Resolution. This game is using custom implementation that using by description target in ms, but it doesn't make any sense to follow that, so use my numbers I have tested from older patches to this game.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
r.DynamicRes.FrameTimeBudget
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101E80DB4                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101E80DB8                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101E80DBC                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E80DC0                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E80DC4                 MOV             W3, WZR
.text:0000007101E80DC8                 BLR             X8
.text:0000007101E80DCC                 ADRP            X8, #qword_7104B711F8@PAGE
.text:0000007101E80DD0                 ADD             X8, X8, #qword_7104B711F8@PAGEOFF
.text:0000007101E80DD4                 ADD             X8, X8, #0x10
.text:0000007101E80DD8                 STR             X0, [X22,#(qword_710579C200 - 0x710579BC70)]
.text:0000007101E80DDC                 ADD             X19, X22, #0x588
.text:0000007101E80DE0                 STR             X8, [X22,#(qword_710579C1F8 - 0x710579BC70)]
.text:0000007101E80DE4                 LDR             X8, [X0]
.text:0000007101E80DE8                 LDR             X8, [X8,#0x48]
.text:0000007101E80DEC                 BLR             X8
.text:0000007101E80DF0                 STR             X0, [X22,#(qword_710579C208 - 0x710579BC70)]
```

So first final address is stored at 0x579C208.

The same way we're searching for 
```
t.MaxFPS
```

Our pointer stores two floats. By default t.MaxFPS is always 0<br>
So our entry for 15 FPS will look like this
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x579C208, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing
```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # t.MaxFPS (default value, NVN interval will ensure 30 FPS lock)
  -
    type: write
    address: [MAIN, 0x579C208, 0]
    value_type: float
    value: [0, 0]
```