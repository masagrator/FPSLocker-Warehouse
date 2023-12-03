# Death end re;Quest 2

> Game info

TitleID: `0100EB701568A000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `6A06F3A2582C0954`
- Engine: `Orochi 4`

> Details

Plugin alone can set FPS above 30, but game is using double buffer, so it's locking itself to 30 FPS if it can't reach 60 FPS.
Game doesn't use loop to create buffers.