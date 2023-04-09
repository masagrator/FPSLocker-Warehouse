# Snake Pass

> Game info

TitleID: `0100C0F0020E8000`<br>
Explanation based on:
- Internal version: `1.4`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `D0798521F563E6A7`
- Engine: `Unreal Engine 4.16.0`

> Details

Game is using internal FPS lock. Requires patch to fix this.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
t.MaxFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:00000071019C1914                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071019C1918                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071019C191C                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071019C1920                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071019C1924                 MOV             W3, WZR
.text:00000071019C1928                 BLR             X8
.text:00000071019C192C                 ADRP            X8, #qword_7103DDAD28@PAGE
.text:00000071019C1930                 ADD             X8, X8, #qword_7103DDAD28@PAGEOFF
.text:00000071019C1934                 ADD             X8, X8, #0x10
.text:00000071019C1938                 STR             X0, [X22,#(qword_71049012B0 - 0x7104900D50)]
.text:00000071019C193C                 ADD             X19, X22, #0x558
.text:00000071019C1940                 STR             X8, [X22,#(qword_71049012A8 - 0x7104900D50)]
.text:00000071019C1944                 LDR             X8, [X0]
.text:00000071019C1948                 LDR             X8, [X8,#0x40]
.text:00000071019C194C                 BLR             X8
.text:00000071019C1950                 STR             X0, [X22,#(qword_71049012B8 - 0x7104900D50)]
```

So final address is stored at 0x49012B8.

Our final address stores pointer that points to two floats. t.MaxFPS is set to 30.<br>
Entry for 15 FPS will look like this:
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x49012B8, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x49012B8, 0]
    value_type: float
    value: [30, 30]

```
