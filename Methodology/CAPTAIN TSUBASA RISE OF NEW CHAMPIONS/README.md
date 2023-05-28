# CAPTAIN TSUBASA RISE OF NEW CHAMPIONS

> Game info

TitleID: `0100EAE010560000`<br>
Explanation based on:
- Internal version: `1.46`
- Nintendo version ID: `v16`/`v1048576`
- BID: `F3C08D1AE79B7BD6`
- Engine: Proprietary

> Details

Plugin alone can set FPS above 30, but game is using double buffer, so for anything above 30 FPS game jumps between 30<->60 FPS.
nvnWindowBuilderSetTexture value is not hardcoded, though changing it in functions originally setting this value causes segfault anyway.
