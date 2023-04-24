# Valkyria Chronicles 4

> Game info

TitleID: `01005C600AC68000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `3758602AA47ADD37`
- Engine: `CANVAS engine`

> Details

Game can be unlocked to 60 FPS with plugin alone, but game speed is tied to framerate, so we need to tweak it for our FPS target.
Lipsync is tied to 30 FPS and we don't know any offset to fix this, so when running game at 60 FPS lipsync ends 2x earlier than it should.
Game has coded blocking itself to 30 FPS if it cannot uphold more than 30 FPS. And for that is increasing whatever game speed is set by 2x. So setting anything between 30 - 60  causes slowdowns when it drops to 30 FPS. Battles are coded to run only at 30 FPS and 60 FPS. If you will set anything between 30 and 60, game will report target FPS is achieved, but gameplay is in fact slowed down. Thus why making FPSLocker patch at this point is useless.

For 60 FPS cheat look [HERE](https://github.com/ChanseyIsTheBest/NX-60FPS-RES-GFX-Cheats/blob/main/titles/01005C600AC68000/cheats/3758602AA47ADD37.txt)
