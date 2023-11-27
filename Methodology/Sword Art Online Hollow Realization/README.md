# SWORD ART ONLINE: Hollow Realization

> Game info

TitleID: `01001B600D1D6000`<br>
Explanation based on:
- Internal version: `1.0.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `0C356A98BCF20184`
- Engine: Modified `Phyre` engine

> Details

Plugin alone can set FPS above 30, but because it's using double buffer, you cannot get anything stable between 30-60 FPS, and 20-30 FPS.
Game doesn't hardcode double buffer, but changing it to triple buffer results in segfault. 
