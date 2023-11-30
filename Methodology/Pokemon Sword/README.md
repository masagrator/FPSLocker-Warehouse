# Pokemon Sword

> Game info

TitleID: `0100ABF008968000`<br>
Explanation based on:
- Internal version: `1.3.2`, 
- Nintendo version ID: `v7`/`v458572`
- BID: `A3B75BCD3311385A`
- Engine: proprietary

> Details

Game can be unlocked to 60 FPS with plugin alone, but because game speed is tied to framerate, we need to patch it.Game is using double buffer, so realistically only 60 FPS matters. Game doesn't hardcode double buffer, but trying to force triple buffer results in crash at second or third frame.

To adjust game speed to 60 FPS, use this cheat (some game elements will still use 30 FPS speed, expect graphical glitches):

```ini
[60 FPS speed]
04000000 0203EEB8 00FE502B

[30 FPS speed]
04000000 0203EEB8 01FCA056
```
