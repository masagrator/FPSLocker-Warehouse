# Format

Patches are converted from YAML files that are tied to the buildid of games, so each one must be designed specifically for one version of one game.
YAML files must be encoded in UTF-8 without BOM.

YAML file consists of keys:
- `unsafeCheck` - setting it to `true` results in the plugin not checking if an address is valid. It is recommended to leave it at `false` if you use HEAP related address. By default it's `true`. This key is not obligatory to have and is deprecated in the favour of `address_unsafe`/`compare_address_unsafe` keys.
- `ALL_FPS` - When Custom FPS Target is set, this part is updating provided addresses regularly. It supports only RW- sections. This section is not obligatory if you use `MASTER_WRITE`.
- `MASTER_WRITE` - This applies data before game starts initialization to any section that can be read, which means R-X, RW- and R--. This section is not obligatory.
- `DECLARATIONS` - It puts data into Core internal buffers, you can reference them with labels in sections above. This section is not obligatory. Compatible only with 64-bit games.

Each key except of unsafeCheck is `a list of dicts`. Example:
```yaml
ALL_FPS:
  -
    type: compare
    compare_address: [MAIN, 0x1A65958]
    compare_type: "!="
    compare_value_type: int8
    compare_value: 1
    address: [MAIN, 0x1A08F98]
    value_type: int32
    value: [1, 1]
  -
    type: evaluate_write
    address: [MAIN, 0x12257C30, 0x434]
    address_unsafe: true
    value_type: float
    value: FPS_TARGET

```


# List of types accepted by `ALL_FPS`

> type: write

