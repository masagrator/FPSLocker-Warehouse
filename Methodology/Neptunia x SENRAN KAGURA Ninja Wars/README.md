# Neptunia x SENRAN KAGURA Ninja Wars

> Game info

TitleID: `01008D0016AF4000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `FB827BF029E0778A`
- Engine: `Tam Engine`

> Details

Plugin alone allows going above 30 FPS in battles, but game speed is tied to framerate. By disabling internal 30 FPS lock game stops tying game speed to framerate above 30 FPS. 

Because game is using double buffer it's not possible to set stable framerate outside of 15, 20, 30 and 60 FPS. Game's code allows to set triple buffer, but when dropping FPS framebuffer glitches like crazy, so triple buffer is not implemented into patch.
