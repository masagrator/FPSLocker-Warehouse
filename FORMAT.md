# Format

Patches are converted from YAML files that are tied to buildid of games, so each one must be designed specifically for one version of one game.

YAML file consists of 11 keys:
- `unsafeCheck` - setting it to `true` results in plugin not checking if address is valid. It is recommended to leave it at `false` if you use HEAP related address
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

Each `*FPS` dict is `a list of dicts`. An examples:
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
Write static value to provided `address`.
- `address` - always starts with one of regions: `MAIN`, `HEAP` or `ALIAS`. Next we have offsets. If offset is not last one, it is treated as pointer address. In provided first example we read pointer from `MAIN + 0x12257C30` and add to it `0x434` to get a final address.
- `value_type` - check "Supported types".
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, from value will be removed all decimals. You may write list of values into it that will be applied one after another.

> type: compare
Compare value from provided `compare_address` with static value and if it's correct, it writes static value to provided `address`
- `compare_address` - always starts with one of regions: `MAIN`, `HEAP` or `ALIAS`. Next we have offsets. If offset is not last one, it is treated as pointer address. In provided second example we add `0x1A65958` to `MAIN` address and this is final address.
- `compare_type` - check "Supported types". `compare_value` is a right operand.
- `compare_value_type` - check "Supported types".
- `compare_value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, from value will be removed all decimals.
- `address` - always starts with one of regions: `MAIN`, `HEAP` or `ALIAS`. Next we have offsets. If offset is not last one, it is treated as pointer address. In provided second example we add `0x1A08F98` to `MAIN` address and this is final address.
- `value_type` - check "Supported types".
- `value` - what value we will write into provided address. Remember that if `value_type` is set to any integer, from value will be removed all decimals. You may write list of values into it that will be applied one after another.

> type: block
- `what` - supported commands:
  - `timing` - it blocks FPSLocker internal frame delay. It is advised to use it when we want to use game's properietary FPS lock.

---

# Supported types

-`compare_type`:
  -`"<"`
  -`"<="`
  -`">"`
  -`">="`
  -`"=="`
  -`"!="`

- `value_type`: 
  -`int8`
  -`int16`
  -`int32`
  -`int64`
  -`uint8`
  -`uint16`
  -`uint32`
  -`uint64`
  -`float`
  -`double`