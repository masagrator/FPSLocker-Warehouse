# Pokémon: Let's Go, Pikachu!

> Game info

TitleID: `010003F003A34000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `C208DB6A4EF4361F`
- Engine: proprietary

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game speed is tied to framerate, we need to patch it. But we cannot do that with FPSLocker patch because game speed is stored in Read Only section of executable. Game is using double buffer, so realistically only 60 FPS matters. To adjust game speed to 60 FPS, use this cheat:

```ini
[60 FPS speed]
04000000 00F7EEC0 00FE502B

[30 FPS speed]
04000000 00F7EEC0 01FCA056
```