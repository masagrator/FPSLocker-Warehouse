# DOOM

> Game info

TitleID: `0100416004C00000`<br>
Explanation based on:
- Internal version: `1.2`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `01ACE43E724259C3`
- Engine: `IdTech 6`

> Details

Game can be set above 30 FPS with plugin alone, but because of dynamic resolution target set to 32.2-33 ms we need to tweak it. Also we block adaptive GPU frequency for anything above 30 FPS.
There are also `com_adaptiveTickMaxHz` that must be tweaked otherwise setting anything above 30 FPS results in wrong game speed + `com_adaptiveTickMinHz` if we set anything below 30 FPS.

# How to find offsets

We need to use disassembler in this case. I will be using IDA.

We need to find in `View->Open Subviews->Names`:
```
rs_460Threshold
rs_raiseMilliseconds
rs_dropMilliseconds
com_adaptiveTickMaxHz
com_adaptiveTickMinHz
```

They are not strings, but labeled offsets.
After finding their offsets, for 
```
com_adaptiveTickMaxHz
com_adaptiveTickMinHz
```
We need to add to offset 0x30. They are stored as int32.
- `com_adaptiveTickMinHz` is setting how much FPS minimum can be considered when adjusting game speed. By default it's 30.
- `com_adaptiveTickMaxHz` is setting how much FPS maximum can be considered when adjusting game speed. By default it's 30.

We should set `com_adaptiveTickMaxHz` to 60 for anything above 30 FPS and set `com_adaptiveTickMinHz` to 15 for anything below 30 FPS.

For
```
rs_460Threshold
rs_raiseMilliseconds
rs_dropMilliseconds
```
We need to add to offset 0x34. They are stored as float.
- `rs_460Threshold` - it's a factor that determines if it should run GPU in handheld at 460 MHz. By default it's 0.285. Setting it to 1 causes game to run constantly at 460 MHz.
- `rs_dropMilliseconds` sets frame time that when exceeded drops resolution. By default it's 33
- `rs_raiseMilliseconds` sets frame time that when not exceeded raises resolution. By default it's 32.2

So for 30 FPS it will look like this:
```yaml
30FPS:
  # rs_460Threshold (default)
  -
    type: write
    address: [MAIN, 0x87AEC74]
    value_type: float
    value: 0.285
  # rs_raiseMilliseconds (default)
  -
    type: write
    address: [MAIN, 0x87AF0B4]
    value_type: float
    value: 32.2
  # rs_dropMilliseconds (default)
  -
    type: write
    address: [MAIN, 0x87AF02C]
    value_type: float
    value: 33
  # com_adaptiveTickMaxHz (default)
  -
    type: write
    address: [MAIN, 0x74B2680]
    value_type: int32
    value: 30
  # com_adaptiveTickMinHz (default)
  -
    type: write
    address: [MAIN, 0x74B25F8]
    value_type: int32
    value: 30
```

For 45 FPS like this:
```yaml
45FPS:
  # rs_460Threshold
  -
    type: write
    address: [MAIN, 0x87AEC74]
    value_type: float
    value: 1
  # rs_raiseMilliseconds
  -
    type: write
    address: [MAIN, 0x87AF0B4]
    value_type: float
    value: 21.46
  # rs_dropMilliseconds
  -
    type: write
    address: [MAIN, 0x87AF02C]
    value_type: float
    value: 22
  # com_adaptiveTickMaxHz
  -
    type: write
    address: [MAIN, 0x74B2680]
    value_type: int32
    value: 60
  # com_adaptiveTickMinHz
  -
    type: write
    address: [MAIN, 0x74B25F8]
    value_type: int32
    value: 15

```
