# EA SPORTS FC 25

> Game info

TitleID: `010054E01D878000`<br>
Explanation based on:
- Internal version: `1.73.d079`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `C3A7D284DA741DBC`
- Engine: `Frostbite`

> Details

Game is using internal FPS lock that must be patched.

# How to find offsets

We need to use disassembler in this case. I will provide instructions based on IDA with enabled analysis macros.

After finishing disassembling main, we need to find those bytes:
```
C1 F7 01 6F
```

We should get only one result.

Above that we need to find first `ADRL X8`:
```asm
.text:00000071055E2290                 ADRL            X8, qword_710CD9BA68
.text:00000071055E2298                 LDR             X8, [X8]
.text:00000071055E229C                 SCVTF           S0, S0
.text:00000071055E22A0                 FDIV            S0, S1, S0
.text:00000071055E22A4                 FMOV            V1.2D, #30.0
```

Our pointer is stored at qword_710CD9BA68. So our final address is MAIN + 0xCD9BA68

Pointer points to double storing FPS lock value. By default it's 30.<br>
Entry for 30 FPS will look like this:
```yaml
30FPS:
  # Internal FPS Lock (default value is 30)
  -
    type: write
    address: [MAIN, 0xCD9BA68, 8]
    value_type: double
    value: 30
```