Write a static value to provided `address`
- `address` - always starts with one of the regions: `MAIN`, `HEAP`, or `ALIAS`. Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided first example we read the pointer from `MAIN + 0x12257C30` and add to it `0x434` to get a final address.
- `address_unsafe` - flag if that address doesn't store correct pointer before first frame is pushed, it will go through address validation in Core before use. It's not obligatory to use, by default it's false if `unsafeCheck` is true.
- `value_type` - check [Supported types](#supported-types).
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, don't use decimals. You may write a list of values into it that will be applied one after another.

> type: evaluate_write

It's the same as `write` with one big difference - it is used to write expressions in `value`. More about expressions [HERE](#expressions).

> type: compare

Compare the value from provided `compare_address` with a static `compare_value` and if it's correct, it writes the static `value` to provided `address`
- `compare_address` - always starts with one of the regions: `MAIN`, `HEAP`, `ALIAS` or `VARIABLE` (64-bit games only). Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided second example we add `0x1A65958` to `MAIN` address to get a final address. For `VARIABLE` you must use name of variable declared in `DECLARATIONS` section instead of offset.
- `compare_address_unsafe` - flag if that compare_address doesn't store correct pointer before first frame is pushed, it will go through address validation in Core before use. It's not obligatory to use, by default it's false if `unsafeCheck` is true.
- `compare_type` - check [Supported types](#supported-types). `compare_value` is the right operand. Write them always with quotes to not trigger yaml formatting exception.
- `compare_value_type` - check [Supported types](#supported-types).
- `compare_value` - what value will be compared with the value from `compare_address`. Remember that if `value_type` is set to any integer, don't use decimals.
- `address` - always starts with one of the regions: `MAIN`, `HEAP`, `ALIAS` or `VARIABLE` (64-bit games only). Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided second example we add `0x1A08F98` to `MAIN` address and this is the final address. This is not required if `value_type` is `refresh_rate`. For `VARIABLE` you must use name of variable declared in `DECLARATIONS` section instead of offset.
- `address_unsafe` - flag if that address doesn't store correct pointer before first frame is pushed, it will go through address validation in Core before use. It's not obligatory to use, by default it's false if `unsafeCheck` is true.
- `value_type` - check [Supported types](#supported-types).
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, don't use decimals. You may write a list of values into it that will be applied one after another.

> type: evaluate_compare

It's the same as `compare` with one big difference - it is used to write expressions in `value`. More about expressions [HERE](#expressions).

> type: block<br>
- `what` - supported commands:
  - `timing` - it blocks FPSLocker internal frame delay. It is advised to use it when we want to use the game's proprietary FPS lock. This is automatically applied when FPS target matches refresh rate or its intervals.

# List of types accepted by `MASTER_WRITE`
> type: bytes

This is used to write data into main executable, it can write to any part of executable, even read only. It's applied only before game actually starts.
- `main_offset` - where value should be written relative to `main` executable start in RAM.
- `value_type` - check "Supported types".
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, don't use decimals. You may write a list of values into it that will be applied one after another.
> type: `asm_a64` and `asm_a32`

This is used to write assembly instructions instead of integers for better maintenance. FPSLocker automatically calculates offsets based of main_offset value. a64 is for 64-bit games, a32 is for 32-bit games.
- `main_offset` - where value should be written relative to `main` executable start in RAM.
- `instructions` - it's always a list, it stores instructions in list format. Read about instructions [HERE](#asm-instructions).

# List of types accepted by `DECLARATIONS`
> [!IMPORTANT]
> ORDER OF PROVIDED ENTRIES IS RESTRICTED! ENTRY CANNOT REFERENCE SOMETHING THAT WAS NOT DECLARED BEFORE!
> 
> ONLY 64-BIT GAMES ARE SUPPORTED!

> type: const

Define 64-bit integer value that will be referenced directly in assembly when generating patch, makes using mov/movk pair more readable. This won't be put standalone into generated patch.<br>
- `name` - label used to reference value. To reference it in assembly, you must use `$` in combination with its name.
- `value` - value that is between 0 and UINT64_MAX
> type: variable

Defines value that will be put into Core's RW- buffer. Variables addresses are size-aligned.
- `name` - label used to reference value. To reference it in assembly, you must use `$` in combination with its name. In `ALL_FPS` section, to reference its address use raw name.
- `value_type` - check [Supported types](#supported-types).
- `default_value` - value that will be used to initialize new variable. Remember that if `value_type` is set to any integer, don't use decimals.
- `evaluate` - math formula that will refresh variable in regular interval if Custom FPS Target is set. It's not obligatory to use it.
> type: code

Defines assembly instructions that will be put into Core's R-X section, which means they can be executed.
- `name` - label used to reference start of code. To reference it in assembly, you must use `_` before provided name and `()` after provided name.
- `instructions` - it's always a list, it stores instructions in list format. Read about instructions [HERE](#asm-instructions).
---

# Supported types

- `compare_type`:
  - `"<"`
  - `"<="`
  - `">"`
  - `">="`
  - `"=="`
  - `"!="`

- `compare_value_type`/`value_type`: 
  - `int8`
  - `int16`
  - `int32`
  - `int64`
  - `uint8`
  - `uint16`
  - `uint32`
  - `uint64`
  - `float`
  - `double`

- `value_type` exclusive for `ALL_FPS`:
  - `refresh_rate` (forces fps lock to target certain framerate, supports decimals. When used, address entry is not needed)

# Expressions

TinyExpr library is used for expressions evaluation. It supports various math C functions, additionally FPSLocker includes globals and one more function.

Additional function:
- `TruncDec([Value], [Dec])` - This function removes decimals from "Value". With "Dec" we can control how many decimals we will leave. For example if we write `TruncDec(FRAMETIME_TARGET, 2)` it will result in `33.33` when 30 FPS is chosen.

Globals (all are stored as double and converted to chosen value_type):
- `FPS_TARGET` - it returns value corresponding to chosen FPS target in FPSLocker.
- `FRAMETIME_TARGET` = `1000 / FPS_TARGET`
- `VSYNC_TARGET` = `60 / FPS_TARGET` without decimals, never goes below 1
- `FPS_LOCK_TARGET` - similar to FPS_TARGET with the difference that if FPS target chosen in FPSLocker matches refresh rate, it is equal to `FPS_TARGET + 2` to avoid stutterings caused by artifical FPS lock.

# ASM Instructions
Example of `asm_a64` entry:
```yaml
  -
    type: asm_a64
    main_offset: 0x193CEA8
    instructions: [
      [str, x8, [x0, 0x10], "!"],
      [adrp, x10, 0x30a7000],
      [ldr, s2, [x10, 0xf00]],
      [movk, x9, 0x3c9, 16]
    ]
```

which translates to
```arm
STR X8, [x0, #0x10]!
ADRP X10, #0x30A7000
LDR S2, [x10, #0xf00]
MOVK X9, 0x3c9, LSL#16
```

As you can see, they are written in very similar way, but avoiding writing whole instructions as one string, so main differences are:
- mnemonic must be separated by comma from the rest of data,
- pre-index `!` must be separated from right square bracket, and be inside quotation marks - that's because in YAML exclamation mark has special use, not doing it this way can result in crashing application,
- Avoid using `#` before immediates, that's because it's used to inform parser that everything after hash is a comment

Only some instructions are supported, some of them don't cover every single case.
Supported mnemonics in asm_a64 (read how they work in ARM64/AArch64 documentation, `V` registers are not supported):
`ADD`, `ADRP`, `B`, `B.EQ`, `B.NE`, `B.CS`, `B.HS`, `B.CC`, `B.LO`, `B.MI`, `B.PL`, `B.VS`, `B.VC`, `B.HI`, `B.LS`, `B.GE`, `B.LT`, `B.GT`, `B.LE`, `B.AL`, `B.NV`, `BL`, `BLR`, `BR`, `CBNZ`, `CBZ`, `CMP`, `CSEL`, `FADD`, `FCMP`, `FCMPE`, `FCSEL`, `FCVT`, `FCVTZU`, `FDIV`, `FMADD`, `FMINNM`, `FMOV`, `FMUL`, `FNEG`, `FSQRT`, `FSUB`, `LDP`, `LDR`, `LDRB`, `LDRH`, `LDUR`, `LDURH`, `LSL`, `MADD`, `MOV`, `MOVK`, `MRS`, `MUL`, `NOP`, `RET`, `SCVTF`, `SDIV`, `STP`, `STR`, `STRB`, `STRH`, `STUR`, `STURH`, `SUB`, `SVC`, `TBNZ`, `TBZ`, `UCVTF`, `UDIV`

Supported mnemonics in asm_a32 (read how they work in ARM/AArch32 documentation, `sl` register is not supported):
`ADC`, `ADCS`, `ADD`, `ADDS`, `AND`, `ANDS`, `ASR`, `ASRS`, `B`, `BIC`, `BICS`, `BL`, `BLX`, `BX`, `CMN`, `CMP`, `EOR`, `EORS`, `LDR`, `LDRB`, `LDRD`, `LDRH`, `LDRSB`, `LDRSH`, `LSL`, `LSLS`, `LSR`, `LSRS`, `MLA`, `MLAS`, `MLS`, `MOV`, `MOVS`, `MOVT`, `MOVW`, `MUL`, `MULS`, `MVN`, `MVNS`, `NOP`, `ORR`, `ORRS`, `POP`, `PUSH`, `ROR`, `RORS`, `RSB`, `RSBS`, `SBC`, `SBCS`, `SDIV`, `SMULL`, `STR`, `STRB`, `STRD`, `STRH`, `SUB`, `SUBS`, `SVC`, `SXTB`, `SXTH`, `TEQ`, `TST`, `UDIV`, `UMULL`, `UXTB`, `UXTH`, `VABS`, `VADD`, `VCMP`, `VCMPE`, `VCVT`, `VCVTR`, `VDIV`, `VFMA`, `VFMS`, `VLDR`, `VMAXNM`, `VMINNM`, `VMLA`, `VMLS`, `VMOV`, `VMRS`, `VMSR`, `VMUL`, `VNEG`, `VNMUL`, `VPOP`, `VPUSH`, `VSQRT`, `VSTR`, `VSUB`

Additional feature is supported by `B` (conditional branches included), `BL`, `CBNZ`, `CBZ`, `TBNZ`, `TBZ` - if for immediate you will write + or - sign, you can use it to inform that it's a relative amount of bytes you want to jump. So if you write for example `[b, -4]`, it will go to previous instruction.

```yaml
  -
    type: asm_a64
    main_offset: 0x193CEA8
    instructions: [
      [b.ne, +8],
      [nop],
      [ldr, s2, [x10, 0xf00]], #it will jump here
      [movk, x9, 0x3c9, 16]
    ]
```

For `B` (conditional branches included), `CBNZ`, `CBZ`, `TBZ`, `TBNZ` you can use labels that work as goto function. Labels must start with `:`

```yaml
  -
    type: asm_a64
    main_offset: 0x193CEA8
    instructions: [
      [b.ne, :goto1],
      [nop],
      :goto1, [ldr, s2, [x10, 0xf00]], #it will jump here
      [movk, x9, 0x3c9, 16]
    ]
```

For `B` and `BL` you can use calls to hardcoded functions:
- `_convertTickToTimeSpan()` - accepting tick value as x0, it will return ticks converted to nanoseconds in x0
- `_setUserInactivityDetectionTimeExtended()` - this is used mainly to avoid using hardcoded pointer in Tears of the Kingdom config. It accepts bool as x0/w0, and when true it blocks auto sleep.

The same way you can call functions declared as `code` in `DECLARATIONS` section.
```yaml
DECLARATIONS:
  -
    type: variable
    name: current_frametime
    value_type: float
    default_value: 0.0333333333
  -
    type: code
    name: overdriveFix
    instructions: [
      [adrp, x0, $current_frametime],
      [ldr, s0, [x0, $current_frametime]],
      [ret]
    ]
MASTER_WRITE:
  -
    type: asm_a64
    main_offset: 0x676D4
    instructions: [
      [bl, _overdriveFix()]
    ]
```

Bitness of code type in DECLARATIONS is detected based on type of MASTER_WRITE entry `asm_*` that calls it.
