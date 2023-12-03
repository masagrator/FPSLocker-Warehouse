# Death end re;Quest

> Game info

TitleID: `0100AEC013DDA000`<br>
Explanation based on:
- Internal version: `1.0.1`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `2F5554EBECAE652B`
- Engine: `Orochi 4`

> Details

Plugin alone can set FPS above 30, but game is using double buffer, so it's locking itself to 30 FPS if it can't reach 60 FPS.
Game doesn't use loop to create buffers.