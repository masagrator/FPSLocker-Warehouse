# Format

Patches are converted from YAML files that are tied to the buildid of games, so each one must be designed specifically for one version of one game.
Patches write/read values only from RAM mappings that allow reading and writing (`RW-`). So they don't support patching R-X mappings.

YAML file consists of 11 keys:
- `unsafeCheck` - setting it to `true` results in the plugin not checking if an address is valid. It is recommended to leave it at `false` if you use HEAP related address
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

Each `*FPS` dict is `a list of dicts`. Examples:
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
60FPS:
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
    type: compare
    compare_address: [MAIN, 0x1A65958]
    compare_type: "!="
    compare_value_type: int8
    compare_value: 0
    address: [MAIN, 0x1A08F98]
    value_type: int32
    value: [2, 2]

```

What should be written in each dict depends on `type`.

> type: write

Write a static value to provided `address`
- `address` - always starts with one of the regions: `MAIN`, `HEAP`, or `ALIAS`. Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided first example we read the pointer from `MAIN + 0x12257C30` and add to it `0x434` to get a final address.
- `value_type` - check "Supported types".
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, don't use decimals. You may write a list of values into it that will be applied one after another.

> type: compare

Compare the value from provided `compare_address` with a static value and if it's correct, it writes the static value to provided `address`
- `compare_address` - always starts with one of the regions: `MAIN`, `HEAP`, or `ALIAS`. Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided second example we add `0x1A65958` to `MAIN` address to get a final address.
- `compare_type` - check "Supported types". `compare_value` is the right operand.
- `compare_value_type` - check "Supported types". Write them always with quotes to not trigger yaml formatting exception.
- `compare_value` - what value will be compared with the value from `compare_address`. Remember that if `value_type` is set to any integer, don't use decimals.
- `address` - always starts with one of the regions: `MAIN`, `HEAP`, or `ALIAS`. Next, we have offsets. If the offset is not the last one, it is treated as a pointer address. In provided second example we add `0x1A08F98` to `MAIN` address and this is the final address.
- `value_type` - check "Supported types".
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, don't use decimals. You may write a list of values into it that will be applied one after another.

> type: block<br>
- `what` - supported commands:
  - `timing` - it blocks FPSLocker internal frame delay. It is advised to use it when we want to use the game's proprietary FPS lock. This is automatically applied for 30 FPS and 60 FPS in games using NVN API.

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
