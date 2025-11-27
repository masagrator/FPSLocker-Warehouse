# FPSLocker Warehouse

Here you will find a list with 30 FPS locked games, if they have FPSLocker configs that allow going above 30 FPS, tweak dynamic resolution frame timing for better performance, etc. At the end of README you can also find a separate list of configs for games that are targeting 30 FPS even though they have unlocked framerate.

Currently this repository is dedicated only to FPSLocker 3.0.2 or newer.

### Some 30 FPS game is not on the list, some game cannot go past 60 FPS? Write about it [HERE](https://github.com/masagrator/FPSLocker-Warehouse/issues/895).

---

> [!IMPORTANT]
> IT IS RECOMMENDED TO USE OVERLAY'S BUILTIN OPTION TO DOWNLOAD CONFIG! Some games may require additional files to fix certain issues (f.e. compatibility with romfs mods in Tears of The Kingdom), using builtin option is a sure way to download all needed files at once!

> [!NOTE]
> To download all configs click [here](https://github.com/masagrator/FPSLocker-Warehouse/archive/refs/heads/v4.zip), unpack it and copy the `SaltySD` and `atmosphere` folder to root of your sdcard.

---

Column `ISSUES` represents what issues you can expect from game when trying to go above default FPS target without using patch. It is valid only for the game's latest version listed here and only up to 60 FPS, above 60 FPS you may have different experience. In older versions it may be different (Example: Horizon Chase 2 1.6.6 uses internal FPS lock, but 1.6.3 doesn't).<br>
Patches status concern only FPSLocker "LOCK" patch format. There may exist cheat/IPS patch/mod that unlocks 60 FPS already.<br>
As the list is filled by community, it may not be up to date.

If any issue is crossed out, it means it was solved to - subjectively - acceptable level.

> <a id="🔐"></a>🔐 - *Internal FPS Lock* - must be removed or adjusted, example: `A Hat in Time`

> <a id="📏"></a>📏 - *Dynamic Resolution* - must be adjusted to target other FPS, example: `SHADOW GENERATIONS`

> <a id="⚔️"></a>⚔️ - *Double Buffer* - changing it to triple buffer allows staying more often at higher FPS, example: `The Legend of Zelda: Breath of the Wild`. It doesn't include games that are not rendering double buffer in `Acquire->Render->Present` order (like `Present->Render->Acquire`), f.e. `The Witcher 3`

> <a id="👄"></a>👄 - *Lipsync* - must be adjusted to work correctly at different FPS, example: `The Legend of Heroes: Trails of Cold Steel 3`

> <a id="⏱️"></a>⏱️ - *Gameplay speed* - must be adjusted to work correctly at different FPS, example: `The Legend of Zelda: Breath of the Wild`

> <a id="🏃"></a>🏃 - *Physics* - must be adjusted to work correctly at different FPS, example: `The Legend of Zelda: Breath of the Wild`

> <a id="🛑"></a>🛑 - *Fake frames* - game must be adjusted to not show them at higher FPS, example: `Agatha Christie - Hercule Poirot: The First Cases`

> <a id="🌤️"></a>🌤️ - *Graphics effects* - game must be adjusted to have them rendered correctly at higher FPS, example: `Gear.Club Unlimited 2`

> <a id="🖥️"></a>🖥️ - *UI speed* - game must be adjusted to have them rendered correctly at higher FPS, example: `The Legend of Zelda: Breath of the Wild`

> <a id="🖌️"></a>🖌️ - *UI broken animations* - game must be adjusted to have them rendered correctly at higher FPS, example: `Another Code: Recollection`

> <a id="📺"></a>📺 - *Cutscenes* - they must be blocked to certain framerate to not cause issues, example: `The Legend of Zelda: Breath of the Wild`

> <a id="🎮"></a>🎮 - *Button polling* - it must be adjusted to not miss button presses at higher FPS, example: `NARUTO SHIPPUDEN: Ultimate Ninja STORM 4 ROAD TO BORUTO`

> <a id="🔢"></a>🔢 - *Logic* - it must be fixed to work correctly at higher FPS, example: `Pikmin 4`

> <a id="🔧"></a>🔧 - *Hindered performance* - something in game is causing performance issues at higher FPS, either on its own (`r.VSync` setting in UE4/UE5 games) or when something from the above is adjusted, example: `Outer Wilds`

> <a id="📷"></a>📷 - *Camera* - It must be fixed to work correctly at higher FPS, example: `妖怪ウォッチ`

PATCH AVAILABILITY<br>
✝️ - patch is not possible to create<br>
❌ - patch not available (📌 means that nobody asked for it, if there is no such icon it means that it was already looked at and deemed too hard to do to fix all issues to acceptable level)
✅ - patch available (click on it for config file that can be converted to patch, config file may require additional files that are listed in "addons" entry inside config).<br>
◯ - this version doesn't need a patch

---

<details>
<summary>List of 30 FPS locked games (919 titles)</summary>

