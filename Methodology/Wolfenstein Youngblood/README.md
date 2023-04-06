# Wolfenstein®: Youngblood™

> Game info

TitleID: `01003BD00CAAE000`<br>
Explanation based on:
- Internal version: `1.5`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `8B40EBBA7244C94A`
- Engine: `IdTech 6`

> Details

Game can be set above 30 FPS with plugin alone, but because of dynamic resolution target set to 32-32.8 ms we need to tweak it. Also we block adaptive GPU frequency for anything above 30 FPS.
There is also one setting `com_adaptiveTickMaxHz` that must be tweaked otherwise setting anything above 30 FPS results in wrong game speed.

# How to find offsets

We need to use disassembler in this case. I will be using IDA.

We need to find in `View->Open Subviews->Names`:
```
rs_force460
rs_raiseThreshold
rs_dropThreshold
com_adaptiveTickMaxHz
```

They are not strings, but labeled offsets.
After finding their offsets, for 
```
rs_force460
com_adaptiveTickMaxHz
```
We need to add to offset 0x30. They are stored as int32.
- `rs_force460` disables dynamic GPU frquency while forcing 460 MHz in handheld mode. By default it's 0
- `com_adaptiveTickMaxHz` is setting how much FPS can be considered when adjusting game speed. By default it's 30.

We should set `rs_force460` to 1 so there won't be a constant battle between game and sys-clk affecting performance + `com_adaptiveTickMaxHz` to 60 for anything above 30 FPS.

For
```
rs_raiseThreshold
rs_dropThreshold
```
We need to add to offset 0x34. They are stored as float.
- `rs_dropMilliseconds` is a result of equation `0.984 * (30/FPS)`. So by default it's 0.984 which is equivalent to 32.8ms. If frame took more than 32.8 ms to render, it drops resolution.
- `rs_raiseMilliseconds` is a result of equation `0.96 * (30/FPS)`. So by default it's 0.96 which is equivalent to 32ms. If frame took less than 32 ms to render, it raises resolution.

So for 30 FPS it will look like this:
```yaml
30FPS:
  # rs_force460 (default)
  -
    type: write
    address: [MAIN, 0x7994DF0]
    value_type: int32
    value: 0
  # rs_raiseThreshold (default)
  -
    type: write
    address: [MAIN, 0x7994F14]
    value_type: float
    value: 0.96
  # rs_dropThreshold (default)
  -
    type: write
    address: [MAIN, 0x7994E84]
    value_type: float
    value: 0.984
  # com_adaptiveTickMaxHz (default)
  -
    type: write
    address: [MAIN, 0x85F74E0]
    value_type: int32
    value: 30
```

For 45 FPS like this:
```yaml
45FPS:
  # rs_force460
  -
    type: write
    address: [MAIN, 0x7994DF0]
    value_type: int32
    value: 1
  # rs_raiseThreshold
  -
    type: write
    address: [MAIN, 0x7994F14]
    value_type: float
    value: 0.64
  # rs_dropThreshold
  -
    type: write
    address: [MAIN, 0x7994E84]
    value_type: float
    value: 0.656
  # com_adaptiveTickMaxHz
  -
    type: write
    address: [MAIN, 0x85F74E0]
    value_type: int32
    value: 60
```