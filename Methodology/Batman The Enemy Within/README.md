# Batman: The Enemy Within

> Game info

TitleID: `0100E6300AA3A000`<br>
Explanation based on:
- Internal version: `1.0.3`, 
- Nintendo version ID: `v1`/`v65536`
- BID: `AAC6FB02E03062EF`
- Engine: `Telltale Tool`

> Details

Plugin alone can set FPS above 30, but game is using fake double buffer - if rendering frame took more than than what is necessary to output consistent 60 FPS, it locks itself to 30 FPS. You can set lock to anything between 30 and 60 and get stable framerate IF normally this would be rendered in 60 FPS.