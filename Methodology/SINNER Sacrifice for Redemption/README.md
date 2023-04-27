# SINNER: Sacrifice for Redemption

> Game info

TitleID: `0100B16009C10000`<br>
Explanation based on:
- Internal version: `1.1.0319`, 
- Nintendo version ID: `v3`/`v196608`
- BID: `490D681909609015`
- Engine: `Unreal Engine 4.19.2`

> Details

Game is using setting that is locking game to 30 FPS and ties game speed to framerate. We need to patch it.

# How to find offsets

First we need to find where is stored bit field with flags responsible for storing `bUseFixedFrameRate` and `bUseSmoothFrameRate`.
Pointer cannot be easily found in main, so we will use a little trick.

Run game and when you're in actual gameplay, run `Edizon-SE` and find in heap u64 value `0x41F0000000000067`. We should have few results, usually it's one of first three that is used.
We are checking which one is used by changing each `0x41F00000` value which is float `30` to `60` and looking up if FPS has changed.
When we find value we need, the bit field containing our flags is stored as int32 just before that float (as `0x00000067`)

Use Edizon-SE Jumpback method to find offset relative to main for this bitfield. To remove those flags we need to remove 2^5 (|= 0x20) and 2^6 (|= 0x40) bits from this integer, so it should result in `7`.

> FPS Lock

Now we will use disassembler to find alternative FPS lock that won't tie game speed to framerate to use it instead of NX-FPS internal lock. I will provide instructions based on IDA as it will calculate automatically needed offsets for us.

After finishing disassembling main, we need to find this string (it's encoded as UTF-32-LE):
```
t.MaxFPS
```

then we go to its xref.

Below we need to find first STR after second BLR. Code looks like this
```asm
.text:0000007101E06334                 ADRP            X1, #aTMaxfps@PAGE ; "t.MaxFPS"
.text:0000007101E06338                 ADRP            X2, #aCapsFpsToTheGi@PAGE ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E0633C                 ADD             X1, X1, #aTMaxfps@PAGEOFF ; "t.MaxFPS"
.text:0000007101E06340                 ADD             X2, X2, #aCapsFpsToTheGi@PAGEOFF ; "Caps FPS to the given value.  Set to <="...
.text:0000007101E06344                 MOV             W3, WZR
.text:0000007101E06348                 BLR             X8
.text:0000007101E0634C                 ADRP            X8, #qword_7104F225E0@PAGE
.text:0000007101E06350                 ADD             X8, X8, #qword_7104F225E0@PAGEOFF
.text:0000007101E06354                 ADD             X8, X8, #0x10
.text:0000007101E06358                 STR             X0, [X23,#(qword_7105CCEBA0 - 0x7105CCE5F0)]
.text:0000007101E0635C                 ADD             X19, X23, #0x5A8
.text:0000007101E06360                 STR             X8, [X23,#(qword_7105CCEB98 - 0x7105CCE5F0)]
.text:0000007101E06364                 LDR             X8, [X0]
.text:0000007101E06368                 LDR             X8, [X8,#0x48]
.text:0000007101E0636C                 BLR             X8
.text:0000007101E06370                 STR             X0, [X23,#(qword_7105CCEBA8 - 0x7105CCE5F0)]
```

So final address is stored at 0x5CCEBA8.

So for 15 FPS it will look like this:
```yaml
15FPS:
  # Disable bSmoothFrameRate and bUseFixedFrameRate to untie game speed from framerate
  -
    type: write
    address: [MAIN, 0x5CCE320, 0x750]
    value_type: uint32
    # Default is 0x67, bSmoothFrameRate |= 0x20, bUseFixedFrameRate |= 0x40 
    # By writing 7 we are making sure that other flags are maintained: 
    # bAllowMultiThreadedAnimationUpdate |= 4
    # bOptimizeAnimBlueprintMemberVariableAccess |= 2
    # bCanBlueprintsTickByDefault |= 1
    value: 7
  # t.MaxFPS
  -
    type: write
    address: [MAIN, 0x5CCEBA8, 0]
    value_type: float
    value: [15, 15]
  -
    type: block
    what: timing
```
