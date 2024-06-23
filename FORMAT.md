# Format

Patches are converted from YAML files that are tied to the buildid of games, so each one must be designed specifically for one version of one game.
Patches write/read values only from RAM mappings that allow reading and writing (`RW-`). So they don't support patching `R-X` mappings.

YAML file consists of keys:
- `unsafeCheck` - setting it to `true` results in the plugin not checking if an address is valid. It is recommended to leave it at `false` if you use HEAP related address
- `ALL_FPS`
- `ALL_REFRESH_RATES` (doesn't work if ALL_FPS is not defined)

if `ALL_FPS` is not defined, those are required to exist:
- `15FPS`
- `20FPS`
- `25FPS`
- `30FPS`
- `35FPS`
- `40FPS`
- `45FPS`
- `50FPS`
- `55FPS`
- `60FPS`

Each key except of unsafeCheck is `a list of dicts`. Examples:
```yaml
15FPS:
  -
    type: write
    address: [MAIN, 0x12257C30, 0x434]
    value_type: float
    value: 15
  -
    type: block
    what: timing

```
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
    value_type: float
    value: FPS_TARGET

```

What should be written in each dict depends on `type`.

> type: write

Write a static value to provided `address`
- `address` - always starts with one of the regions: `MAIN`, `HEAP`, or `ALIAS`. Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided first example we read the pointer from `MAIN + 0x12257C30` and add to it `0x434` to get a final address.
- `value_type` - check "Supported types".
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, don't use decimals. You may write a list of values into it that will be applied one after another.

> type: evaluate_write

It's the same as `write` with one big difference - it is used to write expressions in `value`. More about expressions at the bottom of file.

> type: compare

Compare the value from provided `compare_address` with a static `compare_value` and if it's correct, it writes the static `value` to provided `address`
- `compare_address` - always starts with one of the regions: `MAIN`, `HEAP`, or `ALIAS`. Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided second example we add `0x1A65958` to `MAIN` address to get a final address.
- `compare_type` - check "Supported types". `compare_value` is the right operand.
- `compare_value_type` - check "Supported types". Write them always with quotes to not trigger yaml formatting exception.
- `compare_value` - what value will be compared with the value from `compare_address`. Remember that if `value_type` is set to any integer, don't use decimals.
- `address` - always starts with one of the regions: `MAIN`, `HEAP`, or `ALIAS`. Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided second example we add `0x1A08F98` to `MAIN` address and this is the final address.
- `value_type` - check "Supported types".
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, don't use decimals. You may write a list of values into it that will be applied one after another.

> type: evaluate_compare

It's the same as `compare` with one big difference - it is used to write expressions in `value`. More about expressions at the bottom of file.

> type: block<br>
- `what` - supported commands:
  - `timing` - it blocks FPSLocker internal frame delay. It is advised to use it when we want to use the game's proprietary FPS lock. This is automatically applied when FPS target matches refresh rate + 30 FPS if refresh rate is set to 60 Hz.

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

- `value_type` exclusive:
  - `refresh_rate` (forces chosen refresh rate, supports decimals. When used, address has no impact, as long as it's using valid data)

# Expressions

For expressions evaluation is used TinyExpr library. It support various math C functions with addition to FPSLocker that includes globals and one additional function.

Additional function:
- `TruncDec([Value], [Dec])` - This function removes decimals from "Value". With "Dec" we can control how many decimals we will leave. For example if we write `TruncDec(FRAMETIME_TARGET, 2)` it will result in `33.33` when 30 FPS is chosen.

Globals (all are stored as double and converted to chosen value_type):
- `FPS_TARGET` - it returns value corresponding to chosen FPS target in FPSLocker.
- `FRAMETIME_TARGET` = `1000 / FPS_TARGET`
- `VSYNC_TARGET` = `60 / FPS_TARGET` without decimals
- `FPS_LOCK_TARGET` - similar to FPS_TARGET with the difference that if FPS target chosen in FPSLocker matches refresh rate, it is equal to 120 to avoid stutterings caused by artifical FPS lock.
