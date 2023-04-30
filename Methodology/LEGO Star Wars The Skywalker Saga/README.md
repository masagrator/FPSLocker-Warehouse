# LEGO Star Wars: The Skywalker Saga

> Game info

TitleID: `010042D00D900000`<br>
Explanation based on:
- Internal version: `1.0.8`, 
- Nintendo version ID: `v8`/`v524288`
- BID: `C6901CE5426C704A`
- Engine: `NTT`

> Details

Game is using dynamic resolution timing set to 31ms, performance is subpar. Because DR timing is hardcoded into executable, we can only manipulate target to 30 or 60 FPS with FPSLocker patch. So for 30 FPS and below we will use default target, for anything above we will use second target.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA.

After finishing disassembling main, we need to go to View -> Open Subviews -> Names and find where is stored
```
g_video_swap_mode
```

Setting it to 3 sets dynamic resolution to 30 FPS target, setting to 2 sets to 60 FPS target. Setting it to 1 disables dynamic resolution, setting resolution to max.
In my case address is 0xA9FAE80.

So for 30 FPS and below it will look like this
```yaml
30FPS:
  # g_video_swap_mode
  -
    type: write
    address: [MAIN, 0xA9FAE80]
    value_type: int32
    value: 3

```
And for anything else like this:
```yaml
60FPS:
  # g_video_swap_mode
  -
    type: write
    address: [MAIN, 0xA9FAE80]
    value_type: int32
    value: 2

```
