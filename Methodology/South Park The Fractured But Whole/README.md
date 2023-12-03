# South Park: The Fractured But Whole

> Game info

TitleID: `01008F2005154000`<br>
Explanation based on:
- Internal version: `1.0.5`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `DF15EDAAF603E00C`
- Engine: `Snowdrop Engine`

> Details

Plugin alone can set FPS above 30, but game is using double buffer, so it's locking itself to 30 FPS if it can't reach 60 FPS.
Game doesn't use loop to create buffers.