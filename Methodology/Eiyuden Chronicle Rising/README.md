# Eiyuden Chronicle: Rising

> Game info

TitleID: `010039B015CB6000`<br>
Explanation based on:
- Internal version: `1.02`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `39DC785D9073C22B`
- Engine: `Unity 2020.3.25`

> Details

Plugin alone can set FPS above 30, but because of dynamic resolution frametime range set to 29-31 ms performance is subpar. Requires to fix that.
Because timinngs are hardcoded into executable, we cannot patch it with FPSLocker. Use those cheats to change dynamic resolution to match predefined target FPS.
`FMOV` doesn't allow to set any value we want, so I have stayed with 3 FPS targets.

```ini
[60 FPS Dynamic Resolution]
04000000 02426988 1E65F001
04000000 024269F4 1E65B001

[45 FPS Dynamic Resolution]
04000000 02426988 1E66B001
04000000 024269F4 1E669001

[30 FPS Dynamic Resolution]
04000000 02426988 1E67F001
04000000 024269F4 1E67B001
```

Those timings are stored in `DynamicResolution::LowerResSW()`