| NAME | TITLE ID | BUILD ID (PATCH AVAILABLE, VERSION ID, VERSION) | ISSUES |
| --- | --- | --- | --- |
| .hack//G.U. Last Recode | `0100BA9014A02000` | `4C0ED5711263A6D9` (❌, v0, 1.0.0) | [⏱️](#⏱️)[🖥️](#🖥️)[🎮](#🎮) |
| 60 Parsecs! | `010010100FF14000` | `12F93E2DBBCFA54F` ([✅](SaltySD/plugins/FPSLocker/patches/010010100FF14000/12F93E2DBBCFA54F.yaml), v10, 1.0.10) | [📷](#📷) |
| 8-Bit Adventures 2 | `010008B00D682000` | `89777FD8569E563D` (❌, v3, 1.0.3) | [⚔️](#⚔️)[⏱️](#⏱️) |
| A Hat in Time | `010056E00853A000` | `746F0D697EEEE2DD` ([✅](SaltySD/plugins/FPSLocker/patches/010056E00853A000/746F0D697EEEE2DD.yaml), v4, 1.0.4) | ~~[🔐](#🔐)~~ |
| A Monster's Expedition | `0100C01013302000` | `09CB487D63E4827E` (◯, v3, 1.2.0) |  |
| ABYSS SEEKER――What Do You See Deep in Abyss | `01003990220BE000` | `C17F9C48EEFAB9DF` ([✅](SaltySD/plugins/FPSLocker/patches/01003990220BE000/C17F9C48EEFAB9DF.yaml), v0, 1.1.0.012) <br> `FE67FB035271B5E4` ([✅](SaltySD/plugins/FPSLocker/patches/01003990220BE000/FE67FB035271B5E4.yaml), v1, 1.2.0.020) <br> `820EF220126FF10A` ([✅](SaltySD/plugins/FPSLocker/patches/01003990220BE000/820EF220126FF10A.yaml), v2, 1.3.0.105) | ~~[🛑](#🛑)~~ |
| ABZU | `0100C1300BBC6000` | `59719CFCD1671B98` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1300BBC6000/59719CFCD1671B98.yaml), v1, 1.0.01) | ~~[🔧](#🔧)~~ |
| ACE COMBAT™7 SKIES UNKNOWN | `0100E3401D660000` | `FDBEE885A65A2B92` ([✅](SaltySD/plugins/FPSLocker/patches/0100E3401D660000/FDBEE885A65A2B92.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Achilles Legends Untold | `01007BE01FCC2000` | `BDDD7E8FA07C8C75` ([✅](SaltySD/plugins/FPSLocker/patches/01007BE01FCC2000/BDDD7E8FA07C8C75.yaml), v2, 1.0.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Achilles: Survivor | `0100CD6023C84000` | `163585C5E3885A04` ([✅](SaltySD/plugins/FPSLocker/patches/0100CD6023C84000/163585C5E3885A04.yaml), v0, 1.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Advance Wars 1+2: Re-Boot Camp | `0100300012F2A000` | `320A17744AEFD67F` ([✅](SaltySD/plugins/FPSLocker/patches/0100300012F2A000/320A17744AEFD67F.yaml), v0, 1.0.0) | ~~[🔐](#🔐)~~ |
| Adventure Time: Pirates of the Enchiridion | `0100C4E004406000` | `550CC8AAD902C04F` (◯, v4, 1.0.4.26870) |  |
| AEW: Fight Forever | `0100BD10190C0000` | `45C15AE4450708FD` ([✅](SaltySD/plugins/FPSLocker/patches/0100BD10190C0000/45C15AE4450708FD.yaml), v9, 1.10.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Against the Storm | `010062F01F2CC000` | `99AFEE8180CE93D8` (◯, v3, 1.18) |  |
| Agent Intercept | `0100B80013C1C000` | `A475D0073EA170B0` (◯, v0, 1.0.0) |  |
| Agatha Christie - Hercule Poirot: The First Cases | `010000F012936000` | `1570FE23108B93C4` ([✅](SaltySD/plugins/FPSLocker/patches/010000F012936000/1570FE23108B93C4.yaml), v4, 1.0.3.1) | ~~[🛑](#🛑)~~ |
| Agatha Christie - Hercule Poirot: The London Case | `01002FD01A24C000` | `8F72E0D61C4BA0B1` ([✅](SaltySD/plugins/FPSLocker/patches/01002FD01A24C000/8F72E0D61C4BA0B1.yaml), v2, 1.0.2) | ~~[🛑](#🛑)~~ |
| Agatha Christie - The ABC Murders | `010087C011C4E000` | `655293197620944D` (◯, v2, 1.0.2) |  |
| Airhead | `0100272013014000` | `D1D421137AAE1A5E` ([✅](SaltySD/plugins/FPSLocker/patches/0100272013014000/D1D421137AAE1A5E.yaml), v0, 1.0.0) | ~~[🛑](#🛑)~~ |
| Alan Wake Remastered | `0100623017A58000` | `6520258D00AEA915` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| Alchemy Garden | `0100A4101AC26000` | `FB73B824FB53892E` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| Alfred Hitchcock - Vertigo | `0100DC7013F14000` | `9D5ABEC66FEC1D77` (◯, v1, 1.0.1) |  |
| Alien: Isolation | `010075D00E8BA000` | `397C054A3D25D488` (◯, v5, 1.1.5_64113) |  |
| Alterity Experience | `010056F0186D0000` | `E4F041624093998D` (◯, v2, 2.0) |  |
| Amber Isle | `010073601DF1A000` | `D36459588F85315D` ([✅](SaltySD/plugins/FPSLocker/patches/010073601DF1A000/D36459588F85315D.yaml), v2, 1.0.2) <br> `E8BF195297B63BA2` ([✅](SaltySD/plugins/FPSLocker/patches/010073601DF1A000/E8BF195297B63BA2.yaml), v3, 1.0.3) | ~~[📏](#📏)~~ |
| American Fugitive | `010002B00C534000` | `375A0E11B2397340` (◯, v9, 1.1.1) |  |
| Amnesia Collection | `01003CC00D0BE000` | `F6FB99E54347E740` ([✅](SaltySD/plugins/FPSLocker/patches/01003CC00D0BE000/F6FB99E54347E740.yaml), v3, 1.3.0) | ~~[🔐](#🔐)[📏](#📏)~~[⚔️](#⚔️) |
| Ancestors Legacy | `01009EE0111CC000` | `E1F0CFC02F449EF3` ([✅](SaltySD/plugins/FPSLocker/patches/01009EE0111CC000/E1F0CFC02F449EF3.yaml), v2, 1.2.0) | ~~[🔐](#🔐)[⚔️](#⚔️)~~ |
| Ancient Weapon Holly | `0100F7201D1B0000` | `BF3F18101CBCFB33` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7201D1B0000/BF3F18101CBCFB33.yaml), v3, 1.7.0) <br> `3BBD72F0EB13C1AE` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7201D1B0000/3BBD72F0EB13C1AE.yaml), v4, 1.7.1) | ~~[🏃](#🏃)~~ |
| Animal Crossing: New Horizons | `01006F8002326000` | `CBF780093C874152` (❌, v30, 2.0.8) | [⚔️](#⚔️)[⏱️](#⏱️)[🏃](#🏃)🖥 |
| Animal Shelter Simulator | `0100B1C01B104000` | `AB9EFB08DB5FE4F1` (❌, v1, 1.1.0) | [⏱️](#⏱️) |
| Another Code: Recollection | `0100CB9018F5A000` | `DED0F920799151BE` (❌, v0, 1.0.0) | [🖌️](#🖌️) |
| Another Crab's Treasure | `0100A21017C42000` | `3980F76403AE4CF2` ([✅](SaltySD/plugins/FPSLocker/patches/0100A21017C42000/3980F76403AE4CF2.yaml), v4, 1.0.101.1) <br> `01CBDFDED43B80F5` ([✅](SaltySD/plugins/FPSLocker/patches/0100A21017C42000/01CBDFDED43B80F5.yaml), v5, 1.0.103.9) <br> `B24C86A2B02DE960` ([✅](SaltySD/plugins/FPSLocker/patches/0100A21017C42000/B24C86A2B02DE960.yaml), v6, 1.1.100.1) <br> `693314C08EA157F3` ([✅](SaltySD/plugins/FPSLocker/patches/0100A21017C42000/693314C08EA157F3.yaml), v7, 1.1.100.2) <br> `807A2202464D445B` ([✅](SaltySD/plugins/FPSLocker/patches/0100A21017C42000/807A2202464D445B.yaml), v8, 1.1.100.3) | ~~[📏](#📏)[⏱️](#⏱️)[🏃](#🏃)~~ |
| Apollo Justice Trilogy | `010020D01B890000` | `F1A7E0DB6B0EC65F` (❌, v1, 1.0.1) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| Aragami 2 | `0100787018198000` | `3FFD52E56DD8ADB3` (◯, v1, 1.0.30195.0) |  |
| 아라가미 2 | `0100021019A18000` | `AE1A9D2E97C95384` (◯, v2, 1.0.30196.0) |  |
| Arise: A Simple Story | `0100FE201680A000` | `8F2536786EECCEE5` ([✅](SaltySD/plugins/FPSLocker/patches/0100FE201680A000/8F2536786EECCEE5.yaml), v5, 1.0.5) | ~~[🔐](#🔐)[📏](#📏)~~ |
| ARK: Dinosaur Discovery | `0100A6B01900E000` | `9E0901B84058B5B4` ([✅](SaltySD/plugins/FPSLocker/patches/0100A6B01900E000/9E0901B84058B5B4.yaml), v2, 1.5.0) | ~~[🔐](#🔐)~~ |
| ARK: Survival Evolved | `0100D4A00B284000` | `D1E3FFBA414F4929` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4A00B284000/D1E3FFBA414F4929.yaml), v14, 2.0.11) <br> `DE62C644228E63CC` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4A00B284000/DE62C644228E63CC.yaml), v15, 2.0.12) <br> `44E0F3E8F4996F55` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4A00B284000/44E0F3E8F4996F55.yaml), v16, 2.0.14) <br> `2B70B1A7B478FCA3` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4A00B284000/2B70B1A7B478FCA3.yaml), v17, 2.0.15) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Arrest of a stone Buddha | `0100184011B32000` | `6E617D487F4EE441` (❌, v0, 1.0.0) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| art of rally | `0100A88012504000` | `0D17FD76B32F3040` ([✅](SaltySD/plugins/FPSLocker/patches/0100A88012504000/0D17FD76B32F3040.yaml), v6, 1.1.8) <br> `BCAA04FAF88EEA4A` ([✅](SaltySD/plugins/FPSLocker/patches/0100A88012504000/BCAA04FAF88EEA4A.yaml), v7, 1.1.9) | ~~[📏](#📏)~~ |
| Ary and the Secret of Seasons | `0100C2500CAB6000` | `3EBEDE7394C88C42` (◯, v3, 1.0.3) |  |
| Assassin's Creed II | `0100670014482000` | `824B38A25986B2AB` ([✅](SaltySD/plugins/FPSLocker/patches/0100670014482000/824B38A25986B2AB.yaml), v3, 1.3) | ~~[📏](#📏)~~ |
| Assassin's Creed Brotherhood | `0100670014482001` | `2B59D6C677258A2A` ([✅](SaltySD/plugins/FPSLocker/patches/0100670014482001/2B59D6C677258A2A.yaml), v3, 1.3) | ~~[📏](#📏)~~ |
| Assassin's Creed Revelations | `0100670014482002` | `0AE4D1770B196094` ([✅](SaltySD/plugins/FPSLocker/patches/0100670014482002/0AE4D1770B196094.yaml), v3, 1.3) | ~~[📏](#📏)~~ |
| Assassin's Creed Revelations - The Lost Archive | `0100670014482003` | `729AB05205B9B7E4` (◯, v3, 1.3) |  |
| Assassin's Creed III Remastered | `01007F600B134000` | `43DDF3AED0E7E500` (◯, v3, 1.0.3) |  |
| Assassin's Creed IV Black Flag | `010044700DEB0000` | `85F5D5AB6187F602` (◯, v0, 1.0.0) |  |
| Assassin's Creed Rogue | `010044700DEB0001` | `3DEF0E36AA8C6592` ([✅](SaltySD/plugins/FPSLocker/patches/010044700DEB0001/3DEF0E36AA8C6592.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Asterix & Obelix XXXL - The Ram From Hibernia | `01001F3018880000` | `DF556AF2E30073C0` ([✅](SaltySD/plugins/FPSLocker/patches/01001F3018880000/DF556AF2E30073C0.yaml), v4, 1.04.00) | ~~[📏](#📏)~~ |
| Astor: Blade of the Monolith | `01001D00186E8000` | `C26E93197DEB4004` ([✅](SaltySD/plugins/FPSLocker/patches/01001D00186E8000/C26E93197DEB4004.yaml), v1, 1.0.1) <br> `6133D5CC14F51B7A` ([✅](SaltySD/plugins/FPSLocker/patches/01001D00186E8000/6133D5CC14F51B7A.yaml), v2, 1.0.2) <br> `E2AFE5A73F5C0803` ([✅](SaltySD/plugins/FPSLocker/patches/01001D00186E8000/E2AFE5A73F5C0803.yaml), v3, 1.0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| ASTRAL CHAIN | `01007300020FA000` | `4B159F0F7A360669` ([✅](SaltySD/plugins/FPSLocker/patches/01007300020FA000/4B159F0F7A360669.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)[📺](#📺)~~[🔢](#🔢) |
| Atelier Ayesha | `0100D9D00EE8C000` | `B9146E1CAD9E36BA` (◯, v0, 1.0.0) |  |
| Atelier Escha & Logy | `0100E5600EE8E000` | `4BBB3B3455D306C6` (◯, v0, 1.0.0) |  |
| Atelier Firis | `010023201421E000` | `8BB29E319CCE6357` (◯, v4, 1.0.4) |  |
| Atelier Lulua | `0100B1400CD50000` | `CA7FACAEC708311C` (◯, v4, 1.0.3) |  |
| Atelier Lydie & Suelle DX | `01001A5014220000` | `32EB581C7D9BE094` (◯, v3, 1.0.3) |  |
| Atelier Marie Remake | `0100EAE019904000` | `743CD6A40363900C` (◯, v1, 1.0.0a) |  | 
| Atelier Meruru | `0100ADD00C6FA000` | `E76C3624D3AE3DCE` (◯, v2, 1.0.2) |  |
| Atelier Resleriana | `01000F9020CD4000` | `6ACDAEE7DDC5E503` ([✅](SaltySD/plugins/FPSLocker/patches/01000F9020CD4000/6ACDAEE7DDC5E503.yaml), v4, 1.2a) <br> `F140F141FDC4C331` ([✅](SaltySD/plugins/FPSLocker/patches/01000F9020CD4000/F140F141FDC4C331.yaml), v5, 1.3) <br> `8593E6008F5A883D` ([✅](SaltySD/plugins/FPSLocker/patches/01000F9020CD4000/8593E6008F5A883D.yaml), v6, 1.4) | [🏃](#🏃) |
| Atelier Rorona | `010088600C66E000` | `967D32BE4B10B67E` (◯, v1, 1.0.1) |  |
| Atelier Ryza | `0100D1900EC80000` | `3474FAEE2B35BCAD` (◯, v9, 1.0.9) |  |
| Atelier Ryza 2 | `01009A9012022000` | `2275D20A581F37E3` (◯, v8, 1.0.8) |  |
| Atelier Ryza 3 | `010095E018944000` | `C29B86A5D924BD38` (◯, v9, 1.7.0) |  |
| Atelier Ryza DX | `0100199023B2E000` | `A6BE42F22D2788F8` (◯, v0, 1.0.0) |  |
| ライザのアトリエ DX | `01003B7023A12000` | `F47522A0FB4C6A49` (◯, v0, 1.0.0) |  |
| Atelier Ryza 2 DX | `01004D5023B32000` | `733604C8B4C5AD73` (◯, v0, 1.0.0) |  |
| Atelier Ryza 3 DX | `0100A4C023B34000` | `3458B838BD55F8C4` (◯, v0, 1.0.0) |  |
| Atelier Shallie | `010005C00EE90000` | `AAB0450A965202EC` (◯, v0, 1.0.0) |  |
| Atelier Sophie | `0100D8701421C000` | `9C95108FD8F7464A` (◯, v3, 1.0.3) |  |
| Atelier Sophie 2 | `010082A01538E000` | `4A1B406278346C2B` (◯, v8, 1.0.8) |  |
| ソフィーのアトリエ２ | `0100661013EEE000` | `E93A13EC391CFA19` (◯, v9, 1.0.8) |  |
| Atelier Totori | `01009BC00C6F6000` | `4FD4BFE66C5353D4` (◯, v1, 1.0.1) |  |
| Atelier Yumia | `0100544020572000` | `A947DDE7826A3562` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/A947DDE7826A3562.yaml), v1, 1.0.1) <br> `5E43788065113530` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/5E43788065113530.yaml), v2, 1.0.2) <br> `153DB27728D41305` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/153DB27728D41305.yaml), v3, 1.1.0) <br> `29F67D61B0AD1500` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/29F67D61B0AD1500.yaml), v4, 1.2.0) <br> `3B2CB1C8865E7B1E` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/3B2CB1C8865E7B1E.yaml), v5, 1.2.1) <br> `1CEA83A1E6684665` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/1CEA83A1E6684665.yaml), v6, 1.3.0) <br> `9B9CCD97EB6EF789` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/9B9CCD97EB6EF789.yaml), v9, 1.4.2) <br> `540477886936CDC5` ([✅](SaltySD/plugins/FPSLocker/patches/0100544020572000/540477886936CDC5.yaml), v11, 1.5.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| - 유미아의 아틀리에<br>- 優米雅的鍊金工房 | `010054A020574000` | `6CB3E54C5F648410` ([✅](SaltySD/plugins/FPSLocker/patches/010054A020574000/6CB3E54C5F648410.yaml), v6, 1.3.0) <br> `EF85880A244D33EC` ([✅](SaltySD/plugins/FPSLocker/patches/010054A020574000/EF85880A244D33EC.yaml), v9, 1.4.2) <br> `FB3497202E5934FB` ([✅](SaltySD/plugins/FPSLocker/patches/010054A020574000/FB3497202E5934FB.yaml), v11, 1.5.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Attack on Titan 2 | `010034500641A000` | `586EA519C1CDFAE7` (◯, v14, 1.0.14) |  |
| Aztech Forgotten Gods | `01006B4014564000` | `65EF4BC77B974E05` (◯, v8, 1.0.8) |  |
| Azur Lane: Crosswave | `010065D012FA0000` | `C403B87FCDAD7604` ([✅](SaltySD/plugins/FPSLocker/patches/010065D012FA0000/C403B87FCDAD7604.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| 碧藍航線 Crosswave | `01005D10128D2000` | `1A876E8881CEFBE3` ([✅](SaltySD/plugins/FPSLocker/patches/01005D10128D2000/1A876E8881CEFBE3.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Bakery Simulator | `010018601E9E0000` | `31A37D73E22F1059` ([✅](SaltySD/plugins/FPSLocker/patches/010018601E9E0000/31A37D73E22F1059.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| BALAN WONDERWORLD | `0100438012EC8000` | `1A0EAEC3AE90B018` ([✅](SaltySD/plugins/FPSLocker/patches/0100438012EC8000/1A0EAEC3AE90B018.yaml), v1, 1.01) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Bang-On Balls: Chronicles | `010081E01A45C000` | `25D3C2E9040D1A9A` ([✅](SaltySD/plugins/FPSLocker/patches/010081E01A45C000/25D3C2E9040D1A9A.yaml), v4, 1.0.4) <br> `36C7E946E6C11C8E` ([✅](SaltySD/plugins/FPSLocker/patches/010081E01A45C000/36C7E946E6C11C8E.yaml), v5, 1.0.5) | ~~[📏](#📏)[🔧](#🔧)~~ | 
| Baldo The Guardian Owls | `0100A75005E92000` | `9E29077BE56B5E4D` (◯, v17, 1.0.17) |  |
| Bandle Tale: A League of Legends Story | `010052B01BEC0000` | `8BF051A6E3110A30` (◯, v1, 1.062) |  |
| Bassmaster Fishing 2022 | `0100B8501771A000` | `78BF042012CF9EE8` ([✅](SaltySD/plugins/FPSLocker/patches/0100B8501771A000/78BF042012CF9EE8.yaml), v2, 1.02) | ~~[📏](#📏)~~ |
| Batman - The Telltale Series | `0100011005D92000` | `A3A998AF3252D110` ([✅](SaltySD/plugins/FPSLocker/patches/0100011005D92000/A3A998AF3252D110.yaml), v3, 1.0.4) | ~~[⚔️](#⚔️)~~ |
| Batman: Arkham Asylum | `0100E870163CA000` | `621EE66A6743D750` ([✅](SaltySD/plugins/FPSLocker/patches/0100E870163CA000/621EE66A6743D750.yaml), v1, 1.0.1) | ~~[🔐](#🔐)~~ |
| Batman: Arkham City | `01003F00163CE000` | `8983C5A34B178E5C` (◯, v2, 1.0.2) |  |
| Batman: Arkham Knight | `0100ACD0163D0000` | `C0C37AE212170CAD` (◯, v4, 1.0.4) |  |
| Batman: The Enemy Within | `0100E6300AA3A000` | `AAC6FB02E03062EF` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6300AA3A000/AAC6FB02E03062EF.yaml), v1, 1.0.3) | ~~[⚔️](#⚔️)~~ |
| Batora: Lost Haven | `0100A93016BF4000` | `770A07C35E631CB2` ([✅](SaltySD/plugins/FPSLocker/patches/0100A93016BF4000/770A07C35E631CB2.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Bayonetta Origins: Cereza and the Lost Demon | `0100CF5010FEC000` | `A1CE2940D813ACAB` ([✅](SaltySD/plugins/FPSLocker/patches/0100CF5010FEC000/A1CE2940D813ACAB.yaml), v0, 1.0.0) | ~~[⏱️](#⏱️)~~ |
| Bendy: Lone Wolf | `010071B022A36000` | `E301AFDBCDF9F9AD` (◯, v3, 2.0.5) |  |
| Bendy and the Dark Revival | `0100207021C3C000` | `2C2D599E55912C6C` ([✅](SaltySD/plugins/FPSLocker/patches/0100207021C3C000/2C2D599E55912C6C.yaml), v1, 1.6.3s) | ~~[📏](#📏)[📷](#📷)~~ |
| Bendy and the Ink Machine | `0100D4C00C6C0000` | `91B6BD011F0C2C46` (◯, v2, 1.6.0.0) |  |
| BEYBLADE X EVOBATTLE | `01009F002286E000` | `DF9D9CE09ACC1810` (◯, v1, 1.0.1) |  |
| ベイブレードエックス エボバトル | `0100D9702286C000` | `92A57698A4F90E7D` (◯, v2, 1.0.2) |  |
| BEYBLADE X XONE `EU/US` | `0100E2301FB1E000` | `4B1FF00AF525242D` (◯, v9, 1.0.10) |  |
| BEYBLADE X XONE `ASIA` | `0100FC90205FE000` | `AE69E1BB81CD6FDE` (◯, v9, 1.0.10) |  |
| ベイブレードエックス XONE | `0100E0901E2AA000` | `08AE6D4A4C596C968` (◯, v10, 1.0.10) |  |
| Beyond Galaxyland | `01006E101DBA0000` | `3B3ACCF3458CE10D` (◯, v3, 1.0.4) |  |
| Beyond Good & Evil | `0100E0A01DD20000` | `AC7FD7804398393D` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| Beyond Enemy Lines | `0100AE7010434000` | `5915CDDDC4EEA6CD` ([✅](SaltySD/plugins/FPSLocker/patches/0100AE7010434000/5915CDDDC4EEA6CD.yaml), v1, 1.1.0) | ~~[📏](#📏)~~ |
| Big Helmet Heroes | `010044B01E786000` | `2CF926BBD5D1AB4D` ([✅](SaltySD/plugins/FPSLocker/patches/010044B01E786000/2CF926BBD5D1AB4D.yaml), v2, 1.0.3) | ~~[🔧](#🔧)~~ |
| Biomutant | `01004BA017CD6000` | `4B86FC4FDF7B1A70` ([✅](SaltySD/plugins/FPSLocker/patches/01004BA017CD6000/4B86FC4FDF7B1A70.yaml), v1, 1.0.1) <br> `5BE02E1373BDE2CC` ([✅](SaltySD/plugins/FPSLocker/patches/01004BA017CD6000/5BE02E1373BDE2CC.yaml), v2, 1.0.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| BioShock Remastered | `0100AD10102B2000` | `D89FFAA2062E373D` ([✅](SaltySD/plugins/FPSLocker/patches/0100AD10102B2000/D89FFAA2062E373D.yaml), v1, 1.0.2) | ~~[📏](#📏)~~ |
| BioShock 2 Remastered | `01002620102C6000` | `7D1714279435589C` ([✅](SaltySD/plugins/FPSLocker/patches/01002620102C6000/7D1714279435589C.yaml), v1, 1.0.2) | ~~[📏](#📏)~~ |
| BioShock Infinite | `0100D560102C8000` | `48681F1D90704F6C` ([✅](SaltySD/plugins/FPSLocker/patches/0100D560102C8000/48681F1D90704F6C.yaml), v1, 1.0.2) | ~~[📏](#📏)~~ |
| Biped 2 | `01004240237F6000` | `C591E6A24ED95D54` (◯, v2, 1.0.2) |  |
| Black Skylands | `0100FA601A58C000` | `C13490454BA10AE4` (◯, v3, 1.0.3) |  |
| Blade Assault | `0100EA1018A2E000` | `0DF84BFE1556A443` (◯, v1, 1.0.1) |  |
| Blades of Time | `0100CFA00CC74000` | `679B5FC4F46F5DB7` (❌, v4, 1.2.200127) | [🔐](#🔐) |
| Blair Witch | `01006CC01182C000` | `C31E59266A218855` ([✅](SaltySD/plugins/FPSLocker/patches/01006CC01182C000/C31E59266A218855.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Bloodstained: Ritual of the Night | `0100BF500207C000` | `E380EB35262B4F9C` ([✅](SaltySD/plugins/FPSLocker/patches/0100BF500207C000/E380EB35262B4F9C.yaml), v12, 1.50) <br> `461B14E505AB9555` ([✅](SaltySD/plugins/FPSLocker/patches/0100BF500207C000/461B14E505AB9555.yaml), v13, 1.60) | ~~[⚔️](#⚔️)[📏](#📏)[🔧](#🔧)~~ |
| Blue Fire | `010073B010F6E000` | `2619FF1E39C93BAE` ([✅](SaltySD/plugins/FPSLocker/patches/010073B010F6E000/2619FF1E39C93BAE.yaml), v7, 6.1.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Bomb Rush Cyberfunk | `0100317014B7C000` | `63DEB63518DAA853` (◯, v5, 1.0.20515) |  |
| Boomerang X | `0100C09014530000` | `D92F465FE9920BB6` ([✅](SaltySD/plugins/FPSLocker/patches/0100C09014530000/D92F465FE9920BB6.yaml), v2, 1.0.2) | ~~[📏](#📏)~~ |
| Borderlands | `010064800F66A000` | `1C37C3673E0E4E7A` (◯, v2, 1.0.2) |  |
| Borderlands 2 | `010096F00FF22000` | `F7C233469F20EE3F` (◯, v2, 1.0.2) |  |
| Borderlands: The Pre-Sequel | `010007400FF24000` | `090B1F7F7AF35D00` ([✅](SaltySD/plugins/FPSLocker/patches/010007400FF24000/090B1F7F7AF35D00.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ |
| Boti: Byteland Overclocked | `0100B7C01D480000` | `CCBDDB69038F76FC` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7C01D480000/CCBDDB69038F76FC.yaml), v0, 1.0.0) <br> `E8EA74BE6221F2E4` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7C01D480000/E8EA74BE6221F2E4.yaml), v1, 1.0.1) <br> `567A8410AE613885` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7C01D480000/567A8410AE613885.yaml), v2, 1.0.2) <br> `8A942A9E838E5083` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7C01D480000/8A942A9E838E5083.yaml), v3, 1.0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| BPM: Bullets Per Minute | `0100040016EE2000` | `331E3DFBDF650226` ([✅](SaltySD/plugins/FPSLocker/patches/0100040016EE2000/331E3DFBDF650226.yaml), v1, 0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Bramble The Mountain King | `0100E87017D0E000` | `ACF3FF125C2A3E68` ([✅](SaltySD/plugins/FPSLocker/patches/0100E87017D0E000/ACF3FF125C2A3E68.yaml), v5, 1.0.7) | ~~[📏](#📏)~~ |
| BRAVELY DEFAULT II `Asia` | `010056F00C7B4000` | `B5B9C7BB8D9716F6` ([✅](SaltySD/plugins/FPSLocker/patches/010056F00C7B4000/B5B9C7BB8D9716F6.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| BRAVELY DEFAULT II `Global` | `01006DC010326000` | `05DE5A7F20BD1532` ([✅](SaltySD/plugins/FPSLocker/patches/01006DC010326000/05DE5A7F20BD1532.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Bravery and Greed | `0100F60017D4E000` | `C660EA2CC0478E4B` (◯, v3, 1.0.3) |  |
| Breathedge | `01000AA013A5E000` | `B26DE1669B729335` ([✅](SaltySD/plugins/FPSLocker/patches/01000AA013A5E000/B26DE1669B729335.yaml), v2, 1.0.2) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Bright Memory: Infinite | `01001A9018560000` | `DD425ECC07C305DF` ([✅](SaltySD/plugins/FPSLocker/patches/01001A9018560000/DD425ECC07C305DF.yaml), v3, 1.3) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Bro Falls | `01005EF01A12E000` | `A07FFE2F32878CE9` (◯, v0, 1.57) |  |
| Broken Roads | `0100FAD01861C000` | `D84426C8D6B8D947` ([✅](SaltySD/plugins/FPSLocker/patches/0100FAD01861C000/D84426C8D6B8D947.yaml), v1, 1.2.11059) | ~~[📏](#📏)~~ |
| Builder Simulator | `01000B101E3D8000` | `05DCD7F9AE5727D8` (◯, v0, 1.0.0) |  |
| Bulletstorm | `01003DD00D658000` | `32FC35DF1C50E1F1` (◯, v0, 1.0.0) |  |
| Bum Simulator | `01008E101E868000` | `42AD50169E847BA2` ([✅](SaltySD/plugins/FPSLocker/patches/01008E101E868000/42AD50169E847BA2.yaml), v2, 1.0.2) <br> `CE6953FB28A66265` ([✅](SaltySD/plugins/FPSLocker/patches/01008E101E868000/CE6953FB28A66265.yaml), v3, 1.0.3) | ~~[🔧](#🔧)~~ |
| C.A.R.D.S. RPG: The Misty Battlefield | `010066D01D0F0000` | `6019714364B13966` (◯, v12, 2.0.2) |  |
| Call of Cthulhu | `010046000EE40000` | `8F6B002FEB5D0F8E` ([✅](SaltySD/plugins/FPSLocker/patches/010046000EE40000/8F6B002FEB5D0F8E.yaml), v3, 0.1.6) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Call of Juarez: Gunslinger | `0100B4700BFC6000` | `EBF7DE558D554C7E` (◯, v5, 1.0.5) |  |
| Call of Sentinels | `0100DC2020C50000` | `4A64A3713EEA60CA` ([✅](SaltySD/plugins/FPSLocker/patches/0100DC2020C50000/4A64A3713EEA60CA.yaml), v0, 1.0.1.7) | ~~[🛑](#🛑)~~ |
| Candleman | `010034400CB5E000` | `926DB1056F50372A` (◯, v3, 1.0.3) |  |
| Card-en-Ciel | `0100E6B01BD3A000` | `393323C7FBCBD72D` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6B01BD3A000/393323C7FBCBD72D.yaml), v2, 1.0.4) <br> `27AB93A086868C70` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6B01BD3A000/27AB93A086868C70.yaml), v3, 1.1.0) <br> `59C5C45EF17ACADA` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6B01BD3A000/59C5C45EF17ACADA.yaml), v4, 1.2.0) <br> `6A2E388EB364D4ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6B01BD3A000/6A2E388EB364D4ED.yaml), v6, 1.3.1) <br> `CB3C7EF8E279A22D` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6B01BD3A000/CB3C7EF8E279A22D.yaml), v8, 1.4.1) <br> `0B00B4DFAE47EBA3` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6B01BD3A000/0B00B4DFAE47EBA3.yaml), v10, 1.5.1) <br> `0B00B4DFAE47EBA3` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6B01BD3A000/C9D5E4BE40E7EB66.yaml), v12, 1.5.3) | ~~[🔐](#🔐)~~[⚔️](#⚔️) |
| Cars 3: Driven to Win | `0100744001588000` | `6E191829548C2A41` (❌, v2, 1.0.2) | [⚔️](#⚔️) |
| Cassette Beasts | `010066F01A0E0000` | `65688736640651F6` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/58C1B2EA8257D5F1.yaml), v9, 1.6.3) <br> `2C58E765387F9DDA` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/2C58E765387F9DDA.yaml), v10, 1.6.4) <br> `F09EAE79357E3032` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/F09EAE79357E3032.yaml), v12, 1.7.1) <br> `153D5A2ABB9C0BA6` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/153D5A2ABB9C0BA6.yaml), v13, 1.7.2) <br> `B5DCAAA828DA5034` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/B5DCAAA828DA5034.yaml), v14, 1.8.0) <br> `768428355C994280` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/768428355C994280.yaml), v15, 1.8.2) | ~~[🔐](#🔐)[🏃](#🏃)~~ |
| Castle of Heart | `01003C100445C000` | `38E31B826DE0764C` (❌📌, v3, 1.3.0) | [🔐](#🔐) |
| Castle of Heart: Retold | `0100A0E023952000` | `9F7AA3145A0A8746` (❌📌, v2, 1.0.2) | [🔐](#🔐) |
| Castle Renovator | `010013801A0E4000` | `34E094252A069FE9` (◯, v0, 1.0.0) |  |
| Cat Quest III | `010088501B8F2000` | `A51ED5E6540C4921` (◯, v15, 1.4.7) |  |
| Catherine: Full Body | `0100BF00112C0000` | `93A79C77DA81F7F1` (❌, v2, 1.0.1a) | [⏱️](#⏱️)[🖥️](#🖥️) |
| Cel Damage HD | `010019B00BE72000` | `03B058B1F6BE7195` ([✅](SaltySD/plugins/FPSLocker/patches/010019B00BE72000/03B058B1F6BE7195.yaml), v0, 1.0.0) | ~~[🔐](#🔐)~~[🌤️](#🌤️) |
| Chants of Sennaar | `0100543019CB0000` | `4965231C2C9FA6D3` (◯, v3, 1.0.3) |  |
| Chef Life - A Restaurant Simulator | `0100F24014280000` | `CB098B1BD77BDD1A` (◯, v5, 1.8.0) |  |
| Chernobylite | `01000AB01F9C0000` | `2D2065AEBF94F9AE` ([✅](SaltySD/plugins/FPSLocker/patches/01000AB01F9C0000/2D2065AEBF94F9AE.yaml), v1, 1.1) <br> `657F40EEBD955F31` ([✅](SaltySD/plugins/FPSLocker/patches/01000AB01F9C0000/657F40EEBD955F31.yaml), v2, 1.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Choo-Choo Charles | `01006F901C7F2000` | `406F004D76F961F3` ([✅](SaltySD/plugins/FPSLocker/patches/01006F901C7F2000/406F004D76F961F3.yaml), v0, 1.0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Circus Electrique | `0100ABF015DCE000` | `57019F9781022D15` (◯, v2, 1.2.0) |  |
| Classic Racers Elite | `01003B90137D0000` | `9D9810D42B5AF44D` (◯, v0, 1.0) |  |
| Clive 'N' Wrench | `0100C6C010AE4000` | `FE211DBFAD6EA549` ([✅](SaltySD/plugins/FPSLocker/patches/0100C6C010AE4000/FE211DBFAD6EA549.yaml), v5, 1.0.6) | ~~[📏](#📏)~~ |
| Cobra Kai: The Karate Kid Saga Continues | `01005790110F0000` | `97E45918D2113640` (◯, v2, 1.0.2) |  |
| Cobra Kai 2: Dojos Rising | `0100BD9015B54000` | `BAD8504B110A21AE` (◯, v4, 2.20.8) |  |
| Cocoon | `01002E700C366000` | `5D8B61D234DCE809` (◯, v3, 1.0.3) |  |
| Company of Heroes Collection | `0100ABD0156F8000` | `F18BDC1CD8947ACA` (◯, v1, 1.8_83956) |  |
| Contra: Operation Galuga | `0100CF401A98E000` | `5ECFB8F85105FE3C` ([✅](SaltySD/plugins/FPSLocker/patches/0100CF401A98E000/5ECFB8F85105FE3C.yaml), v2, 1.0.882291) | ~~[📏](#📏)~~ |
| CONTRA: ROGUE CORPS | `0100F2600D710000` | `4CCD2F6D331DD104` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2600D710000/4CCD2F6D331DD104.yaml), v5, 1.3.0) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| CONVERGENCE: A League of Legends Story | `010020B016EF4000` | `7E25622D50D562BF` ([✅](SaltySD/plugins/FPSLocker/patches/010020B016EF4000/7E25622D50D562BF.yaml), v1, 1.0.1) | ~~[🛑](#🛑)~~ |
| Conway: Disappearance at Dahlia View | `010075C01405C000` | `BB52C1E6BC85DA52` (◯, v0, 1.0.0.0) |  |
| Crash Bandicoot N. Sane Trilogy | `0100D1B006744000` | `29E1A37D84227147` (◯, v0, 1.0.0) |  |
| Crash Bandicoot 4: It's About Time | `010073401175E000` | `E8DB38F170B0149D` ([✅](SaltySD/plugins/FPSLocker/patches/010073401175E000/E8DB38F170B0149D.yaml), v2, 1.2) | ~~[📏](#📏)~~ |
| Crash Team Racing Nitro-Fueled | `0100F9F00C696000` | `1C68951840693051` (◯, v15, 1.0.15) |  |
| Cris Tales | `0100B0400EBC4000` | `8A1DF79432172B4D` (◯, v3, 1.03) |  |
| CRISIS CORE -FINAL FANTASY VII- REUNION | `01004BC0166CC000` | `44D207EA6428E3F1` ([✅](SaltySD/plugins/FPSLocker/patches/01004BC0166CC000/44D207EA6428E3F1.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[📏](#📏)~~ |
| CRISIS CORE -FINAL FANTASY VII- REUNION `Asia` | `0100D09016C6A000` | `4710B51EB3A3C05C` ([✅](SaltySD/plugins/FPSLocker/patches/0100D09016C6A000/4710B51EB3A3C05C.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Cry Babies Magic Tears: The Big Game | `0100A1201B82A000` | `7C1D1E7A2B689E40` (◯, v1, 1.1) |  |
| CRYMACHINA | `010055B01AA08000` | `4CBD150A248DA39C` ([✅](SaltySD/plugins/FPSLocker/patches/010055B01AA08000/4CBD150A248DA39C.yaml), v2, 1.0.8) <br> `E196E389FD9E0364` ([✅](SaltySD/plugins/FPSLocker/patches/010055B01AA08000/E196E389FD9E0364.yaml), v3, 1.2.0) | ~~[🔧](#🔧)~~ |
| Crysis Remastered | `0100E66010ADE000` | `45CE2B6625A35771` ([✅](SaltySD/plugins/FPSLocker/patches/0100E66010ADE000/45CE2B6625A35771.yaml), v8, 1.8.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Crysis 2 Remastered | `0100582010AE0000` | `B3967105033ACC08` ([✅](SaltySD/plugins/FPSLocker/patches/0100582010AE0000/B3967105033ACC08.yaml), v3, 1.3.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Crysis 3 Remastered | `0100CD3010AE2000` | `53EA0196A4AEB260` ([✅](SaltySD/plugins/FPSLocker/patches/0100CD3010AE2000/53EA0196A4AEB260.yaml), v4, 1.3.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Crystar | `01003F2016754000` | `7B41D9CC72C2124D` (◯, v2, 1.0.2) |  |
| Cuisineer | `010087E01FCD6000` | `ACD959FBAECADE00` ([✅](SaltySD/plugins/FPSLocker/patches/010087E01FCD6000/ACD959FBAECADE00.yaml), v3, 2.0.27) | ~~[🛑](#🛑)~~ |
| Curse of the Dead Gods | `0100D4A0118EA000` | `DB285A63A090884F` (◯, v5, 1.0.0.5) |  |
| DAEMON X MACHINA | `0100B6400CA56000` | `937209E79E2E0E5D` (❌, v12, 1.4.2a) | [🔢](#🔢) |
| Danganronpa V3: Killing Harmony | `010063F014176000` | `6CBEE0573826FF73` (◯, v2, 1.0.2) |  |
| Dark Souls Remastered | `01004AB00A260000` | `DF3766A2BB651A3E` ([✅](SaltySD/plugins/FPSLocker/patches/01004AB00A260000/DF3766A2BB651A3E.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[🔢](#🔢)~~ |
| Darkest Dungeon II | `0100E5E01C098000` | `FC04D5F903B31D4C` (◯, v10, 1.1.0) |  |
| Darksiders Genesis | `0100F2300D4BA000` | `DB17131624D04A9C` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2300D4BA000/DB17131624D04A9C.yaml), v3, 1.0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Darksiders Warmastered Edition | `0100E1400BA96000` | `A4CC4C44C07AEC14` (◯, v0, 1.0.0) |  |
| Darksiders II Deathinitive Edition | `010071800BA98000` | `173E2EDEA9E5D940` ([✅](SaltySD/plugins/FPSLocker/patches/010071800BA98000/173E2EDEA9E5D940.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Darksiders III | `0100F8F014190000` | `AF7114F019CE6E1D` ([✅](SaltySD/plugins/FPSLocker/patches/0100F8F014190000/AF7114F019CE6E1D.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| DAVE THE DIVER | `010097F018538000` | `2E3EAEB4B6834BEF` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/2E3EAEB4B6834BEF.yaml), v17, 1.0.2.812) <br> `AE7422A20BC9C3B0` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/AE7422A20BC9C3B0.yaml), v18, 1.0.2.828) <br> `37CBC5751D80E70E` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/37CBC5751D80E70E.yaml), v19, 1.0.2.843) <br> `4983F1C36957B7E5` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/4983F1C36957B7E5.yaml), v20, 1.0.2.882) <br> `741C1E11C3A1FD02` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/741C1E11C3A1FD02.yaml), v21, 1.0.2.894) <br> `54300203FF8ABCC6` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/54300203FF8ABCC6.yaml), v25, 1.0.3.938) <br> `491561854A6DC444` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/491561854A6DC444.yaml), v26, 1.0.3.957) <br> `448820AF8E20D65D` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/448820AF8E20D65D.yaml), v27, 1.0.3.972) <br> `500A59C7C5A7C1E8` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/500A59C7C5A7C1E8.yaml), v28, 1.0.3.978) <br> `757760621154BA5A` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/757760621154BA5A.yaml), v30, 1.0.4.1029) <br> `456BDB6160D317A3` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/456BDB6160D317A3.yaml), v31, 1.0.4.1034) <br> `0E7A0A7276477C53` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/0E7A0A7276477C53.yaml), v32, 1.0.4.1039) <br> `8ACF8D236ADAB16F` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/8ACF8D236ADAB16F.yaml), v33, 1.0.4.1040) <br> `682B1552A9C571C9` ([✅](SaltySD/plugins/FPSLocker/patches/010097F018538000/682B1552A9C571C9.yaml), v35, 1.0.4.1075) | ~~[📷](#📷)~~ |
| Daydream: Forgotten Sorrow | `0100B8901AE88000` | `8AF36A929664A94D` ([✅](SaltySD/plugins/FPSLocker/patches/0100B8901AE88000/8AF36A929664A94D.yaml), v1, 1.0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Daymare: 1994 Sandcastle | `010091901E440000` | `8021F22E7A401A3E` ([✅](SaltySD/plugins/FPSLocker/patches/010091901E440000/8021F22E7A401A3E.yaml), v0, 1.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| DC Super Hero Girls: Teen Power | `0100F8F00C4F2000` | `BC714E2D7D32AB41` ([✅](SaltySD/plugins/FPSLocker/patches/0100F8F00C4F2000/BC714E2D7D32AB41.yaml), v1, 1.0.1) | [⚔️](#⚔️)~~[⏱️](#⏱️)~~ |
| DC's Justice League: Cosmic Chaos | `0100157015DD8000` | `3386C3BE1DE696DF` (◯, v5, 1.0.5) |  |
| DEAD OR ALIVE Xtreme 3 Scarlet | `01009CC00C97C000` | `71102550C57D57DB` (❌, v6, 1.0.6) | [⏱️](#⏱️)[🖥️](#🖥️) |
| Death end re;Quest | `0100AEC013DDA000` | `2F5554EBECAE652B` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| Death end re;Quest 2 | `0100EB701568A000` | `6A06F3A2582C0954` (❌, v0, 1.0.0) | [⚔️](#⚔️) |
| Death's Door | `0100B31015AF8000` | `0D20B5FF11828346` (◯, v3, 1.1.6a) |  |
| Decay of Logos | `010027700FD2E000` | `B77B17D7A517384F` (◯, v1, 1.0.1) |  |
| Deliver Us The Moon | `010047401EA8E000` | `928AF9461536F5E3` ([✅](SaltySD/plugins/FPSLocker/patches/010047401EA8E000/928AF9461536F5E3.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| DELTARUNE | `0100A0D022A68000` | `59972BE5A4FE0696` (❌, v5, 1.04) | [🔐](#🔐)[⏱️](#⏱️) |
| DEMON GAZE EXTRA | `0100FCC0168FC000` | `58EE9A90F6FE6D4B` (❌, v2, 1.0.2) | [⏱️](#⏱️)[🖥️](#🖥️) |
| Demon Slayer -Kimetsu no Yaiba- Sweep the Board! | `0100A7101B806000` | `BCC955FF933FEF2E` ([✅](SaltySD/plugins/FPSLocker/patches/0100A7101B806000/BCC955FF933FEF2E.yaml), v8, 1.20) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles | `0100309016E7A000` | `14C878ECCA9D7CB5` ([✅](SaltySD/plugins/FPSLocker/patches/0100309016E7A000/14C878ECCA9D7CB5.yaml), v9, 1.53) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles 2 | `0100AD80208A8000` | `B74F2DA687878275` (❌, v7, 1.20) | [🔐](#🔐)[🔧](#🔧)[🏃](#🏃) |
| 귀멸의 칼날 히노카미 혈풍담2 | `01001080208AA000` | `B74F2DA687878275` (❌, v7, 1.20) | [🔐](#🔐)[🔧](#🔧)[🏃](#🏃) |
| Demon Turf | `0100FF5015492000` | `9D3270945708DE4A` (◯, v2, 1.0.1) |  |
| Demon Turf: Neon Splash | `010010C017B28000` | `500BE42BCD41604F` (◯, v0, 1.0.0) |  |
| Descenders | `0100D4600D0E4000` | `899B8B12DCD0864F` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4600D0E4000/899B8B12DCD0864F.yaml), v7, 1.0.7) | ~~[📏](#📏)~~ |
| Destiny Connect: Tick-Tock Travelers | `010069500DD86000` | `5AD84EFD9D28FDDE` ([✅](SaltySD/plugins/FPSLocker/patches/010069500DD86000/5AD84EFD9D28FDDE.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Destroy All Humans! | `01009E701356A000` | `72E8F20EBBDBA296` ([✅](SaltySD/plugins/FPSLocker/patches/01009E701356A000/72E8F20EBBDBA296.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ |
| Detective Pikachu Returns | `010007500F27C000` | `A2A5ABEF988ABAA2` (◯, v0, 1.0.0) |  |
| Diablo II: Resurrected | `0100726014352000` | `BE7AD359B5CF5AA2` (◯, v27, 1.0.27.0) |  |
| Dinkum | `0100A5A020D5E000` | `8B3609ECB49DBBED` ([✅](SaltySD/plugins/FPSLocker/patches/0100A5A020D5E000/8B3609ECB49DBBED.yaml), v3, 1.0.2.44) | [📷](#📷) |
| Dino Ranch: Ride to the Rescue | `010038301ABDA000` | `DDF3A995F0EC84E1` (◯, v2, 1.0.4) |  |
| Disco Elysium - The Final Cut | `01006C5015E84000` | `26BDCC17F782A7B1` (◯, v12, 1.0.12) |  |
| Disney Dreamlight Valley | `0100D39012C1A000` | `4CD5D66F34BD11CC` (◯, v52, 1.20.2) |  |
| Disney Epic Mickey: Rebrushed | `01004D901AFDA000` | `D334BC060F1FA3AE` ([✅](SaltySD/plugins/FPSLocker/patches/01004D901AFDA000/D334BC060F1FA3AE.yaml), v4, 1.0.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| ディズニー エピックミッキー：Rebrushed | `0100DA201EBF8000` | `21F90AA03BED43F0` ([✅](SaltySD/plugins/FPSLocker/patches/0100DA201EBF8000/21F90AA03BED43F0.yaml), v2, 1.0.2) <br> `EE2CAB96FB6BEDA9` ([✅](SaltySD/plugins/FPSLocker/patches/0100DA201EBF8000/EE2CAB96FB6BEDA9.yaml), v3, 1.0.3) <br> `10844A7A20C5597E` ([✅](SaltySD/plugins/FPSLocker/patches/0100DA201EBF8000/10844A7A20C5597E.yaml), v4, 1.0.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Divinity: Original Sin 2 | `010027400CDC6000` | `4979B200D53BB282` ([✅](SaltySD/plugins/FPSLocker/patches/010027400CDC6000/4979B200D53BB282.yaml), v10, 1.0.10) | [⚔️](#⚔️)~~[📏](#📏)~~ |
| DOKAPON KiNGDOM CONNECT | `01006FD019A36000` | `4B8DE16DA675C702` (❌, v5, 1.1.2) | [⏱️](#⏱️)[🖥️](#🖥️) |
| Dollmare | `0100F09024254000` | `EC30FA360F7BFF02` ([✅](SaltySD/plugins/FPSLocker/patches/0100F09024254000/EC30FA360F7BFF02.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Dolphin Spirit - Ocean Mission | `0100150018200000` | `47B7DC55D707D10A` (◯, v1, 1.00.02) |  |
| Don't Starve Together | `010090100E334000` | `8F26DEF435008AE2` ([✅](SaltySD/plugins/FPSLocker/patches/010090100E334000/8F26DEF435008AE2.yaml), v24, 1.22.0) <br> `05D2208140190484` ([✅](SaltySD/plugins/FPSLocker/patches/010090100E334000/05D2208140190484.yaml), v25, 1.23.0) | [⚔️](#⚔️)~~[🔐](#🔐)[🖥️](#🖥️)~~ |
| DOOM | `0100416004C00000` | `01ACE43E724259C3` ([✅](SaltySD/plugins/FPSLocker/patches/0100416004C00000/01ACE43E724259C3.yaml), v3, 1.2) <br> `2847991952B3D7AB` ([✅](SaltySD/plugins/FPSLocker/patches/0100416004C00000/2847991952B3D7AB.yaml), v4, 1.4) | ~~[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| DOOM Eternal | `0100B1A00D8CE000` | `B059C2C77AD834B8` ([✅](SaltySD/plugins/FPSLocker/patches/0100B1A00D8CE000/B059C2C77AD834B8.yaml), v14, 1.14) <br> `B059C2C77AD834B8` ([✅](SaltySD/plugins/FPSLocker/patches/0100B1A00D8CE000/B059C2C77AD834B8.yaml), v15, 1.15) | ~~[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Double Dragon Revive | `01006AE02236C000` | `DBD5C9EC799E65A9` ([✅](SaltySD/plugins/FPSLocker/patches/01006AE02236C000/DBD5C9EC799E65A9.yaml), v1, N1.10) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Dragon Star VARNIR | `0100A8B014930000` | `E26A54F785A76EE7` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| 용의 별 바르니르 - Ecdysis of the dragon | `0100FB30148EC000` | `253470EA1AD22B4A` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| Dragon's Dogma: Dark Arisen | `010032C00AC58000` | `2CDB9B9D70010E88` ([✅](SaltySD/plugins/FPSLocker/patches/010032C00AC58000/2CDB9B9D70010E88.yaml), v1, 1.0.1) | ~~[🔐](#🔐)~~ |
| ドラゴンズドグマ：ダークアリズン | `010057E00AC56000` | `2D5B93C856CDF009` ([✅](SaltySD/plugins/FPSLocker/patches/010057E00AC56000/2D5B93C856CDF009.yaml), v1, 1.0.1) | ~~[🔐](#🔐)~~ |
| DRAGON BALL XENOVERSE 2 | `010078D000F88000` | `ACD8DFEFD0EA5316` ([✅](SaltySD/plugins/FPSLocker/patches/010078D000F88000/56405C9D6C8C0A6A.yaml), v31, 1.22.02) <br> `1B58983BDFAE165A` ([✅](SaltySD/plugins/FPSLocker/patches/010078D000F88000/1B58983BDFAE165A.yaml), v32, 1.23.00) <br> `8263E738648A23E3` ([✅](SaltySD/plugins/FPSLocker/patches/010078D000F88000/8263E738648A23E3.yaml), v33, 1.23.03) <br> `7640CE319C043D56` ([✅](SaltySD/plugins/FPSLocker/patches/010078D000F88000/7640CE319C043D56.yaml), v34, 1.24.00) <br> `82C912DDD4663022` ([✅](SaltySD/plugins/FPSLocker/patches/010078D000F88000/82C912DDD4663022.yaml), v35, 1.24.03) <br> `81E15238E2B6AABD` ([✅](SaltySD/plugins/FPSLocker/patches/010078D000F88000/81E15238E2B6AABD.yaml), v37, 1.25.01) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~[🌤️](#🌤️)[⚔️](#⚔️) |
| DRAGON BALL: Sparking! ZERO | `010035F022078000` | `7B53433FA04477FC` ([✅](SaltySD/plugins/FPSLocker/patches/010035F022078000/7B53433FA04477FC.yaml), v2, 2.0.73) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| DRAGON BALL Z: KAKAROT | `010051C0134F8000` | `20503FA77FA416B7` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/20503FA77FA416B7.yaml), v12, 1.50) <br> `389E38618E93A5E0` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/389E38618E93A5E0.yaml), v13, 1.51) <br> `72F6F8B54276185C` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/72F6F8B54276185C.yaml), v14, 1.52) <br> `BC99D4D0A9474360` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/BC99D4D0A9474360.yaml), v15, 1.60) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| 드래곤볼 Z 카카로트 | `0100FD70134FA000` | `4246AC9E465556D6` ([✅](SaltySD/plugins/FPSLocker/patches/0100FD70134FA000/4246AC9E465556D6.yaml), v15, 1.60) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| DRAGON QUEST I & II HD-2D Remake | `0100D7C01F254000` | `94B4FA4F36E01BE3` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7C01F254000/94B4FA4F36E01BE3.yaml), v1, 1.0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| DRAGON QUEST III HD-2D Remake | `01003E601E324000` | `6F49452BD0B343B1` ([✅](SaltySD/plugins/FPSLocker/patches/01003E601E324000/6F49452BD0B343B1.yaml), v1, 1.0.1) <br> `4F41309B39EEBE5E` ([✅](SaltySD/plugins/FPSLocker/patches/01003E601E324000/4F41309B39EEBE5E.yaml), v2, 1.1.0) <br> `A6BD61CFB142E663` ([✅](SaltySD/plugins/FPSLocker/patches/01003E601E324000/A6BD61CFB142E663.yaml), v4, 1.1.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| DRAGON QUEST MONSTERS: The Dark Prince | `0100A77018EA0000` | `99C5DEFFA2A401BA` (◯, v6, 1.0.6) |  |
| DRAGON QUEST XI S: Echoes of an Elusive Age | `01006C300E9F0000` | `1719AABFA5EAE42B` ([✅](SaltySD/plugins/FPSLocker/patches/01006C300E9F0000/1719AABFA5EAE42B.yaml), v4, 1.0.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| ドラゴンクエストXI　過ぎ去りし時を求めて S | `010054A0085CA000` | `325E49E94A030B7E` ([✅](SaltySD/plugins/FPSLocker/patches/010054A0085CA000/325E49E94A030B7E.yaml), v4, 1.0.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| DRAGON QUEST TREASURES | `010049B017774000` | `2F81A2EC9B298B37` ([✅](SaltySD/plugins/FPSLocker/patches/0100217014266000/2F81A2EC9B298B37.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| ドラゴンクエスト トレジャーズ | `0100217014266000` | `2F81A2EC9B298B37` ([✅](SaltySD/plugins/FPSLocker/patches/0100217014266000/2F81A2EC9B298B37.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| DreadOut Remastered Collection | `01000B202041A000` | `725731C74E4CA6A9` ([✅](SaltySD/plugins/FPSLocker/patches/01000B202041A000/725731C74E4CA6A9.yaml), v1, 1.0.2) | ~~[📏](#📏)~~ |
| DreadOut 2 | `010032B01C6F2000` | `FEEA420683820CD5` ([✅](SaltySD/plugins/FPSLocker/patches/010032B01C6F2000/FEEA420683820CD5.yaml), v6, 0.7) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Dredge | `01008CD0172D6000` | `B9CC2F4DE53D4F94` ([✅](SaltySD/plugins/FPSLocker/patches/01008CD0172D6000/B9CC2F4DE53D4F94.yaml), v8, 1.4.2) <br> `E711B99C30E041F7` ([✅](SaltySD/plugins/FPSLocker/patches/01008CD0172D6000/E711B99C30E041F7.yaml), v10, 1.5.1) <br> `2B1C8B24F6744644` ([✅](SaltySD/plugins/FPSLocker/patches/01008CD0172D6000/2B1C8B24F6744644.yaml), v11, 1.5.2) <br> `F716D367A6D7F5BA` ([✅](SaltySD/plugins/FPSLocker/patches/01008CD0172D6000/F716D367A6D7F5BA.yaml), v12, 1.5.3) | ~~[🛑](#🛑)~~ |
| Dusk Diver | `0100B2B00E7AA000` | `FAD1AF4EDC6DB267` ([✅](SaltySD/plugins/FPSLocker/patches/0100B2B00E7AA000/FAD1AF4EDC6DB267.yaml), v6, 1.0.6) | ~~[🔐](#🔐)[🔧](#🔧)~~[📏](#📏) |
| Dusk Diver 2 | `01003980174BC000` | `217C9ECF258C0312` ([✅](SaltySD/plugins/FPSLocker/patches/01003980174BC000/217C9ECF258C0312.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| DYNASTY WARRIORS 9 Empires | `010095D012E5E000` | `929D9160BA57A570` ([✅](SaltySD/plugins/FPSLocker/patches/010095D012E5E000/929D9160BA57A570.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[⏱️](#⏱️)~~ |
| 真・三國無双８ Empires | `01002B9012E28000` | `6C3F685C62070885` ([✅](SaltySD/plugins/FPSLocker/patches/01002B9012E28000/6C3F685C62070885.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[⏱️](#⏱️)~~ |
| Dying Light | `01008C8012920000` | `8C93B930348C9787` ([✅](SaltySD/plugins/FPSLocker/patches/01008C8012920000/8C93B930348C9787.yaml), v5, 1.0.5) | ~~[📏](#📏)~~ |
| EA SPORTS FC 24 | `0100BDB01A0E6000` | `217A5C011269C81E` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/217A5C011269C81E.yaml), v24, 1.5a.9115) | ~~[🔐](#🔐)~~[📏](#📏) |
| EA SPORTS FC 25 | `010054E01D878000` | `39296BB1FD4A3F20` ([✅](SaltySD/plugins/FPSLocker/patches/010054E01D878000/39296BB1FD4A3F20.yaml), v26, 1.7e.e73a) | ~~[🔐](#🔐)~~[📏](#📏) |
| EA SPORTS FC 26 | `01004FF021942000` | `5D738626CE19A40F` ([✅](SaltySD/plugins/FPSLocker/patches/01004FF021942000/5D738626CE19A40F.yaml), v4, 1.80.11a0) <br> `DF48D885EB914AC7` ([✅](SaltySD/plugins/FPSLocker/patches/01004FF021942000/DF48D885EB914AC7.yaml), v5, 1.80.43d0) <br> `4EAC4BED64458C8C` ([✅](SaltySD/plugins/FPSLocker/patches/01004FF021942000/4EAC4BED64458C8C.yaml), v6, 1.80.73bf) <br> `EBFF3A6C8EA30490` ([✅](SaltySD/plugins/FPSLocker/patches/01004FF021942000/EBFF3A6C8EA30490.yaml), v8, 1.81.fdc) | ~~[🔐](#🔐)~~[📏](#📏) |
| Earthfall: Alien Horde | `0100DFC00E472000` | `448C08A9533F3CAD` ([✅](SaltySD/plugins/FPSLocker/patches/0100DFC00E472000/448C08A9533F3CAD.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ |
| EarthX | `010069001B820000` | `1F9EA163A82C7D8F` (◯, v2, 1.0.2) |  |
| Easy Come Easy Golf | `0100ECF01800C000` | `7175D9FAE2F8F48B` (◯, v7, 1.9.11) |  |
| Echo Generation | `01007BC018C1C000` | `5C6DC047D93B270B` (◯, v1, 1.0.1) |  |
| Eiyuden Chronicle: Rising | `010039B015CB6000` | `39DC785D9073C22B` ([✅](SaltySD/plugins/FPSLocker/patches/010039B015CB6000/39DC785D9073C22B.yaml), v2, 1.02) | ~~[📏](#📏)~~ |
| Embr | `0100CC6013432000` | `473D222EB1BDAD47` (◯, v6, 1.0.6) |  |
| Endless Ocean Luminous | `010067B017588000` | `E5EFB5ABA3601B97` ([✅](SaltySD/plugins/FPSLocker/patches/010067B017588000/E5EFB5ABA3601B97.yaml), v1, 1.0.1) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Endling | `0100E9400FE34000` | `33DBE39C8A83F1E6` ([✅](SaltySD/plugins/FPSLocker/patches/0100E9400FE34000/33DBE39C8A83F1E6.yaml), v3, 1.3.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Eternights | `010018F01E0A0000` | `1AA4FD0FCA644CD3` (◯, v2, 1.0.2) |  |
| Europa | `0100C8E01DD16000` | `3F2E96A4396944A1` ([✅](SaltySD/plugins/FPSLocker/patches/0100C8E01DD16000/3F2E96A4396944A1.yaml), v4, 1.4.0) | ~~[🔧](#🔧)~~ |
| Everdream Valley | `0100B9801AA3C000` | `9860ED8101DC731B` (◯, v11, 1.0.11) |  |
| Everspace | `0100DCF0093EC000` | `71873FEB4648FA39` ([✅](SaltySD/plugins/FPSLocker/patches/0100DCF0093EC000/71873FEB4648FA39.yaml), v5, 1.0.5) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Everything | `010031F00B246000` | `646BFBEE3CD99F4A` (◯, v1, 1.0.1) |  |
| Exhausted Man | `010017D01F5E6000` | `5FB21A8A4819801C` (◯, v6, 1.0.6) |  |
| Expeditions: A Mudrunner Game | `01002C101C1AA000` | `9ACB108D8DC59245` ([✅](SaltySD/plugins/FPSLocker/patches/01002C101C1AA000/9ACB108D8DC59245.yaml), v18, 1.18.0.0) <br> `0F7616E6F5EE08CE` ([✅](SaltySD/plugins/FPSLocker/patches/01002C101C1AA000/0F7616E6F5EE08CE.yaml), v19, 1.19.0.0) | ~~[📏](#📏)~~ |
| F1 Manager 2024 | `010072E01CE0E000` | `85F60F87D19B5270` ([✅](SaltySD/plugins/FPSLocker/patches/010072E01CE0E000/85F60F87D19B5270.yaml), v11, 1.11) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Fading Afternoon | `01004E601E168000` | `B7D2694AEFBF2AFE` (❌, v3, 1.3.0) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| Fairy Tail 2 | `0100B9801F872000` | `007EA5E2E2541C6F` ([✅](SaltySD/plugins/FPSLocker/patches/0100B9801F872000/007EA5E2E2541C6F.yaml), v8, 1.4.2) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Family Feud | `010060200FC44000` | `45EDF909AE2A3A41` (◯, v2, 1.1) |  |
| FANTASY LIFE i: The Girl Who Steals Time | `0100755017EE0000` | `A697413E1DA7851A` ([✅](SaltySD/plugins/FPSLocker/patches/0100755017EE0000/A697413E1DA7851A.yaml), v2, 1.1.0) <br> `66BC954F5323014C` ([✅](SaltySD/plugins/FPSLocker/patches/0100755017EE0000/66BC954F5323014C.yaml), v4, 1.2.1) <br> `9DBA6AA32721CAB9` ([✅](SaltySD/plugins/FPSLocker/patches/0100755017EE0000/9DBA6AA32721CAB9.yaml), v5, 1.3.0) <br> `546820C12D88850D` ([✅](SaltySD/plugins/FPSLocker/patches/0100755017EE0000/546820C12D88850D.yaml), v6, 1.3.3) <br> `061A7341077C0974` ([✅](SaltySD/plugins/FPSLocker/patches/0100755017EE0000/061A7341077C0974.yaml), v7, 1.4.0) <br> `74BCAC96835DB9AE` ([✅](SaltySD/plugins/FPSLocker/patches/0100755017EE0000/74BCAC96835DB9AE.yaml), v8, 1.5.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Farmagia | `01002C101E2C4000` | `32E79F7A83531FFC` (◯, v1, 1.0.1) |  |
| FAR: Changing Tides | `01008A0014A92000` | `7041BC78D64745A1` (◯, v2, 1.2.0) |  |
| FAR: Lone Sails | `010022700E7D6000` | `CE59C773211A1A49` (◯, v0, 1.0.0) <br> `8FD06AB8DA27EC40` (◯, v1, 1.3) |  |
| Farming Simulator 23 | `01001E3017A10000` | `17F37A56B17DD9CC` ([✅](SaltySD/plugins/FPSLocker/patches/01001E3017A10000/17F37A56B17DD9CC.yaml), v7, 1.7.0.0) | ~~[🔐](#🔐)~~ |
| Fashion Dreamer | `0100E99019B3A000` | `628BE46730A3B09D` (◯, v7, 1.5.1) |  |
| F.I.S.T.: Forged in Shadow Torch | `01009F8017F48000` | `69EE5F71F187EAA9` ([✅](SaltySD/plugins/FPSLocker/patches/01009F8017F48000/69EE5F71F187EAA9.yaml), v4, 1.0.4) | ~~[📏](#📏)~~ |
| 零 ～濡鴉ノ巫女～ | `010082F015576000` | `8BFBF5B8A7098443` ([✅](SaltySD/plugins/FPSLocker/patches/010082F015576000/8BFBF5B8A7098443.yaml), v5, 1.0.5) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| FATAL FRAME: MAIDEN OF BLACK WATER | `0100BEB015604000` | `B38D51E0391187EC` ([✅](SaltySD/plugins/FPSLocker/patches/0100BEB015604000/B38D51E0391187EC.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Fate/EXTELLA | `010053E002EA2000` | `76EC789B99A25BA5` ([✅](SaltySD/plugins/FPSLocker/patches/010053E002EA2000/76EC789B99A25BA5.yaml), v0, 1.0.0) | ~~[⚔️](#⚔️)~~ |
| Fate/EXTELLA LINK | `01001A700C832000` | `97FC79E063E26C9B` ([✅](SaltySD/plugins/FPSLocker/patches/01001A700C832000/97FC79E063E26C9B.yaml), v2, 1.0.2) | ~~[⚔️](#⚔️)~~ |
| Fate/Samurai Remnant | `01003AE01AA76000` | `85D00BDAADD369E6` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/85D00BDAADD369E6.yaml), v10, 1.2.1) <br> `8D6606B544CBCBC8` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/8D6606B544CBCBC8.yaml), v12, 1.3.1) <br> `6C46135714ABB870` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/6C46135714ABB870.yaml), v13, 1.3.2) | ~~[🔐](#🔐)[⚔️](#⚔️)~~ |
| Fe | `0100D2600736A000` | `4FF8F56B697A0949` (◯, v0, 1.0.0) |  |
| FINAL FANTASY CRYSTAL CHRONICLES `US` | `0100CE4010AAC000` | `E1D8B399B787AE41` (❌, v3, 1.0.3) | [⏱️](#⏱️)[🖥️](#🖥️) |
| FINAL FANTASY CRYSTAL CHRONICLES | `0100BE0010AAE000` | `4C3D7BA90267A44F` (❌, v3, 1.0.3) | [⏱️](#⏱️)[🖥️](#🖥️) |
| FINAL FANTASY VIII Remastered | `01008B900DC0A000` | `7F59549F6E792936` (❌, v3, 1.0.1_5) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢) |
| FINAL FANTASY XII THE ZODIAC AGE | `0100EB100AB42000` | `C2932C4D1C84ED7D` (❌, v1, 1.1.0) | [⏱️](#⏱️)[🖥️](#🖥️)[🛑](#🛑) |
| Fire Emblem Engage | `0100A6301214E000` | `8C08B9719E085F91` ([✅](SaltySD/plugins/FPSLocker/patches/0100A6301214E000/8C08B9719E085F91.yaml), v5, 2.0.0) | ~~[⏱️](#⏱️)[🏃](#🏃)[🖥️](#🖥️)~~ |
| Fire Emblem: Three Houses | `010055D009F78000` | `89048449BA238C8C` ([✅](SaltySD/plugins/FPSLocker/patches/010055D009F78000/89048449BA238C8C.yaml), v5, 1.2.0) | ~~[📏](#📏)~~ |
| Fire Emblem Warriors | `0100F15003E64000` | `1953770037ACC52A` ([✅](SaltySD/plugins/FPSLocker/patches/0100F15003E64000/1953770037ACC52A.yaml), v5, 1.5.0) | ~~[🔐](#🔐)~~[📏](#📏) |
| Firewatch | `0100AC300919A000` | `C0D5723A48563E40` (◯, v0, 1.0.0) |  |
| Fishing: North Atlantic | `0100A55019C38000` | `B9DB6040F70BE58F` ([✅](SaltySD/plugins/FPSLocker/patches/0100A55019C38000/B9DB6040F70BE58F.yaml), v1, 1.1) | ~~[📏](#📏)~~ |
| Five Nights at Freddy's: Help Wanted | `0100F7901118C000` | `668FE05AA1AAC5A1` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7901118C000/668FE05AA1AAC5A1.yaml), v4, 1.25) | ~~[🔧](#🔧)~~ |
| Five Nights at Freddy's: Help Wanted 2 | `010032F01F7CC000` | `F7EB23F0D8E5A933` ([✅](SaltySD/plugins/FPSLocker/patches/010032F01F7CC000/F7EB23F0D8E5A933.yaml), v1, 0.2) <br> `DE7B50B9FEF89856` ([✅](SaltySD/plugins/FPSLocker/patches/010032F01F7CC000/DE7B50B9FEF89856.yaml), v2, 0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Five Nights at Freddy's: Security Breach | `01009060193C4000` | `B880EEE5B8946289` ([✅](SaltySD/plugins/FPSLocker/patches/01009060193C4000/B880EEE5B8946289.yaml), v4, 0.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Flooded | `010022201D254000` | `AF274CB758733A56` (❌, v1, 1.0.1) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| Forgive Me Father | `0100A2A01A026000` | `008F995D1A63B383` ([✅](SaltySD/plugins/FPSLocker/patches/0100A2A01A026000/008F995D1A63B383.yaml), v2, 1.5.4.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Formula Legends | `0100690020FBE000` | `CC93EA5C0A2F96FE` ([✅](SaltySD/plugins/FPSLocker/patches/0100690020FBE000/CC93EA5C0A2F96FE.yaml), v3, 1.0.3) <br> `8FDB10262446CB3D` ([✅](SaltySD/plugins/FPSLocker/patches/0100690020FBE000/8FDB10262446CB3D.yaml), v4, 1.0.4) <br> `2735E564A9BD3DA3` ([✅](SaltySD/plugins/FPSLocker/patches/0100690020FBE000/2735E564A9BD3DA3.yaml), v5, 1.0.5) <br> `84C1B1AE29550FC8` ([✅](SaltySD/plugins/FPSLocker/patches/0100690020FBE000/84C1B1AE29550FC8.yaml), v6, 1.0.6) <br> `349E9751D50B3B88` ([✅](SaltySD/plugins/FPSLocker/patches/0100690020FBE000/349E9751D50B3B88.yaml), v7, 1.0.7) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Forrader Hero | `01007C801D5B8000` | `D62574E9298D0AAE` (◯, v0, 1.0) |  |
| FREEDOM WARS | `010075201F578000` | `03AF225D1FE74673` (❌, v9, 1.9.0) | [🔐](#🔐)[⚔️](#⚔️)[👄](#👄)[🖥️](#🖥️)[🏃](#🏃) |
| Fresh Start | `0100AA001BAB8000` | `9B2BC4BAF72D350A` (❌, v0, 1.0.0) | [⚔️](#⚔️) |
| FROGUN DELUXE EDITION | `0100A0A018D3A000` | `7FA5168E6BEA2A40` (◯, v3, 1.3) |  |
| From Space | `010015F018C3C000` | `9806FB67CE24E904` ([✅](SaltySD/plugins/FPSLocker/patches/010015F018C3C000/9806FB67CE24E904.yaml), v3, 1.3.480) | ~~[📏](#📏)~~ |
| FRONT MISSION 1st: Remake | `0100F200178F4000` | `B3A54521BC08F453` (◯, v7, 3.0.1) |  |
| FRONT MISSION 2: Remake | `0100C4E018A24000` | `3FCC3A10C4B34E4A` (◯, v11, 1.0.9) |  |
| FRONT MISSION 3: Remake | `01007E6019872000` | `4885240A66A487A1` (◯, v3, 1.0.3) |  |
| Fueled Up | `010022A01E1F0000` | `F0F6265AEBF4AE2C` (◯, v0, 1.0.0) |  |
| Funko Fusion | `010058F01DF8C000` | `E6B427227FED8411` ([✅](SaltySD/plugins/FPSLocker/patches/010058F01DF8C000/E6B427227FED8411.yaml), v1, 2.3.0)<br> `F0787926C4CFF8F1` ([✅](SaltySD/plugins/FPSLocker/patches/010058F01DF8C000/F0787926C4CFF8F1.yaml), v2, 2.4.0) <br> `BDB53001D5CAD0AE` ([✅](SaltySD/plugins/FPSLocker/patches/010058F01DF8C000/BDB53001D5CAD0AE.yaml), v3, 2.6.2) <br> `F5E599C889DF733A` ([✅](SaltySD/plugins/FPSLocker/patches/010058F01DF8C000/F5E599C889DF733A.yaml), v4, 3.1.1) <br> `1670D126B5E8EE66` ([✅](SaltySD/plugins/FPSLocker/patches/010058F01DF8C000/1670D126B5E8EE66.yaml), v5, 3.3.0) <br> `4CD22960CFB56AB4` ([✅](SaltySD/plugins/FPSLocker/patches/010058F01DF8C000/4CD22960CFB56AB4.yaml), v7, 3.4.1) | ~~[📏](#📏)[🔧](#🔧)~~ | 
| FUSER | `0100E1F013674000` | `E9B47349177722BE` ([✅](SaltySD/plugins/FPSLocker/patches/0100E1F013674000/E9B47349177722BE.yaml), v6, 1.4.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Gal*Gun Returns | `0100047013378000` | `7E65E5BC3564BE46` ([✅](SaltySD/plugins/FPSLocker/patches/0100047013378000/7E65E5BC3564BE46.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[👄](#👄)[🖥️](#🖥️)~~[⚔️](#⚔️) |
| Gal*Gun: Double Peace | `01006FE016FB2000` | `191B397CA0310A18` ([✅](SaltySD/plugins/FPSLocker/patches/01006FE016FB2000/191B397CA0310A18.yaml), v2, 1.0.2) | ~~[🔐](#🔐)~~[⚔️](#⚔️) |
| ぎゃる☆がん２ | `0100803005D52000` | `62B7F19804BCB70E` ([✅](SaltySD/plugins/FPSLocker/patches/0100803005D52000/62B7F19804BCB70E.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Gal*Gun 2 | `010024700901A000` | `9CDFB0CD24CAE030` ([✅](SaltySD/plugins/FPSLocker/patches/010024700901A000/9CDFB0CD24CAE030.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Gamedec - Definitive Edition | `01002A501869E000` | `BFA92380757EF97D` ([✅](SaltySD/plugins/FPSLocker/patches/01002A501869E000/BFA92380757EF97D.yaml), v3, 1.3.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Garden Witch Life | `0100B6C01CDA0000` | `01660DB6F4D0FA81` ([✅](SaltySD/plugins/FPSLocker/patches/0100B6C01CDA0000/01660DB6F4D0FA81.yaml), v3, 1.0.3) <br> `CFC1C6A56575F83A` ([✅](SaltySD/plugins/FPSLocker/patches/0100B6C01CDA0000/CFC1C6A56575F83A.yaml), v4, 1.0.4) <br> `13824B290C931FE5` ([✅](SaltySD/plugins/FPSLocker/patches/0100B6C01CDA0000/13824B290C931FE5.yaml), v5, 1.0.5) | ~~[🔧](#🔧)~~ |
| Garfield Kart Furious Racing | `010061E00E8BE000` | `4A67AFB9EAC0DF44` (◯, v3, 1.0.3) |  |
| Gear.Club Unlimited | `010065E003FD8000` | `CD94FCB8CC23B24A` (◯, v2, 1.2.0) |  |
| Gear.Club Unlimited 2 | `010072900AFF0000` | `FE757810B45C3444` ([✅](SaltySD/plugins/FPSLocker/patches/010072900AFF0000/FE757B10B45C3444.yaml), v14, 1.7.2) | ~~[🔐](#🔐)[📏](#📏)[🌤️](#🌤️)~~ |
| GetsuFumaDen: Undying Moon | `010042A013DB8000` | `8683E654CCD68852` (❌📌, v2, 1.1.1) | [📏](#📏) |
| Ghostbusters: Spirits Unleashed Ecto Edition | `01005D2016934000` | `579CCC60D8E3DAF1` ([✅](SaltySD/plugins/FPSLocker/patches/01005D2016934000/579CCC60D8E3DAF1.yaml), v5, 1.8.0) <br> `4D6E50FF58BF7486` ([✅](SaltySD/plugins/FPSLocker/patches/01005D2016934000/4D6E50FF58BF7486.yaml), v6, 1.9.0) <br> `090A100AA49CE00F` ([✅](SaltySD/plugins/FPSLocker/patches/01005D2016934000/090A100AA49CE00F.yaml), v7, 1.10.0) <br> `49F6F257348A42A1` ([✅](SaltySD/plugins/FPSLocker/patches/01005D2016934000/49F6F257348A42A1.yaml), v8, 1.11.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Ghostbusters: The Video Game Remastered | `0100EAE00D9EC000` | `0FE6747D03EBA4E3` ([✅](SaltySD/plugins/FPSLocker/patches/0100EAE00D9EC000/0FE6747D03EBA4E3.yaml), v2, 1.2) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Ghostrunner | `010090F012916000` | `D3DD5B220DCEB626` ([✅](SaltySD/plugins/FPSLocker/patches/010090F012916000/D3DD5B220DCEB626.yaml), v8, 1.8) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Gigantosaurus The Game | `01002C400E526000` | `1FF442C5ABEB0459` ([✅](SaltySD/plugins/FPSLocker/patches/01002C400E526000/1FF442C5ABEB0459.yaml), v2, 1.0.2) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Gigantosaurus: Dino Kart | `01001890167FE000` | `5F7A2866D8E20BBA` ([✅](SaltySD/plugins/FPSLocker/patches/01001890167FE000/5F7A2866D8E20BBA.yaml), v0, 1.0.0) <br> `512FB8C2D12C4F36` ([✅](SaltySD/plugins/FPSLocker/patches/01001890167FE000/512FB8C2D12C4F36.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| GO VACATION | `0100C1800A9B6000` | `174471C5192F8647` (❌, v0, 1.0.0) | [⚔️](#⚔️) |
| Goat Simulator 3 | `01001CC01B2D4000` | `0DE3020411F4232B` ([✅](SaltySD/plugins/FPSLocker/patches/01001CC01B2D4000/0DE3020411F4232B.yaml), v1, 1.0.7.1) <br> `26AB1CB54DD4508D` ([✅](SaltySD/plugins/FPSLocker/patches/01001CC01B2D4000/26AB1CB54DD4508D.yaml), v3, 1.0.7.3) <br> `A5DA93E6537350D8` ([✅](SaltySD/plugins/FPSLocker/patches/01001CC01B2D4000/A5DA93E6537350D8.yaml), v4, 1.0.7.4) <br> `C606C7DC1C0EC88F` ([✅](SaltySD/plugins/FPSLocker/patches/01001CC01B2D4000/C606C7DC1C0EC88F.yaml), v5, 1.0.7.5) <br> `8D4FD57DB7D63120` ([✅](SaltySD/plugins/FPSLocker/patches/01001CC01B2D4000/8D4FD57DB7D63120.yaml), v6, 1.0.7.6) <br> `504EBEAB62E802AD` ([✅](SaltySD/plugins/FPSLocker/patches/01001CC01B2D4000/504EBEAB62E802AD.yaml), v7, 1.0.7.7) <br> `A45BCB8A63C50DC8` ([✅](SaltySD/plugins/FPSLocker/patches/01001CC01B2D4000/A45BCB8A63C50DC8.yaml), v8, 1.0.7.8) | ~~[📏](#📏)[🔧](#🔧)~~ |
| GOD EATER 3 | `01001C700873E000` | `C0F144F5139F542E` ([✅](SaltySD/plugins/FPSLocker/patches/01001C700873E000/C0F144F5139F542E.yaml), v11, 2.5.1) | ~~[⚔️](#⚔️)~~ |
| GOD WARS The Complete Legend | `0100F3D00B032000` | `3A0835D09F6D1544` (❌, v1, 1.1) | [🏃](#🏃) |
| Gods Will Fall | `0100CFA0111C8000` | `2C22089ABC14264F` (◯, v4, 1.0.4) |  |
| Going Under | `01004D501113C000` | `3AC30B12FEAD3149` (◯, v4, 1.0.4) |  |
| Golazo 2 | `0100997014004000` | `8057D5A82615847E` (◯, v2, 1.2.3) |  |
| Good Job! | `0100B0500FE4E000` | `951D09EECE122A47` ([✅](SaltySD/plugins/FPSLocker/patches/0100B0500FE4E000/951D09EECE122A47.yaml), v0, 1.0.0) | ~~[🛑](#🛑)~~ |
| Gori: Cuddly Carnage | `010000A017F96000` | `EEE598377C0A5966` ([✅](SaltySD/plugins/FPSLocker/patches/010000A017F96000/EEE598377C0A5966.yaml), v5, 1.0.5) <br> `1146A5AA87A93969` ([✅](SaltySD/plugins/FPSLocker/patches/010000A017F96000/1146A5AA87A93969.yaml), v6, 1.0.6) <br> `A21FFE97D09DCE4E` ([✅](SaltySD/plugins/FPSLocker/patches/010000A017F96000/A21FFE97D09DCE4E.yaml), v7, 1.0.7) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Grand Theft Auto III | `0100C3C012718000` | `2CF52C8DA4468946` ([✅](SaltySD/plugins/FPSLocker/patches/0100C3C012718000/2CF52C8DA4468946.yaml), v7, 1.0.7) <br> `BB2DDA80E83D0B2F` ([✅](SaltySD/plugins/FPSLocker/patches/0100C3C012718000/BB2DDA80E83D0B2F.yaml), v8, 1.0.8) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Grand Theft Auto: San Andreas | `010065A014024000` | `6FB56071CCB321B6` ([✅](SaltySD/plugins/FPSLocker/patches/010065A014024000/6FB56071CCB321B6.yaml), v7, 1.0.7) <br> `B898981D361D0201` ([✅](SaltySD/plugins/FPSLocker/patches/010065A014024000/B898981D361D0201.yaml), v8, 1.0.8) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Grand Theft Auto: Vice City | `0100182014022000` | `56EEFA704373BDB3` ([✅](SaltySD/plugins/FPSLocker/patches/0100182014022000/56EEFA704373BDB3.yaml), v7, 1.0.7) <br> `9151E53EE514B03A` ([✅](SaltySD/plugins/FPSLocker/patches/0100182014022000/9151E53EE514B03A.yaml), v8, 1.0.8) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Graveyard Keeper | `0100B6800B5C8000` | `9356531EDD2EC448` (◯, v6, 1.0.0.4633) |  |
| Gray Dawn | `0100A5700C0B2000` | `BA74A217AF6DCB32` (◯, v0, 1.0.0) |  |
| Green Hell | `0100453012FEA000` | `D3A8F87E96C94045` (◯, v2, 2.0) |  |
| GRID Autosport | `0100DC800A602000` | `347A44223C9537A5` (◯, v10, 1.10.1_70328) |  |
| GRIME | `0100F300169B6000` | `326AC32516E23370` (◯, v7, 1.3.9) |  |
| GRIP | `0100459009A2A000` | `ACF717E72EA920C2` ([✅](SaltySD/plugins/FPSLocker/patches/0100459009A2A000/ACF717E72EA920C2.yaml), v8, 1.0.8) | ~~[⚔️](#⚔️)[🔧](#🔧)~~ |
| Gripper | `010099C01896C000` | `60B9AE6094566A23` ([✅](SaltySD/plugins/FPSLocker/patches/010099C01896C000/60B9AE6094566A23.yaml), v2, 1.1.0) | ~~[🔧](#🔧)~~ |
| Grounded | `01006F301AE9C000` | `6C91A8A476E70C5D` ([✅](SaltySD/plugins/FPSLocker/patches/01006F301AE9C000/6C91A8A476E70C5D.yaml), v5, 1.05) <br> `97D2B53D2C0B35EA` ([✅](SaltySD/plugins/FPSLocker/patches/01006F301AE9C000/97D2B53D2C0B35EA.yaml), v7, 1.07) <br> `E9A887A36762C526` ([✅](SaltySD/plugins/FPSLocker/patches/01006F301AE9C000/E9A887A36762C526.yaml), v8, 1.08) <br> `F5ECD5701434461C` ([✅](SaltySD/plugins/FPSLocker/patches/01006F301AE9C000/F5ECD5701434461C.yaml), v9, 1.09) <br> `F89171E031F95ADC` ([✅](SaltySD/plugins/FPSLocker/patches/01006F301AE9C000/F89171E031F95ADC.yaml), v11, 1.11) <br> `F50C38B64DE532F7` ([✅](SaltySD/plugins/FPSLocker/patches/01006F301AE9C000/F50C38B64DE532F7.yaml), v12, 1.12) <br> `B46B22D9AC7E567B` ([✅](SaltySD/plugins/FPSLocker/patches/01006F301AE9C000/B46B22D9AC7E567B.yaml), v13, 1.13) | ~~[🔐](#🔐)[📏](#📏)~~ |
| GUNDAM BREAKER 4 | `010025C0145D4000` | `0FCB7D1E6E4D1836` ([✅](SaltySD/plugins/FPSLocker/patches/010025C0145D4000/0FCB7D1E6E4D1836.yaml), v3, 1.3.0) <br> `F898CCE9C3A291AF` ([✅](SaltySD/plugins/FPSLocker/patches/010025C0145D4000/F898CCE9C3A291AF.yaml), v5, 1.5.0) <br> `EA4853C29547CBBC` ([✅](SaltySD/plugins/FPSLocker/patches/010025C0145D4000/EA4853C29547CBBC.yaml), v6, 1.6.0) <br> `0CC82881FF112C6D` ([✅](SaltySD/plugins/FPSLocker/patches/010025C0145D4000/0CC82881FF112C6D.yaml), v8, 1.9.0) <br> `6267E76E9540F2ED` ([✅](SaltySD/plugins/FPSLocker/patches/010025C0145D4000/6267E76E9540F2ED.yaml), v9, 1.10.0) <br> `E82F8A34CCC706E7` ([✅](SaltySD/plugins/FPSLocker/patches/010025C0145D4000/E82F8A34CCC706E7.yaml), v10, 1.11.0) <br> `0FF5CF27929E07F9` ([✅](SaltySD/plugins/FPSLocker/patches/010025C0145D4000/0FF5CF27929E07F9.yaml), v11, 1.12.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Gungrave G.O.R.E | `010088801B324000` | `9B743181AB8A26F9` ([✅](SaltySD/plugins/FPSLocker/patches/010088801B324000/9B743181AB8A26F9.yaml), v4, 1.0.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| GYLT | `0100AC601DCA8000` | `4584432786F462DB` ([✅](SaltySD/plugins/FPSLocker/patches/0100AC601DCA8000/4584432786F462DB.yaml), v2, 1.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Hammerwatch Anniversary Edition | `0100321017CC0000` | `D147CAEF2BC74574` ([✅](SaltySD/plugins/FPSLocker/patches/0100321017CC0000/D147CAEF2BC74574.yaml), v3, 1.0.3) | ~~[🔐](#🔐)~~ |
| Hammerwatch 2 | `0100367016DF0000` | `38896FEC1B4ADB1C` ([✅](SaltySD/plugins/FPSLocker/patches/0100367016DF0000/38896FEC1B4ADB1C.yaml), v3, 1.0.4) | ~~[🔐](#🔐)~~ |
| Hamster Playground | `010035901701A000` | `243C8F241C196CDA` (◯, v8, 1.0.8) |  |
| HARVESTELLA | `0100521017B2A000` | `249EAB9BF046C5EA` ([✅](SaltySD/plugins/FPSLocker/patches/0100521017B2A000/249EAB9BF046C5EA.yaml), v2, 1.0.2) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Hazel Sky | `0100A8A013AB2000` | `1EFB6879CFAD7DD3` ([✅](SaltySD/plugins/FPSLocker/patches/0100A8A013AB2000/1EFB6879CFAD7DD3.yaml), v7, 1.0.10f) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| HEAVEN SEEKER ――The Savior of This Cruel World | `0100EE00205BA000` | `E7011BF08747297B` ([✅](SaltySD/plugins/FPSLocker/patches/0100EE00205BA000/E7011BF08747297B.yaml), v1, 1.0.4.126) <br> `F2D03CFFB8DE5E4C` ([✅](SaltySD/plugins/FPSLocker/patches/0100EE00205BA000/F2D03CFFB8DE5E4C.yaml), v2, 1.0.4.127) <br> `21B3E4EA75F16551` ([✅](SaltySD/plugins/FPSLocker/patches/0100EE00205BA000/21B3E4EA75F16551.yaml), v3, 1.0.5.130) <br> `AA3EDDE660D630AD` ([✅](SaltySD/plugins/FPSLocker/patches/0100EE00205BA000/AA3EDDE660D630AD.yaml), v4, 1.0.5.134) <br> `135595BF76F46B1B` ([✅](SaltySD/plugins/FPSLocker/patches/0100EE00205BA000/135595BF76F46B1B.yaml), v5, 1.2.0.139) | ~~[🛑](#🛑)~~ |
| Hellblade: Senua's Sacrifice | `010044500CF8E000` | `9B3DDF2FB9100E51` ([✅](SaltySD/plugins/FPSLocker/patches/010044500CF8E000/9B3DDF2FB9100E51.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Hello Kitty Island Adventure | `010027901C89C000` | `B5DF7052EB2ED3DE` (◯, v9, 2.11.0) |  |
| Hellpoint | `010024600C794000` | `3776E7BBC7C01E43` ([✅](SaltySD/plugins/FPSLocker/patches/010024600C794000/3776E7BBC7C01E43.yaml), v3, 1.0.2.0) | ~~[📏](#📏)~~ |
| Hello Neighbor 2 | `0100EAF01527E000` | `AB75C103EEC0D5FC` ([✅](SaltySD/plugins/FPSLocker/patches/0100EAF01527E000/AB75C103EEC0D5FC.yaml), v1, 1.1) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Hero's Hour | `010005E01E5E6000` | `8B0C5F41A0CCDFD9` (❌, v2, 2.5.3) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| High On Life | `0100C1101EE5A000` | `950FB0C3D58D6A7B` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1101EE5A000/950FB0C3D58D6A7B.yaml), v5, 1.0.5) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Highwater | `0100D1A019EBA000` | `3A38653015036D51` (◯, v1, 1.0.1) |  |
| Hitman: Absolution | `010037C022390000` | `96B7F9BD973D298E` ([✅](SaltySD/plugins/FPSLocker/patches/010037C022390000/96B7F9BD973D298E.yaml), v0, 1.2.2RC1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Hitman: Blood Money - Reprisal | `010083A018262000` | `59AF76C13F680B7C` ([✅](SaltySD/plugins/FPSLocker/patches/010083A018262000/59AF76C13F680B7C.yaml), v1, 1.2_71586) | ~~[🔐](#🔐)~~ |
| Hoa | `010022E013A1A000` | `33C97D772C057EF9` (◯, v4, 1.0.4) |  |
| Hob: The Definitive Edition | `01004B100A5CC000` | `4E7978E35F9D7490` ([✅](SaltySD/plugins/FPSLocker/patches/01004B100A5CC000/4E7978E35F9D7490.yaml), v4, 1.1.3) | ~~[📏](#📏)~~ |
| Hogwarts Legacy | `0100F7E00C70E000` | `1C42BC734E792AFB` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7E00C70E000/1C42BC734E792AFB.yaml), v3, 1.0.3) <br> `2980E59C32A0E147` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7E00C70E000/2980E59C32A0E147.yaml), v4, 1.0.4) <br> `0C00FC37B0610FBD` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7E00C70E000/0C00FC37B0610FBD.yaml), v5, 1.0.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Hokko Life | `010022A016250000` | `D9D13603133F3D89` (◯, v5, 1.0.5) |  |
| Hollow 2 | `01007DE016E9E000` | `6348715E851F18EE` ([✅](SaltySD/plugins/FPSLocker/patches/01007DE016E9E000/6348715E851F18EE.yaml), v0, 1.0.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Horizon Chase 2 | `0100001019F6E000` | `F80EEC237D0963EE` ([✅](SaltySD/plugins/FPSLocker/patches/0100001019F6E000/F80EEC237D0963EE.yaml), v6, 1.6.3) <br> `D60A7F43A98034BE` ([✅](SaltySD/plugins/FPSLocker/patches/0100001019F6E000/D60A7F43A98034BE.yaml), v7, 1.6.6) <br> `E13F632FC2A66EEB` ([✅](SaltySD/plugins/FPSLocker/patches/0100001019F6E000/E13F632FC2A66EEB.yaml), v8, 1.6.9) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Hot Lap Racing | `010059301E612000` | `8E8C96D9B3FD9D83` (◯, v6, 1.1.3) |  |
| Hot Wheels Monster Trucks: Stunt Mayhem | `010055D01C8D4000` | `444303671674DD91` ([✅](SaltySD/plugins/FPSLocker/patches/010055D01C8D4000/444303671674DD91.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| HOT WHEELS UNLEASHED | `0100AA60136D2000` | `F73C6504D378C38B` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA60136D2000/F73C6504D378C38B.yaml), v13, 1.0.13) <br> `A7F32A28D882D046` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA60136D2000/A7F32A28D882D046.yaml), v14, 1.0.14) | ~~[📏](#📏)[🔧](#🔧)~~ |
| HOT WHEELS UNLEASHED 2 | `01001BE01908C000` | `C95F34910CE1CDC0` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/C95F34910CE1CDC0.yaml), v9, 1.0.9) <br> `E1F81DC590FDE0B5` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/E1F81DC590FDE0B5.yaml), v10, 1.0.10) <br> `FE78C7B94C4E791A` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/FE78C7B94C4E791A.yaml), v11, 1.0.11) | ~~[📏](#📏)[🔧](#🔧)~~ |
| House Flipper | `0100CAE00EB02000` | `0764284443A86245` (◯, v11, 1.11.0) |  |
| HYKE:Northern Light(s) | `0100EF401D9B2000` | `35FAA72E03DDE0D1` ([✅](SaltySD/plugins/FPSLocker/patches/0100EF401D9B2000/35FAA72E03DDE0D1.yaml), v0, 1.0.0) <br> `2F723E9FD78D184B` ([✅](SaltySD/plugins/FPSLocker/patches/0100EF401D9B2000/2F723E9FD78D184B.yaml), v1, 1.0.1) <br> `2F723E9FD78D184B` ([✅](SaltySD/plugins/FPSLocker/patches/0100EF401D9B2000/2F723E9FD78D184B.yaml), v2, 1.0.2) <br> `9BD042D73D2FC2AE` ([✅](SaltySD/plugins/FPSLocker/patches/0100EF401D9B2000/9BD042D73D2FC2AE.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| HYPERCHARGE: Unboxed | `0100A8B00F0B4000` | `92511355705EA8C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100A8B00F0B4000/92511355705EA8C5.yaml), v5, 0.1.2341.233) | ~~[📏](#📏)~~ |
| Hyrule Warriors: Age of Calamity | `01002B00111A2000` | `C3CF52BF2B05D731` ([✅](SaltySD/plugins/FPSLocker/patches/01002B00111A2000/C3CF52BF2B05D731.yaml), v5, 1.3.0) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~[📺](#📺) |
| I Am Setsuna. | `0100849000BDA000` | `0BBA2167AED893BE` (◯, v1, 1.1.0) |  |
| Imagine Earth | `0100E2701A3D8000` | `77BF3F116454337D` (◯, v4, 1.20.6.6770) |  |
| Immortal Redneck | `01000F400435A000` | `DB367E57EDA9E84F` (◯, v1, 1.3.5) |  |
| Immortals Fenyx Rising | `01004A600EC0A000` | `70F3F6751D73C644` (❌, v11, 1.3.4) | [📏](#📏) |
| In rays of the Light | `0100A760129A0000` | `AB4C861FD0C87F47` (◯, v2, 1.0.2) |  |
| In Sound Mind | `01006DF014682000` | `5FCC5A8EDF6244C4` (❌📌, v4, 1.0.4) | [📏](#📏) |
| INAZUMA ELEVEN: Victory Road | `0100B36008F90000` | `09AD6947189FC6D9` ([✅](SaltySD/plugins/FPSLocker/patches/0100B36008F90000/09AD6947189FC6D9.yaml), v4, 1.2.0) <br> `F9648F3865C8B1AE` ([✅](SaltySD/plugins/FPSLocker/patches/0100B36008F90000/F9648F3865C8B1AE.yaml), v5, 1.3.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| INDIKA | `0100DE302439E000` | `C4E2284BFB7D534C` ([✅](SaltySD/plugins/FPSLocker/patches/0100DE302439E000/C4E2284BFB7D534C.yaml), v0, 1.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Inertial Drift | `01002BD00F626000` | `4C277E67AB50D547` (◯, v10, 1.2.1) |  |
| Infinity Strash: DRAGON QUEST The Adventure of Dai | `01006FA018D40000` | `DB7E474BEFABB6A0` (❌📌, v2, 1.0.2) | [📏](#📏)[🔧](#🔧) |
| INMOST | `0100F1401161E000` | `16CEFEA33FE6E24F` (❌📌, v6, 1.0.4.3) | [📏](#📏) |
| Inscryption | `010027F017B12000` | `036A768CDCDCD742` (◯, v3, 1.41.2) |  |
| Insomnis | `01001CF0190C2000` | `4C6727375D877B90` ([✅](SaltySD/plugins/FPSLocker/patches/01001CF0190C2000/4C6727375D877B90.yaml), v1, 1.01) | ~~[📏](#📏)~~ |
| Ironsmith: Medieval Simulator | `010025A01CD86000` | `D2A5A1FC6EEADF31` ([✅](SaltySD/plugins/FPSLocker/patches/010025A01CD86000/D2A5A1FC6EEADF31.yaml), v1, 1.1.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| It Takes Two | `010092A0172E4000` | `C4067E8CB3258656` ([✅](SaltySD/plugins/FPSLocker/patches/010092A0172E4000/C4067E8CB3258656.yaml), v2, 1.0.2) | ~~[📏](#📏)[⚔️](#⚔️)~~ |
| Jojo's Bizarre Adventure: All-Star Battle R | `010017A0128C4000` | `3D4E3A9252AA6C63` ([✅](SaltySD/plugins/FPSLocker/patches/010017A0128C4000/3D4E3A9252AA6C63.yaml), v16, 2.3.3) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Journey To The Savage Planet | `0100FB90103DE000` | `4BED8F28C0F34C86` ([✅](SaltySD/plugins/FPSLocker/patches/0100FB90103DE000/4BED8F28C0F34C86.yaml), v2, 01.02) | ~~[📏](#📏)[⚔️](#⚔️)~~ |
| 呪術廻戦 戦華双乱 | `01002FC012548000` | `2F33996FD9C81253` ([✅](SaltySD/plugins/FPSLocker/patches/01002FC012548000/2F33996FD9C81253.yaml), v4, 1.2.0) <br> `2E7487767D0CA0EE` ([✅](SaltySD/plugins/FPSLocker/patches/01002FC012548000/2E7487767D0CA0EE.yaml), v5, 1.3.0) <br> `7C724F497564C027` ([✅](SaltySD/plugins/FPSLocker/patches/01002FC012548000/7C724F497564C027.yaml), v6, 1.4.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Jujutsu Kaisen Cursed Clash `GLOBAL` | `010085401A454000` | `2F33996FD9C81253` ([✅](SaltySD/plugins/FPSLocker/patches/010085401A454000/2F33996FD9C81253.yaml), v4, 1.2.0) <br> `2E7487767D0CA0EE` ([✅](SaltySD/plugins/FPSLocker/patches/010085401A454000/2E7487767D0CA0EE.yaml), v5, 1.3.0) <br> `7C724F497564C027` ([✅](SaltySD/plugins/FPSLocker/patches/010085401A454000/7C724F497564C027.yaml), v6, 1.4.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Jujutsu Kaisen Cursed Clash `US` | `010000B01A452000` | `2F33996FD9C81253` ([✅](SaltySD/plugins/FPSLocker/patches/010000B01A452000/2F33996FD9C81253.yaml), v4, 1.2.0) <br> `2E7487767D0CA0EE` ([✅](SaltySD/plugins/FPSLocker/patches/010000B01A452000/2E7487767D0CA0EE.yaml), v5, 1.3.0) <br> `7C724F497564C027` ([✅](SaltySD/plugins/FPSLocker/patches/010000B01A452000/7C724F497564C027.yaml), v6, 1.4.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| JUMP FORCE `EUR` | `010019D010F0E000` | `E1F650BD480CB465` (❌, v7, 1.08) | [⏱️](#⏱️)[🖥️](#🖥️) |
| JUMP FORCE `US` | `0100183010F12000` | `1667568420912C73` (❌, v7, 1.08) | [⏱️](#⏱️)[🖥️](#🖥️) |
| KAMiBAKO - Mythology of Cube - | `01008B40212D2000` | `91925CB98ED597AB` (◯, v1, 1.1.1) |  |
| Kao the Kangaroo `GLOBAL` | `0100956016464000` | `F9C83728910E28A4` ([✅](SaltySD/plugins/FPSLocker/patches/0100956016464000/F9C83728910E28A4.yaml), v5, 1.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Kao the Kangaroo `US` | `010078C01769A000` | `7BA282E94D34C620` ([✅](SaltySD/plugins/FPSLocker/patches/010078C01769A000/7BA282E94D34C620.yaml), v5, 1.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Katamari Damacy REROLL | `0100D7000C2C6000` | `B528B17AD9C71F41` (❌, v2, 1.2) | [⏱️](#⏱️) |
| Kiki | `0100E2D01F290000` | `722D0E06169C2458` (◯, v0, 1.0.0) |  |
| King of Seas | `01008D80148C8000` | `BC82DB38671F8468` ([✅](SaltySD/plugins/FPSLocker/patches/01008D80148C8000/BC82DB38671F8468.yaml), v4, 1.0.4) | ~~[🔧](#🔧)~~ |
| Kingdom Come: Deliverance `GLOBAL` | `0100650018FE0000` | `7A450848CFDEC18E` ([✅](SaltySD/plugins/FPSLocker/patches/0100650018FE0000/7A450848CFDEC18E.yaml), v2, 1.9.6H) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Kingdom Come: Deliverance `JPN` | `010021601C496000` | `7A450848CFDEC18E` ([✅](SaltySD/plugins/FPSLocker/patches/010021601C496000/7A450848CFDEC18E.yaml), v2, 1.9.6H) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Kingdoms of Amalur: Re-Reckoning | `0100EF50132BE000` | `FA48B344ED72F24D` (◯, v7, 1.0.7) |  |
| Kirby and the Forgotten Land | `01004D300C5AE000` | `D9BA7DB72FFAFECD` ([✅](SaltySD/plugins/FPSLocker/patches/01004D300C5AE000/D9BA7DB72FFAFECD.yaml), v0, 1.0.0) <br> `A6CE40DC3AEDB1BE` ([✅](SaltySD/plugins/FPSLocker/patches/01004D300C5AE000/A6CE40DC3AEDB1BE.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~[⚔️](#⚔️) |
| Kirby Star Allies | `01007E3006DDA000` | `D55608916FA56C18` ([✅](SaltySD/plugins/FPSLocker/patches/01007E3006DDA000/D55608916FA56C18.yaml), v6, 4.0.0a) | ~~[🔐](#🔐)[⚔️](#⚔️)~~ |
| Kirby's Dream Buffet | `0100A8E016236000` | `82AF4E16BBC0BEC8` ([✅](SaltySD/plugins/FPSLocker/patches/0100A8E016236000/82AF4E16BBC0BEC8.yaml), v1, 1.0.0a) | ~~[🔐](#🔐)[⚔️](#⚔️)~~ |
| L.A. Noire | `0100830004FB6000` | `40F973CE3B5EC8D7` ([✅](SaltySD/plugins/FPSLocker/patches/0100830004FB6000/40F973CE3B5EC8D7.yaml), v2, 1.2) | ~~[⏱️](#⏱️)[🖥️](#🖥️)[🏃](#🏃)~~ |
| Labirynth Of The Demon King | `010071F0228CA000` | `DE26B43C3D21B3A3` ([✅](SaltySD/plugins/FPSLocker/patches/010071F0228CA000/DE26B43C3D21B3A3.yaml), v1, 1.81.) <br> `9BA2F2849F9D9FDF` ([✅](SaltySD/plugins/FPSLocker/patches/010071F0228CA000/9BA2F2849F9D9FDF.yaml), v2, 5.233.V1SEP3) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Laika: Aged Through Blood | `0100F15020292000` | `EE83530AAB8DD965` (◯, v0, 1.0.3.0) |  |
| Lara Croft and the Guardian of Light | `010079C017F5E002` | `BD5CD5189BC90093` ([✅](SaltySD/plugins/FPSLocker/patches/010079C017F5E002/BD5CD5189BC90093.yaml), v0, 1.1_65791) | ~~[📏](#📏)~~ |
| Lara Croft and the Temple of Osiris | `010079C017F5E001` | `F47C697C2B59443B` ([✅](SaltySD/plugins/FPSLocker/patches/010079C017F5E001/F47C697C2B59443B.yaml), v0, 1.1_65791) | ~~[🔐](#🔐)[📏](#📏)~~ |
| LEGO 2K Drive | `0100739018020000` | `B75E7D3DB78D69C1` ([✅](SaltySD/plugins/FPSLocker/patches/0100739018020000/B75E7D3DB78D69C1.yaml), v17, 1.17) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| LEGO City Undercover | `010085500130A000` | `32C590B064956546` ([✅](SaltySD/plugins/FPSLocker/patches/010085500130A000/32C590B064956546.yaml), v3, 1.0.3) | ~~[📺](#📺)~~ |
| LEGO DC Super-Villains | `010070D009FEC000` | `711C52FC37605D45` (◯, v8, 1.0.8) |  |
| LEGO Horizon Adventures | `010073C01AF34000` | `2D99FA4793E426C3` ([✅](SaltySD/plugins/FPSLocker/patches/010073C01AF34000/2D99FA4793E426C3.yaml), v1, 1.1.0) <br> `675538722EE1FACB` ([✅](SaltySD/plugins/FPSLocker/patches/010073C01AF34000/675538722EE1FACB.yaml), v2, 1.2.0) <br> `B3DFF885ABB66B5C` ([✅](SaltySD/plugins/FPSLocker/patches/010073C01AF34000/B3DFF885ABB66B5C.yaml), v3, 1.3.0) <br> `C6F56735E3837278` ([✅](SaltySD/plugins/FPSLocker/patches/010073C01AF34000/C6F56735E3837278.yaml), v4, 1.4.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| LEGO Jurassic World | `01001C100E772000` | `1B80403BE8882745` (◯, v1, 1.0.1) |  |
| LEGO MARVEL Super Heroes | `01006F600FFC8000` | `5D769ABCAD9F2743` (◯, v1, 1.0.1) |  |
| LEGO MARVEL Super Heroes 2 | `01007690040A0000` | `794534B11CF3BE40` (◯, v7, 1.0.7) |  |
| LEGO Party | `0100A760232D2000` | `C70A4E7B66BB6338` (◯, v2, 1.2.0) |  |
| LEGO Star Wars: The Skywalker Saga | `010042D00D900000` | `EC593A5F9552100A` ([✅](SaltySD/plugins/FPSLocker/patches/010042D00D900000/EC593A5F9552100A.yaml), v9, 1.10.0) | ~~[📏](#📏)~~ |
| LEGO The Incredibles | `0100F19006E04000` | `414D247F3FD8084E` (◯, v2, 1.0.2) |  |
| LEGO Worlds | `0100838002AEA000` | `8174C89125B5404E` (◯, v10, 1.3.2) |  |
| Life is Strange | `0100DC301186A000` | `EE295EAAEA7D31E4` ([✅](SaltySD/plugins/FPSLocker/patches/0100DC301186A000/EE295EAAEA7D31E4.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ |
| Life is Strange 2 | `0100FD101186C000` | `BF0088C59D7E97C0` ([✅](SaltySD/plugins/FPSLocker/patches/0100FD101186C000/BF0088C59D7E97C0.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Life is Strange: Double Exposure | `0100B2301F4A8000` | `C4DD7E5256163FF1` ([✅](SaltySD/plugins/FPSLocker/patches/0100B2301F4A8000/C4DD7E5256163FF1.yaml), v1, 1.0.1) <br> `FF8EFD0E0E71BB03` ([✅](SaltySD/plugins/FPSLocker/patches/0100B2301F4A8000/FF8EFD0E0E71BB03.yaml), v2, 1.0.2) <br> `BBEA8745A7893750` ([✅](SaltySD/plugins/FPSLocker/patches/0100B2301F4A8000/BBEA8745A7893750.yaml), v3, 1.0.3) | ~~[🔧](#🔧)~~ |
| Life is Strange: True Colors | `0100500012AB4000` | `118AA7B71E824B3B` ([✅](SaltySD/plugins/FPSLocker/patches/0100500012AB4000/118AA7B71E824B3B.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Little Big Adventure - Twinsen's Quest | `0100BB901FA12000` | `52802B73E6C71920` (◯, v4, 1.1.2) |  |
| Little Kitty, Big City | `01000A4019FA2000` | `D3276F6AA64F6DE0` (◯, v16, 1.25.10.07_5538) |  |
| Little Noah: Scion of Paradise | `0100535014D76000` | `8CCC67A5A75CB8E5` ([✅](SaltySD/plugins/FPSLocker/patches/0100535014D76000/8CCC67A5A75CB8E5.yaml), v7, 1.41) | ~~[📷](#📷)~~ |
| Little Nightmares II | `010097100EDD6000` | `7F4216B6E784A4B2` ([✅](SaltySD/plugins/FPSLocker/patches/010097100EDD6000/7F4216B6E784A4B2.yaml), v4, 1.4) | ~~[📏](#📏)~~ |
| Little Nightmares III | `010066101A55A000` | `338C569A607B7C30` ([✅](SaltySD/plugins/FPSLocker/patches/010066101A55A000/338C569A607B7C30.yaml), v1, 1.0.2) <br> `F3FFA17B5E56809F` ([✅](SaltySD/plugins/FPSLocker/patches/010066101A55A000/F3FFA17B5E56809F.yaml), v2, 1.0.3) <br> `911284C45A26DD34` ([✅](SaltySD/plugins/FPSLocker/patches/010066101A55A000/911284C45A26DD34.yaml), v3, 1.0.4) | ~~[🔧](#🔧)~~ |
| Little Town Hero | `01000FB00AA90000` | `2BE4AF8B1A137445` (❌, v2, 1.2.0) | [🏃](#🏃) |
| LIVE A LIVE | `0100CF801776C000` | `CF22083371DDACB2` (◯, v1, 1.0.1) |  |
| Loddlenaut | `010086501F826000` | `C000FD620D6A92F0` (◯, v3, 1.2.4) |  |
| Lost In Random | `01005FE01291A000` | `416914C121775277` (◯, v1, 1.0.1) |  |
| LOST SPHEAR | `010077B0038B2000` | `641A9243BA35C638` (◯, v5, 1.3.1) |  |
| Luigi's Mansion 2 HD | `010048701995E000` | `A71EC0B9FF4F54CB` (❌, v0, 1.0.0) | [⚔️](#⚔️) |
| Luigi's Mansion 3 | `0100DCA0064A6000` | `79E5950FFA85ACF6` ([✅](SaltySD/plugins/FPSLocker/patches/0100DCA0064A6000/79E5950FFA85ACF6.yaml), v5, 1.4.0) | ~~[🔐](#🔐)~~[📏](#📏) |
| Lynked: Banner of the Spark | `0100711022E24000` | `BCEB97447A39F9FE` ([✅](SaltySD/plugins/FPSLocker/patches/0100711022E24000/BCEB97447A39F9FE.yaml), v2, 1.2.0) <br> `15AFE82282E0EF30` ([✅](SaltySD/plugins/FPSLocker/patches/0100711022E24000/15AFE82282E0EF30.yaml), v3, 1.2.1) <br> `9646E1065A7E897B` ([✅](SaltySD/plugins/FPSLocker/patches/0100711022E24000/9646E1065A7E897B.yaml), v4, 1.2.2) <br> `98C2DD2B041D3CCC` ([✅](SaltySD/plugins/FPSLocker/patches/0100711022E24000/98C2DD2B041D3CCC.yaml), v5, 1.2.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Lysfanga: The Time Shift Warrior | `0100ED601B876000` | `3B47E57FD8B8EE7B` (◯, v2, 1.0.2) |  |
| Maglam Lord | `01002C0015644000` | `3A3C781930CB8201` ([✅](SaltySD/plugins/FPSLocker/patches/01002C0015644000/3A3C781930CB8201.yaml), v0, 1.00) | ~~[🔐](#🔐)[📏](#📏)~~[🏃](#🏃) |
| Maquette | `0100861018480000` | `B0F09EE3E404D549` (❌, v0, 1.0.0) | [⚔️](#⚔️) |
| Mandragora: Whispers of the Witch Tree `EUR` | `0100D1202322A000` | `89E4C9599C96D7DE` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1202322A000/89E4C9599C96D7DE.yaml), v1, 1.5.3.135819) <br> `E04F5D58727DDE13` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1202322A000/E04F5D58727DDE13.yaml), v2, 1.5.4.135908) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Mandragora：Whispers of the Witch Tree `JPN` | `0100B2002330E000` | `637F8C946F7C512D` ([✅](SaltySD/plugins/FPSLocker/patches/0100B2002330E000/637F8C946F7C512D.yaml), v1, 1.5.3.135819) <br> `AF42903B754D4859` ([✅](SaltySD/plugins/FPSLocker/patches/0100B2002330E000/AF42903B754D4859.yaml), v2, 1.5.4.135908) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Mario & Luigi: Brothership | `01006D0017F7A000` | `59874C9B530095AC` ([✅](SaltySD/plugins/FPSLocker/patches/01006D0017F7A000/59874C9B530095AC.yaml), v0, 1.0.0) <br> `BF0607AC795B593A` ([✅](SaltySD/plugins/FPSLocker/patches/01006D0017F7A000/BF0607AC795B593A.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Mario + Rabbids Kingdom Battle | `010067300059A000` | `3B39E0C06B8841F1` (◯, v9, 1.9.589692) |  |
| Mario + Rabbids Sparks of Hope | `0100317013770000` | `5B76A43B231E0640` (◯, v6, 1.6.2225577) |  |
| 마리오 + 래비드 반짝이는 희망 | `0100FC60185AE000` | `2545826CA04FC82C` (◯, v6, 1.6.2225577) |  |
| Made in Abyss: Binary Star Falling into Darkness | `01006080117C2000` | `DFC7E8979528DE44` ([✅](SaltySD/plugins/FPSLocker/patches/01006080117C2000/DFC7E8979528DE44.yaml), v3, 1.0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Majogami | `0100BEA0244FC000` | `9FD75204E7C17463` ([✅](SaltySD/plugins/FPSLocker/patches/0100BEA0244FC000/9FD75204E7C17463.yaml), v3, 1.1.1) <br> `4AC071F9B9540985` ([✅](SaltySD/plugins/FPSLocker/patches/0100BEA0244FC000/4AC071F9B9540985.yaml), v4, 1.1.3) | ~~[🔐](#🔐)[⏱️](#⏱️)~~[⚔️](#⚔️) |
| Mark of the Ninja: Remastered | `01009A700A538000` | `AE324830FE37FC72` (◯, v2, 1.0.2) |  |
| Marvel Ultimate Alliance 3: The Black Order | `010060700AC50000` | `E853C44FDF18B88F` ([✅](SaltySD/plugins/FPSLocker/patches/010060700AC50000/E853C44FDF18B88F.yaml), v8, 4.0.1) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Mary Skelter Finale | `0100530014438000` | `B1AFBB02475AD7E3` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| Märchen Forest | `01001B2012D5E000` | `7A7C634CDAFE7D42` (◯, v7, 1.0.7) |  |
| Master Detective Archives: RAIN CODE `US` | `0100149019460000` | `F4685ACC91FEDB12` ([✅](SaltySD/plugins/FPSLocker/patches/01004800197F0000/F4685ACC91FEDB12.yaml), v7, 1.4.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Master Detective Archives: RAIN CODE `GLOBAL` | `01004800197F0000` | `B9E42653FB44EF2B` ([✅](SaltySD/plugins/FPSLocker/patches/0100149019460000/B9E42653FB44EF2B.yaml), v7, 1.4.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Masters of Anima | `0100CC7009196000` | `B1C8B55EBD400E57` (◯, v1, 1.0.1) |  |
| Max: The Curse Of Brotherhood | `01001C9007614000` | `F99E70DF48B3DC49` (◯, v1, 1.0.1) |  |
| MEGATON MUSASHI W: WIRED | `01003EB01C2F0000` | `0D28F064B3A5D030` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/0D28F064B3A5D030.yaml), v3, 3.0.3) <br> `4183AB952B599826` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/4183AB952B599826.yaml), v4, 3.1.0) <br> `F1E096F78DFB8263` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/F1E096F78DFB8263.yaml), v5, 3.1.1) <br> `452F9C150D1D17B7` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/452F9C150D1D17B7.yaml), v6, 3.1.2) <br> `FF46A0C56BAD0A32` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/FF46A0C56BAD0A32.yaml), v7, 3.1.3) <br> `8286C091117CAECF` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/8286C091117CAECF.yaml), v8, 3.2.0) <br> `1EC3E6373D7DA9A6` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/1EC3E6373D7DA9A6.yaml), v9, 3.2.2) <br> `D152798E91A87AE7` ([✅](SaltySD/plugins/FPSLocker/patches/01003EB01C2F0000/D152798E91A87AE7.yaml), v10, 3.2.3) | ~~[🛑](#🛑)~~ |
| Metal Gear Solid 2: Sons of Liberty | `0100A4301AA0C000` | `03C2232966780A16` (❌, v9, 2.0.0) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Metal Gear Solid 3: Snake Eater | `010047F01AA10000` | `AE937A8EA9B815AD` (❌, v10, 2.0.0) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢) |
| Metro 2033 Redux | `0100D4900E82C000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4900E82C000/85C362CC9790F0ED.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Metro: Last Light Redux | `0100F0400E850000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100F0400E850000/85C362CC9790F0ED.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Miitopia | `01003DA010E8A000` | `3378B75A3DD2ADA9` (❌, v3, 1.0.3) | [⏱️](#⏱️)[🖥️](#🖥️) |
| Minecraft Dungeons | `01006C100EC08000` | `13F573E3017996E4` (◯, v27, 1.17.0.0) |  |
| MOBILE SUIT GUNDAM SEED BATTLE DESTINY REMASTERED | `010093C01F256000` | `CABB3B5447C2F79F` ([✅](SaltySD/plugins/FPSLocker/patches/010093C01F256000/CABB3B5447C2F79F.yaml), v1, 1.0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Modern Combat Blackout | `0100D8700B712000` | `C56E6F514FADC5C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100D8700B712000/C56E6F514FADC5C5.yaml), v3, 1.1.9) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Momotaro Dentetsu: Showa, Heisei, Reiwa no Teiban! Asia Edition | `010021801DD26000` | `B2D4462B71536EC6` ([✅](SaltySD/plugins/FPSLocker/patches/010021801DD26000/B2D4462B71536EC6.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)[⚔️](#⚔️)[🔢](#🔢)~~ |
| 모모타로전철 ～쇼와 헤이세이 레이와에서도 국룰！～ Korea Edition | `010040A0209DC000` | `A4A3B5A20B03B2A7` ([✅](SaltySD/plugins/FPSLocker/patches/010040A0209DC000/A4A3B5A20B03B2A7.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)[⚔️](#⚔️)[🔢](#🔢)~~ |
| MONARK | `0100E4A01548C000` | `85EB6295023DD394` (◯, v1, 1.0.1) |  |
| MONOPOLY | `01002C201BC40000` | `1AAA3C7D76026D29` (◯, v5, 1.5) |  |
| Monster Hunter Generations Ultimate | `0100770008DD8000` | `FB08F1D20FD1204F` ([✅](SaltySD/plugins/FPSLocker/patches/0100770008DD8000/FB08F1D20FD1204F.yaml), v4, 1.4.0) | ~~[🔐](#🔐)~~ |
| モンスターハンターダブルクロス | `0100C3800049C000` | `9D4C86E6EF74504A` ([✅](SaltySD/plugins/FPSLocker/patches/0100C3800049C000/9D4C86E6EF74504A.yaml), v6, 1.5.1) | ~~[🔐](#🔐)~~ |
| Monster Hunter Rise `GLOBAL` | `0100B04011742000` | `C9A3DD7702075ECD` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/C9A3DD7702075ECD.yaml), v34, 16.0.2) | ~~[🔐](#🔐)~~ |
| Monster Hunter Rise `JPN` | `0100559011740000` | `D2FD97779381FB9A` ([✅](SaltySD/plugins/FPSLocker/patches/0100559011740000/D2FD97779381FB9A.yaml), v34, 16.0.2) | ~~[🔐](#🔐)~~ |
| Monster Jam Showdown | `0100CE101B698000` | `AFE59FDFAC191EBD` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/AFE59FDFAC191EBD.yaml), v1, 1.0.1) <br> `820B3E993D6FE8E1` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/820B3E993D6FE8E1.yaml), v2, 1.0.2) <br> `9035B7A14BADF977` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/9035B7A14BADF977.yaml), v3, 1.0.3) <br> `C4950585861A47EE` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/C4950585861A47EE.yaml), v4, 1.0.4) <br> `D07D96A610514C45` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/D07D96A610514C45.yaml), v5, 1.0.5) <br> `35FC3A7D13060376` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/35FC3A7D13060376.yaml), v6, 1.0.6) <br> `0CE2AE41BCCADC72` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/0CE2AE41BCCADC72.yaml), v7, 1.0.7) <br> `1CE1386EAF0C5EF5` ([✅](SaltySD/plugins/FPSLocker/patches/0100CE101B698000/1CE1386EAF0C5EF5.yaml), v8, 1.0.8) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Monster Jam Steel Titans | `010095C00F354000` | `8CA6136CF49F1A4F` (◯, v1, 1.0.1) |  |
| Monster Jam Steel Titans 2 | `010051B0131F0000` | `E0E9D0429A2458E1` ([✅](SaltySD/plugins/FPSLocker/patches/010051B0131F0000/E0E9D0429A2458E1.yaml), v2, 1.0.2) | ~~[📏](#📏)~~ |
| Monster Truck Championship | `0100D30010C42000` | `682F4A502035678D` ([✅](SaltySD/plugins/FPSLocker/patches/0100D30010C42000/682F4A502035678D.yaml), v2, 1.2.0) | ~~[📏](#📏)~~ |
| Monster Train | `01006D9013894000` | `9DCA1A70C6414A49` (◯, v1, 2.2.0) |  |
| Monster Train 2 | `010051701FB46000` | `ECE035D9E5A2B3F0` (◯, v7, 1.3.1) |  |
| Morbid: The Lords of Ire | `01007B0017C90000` | `55DFB4A664D8B596` ([✅](SaltySD/plugins/FPSLocker/patches/01007B0017C90000/55DFB4A664D8B596.yaml), v2, 1.02) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Moto Racer 4 | `01002ED00B01C000` | `31F61EC3A4FEFDF7` ([✅](SaltySD/plugins/FPSLocker/patches/01002ED00B01C000/31F61EC3A4FEFDF7.yaml), v3, 1.0.3) | ~~[🔧](#🔧)~~ |
| MotoGP 22 | `0100CF3016BBE000` | `6A8373EFB7B2BD5D` ([✅](SaltySD/plugins/FPSLocker/patches/0100CF3016BBE000/6A8373EFB7B2BD5D.yaml), v6, 1.0.6) | ~~[📏](#📏)[🔧](#🔧)~~ |
| MotoGP 23 | `0100B750198C6000` | `FF0DDCCB9C3B9375` ([✅](SaltySD/plugins/FPSLocker/patches/0100B750198C6000/FF0DDCCB9C3B9375.yaml), v7, 1.0.7) | ~~[📏](#📏)[🔧](#🔧)~~ |
| MotoGP 24 | `010040401D564000` | `1053EA8AD2A50F15` ([✅](SaltySD/plugins/FPSLocker/patches/010040401D564000/1053EA8AD2A50F15.yaml), v5, 1.0.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| MotoGP 25 | `01006C7021024000` | `72D353380DD03B52` ([✅](SaltySD/plugins/FPSLocker/patches/01006C7021024000/72D353380DD03B52.yaml), v1, 1.0.1) <br> `BD9B46CAE607D7E8` ([✅](SaltySD/plugins/FPSLocker/patches/01006C7021024000/BD9B46CAE607D7E8.yaml), v2, 1.0.2) <br> `03DBE839CAA0632B` ([✅](SaltySD/plugins/FPSLocker/patches/01006C7021024000/03DBE839CAA0632B.yaml), v3, 1.0.3) <br> `499A85D046C70186` ([✅](SaltySD/plugins/FPSLocker/patches/01006C7021024000/499A85D046C70186.yaml), v4, 1.0.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Moving Out | `0100C4C00E73E000` | `CB3172ED0C3BC646` (◯, v6, 1.0.6) |  |
| Moving Out 2 | `010065D018172000` | `C552B6464E7348A7` (◯, v5, 1.3.315) |  |
| My Time at Sandrock | `0100B63016916000` | `B74FDF27FC9DA1B4` (◯, v13, 1.4.2.0) |  |
| Mythic Ocean | `0100F4F014108000` | `2284DFB25F387719` ([✅](SaltySD/plugins/FPSLocker/patches/0100F4F014108000/2284DFB25F387719.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| NARUTO SHIPPUUDEN: Ultimate Ninja STORM TRILOGY | `0100EC800800C000` | `295564276378B0DF` (❌, v1, 1.0.1) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)[🖌️](#🖌️) |
| NARUTO SHIPPUDEN: Ultimate Ninja STORM 4 ROAD TO BORUTO | `01006CF00CF60000` | `D3016FC0C0402DFB` (❌, v3, 1.3.0) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)[🎮](#🎮) |
| NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS `EUR` | `01005A20190A6000` | `254B4AC2A6395A05` (❌, v9, 1.6.0) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS `US` | `0100D2D0190A4000` | `A281486F065593A2` (❌, v9, 1.6.0) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| NARUTO X BORUTO ナルティメットストームコネクションズ | `0100FA10190A0000` | `7FB76571A9301DC8` (❌, v9, 1.6.0) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| 나루토 X 보루토 나루티밋 스톰 커넥션즈 | `0100D010190A8000` | `A281486F065593A2` (❌, v9, 1.6.0) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| NASCAR Heat | `0100DC7013938000` | `E0E11E95C0DE34D3` (◯, v5, 1.0.5) |  |
| NASCAR Rivals | `0100545016D5E000` | `71A1520B89DEC904` (◯, v5, 1.0.5) |  |
| NBA 2K19 | `01001FF00B544000` | `7C59AFE8A4198447` (◯, v7, 1.07) |  |
| NBA 2K23 | `0100ACA017E4E000` | `BBE7CBE1AC01DC48` (◯, v12, 1.12) |  |
| NBA 2K24 | `010006501A8D8000` | `D418DFA41758684C` (◯, v11, 1.11) |  |
| NBA 2K25 | `0100DFF01ED44000` | `4E232F4CA49E3446` (◯, v11, 1.11) |  |
| NBA 2K26 | `0100CBF022E18000` | `E7D2CD194BD65809` (◯, v3, 1.03) |  |
| Need For Speed Hot Pursuit | `010029B0118E8000` | `799D1061182C1302` ([✅](SaltySD/plugins/FPSLocker/patches/010029B0118E8000/799D1061182C1302.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)~~ |
| Nelke & the Legendary Alchemists | `01006ED00BC76000` | `DBD272113FD196D5` (◯, v3, 1.0.3) |  |
| Neptunia: Sisters VS Sisters | `0100A9001C042000` | `3565E26E8827C846` ([✅](SaltySD/plugins/FPSLocker/patches/0100A9001C042000/3565E26E8827C846.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Neptunia Game Maker R:Evolution | `010082901D6F2000` | `FCA830BAE649B898` ([✅](SaltySD/plugins/FPSLocker/patches/010082901D6F2000/FCA830BAE649B898.yaml), v0, 1.00) | ~~[📏](#📏)~~ |
| Neptunia x SENRAN KAGURA: Ninja Wars | `01008D0016AF4000` | `FB827BF029E0778A` ([✅](SaltySD/plugins/FPSLocker/patches/01008D0016AF4000/FB827BF029E0778A.yaml), v0, 1.0.0) | ~~[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| - 閃亂忍忍忍者大戰戰機少女-少女們的響艷-<br>- 섬란 닌닌닌자 대전 넵튠 -소녀들의 향염- | `010088B017734000` | `288908CE7F6177CC` ([✅](SaltySD/plugins/FPSLocker/patches/010088B017734000/288908CE7F6177CC.yaml), v0, 1.0.0) | ~~[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Never Alone (Kisima Ingitchuna) | `0100A6B01712C000` | `B489970C5C8E79A7` (❌, v2, 1.0.2) | [⚔️](#⚔️) |
| New Super Lucky's Tale | `010017700B6C2000` | `14872049185C584C` (◯, v3, 1.5.9) |  |
| New Tales from the Borderlands | `01002B7013440000` | `A19E113723E5C32E` ([✅](SaltySD/plugins/FPSLocker/patches/01002B7013440000/A19E113723E5C32E.yaml), v2, 1.0.2) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Ni no Kuni: Wrath of the White Witch | `0100E5600D446000` | `C32B29CB5FBA96D9` ([✅](SaltySD/plugins/FPSLocker/patches/0100E5600D446000/C32B29CB5FBA96D9.yaml), v2, 1.0.2) | ~~[⏱️](#⏱️)[🖥️](#🖥️)[📺](#📺)~~ |
| Nickelodeon All-Star Brawl 2 | `010010701AFB2000` | `533BE14853365083` (◯, v14, 1.14.0) |  |
| Nice Day for Fishing | `010074C021210000` | `1D9F49E321B8C939` ([✅](SaltySD/plugins/FPSLocker/patches/010074C021210000/1D9F49E321B8C939.yaml), v6, 1.0.6) | ~~[📷](#📷)~~ |
| NieR:Automata `ASIA` | `0100B8E016F76000` | `992787E2B5425994` ([✅](SaltySD/plugins/FPSLocker/patches/0100B8E016F76000/992787E2B5425994.yaml), v1, 1.0.2) | ~~[📏](#📏)~~ |
| NieR:Automata `GLOBAL` | `010056B015FE8000` | `E43525F22282A477` ([✅](SaltySD/plugins/FPSLocker/patches/010056B015FE8000/E43525F22282A477.yaml), v1, 1.0.2) | ~~[📏](#📏)~~ |
| Nights Of Azure 2: Bride of the New Moon | `0100628004BCE000` | `81DA4F9E1E961CA6` ([✅](SaltySD/plugins/FPSLocker/patches/0100628004BCE000/81DA4F9E1E961CA6.yaml), v1, 1.0.1) | ~~[⚔️](#⚔️)~~ |
| Nikoderiko: The Magical World | `01009FA01FF6C000` | `EBDE239CB7780F58` ([✅](SaltySD/plugins/FPSLocker/patches/01009FA01FF6C000/EBDE239CB7780F58.yaml), v0, 1.0.0) <br> `FCCC4FDA392C1C16` ([✅](SaltySD/plugins/FPSLocker/patches/01009FA01FF6C000/FCCC4FDA392C1C16.yaml), v1, 1.0.1) <br> `6CFA2609A2D00FA5` ([✅](SaltySD/plugins/FPSLocker/patches/01009FA01FF6C000/6CFA2609A2D00FA5.yaml), v2, 1.0.2) <br> `1218D04A7C77F2DA` ([✅](SaltySD/plugins/FPSLocker/patches/01009FA01FF6C000/1218D04A7C77F2DA.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Nine Parchments | `0100D03003F0E000` | `F7893E37FC10C803` (◯, v4, 1.1.1) |  |
| No Man's Sky | `0100853015E86000` | `D5C5F47DFABD0812` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/D5C5F47DFABD0812.yaml), v62, 5.7.5) <br> `4995675B5380FA50` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/4995675B5380FA50.yaml), v63, 6.0.0) <br> `538D60FF5A324C92` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/538D60FF5A324C92.yaml), v64, 6.5.0) <br> `DEA84284F054C693` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/DEA84284F054C693.yaml), v65, 6.10.0) <br> `0C4BD6CA532E589C` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/0C4BD6CA532E589C.yaml), v67, 6.17.0) | ~~[📏](#📏)~~ |
| Oceanhorn 2: Knights of the Lost Realm | `01006CB010840000` | `9F2F187D1C6E44EC` ([✅](SaltySD/plugins/FPSLocker/patches/01006CB010840000/9F2F187D1C6E44EC.yaml), v2, 1.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| OCTOPATH TRAVELER 歧路旅人 | `01000E200DC58000` | `9E6B0D0023F9DB3B` ([✅](SaltySD/plugins/FPSLocker/patches/01000E200DC58000/9E6B0D0023F9DB3B.yaml), v3, 1.0.5) | ~~[🔐](#🔐)~~ |
| OCTOPATH TRAVELER | `010057D006492000` | `67DACC049CEEE858` ([✅](SaltySD/plugins/FPSLocker/patches/010057D006492000/67DACC049CEEE858.yaml), v5, 1.0.5) | ~~[🔐](#🔐)~~ |
| OCTOPATH TRAVELER `JPN` | `0100E66006406000` | `AA4277E6A92FEBE6` ([✅](SaltySD/plugins/FPSLocker/patches/0100E66006406000/AA4277E6A92FEBE6.yaml), v4, 1.0.4) | ~~[🔐](#🔐)~~ |
| OCTOPATH TRAVELER II | `0100A3501946E000` | `0D9649011312F62E` ([✅](SaltySD/plugins/FPSLocker/patches/0100A3501946E000/0D9649011312F62E.yaml), v2, 1.1.1) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Oddworld: Soulstorm | `0100D210177C6000` | `9510D677DCCE4447` ([✅](SaltySD/plugins/FPSLocker/patches/0100D210177C6000/9510D677DCCE4447.yaml), v3, 1.1.3) | ~~[📏](#📏)~~ |
| Off the Road Unleashed | `010045C0112F8000` | `5E8316D212D6D7BD` (◯, v1, 1.0.1) |  |
| Okami HD | `0100276009872000` | `A4FDDC7FD35B30CB` (❌, v0, 1.0.0) | [⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢) |
| Olympic Games Tokyo 2020 `EUR` | `010034B00E14C000` | `C4D1BCED9D8C5B81` (❌, v2, 1.0.2) | [⏱️](#⏱️) |
| 東京2020オリンピック | `01004CE00AAE2000` | `66A8EB853DE90A1A` (❌, v9, 1.0.9) | [⏱️](#⏱️) |
| Once Upon A KATAMARI | `0100BDF0197C8000` | `FF53171B18C7701A` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDF0197C8000/FF53171B18C7701A.yaml), v1, 1.0.2) <br> `41F236A333370F55` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDF0197C8000/41F236A333370F55.yaml), v2, 1.0.3) | ~~[📏](#📏)~~ |
| ONE PIECE ODYSSEY | `0100D9601A994000` | `28ED06F94D767478` ([✅](SaltySD/plugins/FPSLocker/patches/0100D9601A994000/28ED06F94D767478.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Oninaki | `01001AF00CE54000` | `C949E2576F532C43` (◯, v2, 1.0.2) |  |
| Open Roads | `010034401672A000` | `1C651256CC812D06` (◯, v2, 1.0.2) |  |
| Operation: Polygon Storm | `010084501F592000` | `3025AF1CB2515489` (◯, v2, 1.0.2) |  |
| OPUS: Echo of Starsong | `01009B601676C000` | `BFF92D9D3F4CE84D` (◯, v5, 2.3.2f4) |  |
| Othercide | `0100E5900F49A000` | `A8BA2A8F93AAE647` ([✅](SaltySD/plugins/FPSLocker/patches/0100E5900F49A000/A8BA2A8F93AAE647.yaml), v4, 1.3.1.0) | ~~[📏](#📏)~~ |
| Out of Sight | `010098A02288A000` | `7E610F688F92412B` ([✅](SaltySD/plugins/FPSLocker/patches/010098A02288A000/7E610F688F92412B.yaml), v3, 1.0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Outer Wilds | `01003DC0144B6000` | `CD9AF768102ED946` (❌, v5, 1.1.15.1027) | [📏](#📏)[📷](#📷)[🔧](#🔧) |
| Outlast | `01008D4007A1E000` | `C3D46BB3C7059DB1` ([✅](SaltySD/plugins/FPSLocker/patches/01008D4007A1E000/C3D46BB3C7059DB1.yaml), v1, 1.0.1) | ~~[⚔️](#⚔️)~~ |
| Outlast 2 | `0100DE70085E8000` | `F18ACDA7A71CB287` ([✅](SaltySD/plugins/FPSLocker/patches/0100DE70085E8000/F18ACDA7A11CB287.yaml), v0, 1.0.0) | ~~[⚔️](#⚔️)~~ |
| Outward: Definitive Edition | `0100AFB01AAF0000` | `49F913818D086058` (◯, v2, 1.0.2) |  |
| Overcooked! All You Can Eat | `0100F28011892000` | `2854968F71A67B45` (◯, v11, 1.0.11) |  |
| Overcooked! Special Edition | `01009B900401E000` | `41D554623A3F4341` (◯, v4, 1.1.1) |  |
| Overcooked! 2 | `01006FD0080B2000` | `616640F27B936250` (◯, v19, 1.0.19) |  |
| Oxenfree II: Lost Signals | `010061F0176F6000` | `F722A80C29EF4275` (◯, v4, 1.4.8) |  |
| PAC-MAN WORLD Re-PAC | `0100D4401565E000` | `0058D033DAA48B17` (◯, v2, 1.0.2) |  |
| PAC-MAN WORLD 2 Re-PAC | `0100C2801CFB8000` | `B70D6561B718C8E0` ([✅](SaltySD/plugins/FPSLocker/patches/0100C2801CFB8000/B70D6561B718C8E0.yaml), v3, 1.0.3) | ~~[📷](#📷)~~ |
| パックマンワールド2 リ・パック | `010065A01CFB6000` | `B70D6561B718C8E0` ([✅](SaltySD/plugins/FPSLocker/patches/010065A01CFB6000/B70D6561B718C8E0.yaml), v3, 1.0.3) | ~~[📷](#📷)~~ |
| - 팩맨 월드 2 리팩<br>- 吃豆人 吃遍世界2 | `01009F201CFBC000` | `B70D6561B718C8E0` ([✅](SaltySD/plugins/FPSLocker/patches/01009F201CFBC000/B70D6561B718C8E0.yaml), v3, 1.0.3) | ~~[📷](#📷)~~ |
| Pandemic Shooter | `0100B69017120000` | `02D54DEBD40AF215` ([✅](SaltySD/plugins/FPSLocker/patches/0100B69017120000/02D54DEBD40AF215.yaml), v0, 1.0.0) | ~~[🔧](#🔧)~~ |
| Paper Mario: The Origami King | `0100A3900C3E2000` | `E74395F066FD8CCB` (❌, v1, 1.0.1) | [🔐](#🔐)[⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢) |
| Paper Mario: The Thousand-Year Door | `0100ECD018EBE000` | `0EFFE4AF1DEC3A79` (❌, v1, 1.0.1) | [🔐](#🔐)[⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Paradise Killer | `01007FB010DC8000` | `D3744AF2C376CDC4` ([✅](SaltySD/plugins/FPSLocker/patches/01007FB010DC8000/D3744AF2C376CDC4.yaml), v7, 1.2.1) | ~~[📏](#📏)~~ |
| Paradise Lost | `010077A012A5C000` | `F5ECE696120B65B3` ([✅](SaltySD/plugins/FPSLocker/patches/010077A012A5C000/F5ECE696120B65B3.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| Pascal's Wager | `01009B9017D8E000` | `3F9A7276F039B226` (◯, v2, 2.0.0) |  | 
| Passpartout 2: The Lost Artist | `010094E01AA20000` | `ED2F8EEA20A7943D` (◯, v3, 1.1.1) |  | 
| PAW Patrol World | `0100273018D70000` | `54C42C73890100F1` (❌📌, v2, 1.0.2) | [🔐](#🔐) |
| Payday 2 | `0100274004052000` | `AEA19BDA16E7A34F` (◯, v1, 1.1.0) |  |
| Peppa Pig: World Adventures | `0100FF1018E00000` | `696DE87363CDAED0` (◯, v1, 1.0.1) |  |
| Persona 5 Royal | `01005CA01580E000` | `D4B150B29A931CD3` (❌, v1, 1.0.2) | [🖌️](#🖌️) |
| - 女神異聞錄５ 皇家版<br>- 페르소나5 더 로열 | `01004B10157F2000` | `D4B150B29A931CD3` (❌, v1, 1.0.2) | [🖌️](#🖌️) |
| 女神異聞錄５ 亂戰：魅影攻手 | `01005BD010872000` | `496A2F5A9CE4FBEB` ([✅](SaltySD/plugins/FPSLocker/patches/01005BD010872000/496A2F5A9CE4FBEB.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| ペルソナ５ スクランブル　ザ ファントム ストライカーズ | `01001C400E9D8000` | `737E56D43D2C0B38` ([✅](SaltySD/plugins/FPSLocker/patches/01001C400E9D8000/737E56D43D2C0B38.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| 페르소나 5 스크램블 더 팬텀 스트라이커즈 | `01009FE010876000` | `407978D722447B25` ([✅](SaltySD/plugins/FPSLocker/patches/01009FE010876000/407978D722447B25.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Persona 5 Strikers | `0100801011C3E000` | `C4DF04F647BDC727` ([✅](SaltySD/plugins/FPSLocker/patches/0100801011C3E000/C4DF04F647BDC727.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Persona 5 Tactica | `010087701B092000` | `B6333790BE11542C` (◯, v4, 1.1.0) |  |
| Pikmin 1 | `0100AA80194B0000` | `3A8E744D8F65CDEA` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA80194B0000/3A8E744D8F65CDEA.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[📺](#📺)~~ |
| Pikmin 2 | `0100D680194B2000` | `9A257FAB83444214` ([✅](SaltySD/plugins/FPSLocker/patches/0100D680194B2000/9A257FAB83444214.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[📺](#📺)~~ |
| Pikmin 3 Deluxe | `0100F4C009322000` | `D467F5AD367BBEE8` (❌, v4, 1.1.3) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Pikmin 4 | `0100B7C00933A000` | `999AAC4CC07E36BC` (❌, v3, 1.1.0) | [📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢) |
| PJ Masks Power Heroes: Mighty Alliance | `0100FE301A2B4000` | `A91A7BB200C51B01` (◯, v1, 1.0.1) |  |
| Plants vs. Zombies: Battle for Neighborville | `0100C56010FD8000` | `82051A9C802D0A4C` ([✅](SaltySD/plugins/FPSLocker/patches/0100C56010FD8000/82051A9C802D0A4C.yaml), v3, 1.0.3) <br> `5AD255D6667B6EB5` ([✅](SaltySD/plugins/FPSLocker/patches/0100C56010FD8000/5AD255D6667B6EB5.yaml), v4, 1.0.4) | ~~[📏](#📏)~~ |
| Platform 8 | `010036F0201D4000` | `42A0B64E45AD9ABA` ([✅](SaltySD/plugins/FPSLocker/patches/010036F0201D4000/42A0B64E45AD9ABA.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Pokemon: Let's Go, Eevee! | `0100187003A36000` | `5831EC64D6B696FD` (❌, v2, 1.0.2) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Pokemon: Let's Go, Pikachu! | `010003F003A34000` | `C208DB6A4EF4361F` (❌, v2, 1.0.2) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Pokemon Brilliant Diamond | `0100000011D90000` | `94CEAE325C205C4B` (❌, v6, 1.3.0) | [🏃](#🏃) |
| Pokemon Legends: Arceus | `01001F5010DFA000` | `AEE8F150DDA1B5A8` (❌, v4, 1.1.1) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Pokemon Legends: Z-A | `0100F43008C44000` | `7FC4289C78877148` (❌, v2, 1.0.2) | [⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)[⚔️](#⚔️) |
| Pokemon Mystery Dungeon: Rescue Team DX | `01003D200BAA2000` | `3AB632DEE82D5944` (❌, v2, 1.0.2) | [🏃](#🏃) |
| Pokemon Scarlet | `0100A3D008C5C000` | `421C5411B487EB4D` (❌, v12, 4.0.0) | [⚔️](#⚔️)[🏃](#🏃)[⏱️](#⏱️)[🖥️](#🖥️) |
| Pokemon Shield | `01008DB008C2C000` | `A16802625E7826BF` (❌, v7, 1.3.2) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Pokemon Shining Pearl | `010018E011D92000` | `38F59CBDA2EB9C44` (❌, v6, 1.3.0) | [🏃](#🏃) |
| Pokemon Sword | `0100ABF008968000` | `A3B75BCD3311385A` (❌, v7, 1.3.3) | [⚔️](#⚔️)[⏱️](#⏱️)[🖥️](#🖥️) |
| Pokemon Violet | `01008F6008C5E000` | `709BFD6611529864` (❌, v12, 4.0.0) | [⚔️](#⚔️)[🏃](#🏃)[⏱️](#⏱️)[🖥️](#🖥️) |
| Poppy Playtime: Chapter 2 | `0100D3801E6CE000` | `E3A3FC8EEC76A4FB` ([✅](SaltySD/plugins/FPSLocker/patches/0100D3801E6CE000/E3A3FC8EEC76A4FB.yaml), v1, 1.1) <br> `ACCFF102CED838CE` ([✅](SaltySD/plugins/FPSLocker/patches/0100D3801E6CE000/ACCFF102CED838CE.yaml), v4, 1.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Poppy Playtime: Chapter 3 | `0100BD601EC3E000` | `5AF163DEF288F098` ([✅](SaltySD/plugins/FPSLocker/patches/0100BD601EC3E000/5AF163DEF288F098.yaml), v1, 1.0.0.2) <br> `5AF163DEF288F098` ([✅](SaltySD/plugins/FPSLocker/patches/0100BD601EC3E000/3F1843C4FE400063.yaml), v3, 1.2) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Poppy Playtime: Chapter 4 | `0100A2902051A000` | `05ADD0D5FD677639` ([✅](SaltySD/plugins/FPSLocker/patches/0100A2902051A000/05ADD0D5FD677639.yaml), v1, 1.1) <br> `3D6E4BDE905836BC` ([✅](SaltySD/plugins/FPSLocker/patches/0100A2902051A000/3D6E4BDE905836BC.yaml), v2, 1.2) <br> `779FC981128BA290` ([✅](SaltySD/plugins/FPSLocker/patches/0100A2902051A000/779FC981128BA290.yaml), v3, 1.3) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Portal Knights | `0100437004170000` | `D59D81C06F923846` (❌, v8, 1.7.2) | [⚔️](#⚔️) |
| Potion Permit | `010025F0126FE000` | `EAD19EF59A52CC14` (◯, v13, 1.0.13) |  |
| PowerWash Simulator | `0100926016012000` | `8EACFE3E9E92B0FE` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/8EACFE3E9E92B0FE.yaml), v12, 1.7.0) <br> `7FF42DE6AA57290B` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/7FF42DE6AA57290B.yaml), v16, 1.9.1) <br> `B2395B882C2BCB24` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/B2395B882C2BCB24.yaml), v17, 1.9.2) <br> `30997D8F7566EBB5` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/30997D8F7566EBB5.yaml), v18, 1.10.0) <br> `561B0F485E699E4E` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/561B0F485E699E4E.yaml), v19, 1.11.0) | ~~[🔐](#🔐)~~ |
| Project Nightmares Case 36: Henrietta Kedward | `0100736019D8E000` | `72AE4B77322A5B1B` ([✅](SaltySD/plugins/FPSLocker/patches/0100736019D8E000/72AE4B77322A5B1B.yaml), v3, 1.0.3) | ~~[📏](#📏)~~ |
| PROJECT ZERO: MAIDEN OF BLACK WATER | `0100BEB015604000` | `B38D51E0391187EC` ([✅](SaltySD/plugins/FPSLocker/patches/0100BEB015604000/B38D51E0391187EC.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| 零 ～月蝕的假面～ | `010091B01A438000` | `A735894277FF90F3` ([✅](SaltySD/plugins/FPSLocker/patches/010091B01A438000/A735894277FF90F3.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| PROJECT ZERO: Mask of the Lunar Eclipse | `0100DAE019110000` | `0248DC99035AD28A` ([✅](SaltySD/plugins/FPSLocker/patches/0100DAE019110000/0248DC99035AD28A.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Princess Peach Showtime! | `01007A3009184000` | `928EFE2954F68055` ([✅](SaltySD/plugins/FPSLocker/patches/01007A3009184000/928EFE2954F68055.yaml), v0, 1.0.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Prison Simulator | `010094C017B06000` | `56C709E1A63CF9EA` (◯, v0, 1.0.0) |  |
| Project Warlock | `0100BDB01150E000` | `D597DE8544D8ED4F` (◯, v4, 1.0.4) |  |
| Pumpkin Jack | `01006C10131F6000` | `0F73F1D52820F90B` ([✅](SaltySD/plugins/FPSLocker/patches/01006C10131F6000/0F73F1D52820F90B.yaml), v4, 1.4.4) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Rabbids Party of Legends | `01008970149B0000` | `7C0876057EE29DF3` (❌, v1, 1.0.1) | [🛑](#🛑) |
| Raccoo Venture | `0100C1E01CDEE000` | `27BB06DD145F39F5` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1E01CDEE000/27BB06DD145F39F5.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[🏃](#🏃)~~ |
| Rad Rodgers: Radical Edition | `010000600CD54000` | `78885A1CA987C04C` ([✅](SaltySD/plugins/FPSLocker/patches/010000600CD54000/78885A1CA987C04C.yaml), v2, 1.2.0) | ~~[🔐](#🔐)~~ |
| Rain World | `010047600BF72000` | `8216914B5699E2DB` (◯, v11, 1.11.2b) |  |
| RAINBOW HIGH: RUNWAY RUSH | `010039E0182D8000` | `8ECB01C6E7E4F50C` (◯, v0, 1.0.0) |  |
| Raji: An Ancient Epic | `010010B00DDA2000` | `8A39E660F956BB00` ([✅](SaltySD/plugins/FPSLocker/patches/010010B00DDA2000/8A39E660F956BB00.yaml), v4, 1.0.4) | ~~[📏](#📏)~~ |
| Ravenswatch | `0100E6701DF4E000` | `F525CE3D32CD4FF5` (◯, v9, 1.9.0) |  |
| realMyst: Masterpiece Edition | `0100E64010BAA000` | `31E49EEA600A6248` (◯, v3, 1.0.3) |  |
| Red Dead Redemption | `01007820196A6000` | `37531419DA7654EC` (◯, v4, 1.0.4) |  |
| レッド・デッド・リデンプション | `010000B0196AA000` | `005CB235608DCEDD` (◯, v4, 1.0.4) |  |
| Redemption Reapers | `010073F0197DA000` | `955DF07AA5F4497B` ([✅](SaltySD/plugins/FPSLocker/patches/010073F0197DA000/955DF07AA5F4497B.yaml), v7, 1.4.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Redout | `0100DA20021D0000` | `1C81D0BC78A01EE2` (◯, v2, 1.0.2) |  |
| Redout 2 | `0100664016D5C000` | `D45B9332B5742A70` ([✅](SaltySD/plugins/FPSLocker/patches/0100664016D5C000/D45B9332B5742A70.yaml), v6, 1.0.6) <br> `E47783ECB944D857` ([✅](SaltySD/plugins/FPSLocker/patches/0100664016D5C000/E47783ECB944D857.yaml), v7, 1.0.7) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Remnant: From the Ashes | `010010F01418E000` | `49CF6B0B0A62F9E2` ([✅](SaltySD/plugins/FPSLocker/patches/010010F01418E000/49CF6B0B0A62F9E2.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ |
| Remothered: Broken Porcelain | `0100FBD00F5F6000` | `5EFAB20F5C1F0F68` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD00F5F6000/5EFAB20F5C1F0F68.yaml), v9, 2.0.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~[⚔️](#⚔️) |
| Remothered Tormented Fathers | `01008F600F2D0000` | `EB57CF3434044523` ([✅](SaltySD/plugins/FPSLocker/patches/01008F600F2D0000/EB57CF3434044523.yaml), v3, 1.3.0) | ~~[🔐](#🔐)[🔧](#🔧)~~[⚔️](#⚔️) |
| resident evil 0 | `010097000BC10000` | `FB4239AA962B429B` ([✅](SaltySD/plugins/FPSLocker/patches/010097000BC10000/FB4239AA962B429B.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📺](#📺)~~ |
| biohazard 0 | `0100F3000BC0C000` | `F2F3CCA2F8E11965` (❌📌, v0, 1.0.0) | [🔐](#🔐)[📺](#📺) |
| Resident Evil | `010050F00BC1A000` | `6BEC9B23B09DF46C` ([✅](SaltySD/plugins/FPSLocker/patches/010050F00BC1A000/6BEC9B23B09DF46C.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📺](#📺)~~ |
| Resident Evil 4 | `010099A00BC1E000` | `82C2A04A21D3E0B8` (◯, v2, 1.0.2) | ~~[🔐](#🔐)[📺](#📺)~~ |
| REYNATIS | `010050F01DF9C000` | `456F89F80D657095` ([✅](SaltySD/plugins/FPSLocker/patches/010050F01DF9C000/456F89F80D657095.yaml), v4, 1.0.4) <br> `C370209AECC8D2FB` ([✅](SaltySD/plugins/FPSLocker/patches/010050F01DF9C000/C370209AECC8D2FB.yaml), v5, 1.0.5) <br> `25A4C89527E7A6E6` ([✅](SaltySD/plugins/FPSLocker/patches/010050F01DF9C000/25A4C89527E7A6E6.yaml), v6, 1.0.6) <br> `7C8FE1FD610E1F1F` ([✅](SaltySD/plugins/FPSLocker/patches/010050F01DF9C000/7C8FE1FD610E1F1F.yaml), v7, 1.0.7) <br> `11D6D6158B566A74` ([✅](SaltySD/plugins/FPSLocker/patches/010050F01DF9C000/11D6D6158B566A74.yaml), v8, 1.0.8) <br> `C59C89CCDF382602` ([✅](SaltySD/plugins/FPSLocker/patches/010050F01DF9C000/C59C89CCDF382602.yaml), v9, 1.0.9) <br> `5F765D2CC4CDEF1C` ([✅](SaltySD/plugins/FPSLocker/patches/010050F01DF9C000/5F765D2CC4CDEF1C.yaml), v10, 1.0.10) | ~~[📏](#📏)~~ |
| RICO | `01009D5009234000` | `D4852E02DCD55245` (◯, v5, 1.0.5) |  |
| RiME | `0100A62002042000` | `B426F56F027E8231` (◯, v2, 1.0.2) |  |
| Road 96 | `010031B0145B4000` | `EAF3511193618B2A` (◯, v5, 1.05) |  |
| Road 96: Mile 0 | `01008600180CE000` | `DF1EBBA8DE722A3B` (◯, v0, 1.00) |  |
| ROBOBEAT | `01009AC01F8E4000` | `D94E7982DF38E96C` (◯, v2, 1.1.4) |  |
| ROMANCE OF THE THREE KINGDOMS 8 REMAKE | `0100C2A01A730000` | `9F7C33E21279D3E6` ([✅](SaltySD/plugins/FPSLocker/patches/0100C2A01A730000/9F7C33E21279D3E6.yaml), v8, 1.0.8) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| 삼국지8 REMAKE | `010019D01D736000` | `3BA6C7665F67A711` ([✅](SaltySD/plugins/FPSLocker/patches/010019D01D736000/3BA6C7665F67A711.yaml), v8, 1.0.8) | ~~[🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| ROMANCE OF THE THREE KINGDOMS XIV | `0100ED7012DB2000` | `1A971CC40B6D5B3F` ([✅](SaltySD/plugins/FPSLocker/patches/0100ED7012DB2000/1A971CC40B6D5B3F.yaml), v7, 1.0.10) | ~~[🔐](#🔐)[⏱️](#⏱️)~~[🖥️](#🖥️) |
| 三國志14 with 威力加強版 | `0100CD4012DCA000` | `B067B077906C6208` ([✅](SaltySD/plugins/FPSLocker/patches/0100CD4012DCA000/B067B077906C6208.yaml), v10, 1.0.10) | ~~[🔐](#🔐)[⏱️](#⏱️)~~[🖥️](#🖥️) |
| Romancing SaGa 2: Revenge of the Seven | `010045301B86C000` | `791D79EBD7A0115E` ([✅](SaltySD/plugins/FPSLocker/patches/010045301B86C000/791D79EBD7A0115E.yaml), v1, 1.0.1) <br> `1933FBAFE977FA75` ([✅](SaltySD/plugins/FPSLocker/patches/010045301B86C000/1933FBAFE977FA75.yaml), v2, 1.0.2) <br> `D7A32C718E9D6363` ([✅](SaltySD/plugins/FPSLocker/patches/010045301B86C000/D7A32C718E9D6363.yaml), v3, 1.1.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Rooftops & Alleys: The Parkour Game | `0100FC20214B2000` | `03CD4543EE8B0961` (◯, v5, 1.5) |  |
| Roxy Raccoon's Pinball Panic | `0100E070196FE000` | `E1D2D5C27F045CA0` (◯, v0, 1.0.0) |  |
| Ruined King: A League of Legends Story | `0100947013122000` | `9FC46F388F6C684C` ([✅](SaltySD/plugins/FPSLocker/patches/0100947013122000/9FC46F388F6C684C.yaml), v7, 1.7) | ~~[📏](#📏)~~ |
| Ruiner | `01006EC00F2CC000` | `F199FFD7D83F399E` ([✅](SaltySD/plugins/FPSLocker/patches/01006EC00F2CC000/F199FFD7D83F399E.yaml), v3, 1.3) | ~~[📏](#📏)~~ |
| Rune Factory 5 | `0100CDC013238000` | `D626F7A72AF54744` ([✅](SaltySD/plugins/FPSLocker/patches/0100CDC013238000/D626F7A72AF54744.yaml), v2, 1.0.2) | ~~[📏](#📏)~~ |
| Rune Factory: Guardians of Azuma | `01003AF0200B0000` | `7F731AAE7DDCAF66` ([✅](SaltySD/plugins/FPSLocker/patches/01003AF0200B0000/7F731AAE7DDCAF66.yaml), v3, 1.0.3) <br> `5F96AEDEA20AE78F` ([✅](SaltySD/plugins/FPSLocker/patches/01003AF0200B0000/5F96AEDEA20AE78F.yaml), v4, 1.0.4) <br> `E43BBBBFACE60867` ([✅](SaltySD/plugins/FPSLocker/patches/01003AF0200B0000/E43BBBBFACE60867.yaml), v5, 1.0.5) <br> `742CA53262A767AE` ([✅](SaltySD/plugins/FPSLocker/patches/01003AF0200B0000/742CA53262A767AE.yaml), v6, 1.1.0) <br> `F678FD2BB197125B` ([✅](SaltySD/plugins/FPSLocker/patches/01003AF0200B0000/F678FD2BB197125B.yaml), v7, 1.1.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| S.T.A.L.K.E.R.: Call of Prypiat | `010008E01E32A000` | `823FE359B4A99A4D` ([✅](SaltySD/plugins/FPSLocker/patches/010008E01E32A000/823FE359B4A99A4D.yaml), v1, 1.0.1) <br> `BBA39C65C1CC6463` ([✅](SaltySD/plugins/FPSLocker/patches/010008E01E32A000/BBA39C65C1CC6463.yaml), v2, 1.0.2) <br> `AD4CBC4878008E1E` ([✅](SaltySD/plugins/FPSLocker/patches/010008E01E32A000/AD4CBC4878008E1E.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)~~ |
| S.T.A.L.K.E.R.: Clear Sky | `010027B01E32C000` | `38171F8A5687B940` ([✅](SaltySD/plugins/FPSLocker/patches/010027B01E32C000/38171F8A5687B940.yaml), v1, 1.0.1) <br> `227837B490A51033` ([✅](SaltySD/plugins/FPSLocker/patches/010027B01E32C000/227837B490A51033.yaml), v2, 1.0.2) <br> `C7E4E6F4167C8E3A` ([✅](SaltySD/plugins/FPSLocker/patches/010027B01E32C000/C7E4E6F4167C8E3A.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)~~ |
| S.T.A.L.K.E.R.: Shadow Of Chornobyl | `01004A001E32E000` | `0214CA2211DE8313` ([✅](SaltySD/plugins/FPSLocker/patches/01004A001E32E000/0214CA2211DE8313.yaml), v1, 1.0.1) <br> `8E8BFFE66292CFF1` ([✅](SaltySD/plugins/FPSLocker/patches/01004A001E32E000/8E8BFFE66292CFF1.yaml), v2, 1.0.2) <br> `F7D1E815E44D0A56` ([✅](SaltySD/plugins/FPSLocker/patches/01004A001E32E000/F7D1E815E44D0A56.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)~~ |
| SaGa Emerald Beyond | `01008BE01E1C2000` | `9FD4FB446CEDB012` (◯, v4, 1.04) |  |
| Sakuna: Of Rice and Ruin | `0100B1400E8FE000` | `A4F17AB0C365545B` (◯, v9, 1.0.9) |  |
| Samurai Bringer | `01007E30176E6000` | `20F6DC74F8FB9601` (◯, v4, 1.05.0) |  |
| Samurai Jack: Battle Through Time | `01006C600E46E000` | `6D5DB3434CCF63F2` ([✅](SaltySD/plugins/FPSLocker/patches/01006C600E46E000/6D5DB3434CCF63F2.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)~~ |
| SAMURAI WARRIORS 5 | `0100B28014132000` | `810CBA3D7DB83EC0` ([✅](SaltySD/plugins/FPSLocker/patches/0100B28014132000/810CBA3D7DB83EC0.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| 戦国無双５ | `010089A0117D4000` | `9B7A3AC5AF1A3B0D` ([✅](SaltySD/plugins/FPSLocker/patches/010089A0117D4000/9B7A3AC5AF1A3B0D.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Scars of Mars | `01007D101F162000` | `8945AE69329ED1C7` (◯, v3, 1.1.1) |  |
| SD GUNDAM BATTLE ALLIANCE | `01002BE016054000` | `751420FADE402804` ([✅](SaltySD/plugins/FPSLocker/patches/01002BE016054000/751420FADE402804.yaml), v7, 1.4.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| SD シン・仮面ライダー 乱舞 | `0100CD40192AC000` | `651CF2EC3862B82B` (◯, v2, 1.0.2) |  |
| SENRAN KAGURA Peach Ball | `01004DC00D936000` | `31CDAD67EA25CC16` ([✅](SaltySD/plugins/FPSLocker/patches/01004DC00D936000/31CDAD67EA25CC16.yaml), v0, 1.0.0) | ~~[🔐](#🔐)~~[⚔️](#⚔️) |
| Session: Skate Sim | `010023001969A000` | `D40B81867A121EB0` ([✅](SaltySD/plugins/FPSLocker/patches/010023001969A000/D40B81867A121EB0.yaml), v4, 1.1.3) <br> `F327FFD8C2E85895` ([✅](SaltySD/plugins/FPSLocker/patches/010023001969A000/F327FFD8C2E85895.yaml), v5, 1.1.4) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Severed Steel | `0100E1C0148F8000` | `77C053D779EE97F6` ([✅](SaltySD/plugins/FPSLocker/patches/0100E1C0148F8000/77C053D779EE97F6.yaml), v2, 1.0.2) <br> `5EABF05A814EBB1B` ([✅](SaltySD/plugins/FPSLocker/patches/0100E1C0148F8000/5EABF05A814EBB1B.yaml), v3, 1.0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| SHADOW GENERATIONS | `01005EA01C0FC000` | `3AEBA262CC1D26D3` ([✅](SaltySD/plugins/FPSLocker/patches/01005EA01C0FC000/3AEBA262CC1D26D3.yaml), v1, 1.0.1) <br> `C8CDBFD621A6B29B` ([✅](SaltySD/plugins/FPSLocker/patches/01005EA01C0FC000/C8CDBFD621A6B29B.yaml), v2, 1.1.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Shadows of the Damned | `010037A01F96C000` | `5B863A6EFCE084B0` ([✅](SaltySD/plugins/FPSLocker/patches/010037A01F96C000/5B863A6EFCE084B0.yaml), v1, 1.0.1) | ~~[🔐](#🔐)~~ |
| Shadowverse: Champion's Battle | `01003B90136DA000` | `1F936E043FB8C349` ([✅](SaltySD/plugins/FPSLocker/patches/01003B90136DA000/1F936E043FB8C349.yaml), v0, 1.3.0) | ~~[📷](#📷)~~ |
| Shattered: Tale of the Forgotten King | `0100A0F0180D6000` | `4D42A2CA8232E8EB` (◯, v0, 1.0.0) |  |
| Sherlock Holmes The Awakened | `0100CA800F9B2000` | `A1E1EFBA68B846A9` ([✅](SaltySD/plugins/FPSLocker/patches/0100CA800F9B2000/A1E1EFBA68B846A9.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Sherlock Holmes: Crimes and Punishments | `0100651014DBA000` | `789C2939A757C0CD` ([✅](SaltySD/plugins/FPSLocker/patches/0100651014DBA000/789C2939A757C0CD.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Sherlock Holmes: The Devil's Daughter | `010020F014DBE000` | `2B37ED2A971948F3` ([✅](SaltySD/plugins/FPSLocker/patches/010020F014DBE000/2B37ED2A971948F3.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Sherlock Holmes and The<br>Hound of The Baskervilles | `010003D018708000` | `4A06EBBB5A2E4FE4` (❌📌, v2, 1.0.2) | [🔐](#🔐) |
| Shin chan: Me and the Professor<br>on Summer Vacation<br>The Endless Seven-Day Journey | `0100ACC0185FC000` | `C167F81FB2171443` (◯, v2, 1.1.1) |  |
| Shin chan: Shiro and the Coal Town | `0100A8B01E0C8000` | `2AD4407726EEAB86` (◯, v3, 1.0.3) |  |
| Shin Megami Tensei III Nocturne | `01003B0012DC2000` | `F8098979DBC7F34E` (❌, v3, 1.0.3) | [⏱️](#⏱️)[🏃](#🏃)[🖥️](#🖥️) |
| SHIN MEGAMI TENSEI V | `0100B870126CE000` | `019FBFE7738EA314` ([✅](SaltySD/plugins/FPSLocker/patches/0100B870126CE000/019FBFE7738EA314.yaml), v2, 1.0.2) | ~~[📏](#📏)~~ |
| SHIN MEGAMI TENSEI V: Vengeance | `010069C01AB82000` | `541F680F325BD5AC` ([✅](SaltySD/plugins/FPSLocker/patches/010069C01AB82000/541F680F325BD5AC.yaml), v1, 1.0.1) <br> `E1BD1040BFBDDAFF` ([✅](SaltySD/plugins/FPSLocker/patches/010069C01AB82000/E1BD1040BFBDDAFF.yaml), v2, 1.0.2) <br> `0A4F14A5C12F470A` ([✅](SaltySD/plugins/FPSLocker/patches/010069C01AB82000/0A4F14A5C12F470A.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| 진・여신전생5 Vengeance | `0100FD401AB0E000` | `C60BBEE6786A16DB` (❌📌, v3, 1.0.3) | [🔐](#🔐)[📏](#📏)[🔧](#🔧) |
| Shining Resonance Refrain | `01009A5009A9E000` | `069E3EFC16365FFD` ([✅](SaltySD/plugins/FPSLocker/patches/01009A5009A9E000/069E3EFC16365FFD.yaml), v1, 1.0.1) | ~~[⚔️](#⚔️)[🔐](#🔐)[👄](#👄)~~ |
| 光明之響 龍奏回音 | `0100D7700AF88000` | `F5AC009011277359` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7700AF88000/F5AC009011277359.yaml), v0, 1.0.0) | ~~[⚔️](#⚔️)[🔐](#🔐)[👄](#👄)~~ |
| Ship Graveyard Simulator | `010018C01B106000` | `63B72CD5F2A90020` ([✅](SaltySD/plugins/FPSLocker/patches/010018C01B106000/63B72CD5F2A90020.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Ship of Fools | `010076901806C000` | `2C4700E500079C74` (◯, v5, 1.0.5) |  |
| Sifu | `01007B5017A12000` | `4A5D86DA05A4E7BB` ([✅](SaltySD/plugins/FPSLocker/patches/01007B5017A12000/4A5D86DA05A4E7BB.yaml), v6, 0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| SIGNALIS | `0100307018934000` | `C32A27E10515B7B8` (◯, v4, 1.4) |  |
| SINNER: Sacrifice for Redemption | `0100B16009C10000` | `490D681909609015` ([✅](SaltySD/plugins/FPSLocker/patches/0100B16009C10000/490D681909609015.yaml), v3, 1.1.0319) | ~~[🔐](#🔐)~~ |
| Skylanders Imaginators | `0100CCC0002E6000` | `8B03CB047C01EE43` (◯, v2, 1.1.1) |  |
| Smurfs Kart | `01009790186FE000` | `4A8A1A08FCEBE648` (◯, v4, 1.04.3) |  |
| Snake Pass | `0100C0F0020E8000` | `D0798521F563E6A7` ([✅](SaltySD/plugins/FPSLocker/patches/0100C0F0020E8000/D0798521F563E6A7.yaml), v5, 1.4) | ~~[🔐](#🔐)~~ |
| Sniper Elite 3 | `010075A00BA14000` | `6888027D61CF603D` ([✅](SaltySD/plugins/FPSLocker/patches/010075A00BA14000/6888027D61CF603D.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ | 
| Sniper Elite 4 | `010007B010FCC000` | `4EEA2970DF38ECE1` ([✅](SaltySD/plugins/FPSLocker/patches/010007B010FCC000/4EEA2970DF38ECE1.yaml), v3, 1.0.3) | ~~[📏](#📏)~~ | 
| Sniper Elite V2 | `0100BB000A3AA000` | `B61F280560A937D2` ([✅](SaltySD/plugins/FPSLocker/patches/0100BB000A3AA000/B61F280560A937D2.yaml), v5, 1.0.5) | ~~[📏](#📏)~~ |
| Snow Bros. Wonderland | `0100A0A01D520000` | `19A8A4E8372DEF43` (◯, v0, 1.0.0) |  |
| SnowRunner | `0100FBD013AB6000` | `44C6A5004C499464` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/44C6A5004C499464.yaml), v27, 1.0.31) <br> `1B45F85E3DE5615D` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/1B45F85E3DE5615D.yaml), v28, 1.0.32) <br> `EA6728F9AE46C055` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/EA6728F9AE46C055.yaml), v29, 1.0.33) <br> `0D96442AC907A3F8` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/0D96442AC907A3F8.yaml), v30, 1.0.34) <br> `9976A5B49537F7D7` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/9976A5B49537F7D7.yaml), v31, 1.0.35) <br> `038858A1EC679156` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/038858A1EC679156.yaml), v32, 1.0.36) <br> `CD9E844E29E8CA80` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/CD9E844E29E8CA80.yaml), v33, 1.0.37) <br> `53531030A4199B74` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/53531030A4199B74.yaml), v34, 1.0.38) <br> `3E9AC9266BB21FC4` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/3E9AC9266BB21FC4.yaml), v35, 1.0.39) <br> `54551AEABF6E1F41` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/B37F6B200EF31DFC.yaml), v36, 1.0.40) <br> `54551AEABF6E1F41` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/54551AEABF6E1F41.yaml), v37, 1.0.41) <br> `8C7A99CBD1AEA208` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/8C7A99CBD1AEA208.yaml), v38, 1.0.42) | ~~[📏](#📏)~~ |
| Snufkin: Melody of Moominvalley | `010085001A17C000` | `00A50433964D3448` (◯, v7, 1.5.2) |  |
| Solar Ash | `010083501AB36000` | `0959D87753F9FED4` ([✅](SaltySD/plugins/FPSLocker/patches/010083501AB36000/0959D87753F9FED4.yaml), v1, 1.06.0) | ~~[📏](#📏)~~ |
| SOMA | `0100927023A34000` | `9BD1FF915EE92EAA` (❌, v4, 1.4.0) | [🔐](#🔐)[⏱️](#⏱️)[🏃](#🏃) |
| Song of Nunu: A League of Legends Story | `01004F401BEBE000` | `DF2D64FB63F1BD00` ([✅](SaltySD/plugins/FPSLocker/patches/01004F401BEBE000/DF2D64FB63F1BD00.yaml), v2, 1.0.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Sonic Colours: Ultimate | `010040E0116B8000` | `957E1E19958193F9` (◯, v7, 1.0.9) |  |
| SONIC FORCES | `01001270012B6000` | `6D9EA94F8AAC00A8` ([✅](SaltySD/plugins/FPSLocker/patches/01001270012B6000/6D9EA94F8AAC00A8.yaml), v2, 1.2.0) | ~~[🔐](#🔐)[⚔️](#⚔️)~~[🔢](#🔢) |
| SONIC FORCES DIGITAL BONUS EDITION | `0100111004460000` | `6D9EA94F8AAC00A8` ([✅](SaltySD/plugins/FPSLocker/patches/0100111004460000/6D9EA94F8AAC00A8.yaml), v1, 1.1.0) | ~~[🔐](#🔐)[⚔️](#⚔️)~~[🔢](#🔢) |
| Sonic Frontiers | `01004AD014BF0000` | `D7A05D106FF46FC0` ([✅](SaltySD/plugins/FPSLocker/patches/01004AD014BF0000/D7A05D106FF46FC0.yaml), v7, 1.4.1) | ~~[🔐](#🔐)[📏](#📏)~~ |
| SONIC GENERATIONS | `01005EA01C0FC001` | `D91C67509C6AED8D` ([✅](SaltySD/plugins/FPSLocker/patches/01005EA01C0FC001/D91C67509C6AED8D.yaml), v2, 1.1.0) | ~~[🔐](#🔐)~~ |
| Sonic Racing: CrossWorlds | `01006E001823C000` | `CF82524FEAE270B6` (❌, v2, 1.12) | [🔐](#🔐)[⏱️](#⏱️)[🏃](#🏃) |
| Sorry We're Closed | `010024E01DC6A000` | `AA9BF85240409E60` (◯, v6, 1.0.7) |  |
| Soul Stalker | `0100F0401C2BC000` | `38730D109E48050C` ([✅](SaltySD/plugins/FPSLocker/patches/0100F0401C2BC000/38730D109E48050C.yaml), v2, 1.0.2) | ~~[📷](#📷)~~ |
| Soundfall | `0100B7A01386E000` | `39F1BCCB912A12DF` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7A01386E000/39F1BCCB912A12DF.yaml), v3, 1.3.17957) <br> `3AEEE2266CD84B1E` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7A01386E000/3AEEE2266CD84B1E.yaml), v4, 1.5.18245) | ~~[📏](#📏)[🔧](#🔧)~~ |
| South of the Circle | `0100E97016F60000` | `4FB83BAB154A2B56` (◯, v3, 1.0.3) |  |
| SOUTH PARK: SNOW DAY! | `0100D1501ABAE000` | `086789EC0FDA4BF1` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1501ABAE000/086789EC0FDA4BF1.yaml), v5, 1.0.5) <br> `2B7E5D5B9A730F77` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1501ABAE000/2B7E5D5B9A730F77.yaml), v6, 1.0.6) <br> `DCBE53FDF98752AF` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1501ABAE000/DCBE53FDF98752AF.yaml), v7, 1.0.7) <br> `C58AA3A366F82F70` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1501ABAE000/C58AA3A366F82F70.yaml), v8, 1.0.8) <br> `9A2DB2F402A31811` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1501ABAE000/9A2DB2F402A31811.yaml), v10, 1.0.10) <br> `4B7F793B8355C016` ([✅](SaltySD/plugins/FPSLocker/patches/0100D1501ABAE000/4B7F793B8355C016.yaml), v11, 1.0.11) | ~~[📏](#📏)[🔧](#🔧)~~ |
| South Park: The Fractured But Whole | `01008F2005154000` | `DF15EDAAF603E00C` (❌, v5, 1.05) | [⚔️](#⚔️) |
| South Park: The Stick Of Truth `US` | `010095300B6A4000` | `BB789D7392B165F5` (❌📌, v1, 1.01) | [🔐](#🔐)[⚔️](#⚔️) |
| South Park: The Stick Of Truth `EUR` | `010043600B6A6000` | `5BEA90B5335C9B60` (❌📌, v1, 1.01) | [🔐](#🔐)[⚔️](#⚔️) |
| Space Marshals | `0100782013A04000` | `A7790E95F4A47885` (◯, v0, 1.0.2) |  |
| Space Marshals 3 | `0100FC10159EC000` | `0AFE1AE664D9AFA1` ([✅](SaltySD/plugins/FPSLocker/patches/0100FC10159EC000/0AFE1AE664D9AFA1.yaml), v0, 1.0.0) | ~~[🔐](#🔐)~~ |
| Space Tail: Every Journey Leads Home | `0100C37019BC2000` | `0CD7D5F5600CB448` (◯, v1, 1.0.1) |  |
| Spark The Electric Jester 3 | `0100D9901DD98000` | `BACDD75FE7F8882F` (◯, v1, 1.1) |  |
| Speed Crew | `0100C1201A558000` | `998838513F72152F` (◯, v6, 1.2.0) |  |
| Spiritfarer | `0100BD400DC52000` | `482B575F4CCE512B` (◯, v15, 1.15) |  |
| Split | `010071801AB2A000` | `D008ADF7F5DA3315` (◯, v1, 1.1.0) |  |
| SpongeBob SquarePants: The Cosmic Shake | `01009FB0172F4000` | `F712547C68C66A0A` ([✅](SaltySD/plugins/FPSLocker/patches/01009FB0172F4000/F712547C68C66A0A.yaml), v7, 1.0.7) | ~~[📏](#📏)[🔧](#🔧)~~ |
| SpongeBob SquarePants: The Patrick Star Game | `01008AF01AD22000` | `8F3E77E1322E9F6F` ([✅](SaltySD/plugins/FPSLocker/patches/01008AF01AD22000/8F3E77E1322E9F6F.yaml), v1, 1.0.1) <br> `222C0A2546723943` ([✅](SaltySD/plugins/FPSLocker/patches/01008AF01AD22000/222C0A2546723943.yaml), v2, 1.0.2) | ~~[🏃](#🏃)~~ |
| SPY×ANYA: Operation Memories | `010089B01AB44000` | `48419AE7D9BE8B45` (◯, v1, 1.0.1) |  |
| Spyro Reignited Trilogy | `010077B00E046000` | `D2775FAFCF4835CB` ([✅](SaltySD/plugins/FPSLocker/patches/010077B00E046000/D2775FAFCF4835CB.yaml), v1, 1.01) | ~~[🔐](#🔐)[📏](#📏)~~ |
| STAR OCEAN THE SECOND STORY R | `010065301A2E0000` | `D214BA64D902AEDA` (◯, v3, 1.1.0) |  |
| Star Overdrive | `010047E01EA24000` | `C0D9B410A09A4ADD` ([✅](SaltySD/plugins/FPSLocker/patches/010047E01EA24000/C0D9B410A09A4ADD.yaml), v5, 1.0.5) <br> `728D92CB9E54CE7A` ([✅](SaltySD/plugins/FPSLocker/patches/010047E01EA24000/728D92CB9E54CE7A.yaml), v8, 1.0.8) <br> `6D05923E7005E182` ([✅](SaltySD/plugins/FPSLocker/patches/010047E01EA24000/6D05923E7005E182.yaml), v9, 1.0.10) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Starlink: Battle for Atlas | `01002CC003FE6000` | `13C816F2A273653C` (❌📌, v6, 1.0.6) | [📏](#📏) |
| SteamWorld Build | `01004E401B3EA000` | `017834F19C49FA71` (◯, v16, 1.0.156) |  |
| Storm Lancers | `01002A4021B86000` | `99519C9259122E4F` ([✅](SaltySD/plugins/FPSLocker/patches/01002A4021B86000/99519C9259122E4F.yaml), v3, 1.0.1.72) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| STORY OF SEASONS: A Wonderful Life | `010076801929A000` | `FDBD3A3B672290F8` (❌, v2, 1.0.2) | [⚔️](#⚔️) |
| Stray | `010075101EF84000` | `109D974E180A5AA1` ([✅](SaltySD/plugins/FPSLocker/patches/010075101EF84000/109D974E180A5AA1.yaml), v2, 1.6.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Strike Force 3 | `010060200F080000` | `8507336565D4C86B` (❌📌, v1, 1.1.0) | [📏](#📏) |
| Stubbs the Zombie in Rebel Without a Pulse | `0100964012528000` | `ECF4B91AF1B669EC` (❌, v3, 1.0.3) | [⚔️](#⚔️) |
| Subnautica | `0100429011144000` | `B3DB5A1EDAF8454F` (◯, v5, 1.21.71113) |  |
| Subnautica Below Zero | `010014C011146000` | `5B050C55B8264040` (◯, v8, 1.21.49397) |  |
| Suikoden I&II HD Remaster | `01004BD017080000` | `A481E5E6A88FDFB7` (❌, v3, 1.0.3) | [⏱️](#⏱️) |
| Super Crazy Rhythm Castle | `01005B7017828000` | `90B9B162B022DCBF` (◯, v0, 1.0.0.0) |  |
| Super Kirby Clash | `01003FB00C5A8000` | `DCDFA5A4AD9A175D` ([✅](SaltySD/plugins/FPSLocker/patches/01003FB00C5A8000/DCDFA5A4AD9A175D.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[⚔️](#⚔️)~~ |
| Super Neptunia RPG | `01001CE00D7B6000` | `CE5C50E07FBF1E42` (◯, v2, 1.02) |  |
| SWORD ART ONLINE Alicization Lycoris | `010034501225C000` | `B6AF2C0FA614CC87` (❌, v8, 3.0.1) | [⚔️](#⚔️) |
| SWORD ART ONLINE Alicization Lycoris `US` | `0100115012260000` | `33360EA29C2FBEF2` (❌, v8, 3.0.1) | [⚔️](#⚔️) |
| - 刀劍神域 彼岸遊境<br>- 소드 아트 온라인 앨리시제이션 리코리스 | `0100AF0013970000` | `948CA1FDC708FB22` (❌, v8, 3.0.1) | [⚔️](#⚔️) |
| ソードアート・オンライン アリシゼーション リコリス | `0100C6C01225A000` | `6177B5F818BF234D` (❌, v8, 3.0.1) | [⚔️](#⚔️) |
| SWORD ART ONLINE: FATAL BULLET | `01005DF00DC26000` | `029C2837B0EEE8A9` ([✅](SaltySD/plugins/FPSLocker/patches/01005DF00DC26000/029C2837B0EEE8A9.yaml), v2, 1.2.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| ソードアート・オンライン フェイタル・バレット | `0100E4700C648000` | `171EC82D8156810B` (❌📌, v2, 1.2.0) | [🔐](#🔐)[📏](#📏) |
| SWORD ART ONLINE Fractured Daydream `EUR` | `0100727018A10000` | `2EEE840599DC7021` ([✅](SaltySD/plugins/FPSLocker/patches/0100727018A10000/2EEE840599DC7021.yaml), v14, 1.5.2.0) | [🔐](#🔐)[📏](#📏)[🔧](#🔧) |
| SWORD ART ONLINE Fractured Daydream `US` | `0100478018A0E000` | `2EEE840599DC7021` ([✅](SaltySD/plugins/FPSLocker/patches/0100478018A0E000/2EEE840599DC7021.yaml), v14, 1.5.2.0) | [🔐](#🔐)[📏](#📏)[🔧](#🔧) |
| - 刀劍神域 碎夢邊境<br>- 소드 아트 온라인 프랙처드 데이드림 | `0100F85018A14000` | `2EEE840599DC7021` ([✅](SaltySD/plugins/FPSLocker/patches/0100F85018A14000/2EEE840599DC7021.yaml), v14, 1.5.2.0) | [🔐](#🔐)[📏](#📏)[🔧](#🔧) |
| ソードアート・オンライン フラクチュアード デイドリーム | `010009D018A06000` | `3AAA28C9CB8367B9` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/3AAA28C9CB8367B9.yaml), v2, 1.1.1) <br> `520620FBA0B196A3` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/520620FBA0B196A3.yaml), v3, 1.1.2) <br> `3889588A60E1F399` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/3889588A60E1F399.yaml), v4, 1.1.3) <br> `46094C03E2EC668B` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/46094C03E2EC668B.yaml), v5, 1.2.0) <br> `26C1E658E9B5B612` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/26C1E658E9B5B612.yaml), v6, 1.2.1) <br> `012A8C2C413E79B8` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/012A8C2C413E79B8.yaml), v7, 1.2.2) <br> `C2F2C4B700B30598` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/C2F2C4B700B30598.yaml), v8, 1.3.0) <br> `33614E4F6B3267B3` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/33614E4F6B3267B3.yaml), v12, 1.4.1.1) <br> `CA61076D0CE6670D` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/CA61076D0CE6670D.yaml), v13, 1.5.0.0) <br> `2EEE840599DC7021` ([✅](SaltySD/plugins/FPSLocker/patches/010009D018A06000/2EEE840599DC7021.yaml), v14, 1.5.2.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| SWORD ART ONLINE: Hollow Realization `EUR` | `01001B600D1D6000` | `0C356A98BCF20184` (❌, v2, 1.0.2) | [⚔️](#⚔️) |
| SWORD ART ONLINE: Hollow Realization `US` | `0100EC400D54E000` | `03012E346B96E992` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| ソードアート・オンライン -ホロウ・リアリゼーション- | `0100A1100B70E000` | `7C8571B3F244B6DC` (❌, v2, 1.0.2) | [⚔️](#⚔️) |
| Sword of the Necromancer: Resurrection | `01006AC01F630000` | `B70551B5A2D0F15F` ([✅](SaltySD/plugins/FPSLocker/patches/01006AC01F630000/B70551B5A2D0F15F.yaml), v3, 1.0.3) <br> `7C37B073B19F3CCF` ([✅](SaltySD/plugins/FPSLocker/patches/01006AC01F630000/7C37B073B19F3CCF.yaml), v4, 1.0.4) <br> `FFF55266A618D06A` ([✅](SaltySD/plugins/FPSLocker/patches/01006AC01F630000/FFF55266A618D06A.yaml), v5, 1.0.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| SWORD OF THE VAGRANT | `0100BD000CB2C000` | `1F1363EC8CC83C73` ([✅](SaltySD/plugins/FPSLocker/patches/0100BD000CB2C000/1F1363EC8CC83C73.yaml), v1, 1.1) | ~~[📏](#📏)~~ |
| SWORN | `0100BED01E6EE000` | `87F1CEF6D52392AE` ([✅](SaltySD/plugins/FPSLocker/patches/0100BED01E6EE000/87F1CEF6D52392AE.yaml), v2, 1.0.2) | ~~[📏](#📏)~~ |
| Tails Noir | `01006DC012B00000` | `EAAB46ED1E4989C0` ([✅](SaltySD/plugins/FPSLocker/patches/01006DC012B00000/EAAB46ED1E4989C0.yaml), v1, 1.0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |\
| Tails of Iron | `0100EF3013F60000` | `6A28EE5E39F76B6A` (◯, v4, 5) |  |
| Tails of Iron 2: Whiskers of Winter | `01002A701DB9E000` | `435907EA16A90FC5` (◯, v5, 2.4) |  |
| Tales of Kenzera: TAU | `01005C7015D30000` | `110D8FB47B55EA19` ([✅](SaltySD/plugins/FPSLocker/patches/01005C7015D30000/110D8FB47B55EA19.yaml), v4, 1.4.0) <br> `9E7FB72540D748BA` ([✅](SaltySD/plugins/FPSLocker/patches/01005C7015D30000/9E7FB72540D748BA.yaml), v5, 1.5.0) | ~~[🔧](#🔧)~~ |
| Tales from the Borderlands | `0100F0C011A68000` | `818C98B885460561` (◯, v0, 1.0.0) |  |
| Tales of Graces f Remastered | `01005E701D168000` | `49700C9DA58DAD47` (◯, v3, 1.0.3) |  |
| Tales of Symphonia Remastered | `0100A410169A4000` | `42673F5DE16DC698` (❌, v4, 1.3.1) | [⏱️](#⏱️)[🖥️](#🖥️)[⚔️](#⚔️) |
| Tales of the Shire | `010094D01DC7E000` | `80876AF5CEF98E23` (◯, v5, 1.0.5) |  |
| Tales of Xillia Remastered | `0100F1101BB9E000` | `171806C35E4152E7` ([✅](SaltySD/plugins/FPSLocker/patches/0100F1101BB9E000/171806C35E4152E7.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)~~ |
| テイルズ オブ エクシリア リマスター | `010058301BB98000` | `4779B3A56B655418` ([✅](SaltySD/plugins/FPSLocker/patches/010058301BB98000/4779B3A56B655418.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)~~ |
| 테일즈 오브 엑실리아 리마스터 | `01003CC01BBA0000` | `D64B8283BD5CEA63` ([✅](SaltySD/plugins/FPSLocker/patches/01003CC01BBA0000/D64B8283BD5CEA63.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)~~ |
| Tamagotchi Plaza | `010064C01A9BA000` | `1BA8D8FD3897F22F` ([✅](SaltySD/plugins/FPSLocker/patches/010064C01A9BA000/1BA8D8FD3897F22F.yaml), v4, 1.0.4) <br> `FB852EECDE7A745D` ([✅](SaltySD/plugins/FPSLocker/patches/010064C01A9BA000/FB852EECDE7A745D.yaml), v5, 1.0.5) <br> `E73AB32BD1B16098` ([✅](SaltySD/plugins/FPSLocker/patches/010064C01A9BA000/E73AB32BD1B16098.yaml), v6, 1.0.6) | ~~[🔐](#🔐)~~ |
| たまごっちのプチプチおみせっち おまちど～さま！ | `010040601A9B8000` | `9ACE779510EC93C9` ([✅](SaltySD/plugins/FPSLocker/patches/010040601A9B8000/9ACE779510EC93C9.yaml), v2, 1.0.2) | ~~[🔐](#🔐)~~ |
| Taxi Chaos | `0100B76011DAA000` | `C5D73D3EDAADACB2` ([✅](SaltySD/plugins/FPSLocker/patches/0100B76011DAA000/C5D73D3EDAADACB2.yaml), v2, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Taxi Driver - The Simulation | `010073A010430000` | `2972E95EEFF95144` ([✅](SaltySD/plugins/FPSLocker/patches/010073A010430000/2972E95EEFF95144.yaml), v0, 1.0.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| TCG Card Market Simulator | `01001560214B8000` | `15532623187C22FF` (◯, v1, 1.0.1) |  |
| Tchia | `0100CEE01D23C000` | `76B6E5E830A43D97` ([✅](SaltySD/plugins/FPSLocker/patches/0100CEE01D23C000/76B6E5E830A43D97.yaml), v1, 1.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Team Sonic Racing | `010084B00B36E000` | `7D942261130F42A7` (◯, v3, 1.0.3) |  |
| Team Sonic Racing `US` | `010092B0091D0000` | `AD75285A65EB6FFD` (◯, v2, 1.0.3) |  |
| Terra Nil | `01006D501D14A000` | `C8BCCB615DA4BD6C` (◯, v7, 1.2.10) |  |
| Terraformers | `0100C1B01872A000` | `EFA897C8B97F1C9E` (◯, v6, 1.6.21) |  |
| The Beast Inside | `010028901FF00000` | `EB58D577539E9151` ([✅](SaltySD/plugins/FPSLocker/patches/010028901FF00000/EB58D577539E9151.yaml), v2, 1.2.0) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| The Bridge Curse - Road to Salvation | `01006BD019A78000` | `F54FC539CAF24C64` ([✅](SaltySD/plugins/FPSLocker/patches/01006BD019A78000/F54FC539CAF24C64.yaml), v1, 1.6.0.1) | ~~[🔧](#🔧)~~ |
| The Bridge Curse 2: The Extrication | `010033501FF38000` | `B7F344920B6D140E` ([✅](SaltySD/plugins/FPSLocker/patches/010033501FF38000/B7F344920B6D140E.yaml), v1, 1.0.1) | ~~[🔧](#🔧)~~ |
| The Caligula Effect: Overdose | `010069100B7F0000` | `A953B35A45BEA33D` ([✅](SaltySD/plugins/FPSLocker/patches/010069100B7F0000/A953B35A45BEA33D.yaml), v1, 1.01) | ~~[📏](#📏)~~ |
| The Caligula Effect 2 | `0100CC3014886000` | `9265FE6C4DE9600E` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC3014886000/9265FE6C4DE9600E.yaml), v1, 1.1.0) | ~~[🔧](#🔧)~~ |
| The Dark Pictures Anthology: Little Hope | `010084F017B32000` | `2BFF5F7711EE6C9F` ([✅](SaltySD/plugins/FPSLocker/patches/010084F017B32000/2BFF5F7711EE6C9F.yaml), v0, 1.0.0) | ~~[🔐](#🔐)~~ | 
| The Dark Pictures Anthology: Man of Medan | `0100711017B30000` | `2C7A626BA5F25D5F` ([✅](SaltySD/plugins/FPSLocker/patches/0100711017B30000/2C7A626BA5F25D5F.yaml), v1, 1.0.1) | ~~[🔐](#🔐)~~ | 
| The Elder Scrolls V: Skyrim | `01000A10041EA000` | `4F7995092FAA5DC0` ([✅](SaltySD/plugins/FPSLocker/patches/01000A10041EA000/4F7995092FAA5DC0.yaml), v5, 1.1.392.3925134) | ~~[📏](#📏)~~ |
| The Entropy Centre | `0100DDD01ACAA000` | `7AF502E140C13759` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| The Exit 8 | `01003BF01E940000` | `5346BDF1EEC2BA4C` ([✅](SaltySD/plugins/FPSLocker/patches/01003BF01E940000/5346BDF1EEC2BA4C.yaml), v9, 1.0.9) | ~~[📏](#📏)[🔧](#🔧)~~ |
| The Forest Quartet | `010010A01BBF4000` | `47A022F858BA09B1` ([✅](SaltySD/plugins/FPSLocker/patches/010010A01BBF4000/47A022F858BA09B1.yaml), v2, 4.0.2) | ~~[📏](#📏)~~ |
| The friends of Ringo Ishikawa | `010030700CBBC000` | `3749BFEA64DC98DF` (❌, v3, 1.0.3) | [🔐](#🔐)[⏱️](#⏱️)[🖥️](#🖥️) |
| The Great Ace Attorney Chronicles `GLOBAL` | `010036E00FB20000` | `1DA748FC9499882F` ([✅](SaltySD/plugins/FPSLocker/patches/010036E00FB20000/1DA748FC9499882F.yaml), v0, 1.0.0) | ~~[🔐](#🔐)~~ |
| The Great Ace Attorney Chronicles `ASIA` | `0100D7F00FB1A000` | `D871B992E95B71C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7F00FB1A000/D871B992E95B71C5.yaml), v0, 1.0.0) | ~~[🔐](#🔐)~~ |
| The Hundred Line -Last Defense Academy- | `010093C0215B4000` | `7816CA5FECA60315` ([✅](SaltySD/plugins/FPSLocker/patches/010093C0215B4000/7816CA5FECA60315.yaml), v2, 1.0.3) <br> `26350BBA224575AE` ([✅](SaltySD/plugins/FPSLocker/patches/010093C0215B4000/26350BBA224575AE.yaml), v4, 1.0.5) <br> `5AF690F4A8BFCC67` ([✅](SaltySD/plugins/FPSLocker/patches/010093C0215B4000/5AF690F4A8BFCC67.yaml), v5, 1.0.6) <br> `EAADF33F510C5853` ([✅](SaltySD/plugins/FPSLocker/patches/010093C0215B4000/EAADF33F510C5853.yaml), v6, 1.1.1) <br> `D1D3FFB94AB458B4` ([✅](SaltySD/plugins/FPSLocker/patches/010093C0215B4000/D1D3FFB94AB458B4.yaml), v7, 1.1.2) | ~~[🔐](#🔐)~~ |
| The Knight Witch | `0100E8501816E000` | `9C09F15234A270E4` (◯, v5, 1.0.5) |  |
| The Last Worker | `0100ADC014CDE000` | `DAAADE43EA48F66B` (◯, v2, 1.0.4) |  |
| The Legend of Heroes: Trails into Reverie | `01008CB0156BC000` | `7735C8DD89D145F2` ([✅](SaltySD/plugins/FPSLocker/patches/01008CB0156BC000/7735C8DD89D145F2.yaml), v4, 1.0.4) | ~~[🔐](#🔐)[👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️)[🔧](#🔧)~~ |
| 英雄伝説 創の軌跡 | `010053D014C44000` | `086367BD573D1899` ([✅](SaltySD/plugins/FPSLocker/patches/010053D014C44000/086367BD573D1899.yaml), v6, 1.0.6) | ~~[🔐](#🔐)~~ |
| The Legend of Heroes: Trails of Cold Steel III | `01005420101DA000` | `134EC3D8BE75126F` ([✅](SaltySD/plugins/FPSLocker/patches/01005420101DA000/134EC3D8BE75126F.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)[🔧](#🔧)~~ |
| 英雄伝説 閃の軌跡Ⅲ | `0100E57010542000` | `3FB33205C25D3436` ([✅](SaltySD/plugins/FPSLocker/patches/0100E57010542000/3FB33205C25D3436.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)[🔧](#🔧)~~ |
| 英雄傳說 閃之軌跡III | `010044D015F4A000` | `37C3FAEFC9A4C374` ([✅](SaltySD/plugins/FPSLocker/patches/010044D015F4A000/37C3FAEFC9A4C374.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)[🔧](#🔧)~~ |
| The Legend of Heroes: Trails of Cold Steel IV | `0100D3C010DE8000` | `59159483CF88330F` ([✅](SaltySD/plugins/FPSLocker/patches/0100D3C010DE8000/59159483CF88330F.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)[🔧](#🔧)~~ |
| 英雄伝説 閃の軌跡Ⅳ | `010064101356C000` | `652D04C4BD51AE83` ([✅](SaltySD/plugins/FPSLocker/patches/010064101356C000/652D04C4BD51AE83.yaml), v2, 1.0.2) | ~~[🔐](#🔐)[👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)[🔧](#🔧)~~ |
| 영웅전설 섬의 궤적 IV | `0100DE90162A0000` | `0BBD86F62F380844` ([✅](SaltySD/plugins/FPSLocker/patches/0100DE90162A0000/0BBD86F62F380844.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️)[🔢](#🔢)[🔧](#🔧)~~ |
| The Legend of Heroes: Trails through Daybreak | `010040C01D248000` | `43D0D0D68A22E370` ([✅](SaltySD/plugins/FPSLocker/patches/010040C01D248000/43D0D0D68A22E370.yaml), v1, 1.0.1) | ~~[🔐](#🔐)~~ |
| The Legend of Heroes: Trails through Daybreak II | `0100F6701FED4000` | `7CE83658C7B53BB6` ([✅](SaltySD/plugins/FPSLocker/patches/0100F6701FED4000/7CE83658C7B53BB6.yaml), v1, 1.0.1) <br> `EBB5459731354538` ([✅](SaltySD/plugins/FPSLocker/patches/0100F6701FED4000/EBB5459731354538.yaml), v2, 1.0.2) | ~~[⏱️](#⏱️)~~ |
| 英雄傳說 黎之軌跡Ⅱ | `010033801EF3A000` | `503ACC27B3F97603` ([✅](SaltySD/plugins/FPSLocker/patches/010033801EF3A000/503ACC27B3F97603.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)~~ |
| 英雄伝説 黎の軌跡II | `01009EE01EB02000` | `63A4CF08E30A56B1` ([✅](SaltySD/plugins/FPSLocker/patches/01009EE01EB02000/63A4CF08E30A56B1.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)~~ |
| The Legend of Legacy HD Remastered | `010099F01C258000` | `3E659DB2F020AC3B` (❌, v3, 1.0.3) | [⏱️](#⏱️)[🖥️](#🖥️) |
| The Legend of Zelda: Breath of the Wild | `01007EF00011E000` | `8E9978D50BDD20B4` ([✅](SaltySD/plugins/FPSLocker/patches/01007EF00011E000/8E9978D50BDD20B4.yaml), v12, 1.6.0) <br> `A12F75F49B36F4B8` ([✅](SaltySD/plugins/FPSLocker/patches/01007EF00011E000/A12F75F49B36F4B8.yaml), v15, 1.8.1) <br> `DE0B6AC4EFC1DDA7` ([✅](SaltySD/plugins/FPSLocker/patches/01007EF00011E000/DE0B6AC4EFC1DDA7.yaml), v16, 1.8.2) | ~~[📏](#📏)[⚔️](#⚔️)[⏱️](#⏱️)[🏃](#🏃)[🖥️](#🖥️)[📺](#📺)[🔢](#🔢)~~ |
| The Legend of Zelda: Tears of the Kingdom | `0100F2C0115B6000` | `9B4E43650501A4D4` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2C0115B6000/9B4E43650501A4D4.yaml), v6, 1.2.1) <br> `6265F94D606242CE` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2C0115B6000/6265F94D606242CE.yaml), v8, 1.4.0) <br> `965EAB9CEB8EB867` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2C0115B6000/965EAB9CEB8EB867.yaml), v9, 1.4.1) <br> `5CB42B1CF25469FB` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2C0115B6000/5CB42B1CF25469FB.yaml), v10, 1.4.2) | ~~[📏](#📏)[⚔️](#⚔️)[⏱️](#⏱️)[🏃](#🏃)[🖥️](#🖥️)[📺](#📺)[🔢](#🔢)~~ |
| The LEGO Movie 2 - Videogame | `0100A4400BE74000` | `BAC1309DDF75B14D` (◯, v3, 1.0.3) |  |
| The LEGO NINJAGO Movie Video Game | `01000CE002072000` | `346959B36CD9F14D` ([✅](SaltySD/plugins/FPSLocker/patches/01000CE002072000/346959B36CD9F14D.yaml), v3, 1.0.3) | ~~[📺](#📺)~~ |
| The Outer Worlds | `0100626011656000` | `761CD556AB357C87` ([✅](SaltySD/plugins/FPSLocker/patches/0100626011656000/761CD556AB357C87.yaml), v5, 1.0.5) | ~~[📏](#📏)~~ |
| The Settlers: New Allies | `0100F3200E7CA000` | `EAA0B789264F2A75` ([✅](SaltySD/plugins/FPSLocker/patches/0100F3200E7CA000/EAA0B789264F2A75.yaml), v7, 1.0.7) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Sinking City | `010028D00BA1A000` | `85E49C169A8B988A` ([✅](SaltySD/plugins/FPSLocker/patches/010028D00BA1A000/85E49C169A8B988A.yaml), v2, 1.2.0) | ~~[📏](#📏)~~ |
| The Smurfs - Dreams | `01008E401E6D0000` | `C124FFD193F533B4` ([✅](SaltySD/plugins/FPSLocker/patches/01008E401E6D0000/C124FFD193F533B4.yaml), v1, 1.0.1) <br> `E08769D5B56A5A25` ([✅](SaltySD/plugins/FPSLocker/patches/01008E401E6D0000/E08769D5B56A5A25.yaml), v3, 1.0.3) | ~~[🔧](#🔧)~~ |
| The Smurfs Mission Vileaf | `010040A01407E000` | `BBBBB9891F01415E` (◯, v4, 1.0.19.1) |  |
| The Smurfs 2: The Prisoner of the Green Stone | `010073C01B7FE000` | `F294A4EBE966E8A9` ([✅](SaltySD/plugins/FPSLocker/patches/010073C01B7FE000/F294A4EBE966E8A9.yaml), v4, 1.04) | ~~[📏](#📏)[🔧](#🔧)~~ |
| The Stone of Madness | `01000F101B672000` | `C57C02EA53CEF928` (◯, v4, 1.0.4) |  |
| The Stretchers | `0100AA400A238000` | `14D7D1537BD5A986` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA400A238000/14D7D1537BD5A986.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Survivalists | `0100EF200DA60000` | `69A45110D07F0442` (◯, v7, 1.0.7) |  |
| The Thing: Remastered | `0100D4E01E49E000` | `B09099A6218EB51A` (❌, v3, 1.1.1) | [⚔️](#⚔️) |
| The Witcher 3: Wild Hunt - The Complete Edition `PL/CZ/HU/SK/SL` | `010039400E8D6000` | `D27FD8A515077F34` ([✅](SaltySD/plugins/FPSLocker/patches/010039400E8D6000/D27FD8A515077F34.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `West EUR/CY` | `01003D100E9C6000` | `4BC4A8A814FD46A4` ([✅](SaltySD/plugins/FPSLocker/patches/01003D100E9C6000/4BC4A8A814FD46A4.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `US` | `0100BFE00E9CA000` | `4BC4A8A814FD46A4` ([✅](SaltySD/plugins/FPSLocker/patches/0100BFE00E9CA000/4BC4A8A814FD46A4.yaml), v8, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `DE/AT` | `010076F00E9C8000` | `4BC4A8A814FD46A4` ([✅](SaltySD/plugins/FPSLocker/patches/010076F00E9C8000/4BC4A8A814FD46A4.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `RO/BG/AU/ZA/NZ` | `010070A00E9CE000` | `4BC4A8A814FD46A4` ([✅](SaltySD/plugins/FPSLocker/patches/010070A00E9CE000/4BC4A8A814FD46A4.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `KOR` | `010085500E9D0000` | `D27FD8A515077F34` ([✅](SaltySD/plugins/FPSLocker/patches/010085500E9D0000/D27FD8A515077F34.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `CHN` | `010019C00E9CC000` | `4BC4A8A814FD46A4` ([✅](SaltySD/plugins/FPSLocker/patches/010019C00E9CC000/4BC4A8A814FD46A4.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `JPN` | `01000BB00E9D2000` | `4BC4A8A814FD46A4` ([✅](SaltySD/plugins/FPSLocker/patches/01000BB00E9D2000/4BC4A8A814FD46A4.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt - The Complete Edition `LV/LT/EST` | `0100A0800E9C4000` | `D27FD8A515077F34` ([✅](SaltySD/plugins/FPSLocker/patches/0100A0800E9C4000/D27FD8A515077F34.yaml), v7, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| The Witcher 3: Wild Hunt | `0100E67012924000` | `B151A224A429F9A7` ([✅](SaltySD/plugins/FPSLocker/patches/0100E67012924000/B151A224A429F9A7.yaml), v4, 4.04b) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Thronebreaker: The Witcher Tales | `0100E910103B4000` | `1BD046113635234D` (◯, v2, 1.0.2) |  |
| Thirsty Suitors | `0100982019374000` | `9DD9149968A0B8D3` (❌, v0, NS27619.127559) | [📏](#📏) |
| Tiebreak+ | `010008301AA96000` | `2A5244CCB17B44AC` ([✅](SaltySD/plugins/FPSLocker/patches/010008301AA96000/2A5244CCB17B44AC.yaml), v1, 1.1.0) <br> `5BCA5C20C8F8A9B4` ([✅](SaltySD/plugins/FPSLocker/patches/010008301AA96000/5BCA5C20C8F8A9B4.yaml), v2, 1.2.0) <br> `88CC45A195E0BDA8` ([✅](SaltySD/plugins/FPSLocker/patches/010008301AA96000/88CC45A195E0BDA8.yaml), v3, 1.3.0) <br> `612E3D607D2A13BB` ([✅](SaltySD/plugins/FPSLocker/patches/010008301AA96000/612E3D607D2A13BB.yaml), v4, 1.4.0) | ~~[⚔️](#⚔️)[📏](#📏)~~ |
| TinTin Reporter - Cigars of the Pharaoh | `0100E9001A94C000` | `57B6B2062EC8C38A` ([✅](SaltySD/plugins/FPSLocker/patches/0100E9001A94C000/57B6B2062EC8C38A.yaml), v3, 1.3.0) <br> `ACBD89C999804FD2` ([✅](SaltySD/plugins/FPSLocker/patches/0100E9001A94C000/ACBD89C999804FD2.yaml), v5, 1.4.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Tiny Bookshop | `0100F7A023F14000` | `0097C1A5DDBB5FD4` (◯, v3, 1.0.3) |  |
| Tiny Terry's Turbo Trip | `01002B202075A000` | `BDCCA3BAAC2D40DE` (◯, v4, 1.3.1) |  |
| Tiny Troopers: Global Ops | `0100347013E4C000` | `63F1A8874A936747` (◯, v2, 1.0.0.2) |  |
| Tinykin | `0100A73016576000` | `4E2AA28721AFF2C1` ([✅](SaltySD/plugins/FPSLocker/patches/0100A73016576000/4E2AA28721AFF2C1.yaml), v4, 1.1.1) | ~~[📏](#📏)~~ |
| Tokyo Mirage Sessions<br>#FE Encore | `0100A9400C9C2000` | `33463E11899166BB` ([✅](SaltySD/plugins/FPSLocker/patches/0100A9400C9C2000/33463E11899166BB.yaml), v0, 1.0.0) | ~~[⚔️](#⚔️)[⏱️](#⏱️)[🏃](#🏃)~~[🖥️](#🖥️) |
| Tomb Raider: Definitive Edition | `0100092021C80000` | `2A4A71E176DAA356` ([✅](SaltySD/plugins/FPSLocker/patches/0100092021C80000/2A4A71E176DAA356.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ |
| Tony Hawk's Pro Skater 1 + 2 | `0100CC00102B4000` | `8AFCBE6A930CD42E` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC00102B4000/8AFCBE6A930CD42E.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[📏](#📏)~~ |
| Tony Hawk's Pro Skater 3 + 4 | `01000AD01F94A000` | `A31FE9B8AF1156D4` ([✅](SaltySD/plugins/FPSLocker/patches/01000AD01F94A000/A31FE9B8AF1156D4.yaml), v2, 1.0.3) <br> `65A9705A4BB35AA2` ([✅](SaltySD/plugins/FPSLocker/patches/01000AD01F94A000/65A9705A4BB35AA2.yaml), v4, 1.05) <br> `505069EBC0B82A6F` ([✅](SaltySD/plugins/FPSLocker/patches/01000AD01F94A000/505069EBC0B82A6F.yaml), v5, 1.06) <br> `52DA46C0166A8643` ([✅](SaltySD/plugins/FPSLocker/patches/01000AD01F94A000/52DA46C0166A8643.yaml), v6, 1.07) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Towa and the Guardians of the Sacred Tree | `0100F52019002000` | `935ABD9796226E9A` (◯, v2, 1.2) |  |
| Train Life: A Railway Simulator | `0100FC101513E000` | `A9CE4E0196706EC8` (❌📌, v1, 1.0.1) | [📏](#📏) |
| TRANSFORMERS: EARTHSPARK - Expedition | `010005001A8CA000` | `F87BEAF2C5CE13E3` ([✅](SaltySD/plugins/FPSLocker/patches/010005001A8CA000/F87BEAF2C5CE13E3.yaml), v5, 1.0.5) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| TRANSFORMERS: Galactic Trials | `0100C12017BCA000` | `F01A4E60035AF15A` ([✅](SaltySD/plugins/FPSLocker/patches/0100C12017BCA000/F01A4E60035AF15A.yaml), v1, 1.0.1) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Trek to Yomi | `0100D77019324000` | `A52C9938956331C9` ([✅](SaltySD/plugins/FPSLocker/patches/0100D77019324000/A52C9938956331C9.yaml), v3, 0.4) | ~~[📏](#📏)~~ |
| Trials Rising | `01003E800A102000` | `283095029A5AB467` ([✅](SaltySD/plugins/FPSLocker/patches/01003E800A102000/283095029A5AB467.yaml), v13, 1.0.13) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~[⚔️](#⚔️) |
| Triangle Strategy | `0100CC80140F8000` | `9CB4490E8A718BAE` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/9CB4490E8A718BAE.yaml), v4, 1.1.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Trine | `0100D9000A930000` | `32B4BBE0D88214D3` (◯, v2, 1.0.2) |  |
| Trine 2 | `010064E00A932000` | `525B902E6F916EA5` (❌, v1, 1.0.1) | [🏃](#🏃) |
| Trine 3: The Artifacts of Power | `0100DEC00A934000` | `86D9EA9CA4680295` (◯, v0, 1.0.0) |  |
| Trine 4: The Nightmare Prince | `010055E00CA68000` | `B70F06EAC87FA2AF` ([✅](SaltySD/plugins/FPSLocker/patches/010055E00CA68000/B70F06EAC87FA2AF.yaml), v3, 1.0.3) | ~~[📏](#📏)~~ |
| Trine 5: A Clockwork Conspiracy | `0100E2701A888000` | `8322528255D2CC63` ([✅](SaltySD/plugins/FPSLocker/patches/0100E2701A888000/8322528255D2CC63.yaml), v5, 1.0.5) | ~~[📏](#📏)[⚔️](#⚔️)~~ |
| Troublemaker | `01001040220E8000` | `336E56D09501A52E` ([✅](SaltySD/plugins/FPSLocker/patches/01001040220E8000/336E56D09501A52E.yaml), v1, 1.0.2) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Truck Driver | `0100CB50107BA000` | `8D94D7CA2A09FF5D` (◯, v8, 1.36) |  |
| TT Isle of Man | `010099900CAB2000` | `F2F739A2F1CAFF72` ([✅](SaltySD/plugins/FPSLocker/patches/010099900CAB2000/F2F739A2F1CAFF72.yaml), v1, 1.1.0) | ~~[📏](#📏)~~ |
| TT Isle of Man 3 | `0100FA2019AC2000` | `91CE601F6A7174CF` ([✅](SaltySD/plugins/FPSLocker/patches/0100FA2019AC2000/91CE601F6A7174CF.yaml), v7, 1.7.0) | ~~[📏](#📏)~~ |
| TUNIC | `0100DA801624E000` | `0909B4AC280D9D77` ([✅](SaltySD/plugins/FPSLocker/patches/0100DA801624E000/0909B4AC280D9D77.yaml), v3, 1.0.3) | ~~[🏃](#🏃)~~ |
| Turbo Overkill | `0100D1A01D7BA000` | `DD0c5F59DCFF0AB5` (◯, v3, 1.2.0) |  |
| Twilight Monk | `0100D7C021496000` | `5D63D46226DB106F` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7C021496000/5D63D46226DB106F.yaml), v2, 1.0.0) <br> `7926A67119144CFD` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7C021496000/7926A67119144CFD.yaml), v4, 1.2.0) <br> `E9A189C0CA87A30C` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7C021496000/E9A189C0CA87A30C.yaml), v5, 1.3.0) <br> `6D560144F6B09A98` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7C021496000/6D560144F6B09A98.yaml), v6, 1.4.0) <br> `23E85FEDEC96439C` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7C021496000/23E85FEDEC96439C.yaml), v7, 1.4.1) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Twilight Survivors | `01006F401D934000` | `8AA7D10343CB3870` ([✅](SaltySD/plugins/FPSLocker/patches/01006F401D934000/8AA7D10343CB3870.yaml), v7, 0.22.2) <br> `D71970AAA5D34DD0` ([✅](SaltySD/plugins/FPSLocker/patches/01006F401D934000/D71970AAA5D34DD0.yaml), v8, 1.0.8) <br> `66FCB9B306005BBA` ([✅](SaltySD/plugins/FPSLocker/patches/01006F401D934000/66FCB9B306005BBA.yaml), v9, 1.0.9) <br> `E3FBEB5A9C7788CD` ([✅](SaltySD/plugins/FPSLocker/patches/01006F401D934000/E3FBEB5A9C7788CD.yaml), v10, 1.0.10) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Two Point Campus | `0100D4A012FF2000` | `6B90F22CBD35F468` (◯, v29, 10.2.144623) |  |
| TY the Tasmanian Tiger 2 | `0100BC701417A000` | `1F8808E4FC7516D2` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| UFO ROBOT GRENDIZER - The Feast of the Wolves | `0100F1601EF78000` | `848AF40012A27078` (◯, v2, 1.2) |  |
| Ultra Age | `01008D4015904000` | `CA77083E259D87A2` ([✅](SaltySD/plugins/FPSLocker/patches/01008D4015904000/CA77083E259D87A2.yaml), v7, 2.0.4) | ~~[📏](#📏)~~ |
| Ultra Kaiju Monster Rancher | `01008E0019388000` | `53384CC3D2B4CA9F` (❌, v0, 1.0.1) | [⏱️](#⏱️)[🖥️](#🖥️) |
| Umurangi Generation | `0100CA3014ADE000` | `372AB37327DB2C31` ([✅](SaltySD/plugins/FPSLocker/patches/0100CA3014ADE000/372AB37327DB2C31.yaml), v6, 1.6.6.0) | ~~[🔐](#🔐)~~ |
| Unbox: Newbie's Adventure | `0100592005164000` | `83A6B710A3F3F4F9` ([✅](SaltySD/plugins/FPSLocker/patches/0100592005164000/83A6B710A3F3F4F9.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[🔧](#🔧)~~ |
| Unbound: Worlds Apart | `0100C5A013B7A000` | `1B98D227021142B1` ([✅](SaltySD/plugins/FPSLocker/patches/0100C5A013B7A000/1B98D227021142B1.yaml), v3, 1.0.3) | ~~[🔧](#🔧)~~ |
| Undertale | `010080B00AD66000` | `24DB41FCD513D080` (❌, v2, 1.11) | [🔐](#🔐)[⏱️](#⏱️) |
| Undungeon | `0100CA3018EA4000` | `6A5B168E1D2C6647` (◯, v0, 0.002) |  |
| Unravel Two | `0100E5D00CC0C000` | `F04D4FE8BF580369` (❌, v1, 1.0.1) | [⚔️](#⚔️) |
| Upin & Ipin Universe | `010058C01F3EE000` | `A15393F630A9767F` ([✅](SaltySD/plugins/FPSLocker/patches/010058C01F3EE000/A15393F630A9767F.yaml), v1, 1.0.1) <br> `301E4A1FB0BA1575` ([✅](SaltySD/plugins/FPSLocker/patches/010058C01F3EE000/301E4A1FB0BA1575.yaml), v2, 1.0.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| V-Rally 4 | `010064400B138000` | `EB8A679B5DDD0060` ([✅](SaltySD/plugins/FPSLocker/patches/010064400B138000/EB8A679B5DDD0060.yaml), v2, 1.2.0) | ~~[📏](#📏)~~ |
| Valkyria Chronicles | `0100CAF00B744000` | `FE77FFB8CBFB3A5C` ([✅](SaltySD/plugins/FPSLocker/patches/0100CAF00B744000/FE77FFB8CBFB3A5C.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)~~[🖥️](#🖥️)[⚔️](#⚔️) |
| 戦場のヴァルキュリア | `0100E6900A5A8000` | `A184B59D5091B68A` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6900A5A8000/A184B59D5091B68A.yaml), v1, 1.0.1) | ~~[⏱️](#⏱️)~~[🖥️](#🖥️)[⚔️](#⚔️) |
| Valkyria Chronicles 4 | `01005C600AC68000` | `3758602AA47ADD37` (❌, v0, 1.0.0) | [👄](#👄)[⏱️](#⏱️)[🖥️](#🖥️) |
| Vampire: The Masquerade – Swansong | `01007EE01318E000` | `36080563369C45D8` (◯, v0, 1.0.0) |  |
| Vampyr | `01000BD00CE64000` | `E417100FFEEFD1DE` ([✅](SaltySD/plugins/FPSLocker/patches/01000BD00CE64000/E417100FFEEFD1DE.yaml), v2, 0.4) | ~~[📏](#📏)~~ |
| Warhammer 40,000: Boltgun | `01005FD017E60000` | `7C992B6A003C599F` ([✅](SaltySD/plugins/FPSLocker/patches/01005FD017E60000/7C992B6A003C599F.yaml), v3, 1.0.0.3) <br> `B8630C6EE3A22FE8` ([✅](SaltySD/plugins/FPSLocker/patches/01005FD017E60000/B8630C6EE3A22FE8.yaml), v5, 1.0.0.6) <br> `3E961285846C72A5` ([✅](SaltySD/plugins/FPSLocker/patches/01005FD017E60000/3E961285846C72A5.yaml), v6, 1.0.0.7) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Warhammer 40000: Shootas, Blood & Teef | `010088B0155E2000` | `C9300E99B4975DCF` (◯, v3, 1.0.3_Switch) |  |
| WARRIORS: Abyss | `01005AE0209A8000` | `50C9028B61A0BB7F` ([✅](SaltySD/plugins/FPSLocker/patches/01005AE0209A8000/50C9028B61A0BB7F.yaml), v3, 1.1.0) <br> `293D73083149473E` ([✅](SaltySD/plugins/FPSLocker/patches/01005AE0209A8000/293D73083149473E.yaml), v6, 1.2.1) <br> `71C5F3CB333F1542` ([✅](SaltySD/plugins/FPSLocker/patches/01005AE0209A8000/71C5F3CB333F1542.yaml), v8, 1.3.0) <br> `36B692C0FA9F6F46` ([✅](SaltySD/plugins/FPSLocker/patches/01005AE0209A8000/36B692C0FA9F6F46.yaml), v10, 1.4.0) <br> `2D22A87AE49C75AA` ([✅](SaltySD/plugins/FPSLocker/patches/01005AE0209A8000/2D22A87AE49C75AA.yaml), v11, 1.4.2) | ~~[🔐](#🔐)[📏](#📏)~~ |
| 無双OROCHI３ | `0100E8500AD58000` | `07650FD5E5E2B82C` ([✅](SaltySD/plugins/FPSLocker/patches/0100E8500AD58000/07650FD5E5E2B82C.yaml), v13, 1.0.13) | ~~[🔐](#🔐)~~ |
| WARRIORS OROCHI 4 | `010016A00AEC0000` | `5C9CCD358BE85FC9` ([✅](SaltySD/plugins/FPSLocker/patches/010016A00AEC0000/5C9CCD358BE85FC9.yaml), v8, 1.0.13) | ~~[🔐](#🔐)~~ |
| We Love Katamari REROLL+ Royal Reverie | `0100E71018D1A000` | `8B1BC6D7B367605F` (❌, v3, 1.0.3) | [⏱️](#⏱️) |
| みんな大好き塊魂アンコール＋ 王様プチメモリー | `010089D018D18000` | `9FC7AF389B98F61A` (❌, v2, 1.0.3) | [⏱️](#⏱️) |
| What Remains of Edith Finch | `010038900DFE0000` | `E9578A470B175851` ([✅](SaltySD/plugins/FPSLocker/patches/010038900DFE0000/E9578A470B175851.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)~~ |
| While Waiting | `0100E9A021946000` | `47C0168998492210` (◯, v1, 1.1.2) |  |
| White Day: A Labirynth Named School | `010076601839C000` | `36D6740B3873CE4A` (◯, v1, 1.0.2) |  |
| Winter Burrow | `01006690239D8000` | `DD49E7493C34E809` (◯, v2, 1.0.2) |  |
| WitchSpringR | `010018401EEA8000` | `5E3F71147A485112` (◯, v6, 1.4.9) |  |
| Wobbly Life | `010039501F11C000` | `B174F363C2823CBE` (❌📌, v5, 1.0.0.3) | [📏](#📏) |
| Wolfenstein: Youngblood | `01003BD00CAAE000` | `8B40EBBA7244C94A` ([✅](SaltySD/plugins/FPSLocker/patches/01003BD00CAAE000/8B40EBBA7244C94A.yaml), v5, 1.5) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Wolfenstein II: The New Colossus | `01009040091E0000` | `F2FE5EF877839F4F` ([✅](SaltySD/plugins/FPSLocker/patches/01009040091E0000/F2FE5EF877839F4F.yaml), v2, 1.2) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| WORLD OF FINAL FANTASY MAXIMA | `010072000BD32000` | `5767FD44C331B44B` (❌, v1, 1.0.1) | [⚔️](#⚔️)[👄](#👄)[📺](#📺) |
| World's End Club | `01005A2014362000` | `F00EFE6846627B4A` ([✅](SaltySD/plugins/FPSLocker/patches/01005A2014362000/F00EFE6846627B4A.yaml), v6, 1.0.6) | ~~[🛑](#🛑)~~ |
| WRATH Aeon of Ruin | `0100C1E00CF30000` | `9587F6793464E033` (◯, v3, 1.0.3) |  |
| WRC10 | `01003E3014AFE000` | `69CACEEC5F01C41B` ([✅](SaltySD/plugins/FPSLocker/patches/01003E3014AFE000/69CACEEC5F01C41B.yaml), v1, 1.1.0) | ~~[📏](#📏)~~ |
| WRC Generations | `0100041018810000` | `B8BE1CFAE53CAEBE` ([✅](SaltySD/plugins/FPSLocker/patches/0100041018810000/B8BE1CFAE53CAEBE.yaml), v4, 1.2.2) | ~~[📏](#📏)~~ |
| Wreckfest | `0100DC0012E48000` | `7BCD694B69C98104` (◯, v2, 1.0.2) |  |
| WW2: Bunker Simulator | `01009A601B032000` | `0C2E9A763F9AB7A2` (◯, v0, 01.00) |  |
| WWE 2K18 | `010009800203E000` | `DEEE18D307C81634` (❌, v5, 1.04) | [⏱️](#⏱️)[📏](#📏)[⚔️](#⚔️) |
| Xenoblade2 (ゼノブレイド2) | `0100F3400332C000` | `E3938FA78579C1CA` ([✅](SaltySD/plugins/FPSLocker/patches/0100F3400332C000/E3938FA78579C1CA.yaml), v14, 2.0.2) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)[📺](#📺)~~[🔢](#🔢)[⚔️](#⚔️) |
| Xenoblade Chronicles: Definitive Edition | `0100FF500E34A000` | `92C78BB3DCBBC3F7` ([✅](SaltySD/plugins/FPSLocker/patches/0100FF500E34A000/92C78BB3DCBBC3F7.yaml), v3, 1.1.2) | ~~[🔐](#🔐)[📏](#📏)[🖥️](#🖥️)~~[⚔️](#⚔️) |
| Xenoblade Chronicles 2 | `0100E95004038000` | `F77F1559371C0EC6` ([✅](SaltySD/plugins/FPSLocker/patches/0100E95004038000/F77F1559371C0EC6.yaml), v15, 2.1.0) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)[📺](#📺)~~[🔢](#🔢)[⚔️](#⚔️) |
| Xenoblade Chronicles 3 | `010074F013262000` | `82D187FE9EF9BE92` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/82D187FE9EF9BE92.yaml), v11, 2.2.1) | ~~[🔐](#🔐)[📏](#📏)[🖥️](#🖥️)[📺](#📺)~~[⚔️](#⚔️) |
| Xenoblade Chronicles X | `0100453019AA8000` | `3F2425864CF22684` ([✅](SaltySD/plugins/FPSLocker/patches/0100453019AA8000/3F2425864CF22684.yaml), v1, 1.0.1) <br> `2A720C7CE5C84905` ([✅](SaltySD/plugins/FPSLocker/patches/0100453019AA8000/2A720C7CE5C84905.yaml), v2, 1.0.2) | ~~[🔐](#🔐)[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)[📺](#📺)[🔢](#🔢)~~[⚔️](#⚔️) |
| XUAN YUAN SWORD 7 | `010029F01BA3E000` | `F8EA898027152437` ([✅](SaltySD/plugins/FPSLocker/patches/010029F01BA3E000/F8EA898027152437.yaml), v0, 1.0.0) | ~~[🔐](#🔐)[📏](#📏)[🔧](#🔧)~~ |
| Yakuza Kiwami | `0100C9801FEE6000` | `53F407A2CFBF5202` ([✅](SaltySD/plugins/FPSLocker/patches/0100C9801FEE6000/53F407A2CFBF5202.yaml), v0, 1.00) <br> `AE90FD64E7B2FE1E` ([✅](SaltySD/plugins/FPSLocker/patches/0100C9801FEE6000/AE90FD64E7B2FE1E.yaml), v1, 1.01) | ~~[📺](#📺)~~ |
| Yooka-Laylee | `0100F110029C8000` | `6352FCBB7C75E478` (◯, v2, 1.2.0) |  |
| Young Souls | `010097900F550000` | `E43952D95F17FA48` (◯, v3, 1.0.3) |  |
| Ys VIII: Lacrimosa of DANA | `01007F200B0C0000` | `F7C4835FD8AE9D10` (◯, v5, 1.05) |  |
| Ys IX: Monstrum Nox | `0100E390124D8000` | `4D33981B6DB6125A` (◯, v3, 1.0.3) |  |
| Ys X: Nordics | `0100BAC01E57E000` | `E5816E16CC5D72A5` ([✅](SaltySD/plugins/FPSLocker/patches/0100BAC01E57E000/E5816E16CC5D72A5.yaml), v2, 1.0.2) <br> `C55F6B8AEFA54324` ([✅](SaltySD/plugins/FPSLocker/patches/0100BAC01E57E000/C55F6B8AEFA54324.yaml), v3, 1.0.3) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| 伊蘇X -北境歷險- | `0100A0C01BED8000` | `7E06539B5874B9C4` ([✅](SaltySD/plugins/FPSLocker/patches/0100A0C01BED8000/7E06539B5874B9C4.yaml), v5, 1.0.5) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| イースX -NORDICS- | `0100CC401A16C000` | `ACF8E5931E38EAA0` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC401A16C000/ACF8E5931E38EAA0.yaml), v4, 1.0.4) | ~~[📏](#📏)[⏱️](#⏱️)[🖥️](#🖥️)~~ |
| Zombie Army Trilogy | `0100C7300EEE4000` | `54211726D36A8D9C` ([✅](SaltySD/plugins/FPSLocker/patches/0100C7300EEE4000/54211726D36A8D9C.yaml), v2, 1.0.2) | ~~[📏](#📏)~~ |
| Zombie Army 4: Dead War | `01000BF0152FA000` | `12024D08CCFD25EB` ([✅](SaltySD/plugins/FPSLocker/patches/01000BF0152FA000/12024D08CCFD25EB.yaml), v2, 1.1.1) | ~~[📏](#📏)~~ | 
| Zomborg | `01006401D48A000` | `A371513D3E16409B` (◯, v0, 1.0.0) |  |
| 妖怪ウォッチ | `0100C0000CEEA000` | `7F35BDFC5DE46CF1` (❌, v4, 1.4.0) | [🔐](#🔐)[📷](#📷) |
| 妖怪ウォッチ4++ | `010086C00AF7C000` | `C7DAB27F22ACD2ED` ([✅](SaltySD/plugins/FPSLocker/patches/010086C00AF7C000/C7DAB27F22ACD2ED.yaml), v14, 2.2.0) | ~~[🔐](#🔐)~~[⚔️](#⚔️) |
| 妖怪学園Y ～ワイワイ学園生活～ | `010051D010FC2000` | `1DF8D13059E84915` (❌📌, v10, 4.0.0) | [🔐](#🔐)[⚔️](#⚔️) |
| 英雄伝説 閃の軌跡I<br>改 -Thors Military Academy 1204- | `0100AD0014AB4000` | `AC8C8EC9DB1A8EF4` ([✅](SaltySD/plugins/FPSLocker/patches/0100AD0014AB4000/AC8C8EC9DB1A8EF4.yaml), v3, 1.0.3) | ~~[🔐](#🔐)~~ |
| 英雄伝説 閃の軌跡II<br>改 -The Erebonian Civil War- | `0100906014C3C000` | `EAB1DC1D53E319F9` ([✅](SaltySD/plugins/FPSLocker/patches/0100906014C3C000/EAB1DC1D53E319F9.yaml), v5, 1.0.5) | ~~[🔐](#🔐)~~ |
| ドラゴンクエストX<br>目覚めし五つの種族　オフライン | `0100E2E0152E4000` | `13F322A6161F787C` ([✅](SaltySD/plugins/FPSLocker/patches/0100E2E0152E4000/13F322A6161F787C.yaml), v4, 2.0.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| 電車でＧＯ！！ はしろう山手線 | `0100BC501355A000` | `7C9F89C3743F202F` ([✅](SaltySD/plugins/FPSLocker/patches/0100BC501355A000/7C9F89C3743F202F.yaml), v3, 1.1.2) | ~~[📏](#📏)[🔧](#🔧)~~ |
| 牧場物語 Let's！風のグランドバザール | `0100DAE01E4C8000` | `2D532E9C1B773907` (◯, v7, 1.2.0) |  |
| 창세기전 \~회색의 잔영\~ | `0100276019E96000` | `EC983B9153629AC8` ([✅](SaltySD/plugins/FPSLocker/patches/0100276019E96000/EC983B9153629AC8.yaml), v1, 1.1.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| ドラゴンクエストヒーローズI・II | `0100CD3000BDC000` | `5C598E5025BF97BC` ([✅](SaltySD/plugins/FPSLocker/patches/0100CD3000BDC000/5C598E5025BF97BC.yaml), v3, 1.0.3) | ~~[🔐](#🔐)[⏱️](#⏱️)[⚔️](#⚔️)~~
| エアコンフリクト：パシフィックキャリアー | `010020700C952000` | `E0875F171671C8F7` (❌, v0, 1.0.0) | [⚔️](#⚔️) |

</details>

<details>
<summary>Patches for games not locked to 30 FPS, but with graphics settings targeting strictly 30 or 60 FPS (24 titles)</summary>

| NAME | TITLE ID | BUILD ID (PATCH AVAILABLE, VERSION ID, VERSION) | ISSUES |
| --- | --- | --- | --- |
| AO Tennis 2 | `010047000E9AA000` | `01EB7A6DE827BFD9` ([✅](SaltySD/plugins/FPSLocker/patches/010047000E9AA000/01EB7A6DE827BFD9.yaml), v7, 1.7.0) | ~~[⚔️](#⚔️)[📏](#📏)~~ |
| Borderlands 3 | `01009970122E4000` | `AE2768797E3337EE` ([✅](SaltySD/plugins/FPSLocker/patches/01009970122E4000/AE2768797E3337EE.yaml), v3, 1.0.3) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Caravan SandWitch | `0100D5801E904000` | `CE493FC8CDD3D7B2` ([✅](SaltySD/plugins/FPSLocker/patches/0100D5801E904000/CE493FC8CDD3D7B2.yaml), v5, 1.0.5) <br> `89349071D2B0BFF7` ([✅](SaltySD/plugins/FPSLocker/patches/0100D5801E904000/89349071D2B0BFF7.yaml), v7, 1.0.7) | ~~[📏](#📏)~~ |
| City of Brass | `01009BC00B872000` | `53116900DC7BBE11` ([✅](SaltySD/plugins/FPSLocker/patches/01009BC00B872000/53116900DC7BBE11.yaml), v2, 1.2.0) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Empire of Sin | `010058600E530000` | `BD5F1ED30FDBA245` ([✅](SaltySD/plugins/FPSLocker/patches/010058600E530000/BD5F1ED30FDBA245.yaml), v10, 1.10.0) | ~~[📏](#📏)~~ |
| Misc. A Tiny Tale | `0100A5E014196000` | `0E9D849EF47198D8` ([✅](SaltySD/plugins/FPSLocker/patches/0100A5E014196000/0E9D849EF47198D8.yaml), v5, 1.0.4) <br> `D24A46A2618C9E38` ([✅](SaltySD/plugins/FPSLocker/patches/0100A5E014196000/D24A46A2618C9E38.yaml), v6, 1.0.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Mortal Shell | `0100154019A7C000` | `6D9F6C7B79F5197F` ([✅](SaltySD/plugins/FPSLocker/patches/0100154019A7C000/6D9F6C7B79F5197F.yaml), v2, 1.2.0) | ~~[📏](#📏)~~ |
| MY HERO ONE'S JUSTICE 2 | `01007E700DBF6000` | `29E1CD0FBB24697E` ([✅](SaltySD/plugins/FPSLocker/patches/01007E700DBF6000/29E1CD0FBB24697E.yaml), v15, 1.1.5) | ~~[📏](#📏)[🔧](#🔧)~~ |
| NINJA GAIDEN: Ragebound | `0100781020710000` | `C7BD9BFC5F202073` ([✅](SaltySD/plugins/FPSLocker/patches/0100781020710000/C7BD9BFC5F202073.yaml), v3, 1.0.3) <br> `48D35EF3C7EFBF5F` ([✅](SaltySD/plugins/FPSLocker/patches/0100781020710000/48D35EF3C7EFBF5F.yaml), v4, 1.0.4) <br> `CEDA530B146C0260` ([✅](SaltySD/plugins/FPSLocker/patches/0100781020710000/CEDA530B146C0260.yaml), v5, 1.0.5) <br> `1FF44387A22D39F8` ([✅](SaltySD/plugins/FPSLocker/patches/0100781020710000/1FF44387A22D39F8.yaml), v6, 1.0.6) | ~~[🛑](#🛑)~~ |
| Saints Row: The Third | `0100DE600BEEE000` | `A8631EDCC0013045` ([✅](SaltySD/plugins/FPSLocker/patches/0100DE600BEEE000/A8631EDCC0013045.yaml), v7, 1.6.1) | ~~[📏](#📏)~~ |
| Saints Row IV | `01008D100D43E000` | `B6CFBB9BB8F8A2E7` ([✅](SaltySD/plugins/FPSLocker/patches/01008D100D43E000/B6CFBB9BB8F8A2E7.yaml), v7, 1.8.0) | ~~[📏](#📏)~~ |
| Red Faction Guerrilla | `010075000C608000` | `F1D71307616AB7E4` ([✅](SaltySD/plugins/FPSLocker/patches/010075000C608000/F1D71307616AB7E4.yaml), v0, 1.0.0) | ~~[📏](#📏)~~ |
| RiMS Racing | `01003CD01299E000` | `4232D493269475B2` ([✅](SaltySD/plugins/FPSLocker/patches/01003CD01299E000/4232D493269475B2.yaml), v2, 1.2.0) | ~~[📏](#📏)~~ |
| Tennis World Tour 2 | `01002AF011D14000` | `D1B29E1ABDCD955E` ([✅](SaltySD/plugins/FPSLocker/patches/01002AF011D14000/D1B29E1ABDCD955E.yaml), v3, 1.3.0) | ~~[⚔️](#⚔️)[📏](#📏)~~ |
| The Long Dark | `01007A700A87C000` | `88C035C2E44076ED` ([✅](SaltySD/plugins/FPSLocker/patches/01007A700A87C000/88C035C2E44076ED.yaml), v12, 2.40.153678) | ~~[📏](#📏)~~ |
| The Long Dark: Tales from the Far Territory | `01007A700A87C001` | `F7A872504BDA3100` ([✅](SaltySD/plugins/FPSLocker/patches/01007A700A87C001/F7A872504BDA3100.yaml), v12, 2.40.153678) | ~~[📏](#📏)~~ |
| The Plucky Squire | `01006BD018B54000` | `B771B34505774A8E` ([✅](SaltySD/plugins/FPSLocker/patches/01006BD018B54000/B771B34505774A8E.yaml), v3, 1.0.3) <br> `D53CF6573CAED4B1` ([✅](SaltySD/plugins/FPSLocker/patches/01006BD018B54000/D53CF6573CAED4B1.yaml), v4, 1.0.4) <br> `0A1AC10CCFE46061` ([✅](SaltySD/plugins/FPSLocker/patches/01006BD018B54000/0A1AC10CCFE46061.yaml), v5, 1.0.5) <br> `FD3AC4FFB1B769D5` ([✅](SaltySD/plugins/FPSLocker/patches/01006BD018B54000/FD3AC4FFB1B769D5.yaml), v6, 1.0.6) <br> `AFDEB128252898AC` ([✅](SaltySD/plugins/FPSLocker/patches/01006BD018B54000/AFDEB128252898AC.yaml), v7, 1.0.7) <br> `892E6C4FE0D850B5` ([✅](SaltySD/plugins/FPSLocker/patches/01006BD018B54000/892E6C4FE0D850B5.yaml), v8, 1.0.8) | ~~[📏](#📏)[🔧](#🔧)~~ |
| Trails in the Sky 1st Chapter | `01002C9022770000` | `2AD8CC7892EBF9FA` ([✅](SaltySD/plugins/FPSLocker/patches/01002C9022770000/2AD8CC7892EBF9FA.yaml), v3, 1.0.4) <br> `E5F70FFCBD0DD378` ([✅](SaltySD/plugins/FPSLocker/patches/01002C9022770000/E5F70FFCBD0DD378.yaml), v4, 1.0.5) <br> `2B18130BD191CAC5` ([✅](SaltySD/plugins/FPSLocker/patches/01002C9022770000/2B18130BD191CAC5.yaml), v5, 1.0.6) | ~~[⏱️](#⏱️)[📏](#📏)~~ |
| 하늘의 궤적 the 1st | `01001E9023920000` | `4FC3CB13E1D3292E` ([✅](SaltySD/plugins/FPSLocker/patches/01001E9023920000/4FC3CB13E1D3292E.yaml), v2, 1.0.3) <br> `169AD641E042A8B4` ([✅](SaltySD/plugins/FPSLocker/patches/01001E9023920000/169AD641E042A8B4.yaml), v3, 1.0.4) <br> `8CFF66758D7BD507` ([✅](SaltySD/plugins/FPSLocker/patches/01001E9023920000/8CFF66758D7BD507.yaml), v4, 1.0.5) <br> `6656BA1B5B8AC30A` ([✅](SaltySD/plugins/FPSLocker/patches/01001E9023920000/6656BA1B5B8AC30A.yaml), v6, 1.0.6.1) | ~~[⏱️](#⏱️)[📏](#📏)~~ |
| 空の軌跡 the 1st | `01004D20219E0000` | `6DE3725465A43249` ([✅](SaltySD/plugins/FPSLocker/patches/01004D20219E0000/6DE3725465A43249.yaml), v3, 1.0.4) <br> `555E8872455F107E` ([✅](SaltySD/plugins/FPSLocker/patches/01004D20219E0000/555E8872455F107E.yaml), v4, 1.0.5) <br> `4583D73E326FFE7B` ([✅](SaltySD/plugins/FPSLocker/patches/01004D20219E0000/4583D73E326FFE7B.yaml), v5, 1.0.6) | ~~[⏱️](#⏱️)[📏](#📏)~~ |
| Trials of Mana | `0100D7800E9E0000` | `92C25172D38DFEDB` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7800E9E0000/92C25172D38DFEDB.yaml), v3, 1.1.1) | ~~[📏](#📏)[🔧](#🔧)~~ |
| TT Isle of Man 2 | `010000400F582000` | `02F2E5C8CBF5A92F` ([✅](SaltySD/plugins/FPSLocker/patches/010000400F582000/02F2E5C8CBF5A92F.yaml), v1, 1.0.1) | ~~[📏](#📏)~~ |
| WRC8 | `010087800DCEA000` | `6B0B26802F0DAAAF` ([✅](SaltySD/plugins/FPSLocker/patches/010087800DCEA000/6B0B26802F0DAAAF.yaml), v4, 1.4.0) | ~~[📏](#📏)~~ |
| WRC9 | `01001A0011798000` | `66B2DEA98B5CDF65` ([✅](SaltySD/plugins/FPSLocker/patches/01001A0011798000/66B2DEA98B5CDF65.yaml), v2, 1.2.0) | ~~[📏](#📏)~~ |

</details>
