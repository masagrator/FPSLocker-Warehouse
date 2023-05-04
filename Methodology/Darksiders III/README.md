# Darksiders III

> Game info

TitleID: `0100F8F014190000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `AF7114F019CE6E1D`
- Engine: `Unreal Engine 4.25.0`

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
.text:000000710209F8B4                 ADRP            X1, #aRDynamicresFra@PAGE ; "r.DynamicRes.FrameTimeBudget"
.text:000000710209F8B8                 ADD             X1, X1, #aRDynamicresFra@PAGEOFF ; "r.DynamicRes.FrameTimeBudget"
.text:000000710209F8BC                 ADRP            X2, #aFrameSTimeBudg@PAGE ; "Frame's time budget in milliseconds."
.text:000000710209F8C0                 ADD             X2, X2, #aFrameSTimeBudg@PAGEOFF ; "Frame's time budget in milliseconds."
.text:000000710209F8C4                 LDR             X8, [X8,#0x10]
.text:000000710209F8C8                 MOV             W3, #0x20
.text:000000710209F8CC                 BLR             X8
.text:000000710209F8D0                 ADRP            X19, #qword_71064F2150@PAGE
.text:000000710209F8D4                 ADD             X19, X19, #qword_71064F2150@PAGEOFF
.text:000000710209F8D8                 STP             X24, X0, [X19]
.text:000000710209F8DC                 LDR             X8, [X0]
.text:000000710209F8E0                 LDR             X8, [X8,#0x68]
.text:000000710209F8E4                 BLR             X8
.text:000000710209F8E8                 STR             X0, [X19,#(qword_71064F2160 - 0x71064F2150)]
```

So first final address is stored at 0x64F2160.

The same way we're searching for 
```
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

We are following similar pattern as for previous command. Whole piece of code looks something like this:
```asm
.text:0000007101DFA968                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101DFA96C                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101DFA970                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101DFA974                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101DFA978                 LDR             X8, [X8,#0x10]
.text:0000007101DFA97C                 MOV             W3, WZR
.text:0000007101DFA980                 BLR             X8
.text:0000007101DFA984                 ADRP            X19, #qword_71064E86A0@PAGE
.text:0000007101DFA988                 ADD             X19, X19, #qword_71064E86A0@PAGEOFF
.text:0000007101DFA98C                 ADRP            X8, #off_71050B08B0@PAGE
.text:0000007101DFA990                 ADD             X8, X8, #off_71050B08B0@PAGEOFF
.text:0000007101DFA994                 STP             X8, X0, [X19]
.text:0000007101DFA998                 LDR             X8, [X0]
.text:0000007101DFA99C                 LDR             X8, [X8,#0x68]
.text:0000007101DFA9A0                 BLR             X8
.text:0000007101DFA9A4                 STR             X0, [X19,#(qword_71064E86B0 - 0x71064E86A0)]
```
So our second final address is 0x64E86B0.

Each of our final address stores pointer that points to two floats. By default t.MaxFPS is in cutscenes 30, everywhere else 0. r.DynamicRes.FrameTimeBudget is 33.3.<br>
As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicRes.FrameTimeBudget = (1000/FPS) cutted to 1 decimal
  -
    type: write
    address: [MAIN, 0x64F2160, 0]
    value_type: float
    value: [66.6, 66.6]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x64E86B0, 0]
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
    address: [MAIN, 0x64F2160, 0]
    value_type: float
    value: [33.3, 33.3]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x64E86B0, 0]
    value_type: float
    value: [0, 0]

```