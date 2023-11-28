# Cars 3: Driven to Win

> Game info

TitleID: `0100744001588000`<br>
Explanation based on:
- Internal version: `1.0.2`
- Nintendo version ID: `v2`/`v131072`
- BID: `6E191829548C2A41`
- Engine: Proprietary

> Details

Plugin alone can set FPS above 30, but game is using double buffer, so for anything above 30 FPS game jumps between 30<->60 FPS.
nvnWindowBuilderSetTexture value is hardcoded, and buffers are not created in loop.
