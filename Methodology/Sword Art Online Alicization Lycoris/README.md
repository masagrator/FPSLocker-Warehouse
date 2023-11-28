# SWORD ART ONLINE Alicization Lycoris

> Game info

TitleID: `010034501225C000`<br>
Explanation based on:
- Internal version: `3.0.1`, 
- Nintendo version ID: `v8`/`v524288`
- BID: `B6AF2C0FA614CC87`
- Engine: Modified `Phyre` engine

> Details

Plugin alone can set FPS above 30, but because game is using double buffer, you cannot get anything stable between 30-60 FPS, and 20-30 FPS.
Game doesn't hardcode double buffer, but changing it to triple buffer results in segfault.
