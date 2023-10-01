# Pokemon Legends: Arceus

> Game info

TitleID: `01001F5010DFA000`<br>
Explanation based on:
- Internal version: `1.1.1`, 
- Nintendo version ID: `v4`/`v262144`
- BID: `AEE8F150DDA1B5A8`
- Engine: proprietary

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game speed is tied to framerate, we need to patch it. Use those cheats to apply to game for FPS target you want (to disable double buffer turn off Sync Wait in FPSLocker) (still some 2D elements are tied to 30 FPS speed, graphical glitches can occur):

```ini
[60 FPS Game speed]
040B0000 0397E8D8 00FE502B

[55 FPS Game speed]
040B0000 0397E8D8 01156EBB

[50 FPS Game speed]
040B0000 0397E8D8 01312D01

[45 FPS Game speed]
040B0000 0397E8D8 0153158F

[40 FPS Game speed]
040B0000 0397E8D8 017D7841

[35 FPS Game speed]
040B0000 0397E8D8 01B32435

[30 FPS Game speed]
040B0000 0397E8D8 01FCA056

[25 FPS Game speed]
040B0000 0397E8D8 02625A01

[20 FPS Game speed]
040B0000 0397E8D8 02FAF081

[15 FPS Game speed]
040B0000 0397E8D8 03F940AB
```
