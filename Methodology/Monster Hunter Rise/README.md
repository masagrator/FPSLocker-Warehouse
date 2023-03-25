# Monster Hunter Rise

> Game info

TitleID: `010074F013262000`<br>
Explanation based on:
- Internal version: `14.0.0`, 
- Nintendo version ID: `v29`/`v1900544`
- BID: `11C9CE3F0676EEFD`
- Engine: `RE Engine`

# Warning

Game has issues with using FPSLocker delay function at the boot of game.<br>
If you saved settings in FPSLocker with custom FPS target and patch for your version of game is not available, game will crash when booting.<br>

---

> Details

Game is using internal FPS lock that is set as float 30. We will be using that to change our FPS target.
Since we want to rely on game's logic to handle FPS target whenever possible since they should be better at this, we want to block FPSLocker frame delay.

That's why for each FPS entry in yaml file we want to add this entry
```yaml
  -
    type: block
    what: timing

```

# How to find offsets

We need to use disassembler in this case.

After finishing disassembling `main`, we need to find those bytes:
```
09 20 E8 F2 08 D1 10 91
```

Above them we have a pointer to some struct, and below that offset of that struct in which FPS target is set.

This piece of code looks like this:
```asm
.text:0000007105B1AED0                 ADRP            X8, #qword_7112257C30@PAGE
.text:0000007105B1AED4                 LDR             X8, [X8,#qword_7112257C30@PAGEOFF]
.text:0000007105B1AED8                 MOV             X9, #0x41F00000
.text:0000007105B1AEDC                 MOVK            X9, #0x4100,LSL#48
.text:0000007105B1AEE0                 ADD             X8, X8, #0x434
.text:0000007105B1AEE4                 STR             X9, [X8]
```

`qword_7112257C30` stores pointer, `0x434` is our offset.
So our address is `[MAIN, 0x12257C30, 0x434]`.

FPS lock is stored as float, so in case of 30 FPS we want our entry to look like this:
```yaml
30FPS:
  -
    type: write
    address: [MAIN, 0x12257C30, 0x434]
    value_type: float
    value: 30
  -
    type: block
    what: timing

```
