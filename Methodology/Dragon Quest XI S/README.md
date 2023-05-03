# DRAGON QUEST XI S: Echoes of an Elusive Age - Definitive Edition

> Game info

TitleID: `01006C300E9F0000`<br>
Explanation based on:
- Internal version: `1.0.3`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `1719AABFA5EAE42B`
- Engine: `Unreal Engine 4.18.3`

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game is using dynamic resolution set to target 30 FPS, performance is subpar. Requires patch to fix that.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
r.DynamicResolution.MaxTimeBudget
```

then we go to its xref.

Above that instruction loading pointer to string we need to find first set of ADRP/ADD instructions that calculates pointer to register.
```asm
.text:00000071001DDF6C                 ADRP            X21, #qword_71084ECDC8@PAGE
.text:00000071001DDF70                 ADD             X21, X21, #qword_71084ECDC8@PAGEOFF
.text:00000071001DDF74                 MOV             W8, #0x42000000
.text:00000071001DDF78                 ADRP            X1, #aRDynamicresolu_7@PAGE ; "r.DynamicResolution.MaxTimeBudget"
.text:00000071001DDF7C                 ADD             X1, X1, #aRDynamicresolu_7@PAGEOFF ; "r.DynamicResolution.MaxTimeBudget"
.text:00000071001DDF80                 STR             W8, [SP,#0x80+var_78]
.text:00000071001DDF84                 ADRP            X3, #aWhenRenderingT_0@PAGE ; "When rendering time exceeds MaxTimeBudg"...
.text:00000071001DDF88                 ADD             X3, X3, #aWhenRenderingT_0@PAGEOFF ; "When rendering time exceeds MaxTimeBudg"...
```

As we can see here it provides offset 0x84ECDC8. We need to add 0x10 to it to get an offset that points to used values.
So first final address is stored at 0x84ECDD8.

The same way we're searching for 
```
r.DynamicResolution.MinTimeBudget
r.DynamicResolution.HeavyTimeBudget
r.DynamicResolution.LightTimeBudget
t.MaxFPS
```
If it has more than 1 xref, we are interested in the one that has description pointer loaded.

Each of our final address stores pointer that points to two floats. 

As we want to use internal FPS lock instead of FPSLocker function whenever possible, our entry for 15 FPS will look like this:
```yaml
15FPS:
  # r.DynamicResolution.MaxTimeBudget = 0.99 * (1000/FPS)
  -
    type: write
    address: [MAIN, 0x84ECDD8, 0]
    value_type: float
    value: [66, 66]
  # r.DynamicResolution.MinTimeBudget = 0.9 * (1000/FPS)
  -
    type: write
    address: [MAIN, 0x84ECDF0, 0]
    value_type: float
    value: [60, 60]
  # r.DynamicResolution.HeavyTimeBudget = 1.05 * (1000/FPS)
  -
    type: write
    address: [MAIN, 0x84ECE08, 0]
    value_type: float
    value: [70, 70]
  # r.DynamicResolution.LightTimeBudget = 0.9 * (1000/FPS)
  -
    type: write
    address: [MAIN, 0x84ECE20, 0]
    value_type: float
    value: [60, 60]
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x8501C48, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing

```
But for 30 FPS like this (since plugin's FPS lock is blocked by default at 30 and 60 FPS):
```yaml
30FPS:
  # r.DynamicResolution.MaxTimeBudget (default value)
  -
    type: write
    address: [MAIN, 0x84ECDD8, 0]
    value_type: float
    value: [33, 33]
  # r.DynamicResolution.MinTimeBudget (default value)
  -
    type: write
    address: [MAIN, 0x84ECDF0, 0]
    value_type: float
    value: [30, 30]
  # r.DynamicResolution.HeavyTimeBudget (default value)
  -
    type: write
    address: [MAIN, 0x84ECE08, 0]
    value_type: float
    value: [35, 35]
  # r.DynamicResolution.LightTimeBudget (default value)
  -
    type: write
    address: [MAIN, 0x84ECE20, 0]
    value_type: float
    value: [30, 30]
  # t.MaxFPS (default value)
  -
    type: write
    address: [MAIN, 0x8501C48, 0]
    value_type: float
    value: [0, 0]

```