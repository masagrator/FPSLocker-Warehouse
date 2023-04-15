# Vampyr

> Game info

TitleID: `01000BD00CE64000`<br>
Explanation based on:
- Internal version: `0.4`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `E417100FFEEFD1DE`
- Engine: `Unreal Engine 4.15.1`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution with FPS target set to 30 FPS, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
r.DynResTargetFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:00000071006DC7F8                 ADRP            X1, #aRDynrestargetf@PAGE ; "r.DynResTargetFPS"
.text:00000071006DC7FC                 ADD             X1, X1, #aRDynrestargetf@PAGEOFF ; "r.DynResTargetFPS"
.text:00000071006DC800                 ADRP            X3, #aDynamicResolut@PAGE ; "Dynamic Resolution target FPS.\n<=0:off"...
.text:00000071006DC804                 ADD             X3, X3, #aDynamicResolut@PAGEOFF ; "Dynamic Resolution target FPS.\n<=0:off"...
.text:00000071006DC808                 MOV             W2, WZR
.text:00000071006DC80C                 MOV             W4, WZR
.text:00000071006DC810                 BLR             X8
.text:00000071006DC814                 ADRP            X19, #qword_71071A31E8@PAGE
.text:00000071006DC818                 ADD             X19, X19, #qword_71071A31E8@PAGEOFF
.text:00000071006DC81C                 STP             X22, X0, [X19]
.text:00000071006DC820                 LDR             X8, [X0]
.text:00000071006DC824                 LDR             X8, [X8,#0x38]
.text:00000071006DC828                 BLR             X8
.text:00000071006DC82C                 STR             X0, [X19,#(qword_71071A31F8 - 0x71071A31E8)]
```

So first final address is stored at 0x71A31F8.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:00000071006E770C                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:00000071006E7710                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:00000071006E7714                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:00000071006E7718                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:00000071006E771C                 MOV             W3, WZR
.text:00000071006E7720                 BLR             X8
.text:00000071006E7724                 ADRP            X19, #qword_71071B2BC0@PAGE
.text:00000071006E7728                 ADD             X19, X19, #qword_71071B2BC0@PAGEOFF
.text:00000071006E772C                 ADRP            X8, #off_7105974DC8@PAGE
.text:00000071006E7730                 ADD             X8, X8, #off_7105974DC8@PAGEOFF
.text:00000071006E7734                 STP             X8, X0, [X19]
.text:00000071006E7738                 LDR             X8, [X0]
.text:00000071006E773C                 LDR             X8, [X8,#0x40]
.text:00000071006E7740                 BLR             X8
.text:00000071006E7744                 STR             X0, [X19,#(qword_71071B2BD0 - 0x71071B2BC0)]
```
So our second final address is 0x71B2BD0.

Each of our final address stores pointer that points to two 32-bit integers. By default t.MaxFPS is always 0. r.DynResTargetFPS is 30.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynResTargetFPS
  -
    type: write
    address: [MAIN, 0x71A31F8, 0]
    value_type: int32
    value: [15, 15]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x71B2BD0, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # r.DynResTargetFPS (default value)
  -
    type: write
    address: [MAIN, 0x71A31F8, 0]
    value_type: int32
    value: [30, 30]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x71B2BD0, 0]
    value_type: float
    value: [0, 0]

```
