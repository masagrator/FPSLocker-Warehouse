# Life is Strange 2

> Game info

TitleID: `0100FD101186C000`<br>
Explanation based on:
- Internal version: `1.1.0`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `BF0088C59D7E97C0`
- Engine: `Unreal Engine 4.26.2`

> Details

Game is using internal FPS lock. Requires patch to fix those.
Game doesn't use dynamic resolution because enabling causes graphical glitches. It's blocking some graphics effects related to physics (for example hairs reacting to gravity) if rendering frame takes too much time, but cannot find what is responsible for this behaviour.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-16-LE):
```
t.MaxFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:00000071030AE478                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071030AE47C                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071030AE480                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071030AE484                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071030AE488                 LDR             X8, [X8,#0x10]
.text:00000071030AE48C                 MOV             W3, WZR
.text:00000071030AE490                 BLR             X8
.text:00000071030AE494                 ADRP            X19, #qword_7108082C58@PAGE
.text:00000071030AE498                 ADD             X19, X19, #qword_7108082C58@PAGEOFF
.text:00000071030AE49C                 ADRP            X8, #off_71063D88A8@PAGE
.text:00000071030AE4A0                 ADD             X8, X8, #off_71063D88A8@PAGEOFF
.text:00000071030AE4A4                 STP             X8, X0, [X19]
.text:00000071030AE4A8                 LDR             X8, [X0]
.text:00000071030AE4AC                 LDR             X8, [X8,#0x68]
.text:00000071030AE4B0                 BLR             X8
.text:00000071030AE4B4                 STR             X0, [X19,#(qword_7108082C68 - 0x7108082C58)]
```

So final address is stored at 0x8051770.

Our final address stores pointer that points to two floats. By default t.MaxFPS is always 0. Game is using SmoothedFrameRateRange to lock FPS, but t.MaxFPS has higher priority, so we will use that.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x8082C68, 0]
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
    address: [MAIN, 0x8082C68, 0]
    value_type: float
    value: [0, 0]

```