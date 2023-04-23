# Monster Hunter Rise

> Game info

TitleID: `010074F013262000`<br>
Explanation based on:
- Internal version: `15.0.0`, 
- Nintendo version ID: `v30`/`v1966080`
- BID: `60EFBA0CB724E3FE`
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
00 31 44 BD 00 C0 22 1E
```

Above them we have a pointer to a struct pointer, and below that offset of that struct in which game speed is set, FPS lock is set just after that.

Whole function looks like this:
```asm
.text:0000007100036F44 sub_7100036F44                          ; DATA XREF: .got:off_711262CC48↓o
.text:0000007100036F44                 ADRP            X8, #off_71125F67E8@PAGE
.text:0000007100036F48                 LDR             X8, [X8,#off_71125F67E8@PAGEOFF]
.text:0000007100036F4C                 LDR             X8, [X8]
.text:0000007100036F50                 LDR             S0, [X8,#0x430]
.text:0000007100036F54                 FCVT            D0, S0
.text:0000007100036F58                 STR             D0, [X0,#0x38]
.text:0000007100036F5C                 RET
.text:0000007100036F5C ; End of function sub_7100036F44
```

`off_71125F67E8` stores hardcoded pointer `qword_71128CEEB8`, `0x434` is our offset where FPS lock is stored.
So our address is `[MAIN, 0x128CEEB8, 0x434]`.

FPS lock is stored as float, so in case of 30 FPS we want our entry to look like this:
```yaml
30FPS:
  -
    type: write
    address: [MAIN, 0x128CEEB8, 0x434]
    value_type: float
    value: 30
  -
    type: block
    what: timing

```
