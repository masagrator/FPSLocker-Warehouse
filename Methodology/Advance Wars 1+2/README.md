# Advance Wars 1+2: Re-Boot Camp

> Game info

TitleID: `0100300012F2A000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `C320A17744AEFD67F`
- Engine: `Unity 2020.2.1`

> Details

Game in battles is locked to 30 FPS and plugin alone cannot set there FPS above 30, so we need patch.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on Ghidra.

We need to import `main` to Ghidra, apply `script.json` generated with il2cppdumper, then search where is
```cs
UnityEngine.Rendering.OnDemandRendering_TypeInfo
```

To pointer stored there we add 0xB8, then we read from that pointer our address where `renderFrameInterval` is stored.

So by default it looks like this:
```yaml
30FPS:
  # _UnityEngine.Rendering.OnDemandRendering_TypeInfo
  -
    type: write
    address: [MAIN, 0x481B2F8, 0xB8, 0]
    value_type: int32
    value: 2
```

But because setting this with vsync interval to 2 causes bigger input lag, we will set our value for all FPS entries as 1.
So finally it should be:
```yaml
30FPS:
  # _UnityEngine.Rendering.OnDemandRendering_TypeInfo
  -
    type: write
    address: [MAIN, 0x481B2F8, 0xB8, 0]
    value_type: int32
    value: 1
```
