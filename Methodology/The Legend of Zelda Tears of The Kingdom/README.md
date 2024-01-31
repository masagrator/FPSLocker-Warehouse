# The Legend of Zelda: Tears of the Kingdom

> Game info

TitleID: `0100F2C0115B6000`<br>
Explanation based on:
- Internal version: `1.2.1`, 
- Nintendo version ID: `v6`/`v393216`
- BID: `9B4E43650501A4D4`
- Engine: proprietary (heavily modified Breath of The Wild engine)

> Details

Plugin alone can set FPS above 30, but game speed is tied to framerate, is using dynamic resolution and is using double buffer. Available patch makes game speed not tied to framerate, dynamic resolution target is adjusted to chosen FPS and triple buffer is used. 

This readme will mainly focus on known issues, but they won't be fixed because I don't care that much:
- **romfs mods are crashing game** because of triple buffer enabled, Atmosphere CFW has not enough space to make romfs listing cache. Solution is to download file from [HERE](../../atmosphere/contents/0100F2C0115B6000/exefs/main.npdm) and put `main.npdm` to `atmosphere/contents/0100F2C0115B6000/exefs/` (create folders if they don't exist). This file expands FileSystem permissions for game, which for some reason decreases slightly game's RAM usage, just enough for triple buffer to not collide with romfs listing cache creation. There is no other way to fix that, excluding going back to double buffer.
- **When switching between main menu choices, arrows are blinking weirdly** because of my fix for black background that was occuring when you were using d-pad to change weapons or shield. 
- **Soryatonog Shrine** hidden treasure is locked behind bars that require from big cog to push with certain power that is not achievable at higher framerates. Lower FPS to make it open.
- **Turakamik Shrine** big cog doesn't move at higher framerates. Lower FPS to at least 40 to make it move.
