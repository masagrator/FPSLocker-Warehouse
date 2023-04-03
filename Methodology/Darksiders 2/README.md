# Darksiders 2 Deathnitive Edition

> Game info

TitleID: `010071800BA98000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `173E2EDEA9E5D940`
- Engine: `Phoenix Engine`

> Details

Game can above 30 FPS with plugin alone, but we need to patch dynamic resolution frame timing to get better performance.
Thanks to game including .nss executable we could easily find which numbers are used.

# How to find offsets

We don't need to analyze main. Just try to find those bytes:
```
18 79 00 00 48 71 00 00
```
First 4 bytes represent integer storing high threshold of dynamic resolution in ms.
Next 4 bytes represent integer storing low threshold of dynamic resolution in ms.

In my case I have found them at MAIN+0x3293F94

So for 30 FPS it looks like this:
```yaml
  # gNXHighThresholdUS_hidden, gNXLowThresholdUS_hidden (default)
  -
    type: write
    address: [MAIN, 0x3293F94]
    value_type: int32
    value: [31000, 29000]
```