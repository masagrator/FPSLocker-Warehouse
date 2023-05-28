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
nvnWindowBuilderSetTexture value is not hardcoded, but changing it to use triple buffering results in glitched output, so it seems game is coded to take advantage of double buffer.
