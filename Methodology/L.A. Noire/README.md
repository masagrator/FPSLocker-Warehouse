# L.A. Noire

> Game info

TitleID: `0100830004FB6000`<br>
Explanation based on:
- Internal version: `1.2`, 
- Nintendo version ID: `v2`/`v131072`
- BID: `40F973CE3B5EC8D7`
- Engine: `Rockstar Advanced Game Engine`

> Details

Game speed and physics are tied in many places to 30 FPS. We need to patch it.<br>
**WARNING**: Patch was not tested thoroughly. It is known on PC that setting FPS above 30 FPS causes physics issues with cars (for 60 FPS it results in 2x longer braking distance and 2x sharper cornering). Also it can crash game in one scene with projector, in pen minigame you may not be able to use pen - in those cases setting back game to 30 FPS solves the issue. Don't set below 25 FPS otherwise camera goes crazy. 

---

# How to find offsets

We need to use disassembler in this case. 

After finishing disassembling `main` in IDA we go to View->Names and search for `g_LANoireEnableRenderSkip`. In our case it's 0x1A5BE70.<br>
Next we need to find `Singleton<I3DEngine>::m_Instance`. At address 0x1A32900 stores pointer to instance, frame timing is stored at 0xA0.

So for 60 FPS we want to write:
```yaml
60FPS:
  # Game speed ((FPS/30) * 59.94)
  -
    type: write
    address: [MAIN, 0x1A32900, 0xA0]
    value_type: float
    value: 119.88
  # Frameskipping (otherwise you will get slowdowns at framedrops)
  -
    type: write
    address: [MAIN, 0x1A5BE70]
    value_type: int8
    value: 1

```
