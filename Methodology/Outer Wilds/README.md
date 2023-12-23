# Outer Wilds

> Game info

TitleID: `01003DC0144B6000`<br>
Explanation based on:
- Internal version: `1.1.14.841`, 
- Nintendo version ID: `v1/v65536`
- BID: `30DAEEF64B06974C`
- Engine: `Unity 2019.4.40`

> Details

FPS can be unlocked with plugin alone, but camera is locked to 30 FPS movement. We can unlock it by settings fixedFrameRate to 1/60 float, but for some reason this artificially increases hardware usage and makes reaching 60 FPS harder than expected (by using stock clocks and changing this to lower value, you can see how performance tanks by 30%). I don't plan to release this officially until this will be fixed.
Function causing this issue is at offset 0x643C2C which calculates passed time, which means patching only this function manipulates also game speed.

```yaml
# Outer Wilds 1.0.1
# BID: 30DAEEF64B06974C

unsafeCheck: true

15FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.033333333333
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.033333333333
  # SwitchDynamicResolutionManager_TypeInfo (IdealGpuTimeMs = 20*(30/FPS), IdealCpuTimeMs = 30 *(30/FPS), FramesToSmoothFpsOver, FramesToSmoothGpuTimeOver, FramesToSmoothCpuTimeOver = FPS)
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [40, 60, 15, 15, 15]
  -
    type: block
    what: timing
20FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.033333333333
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.033333333333
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [30, 45, 20, 20, 20]
25FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.033333333333
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.033333333333
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [24, 36, 25, 25, 25]
30FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.033333333333
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.033333333333
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [20, 30, 30, 30, 30]
35FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.0166666666
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.0166666666
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [17.14, 25.71, 35, 35, 35]
40FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.0166666666
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.0166666666
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [15, 22.5, 40, 40, 40]
45FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.0166666666
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.0166666666
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [13.33, 20, 45, 45, 45]
50FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.0166666666
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.0166666666
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [12, 18, 50, 50, 50]
55FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.0166666666
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.0166666666
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [10.9, 16.36, 55, 55, 55]
60FPS:
  # MaximumDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x100]
    value_type: float
    value: 0.066666666666
  # fixedDeltaTime
  -
    type: write
    address: [MAIN, 0x4C83640, 0x48]
    value_type: float
    value: 0.0166666666
  # OWTime_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B3C40, 0xB8, 0x10]
    value_type: float
    value: 0.0166666666
  # SwitchDynamicResolutionManager_TypeInfo
  -
    type: write
    address: [MAIN, 0x49B6158, 0xB8, 0, 0x20]
    value_type: float
    value: [10, 15, 60, 60, 60]
```
