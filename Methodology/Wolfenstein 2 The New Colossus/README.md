# Wolfenstein II®: The New Colossus™

> Game info

TitleID: `01009040091E0000`<br>
Explanation based on:
- Internal version: `1.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `F2FE5EF877839F4F`
- Engine: `IdTech 6`

> Details

Game can be set above 30 FPS with plugin alone, but because of dynamic resolution target set to 32-32.8 ms we need to tweak it. Also we block adaptive GPU frequency for anything above 30 FPS.
There is also one setting `com_adaptiveTickMaxHz` that must be tweaked otherwise setting anything above 30 FPS results in wrong game speed.

# How to find offsets

We need to use disassembler in this case. I will be using IDA.

We need to find in `View->Open Subviews->Names`:
```
rs_force460
rs_raiseMilliseconds
rs_dropMilliseconds
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
rs_raiseMilliseconds
rs_dropMilliseconds
```
We need to add to offset 0x34. They are stored as float.
- `rs_dropMilliseconds` sets frame time that when exceeded drops resolution. By default it's 32.8
- `rs_raiseMilliseconds` sets frame time that when not exceeded raises resolution. By default it's 32

So for 30 FPS it will look like this:
```yaml
30FPS:
  # rs_force460 (default)
  -
    type: write
    address: [MAIN, 0x60E0170]
    value_type: int32
    value: 0
  # rs_raiseMilliseconds (default)
  -
    type: write
    address: [MAIN, 0x60E0294]
    value_type: float
    value: 32
  # rs_dropMilliseconds (default)
  -
    type: write
    address: [MAIN, 0x60E0204]
    value_type: float
    value: 32.8
  # com_adaptiveTickMaxHz (default)
  -
    type: write
    address: [MAIN, 0x62D0570]
    value_type: int32
    value: 30
```

For 45 FPS like this:
```yaml
45FPS:
  # rs_force460
  -
    type: write
    address: [MAIN, 0x60E0170]
    value_type: int32
    value: 1
  # rs_raiseMilliseconds
  -
    type: write
    address: [MAIN, 0x60E0294]
    value_type: float
    value: 21.33
  # rs_dropMilliseconds
  -
    type: write
    address: [MAIN, 0x60E0204]
    value_type: float
    value: 21.86
  # com_adaptiveTickMaxHz
  -
    type: write
    address: [MAIN, 0x62D0570]
    value_type: int32
    value: 60
```