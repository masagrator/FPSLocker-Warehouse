# Flooded

> Game info

TitleID: `010022201D254000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `94A11D3D609BF5EF`
- Engine: `GameMaker Studio 2 2023.4.0.113`

> Details

Game is using internal FPS lock + speed is tied to framerate. FPS Lock is stored as double 30 at [MAIN, 0x219DCD0], but game speed was not found, so after changing FPS Lock to 60 game is running at double speed.