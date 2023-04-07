# Metro Redux Collection (Metro 2033 & Metro: Last Light)

> Game info

TitleIDs: 
- Metro 2033: `0100D4900E82C000`
- Metro: Last Light: `0100F0400E850000`

Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `85C362CC9790F0ED`
- Engine: `4A Engine`

> Details

Plugin alone allows going above 30 FPS, but we need to tweak dynamic resolution to improve performance.<br>
Both games are using exactly the same executable, so we can work on one game and use result on other game without any change.


# How to find offsets

We need to use disassembler in this case. I will be using IDA.

On romfs you can find file `NxLauncher.nss` which is a `main` but with debug data which helps us a lot.

After analyze of `NxLauncher.nss` is finished we search in `View->Open subviews->Names`:
```
r_sr_target_fps
```

This is not a string, but label of offset at which struct related to this setting exists.

After finding address of this we add to it 0x28

It's stored as float and matches equation `0.989 * FPS`, so by default it's 29.67

For 30 FPS entry will look like this:
```yaml
30FPS:
  # Dynamic resolution FPS factor (default)
  -
    type: write
    address: [MAIN, 0x17321D8]
    value_type: float
    value: 29.67
```

For 45 FPS like this:
```yaml
45FPS:
  # Dynamic resolution FPS factor
  -
    type: write
    address: [MAIN, 0x17321D8]
    value_type: float
    value: 44.505
```
