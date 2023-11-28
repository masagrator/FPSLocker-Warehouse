# Alan Wake Remastered

> Game info

TitleID: `0100623017A58000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `6520258D00AEA915`
- Engine: `Northlight Engine`

> Details

Plugin alone can set FPS above 30, but because game is using double buffer it's not possible to set any FPS between 30 and 60.
nvnWindowBuilderSetTextures has hardcoded value, and buffers are not created in loop.
