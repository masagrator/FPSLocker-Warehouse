# Sniper Elite V2 Remastered

> Game info

TitleID: `0100BB000A3AA000`<br>
Explanation based on:
- Internal version: `1.0.5`, 
- Nintendo version ID: `v5`/`v327680`
- BID: `B61F280560A937D2`
- Engine: `Asura`

> Details

Plugin alone allows going above 30 FPS, but it's using double buffer, so setting anything else than 60, 30, 20 and 15 FPS results in unstable framerate. Game has hardcoded buffers, so it's not easy to change to triple buffer.
Only I will explain how to get a dynamic resolution frame timing, which by default is 30.<br>
Thanks to Hazerou for figuring out where resolution setting is stored, this helped me a lot at determining where dynamic resolution frame timing is stored.

# How to find offsets

We need to disassemble main. I will be using IDA.

After analyzing `main` we need to find function:
```cpp
nn::oe::GetCurrentFocusState(void)
```

It will have only 2 xrefs, in my case it's first one.<br>
We are going to this xref and after BL that calls this function we need to find first BL instruction that calls `operator new(ulong)`.<br>
Then we are searching before that instruction for first pointer loading instruction.

In my case it looks like this:
```asm
.text:000000710032C25C                 LDR             X24, [X24,#off_7100C27AE8@PAGEOFF]
.text:000000710032C260                 LDR             X26, [X24]
.text:000000710032C264                 MOV             W0, #0x18 ; unsigned __int64
.text:000000710032C268                 BL              _Znwm_0 ; operator new(ulong)
```
At off_7100C27AE8 is stored hardcoded pointer qword_710155A880. Our float value is stored at offset 4, so our dynamic resolution value is stored at `[MAIN+0x155A880]+4`.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # Dynamic Resolution frame time target = (30/(1000/30)) * (1000/FPS)
  -
    type: write
    address: [MAIN, 0x155A880, 4]
    value_type: float
    value: 60
```
