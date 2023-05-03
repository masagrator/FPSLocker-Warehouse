# Sherlock Holmes The Awakened

> Game info

TitleID: `0100CA800F9B2000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `32BF1643370F70AA`
- Engine: `Unreal Engine 4.27.2`

> Details

Game is using internal FPS lock. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
t.MaxFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007103BBA154                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007103BBA158                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007103BBA15C                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007103BBA160                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007103BBA164                 MOV             W3, WZR
.text:0000007103BBA168                 LDR             X8, [X8,#0x10]
.text:0000007103BBA16C                 BLR             X8
.text:0000007103BBA170                 ADRP            X19, #qword_7107D7E958@PAGE
.text:0000007103BBA174                 ADD             X19, X19, #qword_7107D7E958@PAGEOFF
.text:0000007103BBA178                 ADRP            X8, #off_71066928B8@PAGE
.text:0000007103BBA17C                 ADD             X8, X8, #off_71066928B8@PAGEOFF
.text:0000007103BBA180                 STP             X8, X0, [X19]
.text:0000007103BBA184                 LDR             X8, [X0]
.text:0000007103BBA188                 LDR             X8, [X8,#0x68]
.text:0000007103BBA18C                 BLR             X8
.text:0000007103BBA190                 STR             X0, [X19,#(qword_7107D7E968 - 0x7107D7E958)]
```

So final address is stored at 0x7D7E968.

Our final address stores pointer that points to two floats. By default t.MaxFPS is always 30.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7D7E968, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x7D7E968, 0]
    value_type: float
    value: [0, 0]

```