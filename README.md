# FPSLocker Warehouse

Here you will find a list with 30 FPS locked games, if they have FPSLocker configs that allow going above 30 FPS, tweak dynamic resolution frame timing for better performance, etc. At the end of README you can also find a separate list of configs for games that are targeting 30 FPS even though they have unlocked framerate.

Remember that NX-FPS is limited by SaltyNX capabilities. 
Read SaltyNX readme to check which games are not compatible.

---

> To download all configs click [here](https://github.com/masagrator/FPSLocker-Warehouse/archive/refs/heads/main.zip), unpack it and copy the `SaltySD` and `atmosphere` folder to root of your sdcard.

---

Column with colors stores info if the plugin is enough to go above 30 FPS or you must use additional patches that are created from configs available in this repository.<br>
This involves only handheld mode. For docked mode different color could be attached.<br>
Patches status concern only FPSLocker "LOCK" patch format. There may exist cheat/IPS patch/mod that unlocks 60 FPS already.<br>
As the list is filled by community, it may not be up to date.

🟢 - Plugin alone is enough<br>
🔵 - Plugin alone allows going above 30 FPS, but game requires patch to fix non-breaking gameplay elements (f.e. dynamic resolution frame time to improve performance, adjust lipsync, remove double buffer)<br>
🟡 - Plugin alone allows going above 30 FPS, but game requires patch to fix breaking gameplay elements (f.e. game speed or physics) or removing fake frames (aka game reporting 60 FPS while in fact it's 30 FPS)<br>
🔴 - Plugin alone is not enough, game patch is required<br>
🟣 - Game is not compatible with the plugin

PATCH AVAILABILITY<br>
✝️ - patch is not possible to create<br>
❌ - patch not available<br>
✅ - patch available (click on it for config file that can be converted to patch).<br>
◯ - this version doesn't need a patch

---

DETAILS contains links to documents explaining why patch is necessary, possible issues with using FPSLocker in this game and how to update patch yourself for any version (It won't explain how to use IDA/Ghidra/Edizon-SE/GDB or how it was determined that those offsets are correct).

---

| NAME | TITLE ID | BUILD ID (PATCH AVAILABLE, VERSION ID, VERSION) |  | DETAILS |
| --- | --- | --- | --- | --- |
| .hack//G.U. Last Recode | `0100BA9014A02000` | `4C0ED5711263A6D9` (❌, v0, 1.0.0) | 🟡 |  |
| A Hat in Time | `010056E00853A000` | `746F0D697EEEE2DD` ([✅](SaltySD/plugins/FPSLocker/patches/010056E00853A000/746F0D697EEEE2DD.yaml), v4, 1.0.4) | 🔴 |  |
| ABZU | `0100C1300BBC6000` | `59719CFCD1671B98` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1300BBC6000/59719CFCD1671B98.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/ABZU) |
| Advance Wars 1+2: Re-Boot Camp | `0100300012F2A000` | `320A17744AEFD67F`  ([✅](SaltySD/plugins/FPSLocker/patches/0100300012F2A000/320A17744AEFD67F.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/Advance%20Wars%201%2B2) |
| Adventure Time: Pirates of the Enchiridion | `0100C4E004406000` | `550CC8AAD902C04F` (◯, v4, 1.0.4.26870) | 🟢 |  |
| Agent Intercept | `0100B80013C1C000` | `A475D0073EA170B0` (◯, v0, 1.0.0) | 🟢 |  |
| Agatha Christie - Hercule Poirot: The First Cases | `010000F012936000` | `1570FE23108B93C4` ([✅](SaltySD/plugins/FPSLocker/patches/010000F012936000/1570FE23108B93C4.yaml), v3, 1.0.3) | 🟡 |  |
| Agatha Christie - Hercule Poirot: The London Case | `01002FD01A24C000` | `8F72E0D61C4BA0B1` ([✅](SaltySD/plugins/FPSLocker/patches/01002FD01A24C000/8F72E0D61C4BA0B1.yaml), v2, 1.0.2) | 🟡 |  |
| Agatha Christie - The ABC Murders | `010087C011C4E000` | `655293197620944D` (◯, v2, 1.0.2) | 🟢 |  |
| Alan Wake Remastered | `0100623017A58000` | `6520258D00AEA915` (❌, v1, 1.0.1) | 🔵 | [LINK](Methodology/Alan%20Wake) |
| Alchemy Garden | `0100A4101AC26000` | `FB73B824FB53892E` (❌, v1, 1.0.1) | 🔵 |  |
| Alfred Hitchcock - Vertigo | `0100DC7013F14000` | `9D5ABEC66FEC1D77` (◯, v1, 1.0.1) | 🟢 |  |
| Alien: Isolation | `010075D00E8BA000` | `397C054A3D25D488` (◯, v5, 1.1.5_64113) | 🟢 |  |
| Alterity Experience | `010056F0186D0000` | `E4F041624093998D` (◯, v2, 2.0) | 🟢 |  |
| American Fugitive | `010002B00C534000` | `375A0E11B2397340` (◯, v9, 1.1.1) | 🟢 |  |
| Ancestors Legacy | `01009EE0111CC000` | `EE20B8DD92B8F9B4` ([✅](SaltySD/plugins/FPSLocker/patches/01009EE0111CC000/EE20B8DD92B8F9B4.yaml), v1, 1.1.0) <br> `E1F0CFC02F449EF3` ([✅](SaltySD/plugins/FPSLocker/patches/01009EE0111CC000/E1F0CFC02F449EF3.yaml), v2, 1.2.0) | 🔴 | [LINK](Methodology/Ancestors%20Legacy) |
| Ancient Weapon Holly | `0100F7201D1B0000` | `0606DF0999FBA333` (◯, v1, 1.1.0) | 🟢 |  |
| Animal Crossing: New Horizons | `01006F8002326000` | `15765149DF53BA41` (❌, v28, 2.0.6) | 🟡 | [LINK](Methodology/Animal%20Crossing%20New%20Horizons) |
| Animal Shelter Simulator | `0100B1C01B104000` | `AB9EFB08DB5FE4F1` (❌, v1, 1.1.0) | 🟡 |  |
| Another Code: Recollection | `0100CB9018F5A000` | `DED0F920799151BE` (❌, v0, 1.0.0) | 🔵 |  |
| Apollo Justice Trilogy | `010020D01B890000` | `F1A7E0DB6B0EC65F` (❌, v1, 1.0.1) | 🔴 |  |
| Aragami 2 | `0100787018198000` | `3FFD52E56DD8ADB3` (◯, v1, 1.0.30195.0) | 🟢 |  |
| Arise: A Simple Story | `0100FE201680A000` | `8F2536786EECCEE5` ([✅](SaltySD/plugins/FPSLocker/patches/0100FE201680A000/8F2536786EECCEE5.yaml), v5, 1.0.5) | 🔴 |  |
| ARK: Dinosaur Discovery | `0100A6B01900E000` | `9E0901B84058B5B4` ([✅](SaltySD/plugins/FPSLocker/patches/0100A6B01900E000/9E0901B84058B5B4.yaml), v2, 1.5.0) | 🔴 |  |
| ARK: Survival Evolved | `0100D4A00B284000` | `5418E22D160F766F` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4A00B284000/5418E22D160F766F.yaml), v10, 2.0.7) <br> `49F3DD78CB5490B5` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4A00B284000/49F3DD78CB5490B5.yaml), v13, 2.0.10) <br> `D1E3FFBA414F4929` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4A00B284000/D1E3FFBA414F4929.yaml), v14, 2.0.11) | 🔴 |  |
| art of rally | `0100A88012504000` | `116535367286904C` ([✅](SaltySD/plugins/FPSLocker/patches/0100A88012504000/116535367286904C.yaml), v4, 1.1.6) <br> `0D17FD76B32F3040` ([✅](SaltySD/plugins/FPSLocker/patches/0100A88012504000/0D17FD76B32F3040.yaml), v6, 1.1.8) | 🔵 |  |
| Assassin's Creed II | `0100670014482000` | `824B38A25986B2AB` ([✅](SaltySD/plugins/FPSLocker/patches/0100670014482000/824B38A25986B2AB.yaml), v3, 1.3) | 🔵 |  |
| Assassin's Creed Brotherhood | `0100670014482001` | `2B59D6C677258A2A` ([✅](SaltySD/plugins/FPSLocker/patches/0100670014482001/2B59D6C677258A2A.yaml), v3, 1.3) | 🔵 |  |
| Assassin's Creed Revelations | `0100670014482002` | `0AE4D1770B196094` ([✅](SaltySD/plugins/FPSLocker/patches/0100670014482002/0AE4D1770B196094.yaml), v3, 1.3) | 🔵 |  |
| Assassin's Creed Revelations - The Lost Archive | `0100670014482003` | `729AB05205B9B7E4` (◯, v3, 1.3) | 🟢 |  |
| Assassin's Creed III Remastered | `01007F600B134000` | `43DDF3AED0E7E500` (◯, v3, 1.0.3) | 🟢 |  |
| Assassin's Creed IV Black Flag | `010044700DEB0000` | `85F5D5AB6187F602` (◯, v0, 1.0.0) | 🟢 |  |
| Assassin's Creed Rogue | `010044700DEB0001` | `3DEF0E36AA8C6592` ([✅](SaltySD/plugins/FPSLocker/patches/010044700DEB0001/3DEF0E36AA8C6592.yaml), v0, 1.0.0) | 🔵 |  |
| Asterix & Obelix XXXL - The Ram From Hibernia | `01001F3018880000` | `DF556AF2E30073C0` ([✅](SaltySD/plugins/FPSLocker/patches/01001F3018880000/DF556AF2E30073C0.yaml), v4, 1.04.00) | 🔵 |  |
| ASTRAL CHAIN | `01007300020FA000` | `4B159F0F7A360669` ([✅](SaltySD/plugins/FPSLocker/patches/01007300020FA000/4B159F0F7A360669.yaml), v1, 1.0.1) | 🟡 |  |
| Atelier Ayesha | `0100D9D00EE8C000` | `B9146E1CAD9E36BA` (◯, v0, 1.0.0) | 🟢 |  |
| Atelier Escha & Logy | `0100E5600EE8E000` | `4BBB3B3455D306C6` (◯, v0, 1.0.0) | 🟢 |  |
| Atelier Firis | `010023201421E000` | `8BB29E319CCE6357` (◯, v4, 1.0.4) | 🟢 |  |
| Atelier Lulua | `0100B1400CD50000` | `CA7FACAEC708311C` (◯, v4, 1.0.3) | 🟢 |  |
| Atelier Lydie & Suelle | `01001A5014220000` | `32EB581C7D9BE094` (◯, v3, 1.0.3) | 🟢 |  |
| Atelier Marie Remake | `0100EAE019904000` | `743CD6A40363900C` (◯, v1, 1.0.0a) | 🟢 |  | 
| Atelier Meruru | `0100ADD00C6FA000` | `E76C3624D3AE3DCE` (◯, v2, 1.0.2) | 🟢 |  |
| Atelier Rorona | `010088600C66E000` | `967D32BE4B10B67E` (◯, v1, 1.0.1) | 🟢 |  |
| Atelier Ryza | `0100D1900EC80000` | `6BAE122EA063FFEB` (◯, v8, 1.0.8) | 🟢 |  |
| Atelier Ryza 2 | `01009A9012022000` | `C2979457A5785216` (◯, v7, 1.0.7) | 🟢 |  |
| Atelier Ryza 3 | `010095E018944000` | `E116C2CF4896A4F2` (◯, v8, 1.6.0) | 🟢 |  |
| Atelier Shallie | `010005C00EE90000` | `AAB0450A965202EC` (◯, v0, 1.0.0) | 🟢 |  |
| Atelier Sophie | `0100D8701421C000` | `9C95108FD8F7464A` (◯, v3, 1.0.3) | 🟢 |  |
| Atelier Sophie 2 | `010082A01538E000` | `4A1B406278346C2B` (◯, v8, 1.0.8) | 🟢 |  |
| Atelier Totori | `01009BC00C6F6000` | `4FD4BFE66C5353D4` (◯, v1, 1.0.1) | 🟢 |  |
| Attack on Titan 2 | `010034500641A000` | `586EA519C1CDFAE7` (◯, v14, 1.0.14) | 🟢 |  |
| Aztech Forgotten Gods | `01006B4014564000` | `65EF4BC77B974E05` (◯, v8, 1.0.8) | 🟢 |  |
| BALAN WONDERWORLD | `0100438012EC8000` | `1A0EAEC3AE90B018` ([✅](SaltySD/plugins/FPSLocker/patches/0100438012EC8000/1A0EAEC3AE90B018.yaml), v1, 1.01) | 🔴 |  |
| Bang-On Balls: Chronicles | `010081E01A45C000` | `6B5E31BAA58DB229` ([✅](SaltySD/plugins/FPSLocker/patches/010081E01A45C000/6B5E31BAA58DB229.yaml), v1, 1.0.1) <br> `20A5199D55EA5E93` ([✅](SaltySD/plugins/FPSLocker/patches/010081E01A45C000/20A5199D55EA5E93.yaml), v2, 1.0.2) <br> `25D3C2E9040D1A9A` ([✅](SaltySD/plugins/FPSLocker/patches/010081E01A45C000/25D3C2E9040D1A9A.yaml), v4, 1.0.4) | 🔵 | [LINK](Methodology/Bang-On%20Balls%3A%20Chronicles) | 
| Baldo The Guardian Owls | `0100A75005E92000` | `9E29077BE56B5E4D` (◯, v17, 1.0.17) | 🟢 |  |
| Bandle Tale: A League of Legends Story | `010052B01BEC0000` | `8BF051A6E3110A30` (◯, v1, 1.062) | 🟢 |  |
| Batman - The Telltale Series | `0100011005D92000` | `A3A998AF3252D110` ([✅](SaltySD/plugins/FPSLocker/patches/0100011005D92000/A3A998AF3252D110.yaml), v3, 1.0.4) | 🔵 |  |
| Batman: Arkham Asylum | `0100E870163CA000` | `ADC8FED84D846EE8` ([✅](SaltySD/plugins/FPSLocker/patches/0100E870163CA000/ADC8FED84D846EE8.yaml), v0, 1.0.0) <br> `621EE66A6743D750` ([✅](SaltySD/plugins/FPSLocker/patches/0100E870163CA000/621EE66A6743D750.yaml), v1, 1.0.1) | 🔴 |  |
| Batman: Arkham City | `01003F00163CE000` | `8983C5A34B178E5C` (◯, v2, 1.0.2) | 🟢 |  |
| Batman: Arkham Knight | `0100ACD0163D0000` | `7DC6FDFAD9368F08` (◯, v3, 1.0.3) | 🟢 |  |
| Batman: The Enemy Within | `0100E6300AA3A000` | `AAC6FB02E03062EF` ([✅](SaltySD/plugins/FPSLocker/patches/0100E6300AA3A000/AAC6FB02E03062EF.yaml), v1, 1.0.3) | 🔵 |  |
| Batora: Lost Haven | `0100A93016BF4000` | `770A07C35E631CB2` ([✅](SaltySD/plugins/FPSLocker/patches/0100A93016BF4000/770A07C35E631CB2.yaml), v1, 1.0.1) | 🔴 | [LINK](Methodology/Batora%20Lost%20Haven) |
| Bassmaster Fishing 2022 | `0100B8501771A000` | `78BF042012CF9EE8` ([✅](SaltySD/plugins/FPSLocker/patches/0100B8501771A000/78BF042012CF9EE8.yaml), v2, 1.02) | 🔵 | [LINK](Methodology/Bassmaster%20Fishing%202022%20Super%20Deluxe%20Edition) |
| Bendy and the Ink Machine | `0100D4C00C6C0000` | `91B6BD011F0C2C46` (◯, v2, 1.6.0.0) | 🟢 |  |
| Beyond Enemy Lines | `0100AE7010434000` | `5915CDDDC4EEA6CD` ([✅](SaltySD/plugins/FPSLocker/patches/0100AE7010434000/5915CDDDC4EEA6CD.yaml), v1, 1.1.0) | 🔵 |  |
| BioShock Remastered | `0100AD10102B2000` | `D89FFAA2062E373D` ([✅](SaltySD/plugins/FPSLocker/patches/0100AD10102B2000/D89FFAA2062E373D.yaml), v1, 1.0.2) | 🔵 | [LINK](Methodology/BioShock%20Remastered) |
| BioShock 2 Remastered | `01002620102C6000` | `7D1714279435589C` ([✅](SaltySD/plugins/FPSLocker/patches/01002620102C6000/7D1714279435589C.yaml), v1, 1.0.2) | 🔵 | [LINK](Methodology/BioShock%202%20Remastered) |
| BioShock Infinite | `0100D560102C8000` | `48681F1D90704F6C` ([✅](SaltySD/plugins/FPSLocker/patches/0100D560102C8000/48681F1D90704F6C.yaml), v1, 1.0.2) | 🔵 | [LINK](Methodology/BioShock%20Infinite) |
| Blade Assault | `0100EA1018A2E000` | `0DF84BFE1556A443` (◯, v1, 1.0.1) | 🟢 |  |
| Blair Witch | `01006CC01182C000` | `C31E59266A218855` ([✅](SaltySD/plugins/FPSLocker/patches/01006CC01182C000/C31E59266A218855.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Blair%20Witch) |
| Bloodstained: Ritual of the Night | `0100BF500207C000` | `12E0B62494B22F62` ([✅](SaltySD/plugins/FPSLocker/patches/0100BF500207C000/12E0B62494B22F62.yaml), v11, 1.40) | 🔵 | [LINK](Methodology/Bloodstained%20Ritual%20of%20the%20Night) |
| Boomerang X | `0100C09014530000` | `D92F465FE9920BB6` ([✅](SaltySD/plugins/FPSLocker/patches/0100C09014530000/D92F465FE9920BB6.yaml), v2, 1.0.2) | 🔵 |  |
| Borderlands | `010064800F66A000` | `1C37C3673E0E4E7A` (◯, v2, 1.0.2) | 🟢 |  |
| Borderlands 2 | `010096F00FF22000` | `F7C233469F20EE3F` (◯, v2, 1.0.2) | 🟢 |  |
| Borderlands: The Pre-Sequel | `010007400FF24000` | `090B1F7F7AF35D00` (◯, v1, 1.0.1) | 🟢 |  |
| BPM: Bullets Per Minute | `0100040016EE2000` | `331E3DFBDF650226` ([✅](SaltySD/plugins/FPSLocker/patches/0100040016EE2000/331E3DFBDF650226.yaml), v1, 0.1) | 🔵 |  |
| Bramble The Mountain King | `0100E87017D0E000` | `ACF3FF125C2A3E68` ([✅](SaltySD/plugins/FPSLocker/patches/0100E87017D0E000/ACF3FF125C2A3E68.yaml), v5, 1.0.7) | 🔵 |  |
| BRAVELY DEFAULT II | `01006DC010326000` | `05DE5A7F20BD1532` ([✅](SaltySD/plugins/FPSLocker/patches/01006DC010326000/05DE5A7F20BD1532.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/Bravely%20Default%202) |
| Bravery and Greed | `0100F60017D4E000` | `C660EA2CC0478E4B` (◯, v3, 1.0.3) | 🟢 |  |
| Bright Memory: Infinite | `01001A9018560000` | `323631B628A32D84` ([✅](SaltySD/plugins/FPSLocker/patches/01001A9018560000/323631B628A32D84.yaml), v2, 1.2) <br> `DD425ECC07C305DF` ([✅](SaltySD/plugins/FPSLocker/patches/01001A9018560000/DD425ECC07C305DF.yaml), v3, 1.3) | 🔴 |  |
| Bro Falls | `01005EF01A12E000` | `A07FFE2F32878CE9` (◯, v0, 1.57) | 🟢 |  |
| Bulletstorm | `01003DD00D658000` | `32FC35DF1C50E1F1` (◯, v0, 1.0.0) | 🟢 |  |
| Call of Cthulhu | `010046000EE40000` | `8F6B002FEB5D0F8E` ([✅](SaltySD/plugins/FPSLocker/patches/010046000EE40000/8F6B002FEB5D0F8E.yaml), v3, 0.1.6) | 🔴 |  |
| Call of Juarez: Gunslinger | `0100B4700BFC6000` | `EBF7DE558D554C7E` (◯, v5, 1.0.5) | 🟢 |  |
| Candleman | `010034400CB5E000` | `55AA8D007FAEC044` (◯, v1, 1.0.1) | 🟢 |  |
| Cars 3: Driven to Win | `0100744001588000` | `6E191829548C2A41` (❌, v2, 1.0.2) | 🔵 | [LINK](Methodology/Cars%203) |
| Cassette Beasts | `010066F01A0E0000` | `224357DED42E86ED` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/224357DED42E86ED.yaml), v4, 1.4.0) <br> `65688736640651F6` ([✅](SaltySD/plugins/FPSLocker/patches/010066F01A0E0000/65688736640651F6.yaml), v5, 1.5.0) | 🔴 | [LINK](Methodology/Casette%20Beasts) |
| Castle Renovator | `010013801A0E4000` | `34E094252A069FE9` (◯, v0, 1.0.0) | 🟢 |  |
| Catherine: Full Body | `0100BF00112C0000` | `93A79C77DA81F7F1` (❌, v1, 1.0.1) | 🟡 |  |
| Cel Damage HD | `010019B00BE72000` | `03B058B1F6BE7195` (✝️, v0, 1.0.0) | 🟣 | [LINK](Methodology/CelDamage%20HD) |
| Chants of Sennaar | `0100543019CB0000` | `CEFFC8421D584F8C` (◯, v2, 1.0.2) | 🟢 |  |
| Chef Life - A Restaurant Simulator | `0100F24014280000` | `DF27862149F6536D` (◯, v4, 1.6.0) | 🟢 |  |
| Choo-Choo Charles | `01006F901C7F2000` | `406F004D76F961F3` ([✅](SaltySD/plugins/FPSLocker/patches/01006F901C7F2000/406F004D76F961F3.yaml), v0, 1.0.1) | 🔵 |  |
| Circus Electrique | `0100ABF015DCE000` | `57019F9781022D15` (◯, v2, 1.2.0) | 🟢 |  |
| Classic Racers Elite | `01003B90137D0000` | `9D9810D42B5AF44D` (◯, v0, 1.0) | 🟢 |  |
| Clive 'N' Wrench | `0100C6C010AE4000` | `FE211DBFAD6EA549` ([✅](SaltySD/plugins/FPSLocker/patches/0100C6C010AE4000/FE211DBFAD6EA549.yaml), v5, 1.0.6) | 🔵 |  |
| Cobra Kai: The Karate Kid Saga Continues | `01005790110F0000` | `97E45918D2113640` (◯, v2, 1.0.2) | 🟢 |  |
| Cobra Kai 2: Dojos Rising | `0100BD9015B54000` | `BAD8504B110A21AE` (◯, v4, 2.20.8) | 🟢 |  |
| Cocoon | `01002E700C366000` | `5D8B61D234DCE809` (◯, v3, 1.0.3) | 🟢 |  |
| Company of Heroes Collection | `0100ABD0156F8000` | `F2C994AB5CA5A756` (◯, v0, 1.5_66915) | 🟢 |  |
| Contra: Operation Galuga | `0100CF401A98E000` | `0C96F996FDE48DA8` ([✅](SaltySD/plugins/FPSLocker/patches/0100CF401A98E000/0C96F996FDE48DA8.yaml), v1, 1.0.876634) | 🔵 |  |
| CONTRA: ROGUE CORPS | `0100F2600D710000` | `4CCD2F6D331DD104` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2600D710000/4CCD2F6D331DD104.yaml), v5, 1.3.0) | 🟡 |  |
| CONVERGENCE: A League of Legends Story | `010020B016EF4000` | `7E25622D50D562BF` ([✅](SaltySD/plugins/FPSLocker/patches/010020B016EF4000/7E25622D50D562BF.yaml), v1, 1.0.1) | 🟡 |  |
| Conway: Disappearance at Dahlia View | `010075C01405C000` | `BB52C1E6BC85DA52` (◯, v0, 1.0.0.0) | 🟢 |  |
| Crash Bandicoot N. Sane Trilogy | `0100D1B006744000` | `29E1A37D84227147` (◯, v0, 1.0.0) | 🟢 |  |
| Crash Bandicoot 4: It's About Time | `010073401175E000` | `E8DB38F170B0149D` ([✅](SaltySD/plugins/FPSLocker/patches/010073401175E000/E8DB38F170B0149D.yaml), v2, 1.2) | 🔵 |  |
| Crash Team Racing Nitro-Fueled | `0100F9F00C696000` | `1C68951840693051` (◯, v15, 1.0.15) | 🟢 |  |
| Cris Tales | `0100B0400EBC4000` | `8A1DF79432172B4D` (◯, v3, 1.03) | 🟢 |  |
| CRISIS CORE -FINAL FANTASY VII- REUNION | `01004BC0166CC000` | `44D207EA6428E3F1` ([✅](SaltySD/plugins/FPSLocker/patches/01004BC0166CC000/44D207EA6428E3F1.yaml), v4, 1.0.4) | 🔴 | [LINK](Methodology/CRISIS%20CORE) |
| Cry Babies Magic Tears: The Big Game | `0100A1201B82A000` | `7C1D1E7A2B689E40` (◯, v1, 1.1) | 🟢 |  |
| Crysis Remastered | `0100E66010ADE000` | `45CE2B6625A35771` ([✅](SaltySD/plugins/FPSLocker/patches/0100E66010ADE000/45CE2B6625A35771.yaml), v8, 1.8.0) | 🔴 |  |
| Crysis 2 Remastered | `0100582010AE0000` | `B3967105033ACC08` ([✅](SaltySD/plugins/FPSLocker/patches/0100582010AE0000/B3967105033ACC08.yaml), v3, 1.3.0) | 🔴 |  |
| Crysis 3 Remastered | `0100CD3010AE2000` | `53EA0196A4AEB260` ([✅](SaltySD/plugins/FPSLocker/patches/0100CD3010AE2000/53EA0196A4AEB260.yaml), v4, 1.3.0) | 🔴 |  |
| Crystar | `01003F2016754000` | `7B41D9CC72C2124D` (◯, v2, 1.0.2) | 🟢 |  |
| Cult of the Lamb | `01002E7016C46000` | `8908DBE830187BC8` (◯, v17, 1.3.5) | 🟢 |  |
| Curse of the Dead Gods | `0100D4A0118EA000` | `DB285A63A090884F` (◯, v5, 1.0.0.5) | 🟢 |  |
| DAEMON X MACHINA | `0100B6400CA56000` | `937209E79E2E0E5D` (❌, v12, 1.4.2a) | 🟡 | [LINK](Methodology/Daemon%20X%20Machina) |
| Danganronpa V3: Killing Harmony | `010063F014176000` | `6CBEE0573826FF73` (◯, v2, 1.0.2) | 🟢 |  |
| Dark Souls Remastered | `01004AB00A260000` | `DF3766A2BB651A3E` ([✅](SaltySD/plugins/FPSLocker/patches/01004AB00A260000/DF3766A2BB651A3E.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Dark%20Souls/README.md) |
| Darksiders Genesis | `0100F2300D4BA000` | `DB17131624D04A9C` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2300D4BA000/DB17131624D04A9C.yaml), v3, 1.0.3) | 🔵 | [LINK](Methodology/Darksiders%20Genesis) |
| Darksiders Warmastered Edition | `0100E1400BA96000` | `A4CC4C44C07AEC14` (◯, v0, 1.0.0) | 🟢 |  |
| Darksiders II Deathinitive Edition | `010071800BA98000` | `173E2EDEA9E5D940` ([✅](SaltySD/plugins/FPSLocker/patches/010071800BA98000/173E2EDEA9E5D940.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Darksiders%202) |
| Darksiders III | `0100F8F014190000` | `AF7114F019CE6E1D` ([✅](SaltySD/plugins/FPSLocker/patches/0100F8F014190000/AF7114F019CE6E1D.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Darksiders%20III) |
| DAVE THE DIVER | `010097F018538000` | `8BFC21490C5E20FF` (◯, v11, 1.0.2.651) | 🟢 |  |
| Dawn of the Monsters | `01006960155C4000` | `6E6BE8185BB7E140` (◯, v2, 1.2.1) | 🟢 |  |
| DC's Justice League: Cosmic Chaos | `0100157015DD8000` | `3386C3BE1DE696DF` (◯, v5, 1.0.5) | 🟢 |  |
| Death end re;Quest | `0100AEC013DDA000` | `2F5554EBECAE652B` (❌, v1, 1.0.1) | 🔵 | [LINK](Methodology/Death%20End%20Re%3BQuest) |
| Death end re;Quest 2 | `0100EB701568A000` | `6A06F3A2582C0954` (❌, v0, 1.0.0) | 🔵 | [LINK](Methodology/Death%20End%20Re%3BQuest%202) |
| Death's Door | `0100B31015AF8000` | `0D20B5FF11828346` (◯, v3, 1.1.6a) | 🟢 |  |
| Decay of Logos | `010027700FD2E000` | `B77B17D7A517384F` (◯, v1, 1.0.1) | 🟢 |  |
| DEMON GAZE EXTRA | `0100FCC0168FC000` | `58EE9A90F6FE6D4B` (❌, v2, 1.0.2) | 🟡 |  |
| Demon Slayer -Kimetsu no Yaiba- The Hinokami Chronicles | `0100309016E7A000` | `14C878ECCA9D7CB5` ([✅](SaltySD/plugins/FPSLocker/patches/0100309016E7A000/14C878ECCA9D7CB5.yaml), v9, 1.53) | 🔴 |  |
| Demon Turf | `0100FF5015492000` | `9D3270945708DE4A` (◯, v2, 1.0.1) | 🟢 |  |
| Demon Turf: Neon Splash | `010010C017B28000` | `500BE42BCD41604F` (◯, v0, 1.0.0) | 🟢 |  |
| Destiny Connect: Tick-Tock Travelers | `010069500DD86000` | `5AD84EFD9D28FDDE` ([✅](SaltySD/plugins/FPSLocker/patches/010069500DD86000/5AD84EFD9D28FDDE.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Destiny%20Connect%20Tick-Tock%20Travelers) |
| Destroy All Humans! | `01009E701356A000` | `72E8F20EBBDBA296` ([✅](SaltySD/plugins/FPSLocker/patches/01009E701356A000/72E8F20EBBDBA296.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Destroy%20All%20Humans) |
| Detective Pikachu Returns | `010007500F27C000` | `A2A5ABEF988ABAA2` (◯, v0, 1.0.0) | 🟢 |  |
| Diablo II: Resurrected | `0100726014352000` | `786D5F0A9B0591B9` (❌, v24, 1.0.24.0) | 🔵 |  |
| Dino Ranch: Ride to the Rescue | `010038301ABDA000` | `DDF3A99F0EC84E1` (◯, v1, 1.0.3) | 🟢 |  |
| Disco Elysium - The Final Cut | `01006C5015E84000` | `EAA1EDBEAEF50854` (◯, v9, 1.0.9) | 🟢 |  |
| Disney Dreamlight Valley | `0100D39012C1A000` | `34A7473ABF0EFCCC` (◯, v27, 1.9.0) | 🟢 |  |
| Divinity: Original Sin 2 | `010027400CDC6000` | `4979B200D53BB282` ([✅](SaltySD/plugins/FPSLocker/patches/010027400CDC6000/4979B200D53BB282.yaml), v10, 1.0.10) | 🔵 |  |
| Dolphin Spirit - Ocean Mission | `0100150018200000` | `47B7DC55D707D10A` (◯, v1, 1.00.02) | 🟢 |  |
| DOOM | `0100416004C00000` | `01ACE43E724259C3` ([✅](SaltySD/plugins/FPSLocker/patches/0100416004C00000/01ACE43E724259C3.yaml), v3, 1.2) | 🟡 | [LINK](Methodology/DOOM) |
| DOOM Eternal | `0100B1A00D8CE000` | `5AF6F31EAC42DBC0` ([✅](SaltySD/plugins/FPSLocker/patches/0100B1A00D8CE000/5AF6F31EAC42D8C0.yaml), v13, 1.13) <br> `B059C2C77AD834B8` ([✅](SaltySD/plugins/FPSLocker/patches/0100B1A00D8CE000/B059C2C77AD834B8.yaml), v14, 1.14) | 🟡 | [LINK](Methodology/DOOM%20Eternal) |
| Dragon's Dogma: Dark Arisen | `010032C00AC58000` <br> `010057E00AC56000` | `2CDB9B9D70010E88` ([✅](SaltySD/plugins/FPSLocker/patches/010032C00AC58000/2CDB9B9D70010E88.yaml), v1, 1.0.1) <br> `2D5B93C856CDF009` ([✅](SaltySD/plugins/FPSLocker/patches/010057E00AC56000/2D5B93C856CDF009.yaml), v1, 1.0.1) | 🔴 |  |
| DRAGON BALL XENOVERSE 2 | `010078D000F88000` | `ACD8DFEFD0EA5316` (❌, v27, 1.20.01) | 🔴 |  |
| DRAGON BALL Z: KAKAROT | `010051C0134F8000` | `13B450093A7DA8E2` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/13B450093A7DA8E2.yaml), v8, 1.32) <br> `0C1B09D4D2FD0972` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/0C1B09D4D2FD0972.yaml), v10, 1.41) <br> `FFD9B653EAE305F7` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/FFD9B653EAE305F7.yaml), v11, 1.42) <br> `20503FA77FA416B7` ([✅](SaltySD/plugins/FPSLocker/patches/010051C0134F8000/20503FA77FA416B7.yaml), v12, 1.50) | 🔴 |  |
| DRAGON QUEST MONSTERS: The Dark Prince | `0100A77018EA0000` | `D1E6883BD8F9EB22` (◯, v5, 1.0.5) | 🟢 |  |
| DRAGON QUEST XI S: Echoes of an Elusive Age | `01006C300E9F0000` | `1719AABFA5EAE42B` ([✅](SaltySD/plugins/FPSLocker/patches/01006C300E9F0000/1719AABFA5EAE42B.yaml), v3, 1.0.3) | 🔵 | [LINK](Methodology/Dragon%20Quest%20XI%20S) |
| DRAGON QUEST TREASURES | `010049B017774000` | `2F81A2EC9B298B37` ([✅](SaltySD/plugins/FPSLocker/patches/010049B017774000/2F81A2EC9B298B37.yaml), v1, 1.0.1) | 🔴 |  |
| Dredge | `01008CD0172D6000` | `D16558D855603353` ([✅](SaltySD/plugins/FPSLocker/patches/01008CD0172D6000/D16558D855603353.yaml), v4, 1.1.0) <br> `B9CC2F4DE53D4F94` ([✅](SaltySD/plugins/FPSLocker/patches/01008CD0172D6000/B9CC2F4DE53D4F94.yaml), v8, 1.4.2) | 🟡 |  |
| Dusk Diver | `0100B2B00E7AA000` | `FAD1AF4EDC6DB267` ([✅](SaltySD/plugins/FPSLocker/patches/0100B2B00E7AA000/FAD1AF4EDC6DB267.yaml), v6, 1.0.6) | 🔴 |  |
| Dusk Diver 2 | `01003980174BC000` | `217C9ECF258C0312` ([✅](SaltySD/plugins/FPSLocker/patches/01003980174BC000/217C9ECF258C0312.yaml), v1, 1.0.1) | 🔴 |  |
| Dying Light | `01008C8012920000` | `8C93B930348C9787` ([✅](SaltySD/plugins/FPSLocker/patches/01008C8012920000/8C93B930348C9787.yaml), v5, 1.0.5) | 🔵 |  |
| EA SPORTS FC 24 | `0100BDB01A0E6000` | `6B6D4D60E3187FFC` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/6B6D4D60E3187FFC.yaml), v1, 1.0.0) <br> `A8D4FEE18023F15C` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/A8D4FEE18023F15C.yaml), v2, 1.53.dd6d) <br> `E0A5A92EA4F37A3A` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/E0A5A92EA4F37A3A.yaml), v3, 1.54.1d19) <br> `58636D33E56B931B` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/58636D33E56B931B.yaml), v4, 1.54.2d45) <br> `9C33602289E55F7A` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/9C33602289E55F7A.yaml), v5, 1.54.6f8d) <br> `59BAA4874FE56C9A` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/59BAA4874FE56C9A.yaml), v6, 1.54.872c) <br> `C621E3FB41BF3858` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/C621E3FB41BF3858.yaml), v7, 1.54.e482) <br> `355CD175B2498C22` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/355CD175B2498C22.yaml), v8, 1.55.6363) <br> `538BB4DE29BF89F3` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/538BB4DE29BF89F3.yaml), v9, 1.55.7eb0) <br> `51D25A22EBBBAB37` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/51D25A22EBBBAB37.yaml), v10, 1.55.bc14) <br> `1CE25F1C48FE03E0` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/1CE25F1C48FE03E0.yaml), v11, 1.56.39f6) <br> `211F141951057FBA` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/211F141951057FBA.yaml), v12, 1.56.46a8) <br> `29D2EC9632DE7D8C` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/29D2EC9632DE7D8C.yaml), v13, 1.56.a976) <br> `E6943FAD2661916E` ([✅](SaltySD/plugins/FPSLocker/patches/0100BDB01A0E6000/E6943FAD2661916E.yaml), v14, 1.56.d68f) | 🔴 | [LINK](Methodology/EA%20SPORTS%20FC%2024) |
| Earthfall: Alien Horde | `0100DFC00E472000` | `448C08A9533F3CAD` ([✅](SaltySD/plugins/FPSLocker/patches/0100DFC00E472000/448C08A9533F3CAD.yaml), v1, 1.0.1) | 🔵 |  |
| EarthX | `010069001B820000` | `1F9EA163A82C7D8F` (◯, v2, 1.0.2) | 🟢 |  |
| Easy Come Easy Golf | `0100ECF01800C000` | `FA0A3A55243FAC21` (◯, v4, 1.9.1) | 🟢 |  |
| Eiyuden Chronicle: Rising | `010039B015CB6000` | `39DC785D9073C22B` ([✅](SaltySD/plugins/FPSLocker/patches/010039B015CB6000/39DC785D9073C22B.yaml), v2, 1.02) | 🔵 |  |
| Embr | `0100CC6013432000` | `473D222EB1BDAD47` (◯, v6, 1.0.6) | 🟢 |  |
| Everdream Valley | `0100B9801AA3C000` | `DE1DF9385F18D3B5` (◯, v8, 1.0.8) | 🟢 |  |
| Everspace | `0100DCF0093EC000` | `71873FEB4648FA39` ([✅](SaltySD/plugins/FPSLocker/patches/0100DCF0093EC000/71873FEB4648FA39.yaml), v5, 1.0.5) | 🔴 | [LINK](Methodology/Everspace) |
| Expeditions: A Mudrunner Game | `01002C101C1AA000` | `2DF3FBBCB5B00404` ([✅](SaltySD/plugins/FPSLocker/patches/01002C101C1AA000/2DF3FBBCB5B00404.yaml), v2, 1.2.0.0) <br> `2D32512D25F74760` ([✅](SaltySD/plugins/FPSLocker/patches/01002C101C1AA000/2D32512D25F74760.yaml), v3, 1.3.0.0) | 🔵 |  |
| FAR: Changing Tides | `01008A0014A92000` | `7041BC78D64745A1` (◯, v2, 1.2.0) | 🟢 |  |
| FAR: Lone Sails | `010022700E7D6000` | `CE59C773211A1A49` (◯, v0, 1.0.0) <br> `8FD06AB8DA27EC40` (◯, v1, 1.3) | 🟢 |  |
| Farming Simulator 23 | `01001E3017A10000` | `1C38F0E269ED4438` ([✅](SaltySD/plugins/FPSLocker/patches/01001E3017A10000/1C38F0E269ED4438.yaml), v1, 1.1.0.0) <br> `0204E8D91F22A2D1` ([✅](SaltySD/plugins/FPSLocker/patches/01001E3017A10000/0204E8D91F22A2D1.yaml), v4, 1.4.0.1) <br> `17F37A56B17DD9CC` ([✅](SaltySD/plugins/FPSLocker/patches/01001E3017A10000/17F37A56B17DD9CC.yaml), v5, 1.5.0.0) | 🔴 |  |
| F.I.S.T.: Forged in Shadow Torch | `01009F8017F48000` | `69EE5F71F187EAA9` ([✅](SaltySD/plugins/FPSLocker/patches/01009F8017F48000/69EE5F71F187EAA9.yaml), v4, 1.0.4) | 🔵 | [LINK](Methodology/F.I.S.T) |
| Fate/EXTELLA | `010053E002EA2000` | `76EC789B99A25BA5` ([✅](SaltySD/plugins/FPSLocker/patches/010053E002EA2000/76EC789B99A25BA5.yaml), v0, 1.0.0) | 🔵 |  |
| Fate/EXTELLA LINK | `01001A700C832000` | `97FC79E063E26C9B` ([✅](SaltySD/plugins/FPSLocker/patches/01001A700C832000/97FC79E063E26C9B.yaml), v2, 1.0.2) | 🔵 |  |
| Fate/Samurai Remnant | `01003AE01AA76000` | `B3F271EF130A5338` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/B3F271EF130A5338.yaml), v1, 1.0.1) <br> `9570C86D7B480C1E` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/9570C86D7B480C1E.yaml), v2, 1.0.2) <br> `A48A8BC73E155AB8` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/A48A8BC73E155AB8.yaml), v3, 1.0.3) <br> `0F09DF1B3AA9E3FD` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/0F09DF1B3AA9E3FD.yaml), v7, 1.1.3) <br> `FBF410FC5DD41876` ([✅](SaltySD/plugins/FPSLocker/patches/01003AE01AA76000/FBF410FC5DD41876.yaml), v8, 1.1.4) | 🔴 |  |
| Fe | `0100D2600736A000` | `4FF8F56B697A0949` (◯, v0, 1.0.0) | 🟢 |  |
| FINAL FANTASY VIII Remastered | `01008B900DC0A000` | `7F59549F6E792936` (❌, v3, 1.0.1_5) | 🔴 |  |
| FINAL FANTASY XII THE ZODIAC AGE | `0100EB100AB42000` | `C2932C4D1C84ED7D` (❌, v1, 1.1.0) | 🟡 |  |
| Fire Emblem Engage | `0100A6301214E000` | `8C08B9719E085F91` ([✅](SaltySD/plugins/FPSLocker/patches/0100A6301214E000/8C08B9719E085F91.yaml), v5, 2.0.0) | 🟡 |  |
| Fire Emblem: Three Houses | `010055D009F78000` | `89048449BA238C8C` ([✅](SaltySD/plugins/FPSLocker/patches/010055D009F78000/89048449BA238C8C.yaml), v5, 1.2.0) | 🔵 |  |
| Fishing: North Atlantic | `0100A55019C38000` | `B9DB6040F70BE58F` ([✅](SaltySD/plugins/FPSLocker/patches/0100A55019C38000/B9DB6040F70BE58F.yaml), v1, 1.1) | 🔵 | [LINK](Methodology/Fishing%20North%20Atlantic) |
| Flooded | `010022201D254000` | `AF274CB758733A56` (❌, v1, 1.0.1) | 🔴 | [LINK](Methodology/Flooded) |
| Forgive Me Father | `0100A2A01A026000` | `008F995D1A63B383` ([✅](SaltySD/plugins/FPSLocker/patches/0100A2A01A026000/008F995D1A63B383.yaml), v2, 1.5.4.3) | 🔵 |  |
| Fresh Start | `0100AA001BAB8000` | `9B2BC4BAF72D350A` (❌, v0, 1.0.0) | 🔵 |  |
| FROGUN DELUXE EDITION | `0100A0A018D3A000` | `7FA5168E6BEA2A40` (◯, v3, 1.3) | 🟢 |  |
| From Space | `010015F018C3C000` | `593BD545295A65FB` ([✅](SaltySD/plugins/FPSLocker/patches/010015F018C3C000/593BD545295A65FB.yaml), v2, 1.0.357) <br> `9806FB67CE24E904` ([✅](SaltySD/plugins/FPSLocker/patches/010015F018C3C000/9806FB67CE24E904.yaml), v3, 1.3.480) | 🔵 |  |
| FRONT MISSION 1st: Remake | `0100F200178F4000` | `188BF4CBE682C3AC` (◯, v5, 2.0.5) | 🟢 |  |
| FRONT MISSION 2: Remake | `0100C4E018A24000` | `A1562F9B4AA3494A` (◯, v5, 1.0.4.2) | 🟢 |  |
| Gamedec - Definitive Edition | `01002A501869E000` | `BFA92380757EF97D` ([✅](SaltySD/plugins/FPSLocker/patches/01002A501869E000/BFA92380757EF97D.yaml), v3, 1.3.0) | 🔴 | [LINK](Methodology/Gamedec) |
| Garfield Kart Furious Racing | `010061E00E8BE000` | `4A67AFB9EAC0DF44` (◯, v3, 1.0.3) | 🟢 |  |
| Gear.Club Unlimited 2 | `010072900AFF0000` | `FE757810B45C3444` ([✅](SaltySD/plugins/FPSLocker/patches/010072900AFF0000/FE757B10B45C3444.yaml), v14, 1.7.2) | 🔴 |  |
| GetsuFumaDen: Undying Moon | `010042A013DB8000` | `8683E654CCD68852` (❌, v2, 1.1.1) | 🔵 | [LINK](Methodology/GetsuFumaDen) |
| Ghostbusters: Spirits Unleashed Ecto Edition | `01005D2016934000` | `0515F2089A2FC744` ([✅](SaltySD/plugins/FPSLocker/patches/01005D2016934000/0515F2089A2FC744.yaml), v4, 1.7.3) |  |
| Ghostrunner | `010090F012916000` | `D3DD5B220DCEB626` ([✅](SaltySD/plugins/FPSLocker/patches/010090F012916000/D3DD5B220DCEB626.yaml), v8, 1.8) | 🔴 |
| Gigantosaurus The Game | `01002C400E526000` | `EF7B49570430043E` ([✅](SaltySD/plugins/FPSLocker/patches/01002C400E526000/EF7B49570430043E.yaml), v0, 1.0.0) <br> `1FF442C5ABEB0459` ([✅](SaltySD/plugins/FPSLocker/patches/01002C400E526000/1FF442C5ABEB0459.yaml), v2, 1.0.2) | 🔴 | [LINK](Methodology/Gigantosaurus%20The%20Game) |
| Gigantosaurus: Dino Kart | `01001890167FE000` | `5F7A2866D8E20BBA` ([✅](SaltySD/plugins/FPSLocker/patches/01001890167FE000/5F7A2866D8E20BBA.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/Gigantosaurus%20Dino%20Kart) |
| GO VACATION | `0100C1800A9B6000` | `174471C5192F8647` (❌, v0, 1.0.0) | 🔵 |  |
| GOD EATER 3 | `01001C700873E000` | `C0F144F5139F542E` ([✅](SaltySD/plugins/FPSLocker/patches/01001C700873E000/C0F144F5139F542E.yaml), v11, 2.5.1) | 🔵 |  |
| GOD WARS The Complete Legend | `0100F3D00B032000` | `3A0835D09F6D1544` (❌, v1, 1.1) | 🔵 | [LINK](Methodology/God%20Wars) |
| Gods Will Fall | `0100CFA0111C8000` | `2C22089ABC14264F` (◯, v4, 1.0.4) | 🟢 |  |
| Going Under | `01004D501113C000` | `3AC30B12FEAD3149` (◯, v4, 1.0.4) | 🟢 |  |
| Golazo 2 | `0100997014004000` | `8057D5A82615847E` (◯, v2, 1.2.3) | 🟢 |  |
| Good Job! | `0100B0500FE4E000` | `951D09EECE122A47` (◯, v0, 1.0.0) | 🟢 |  |
| Grand Theft Auto III | `0100C3C012718000` | `2CF52C8DA4468946` ([✅](SaltySD/plugins/FPSLocker/patches/0100C3C012718000/2CF52C8DA4468946.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20III) |
| Grand Theft Auto: San Andreas | `010065A014024000` | `6FB56071CCB321B6` ([✅](SaltySD/plugins/FPSLocker/patches/010065A014024000/6FB56071CCB321B6.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20San%20Andreas) |
| Grand Theft Auto: Vice City | `0100182014022000` | `56EEFA704373BDB3` ([✅](SaltySD/plugins/FPSLocker/patches/0100182014022000/56EEFA704373BDB3.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20Vice%20City) |
| Graveyard Keeper | `0100B6800B5C8000` | `9356531EDD2EC448` (◯, v6, 1.0.0.4633) | 🟢 |  |
| GRID Autosport | `0100DC800A602000` | `347A44223C9537A5` (◯, v10, 1.10.1_70328) | 🟢 |  |
| GRIME | `0100F300169B6000` | `30D54FEC2708DFA8` (◯, v3, 1.3.2) | 🟢 |  |
| Gripper | `010099C01896C000` | `60B9AE6094566A23` ([✅](SaltySD/plugins/FPSLocker/patches/010099C01896C000/60B9AE6094566A23.yaml), v2, 1.1.0) | 🔵 |  |
| Gungrave G.O.R.E | `010088801B324000` | `A0E97BF4475FE385` (◯, v1, 1.0.1) <br> `919A5D41DCD21F9E` ([✅](SaltySD/plugins/FPSLocker/patches/010088801B324000/919A5D41DCD21F9E.yaml), v3, 1.0.3) <br> `9B743181AB8A26F9` ([✅](SaltySD/plugins/FPSLocker/patches/010088801B324000/9B743181AB8A26F9.yaml), v4, 1.0.4) | 🔵 |  |
| GYLT | `0100AC601DCA8000` | `4584432786F462DB` ([✅](SaltySD/plugins/FPSLocker/patches/0100AC601DCA8000/4584432786F462DB.yaml), v2, 1.2) | 🔵 |  |
| HARVESTELLA | `0100521017B2A000` | `249EAB9BF046C5EA` ([✅](SaltySD/plugins/FPSLocker/patches/0100521017B2A000/249EAB9BF046C5EA.yaml), v2, 1.0.2) | 🔴 | [LINK](Methodology/HARVESTELLA) |
| Hellblade: Senua's Sacrifice | `010044500CF8E000` | `9B3DDF2FB9100E51` ([✅](SaltySD/plugins/FPSLocker/patches/010044500CF8E000/9B3DDF2FB9100E51.yaml), v1, 1.1.0) | 🔴 |  |
| Hitman: Blood Money - Reprisal | `010083A018262000` | `688C23D524730AB8` ([✅](SaltySD/plugins/FPSLocker/patches/010083A018262000/688C23D524730AB8.yaml), v0, 1.0_68328) | 🔴 |  |
| Hoa | `010022E013A1A000` | `1A9DF794AC0099F3` (◯, v3, 1.0.3) | 🟢 |  |
| Hogwarts Legacy | `0100F7E00C70E000` | `550F2E8B387B4520` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7E00C70E000/550F2E8B387B4520.yaml), v1, 1.0.1) <br> `F1AE192C465BD920` ([✅](SaltySD/plugins/FPSLocker/patches/0100F7E00C70E000/F1AE192C465BD920.yaml), v2, 1.0.2) | 🔵 |  |
| Hokko Life | `010022A016250000` | `D9D13603133F3D89` (◯, v5, 1.0.5) | 🟢 |  |
| Horizon Chase 2 | `0100001019F6E000` | `3CE4DB955A23026E` ([✅](SaltySD/plugins/FPSLocker/patches/0100001019F6E000/3CE4DB955A23026E.yaml), v3, 1.5.2) <br> `95B2E97C5D16385A` ([✅](SaltySD/plugins/FPSLocker/patches/0100001019F6E000/95B2E97C5D16385A.yaml), v4, 1.5.4) <br> `1C95A999050892E0` ([✅](SaltySD/plugins/FPSLocker/patches/0100001019F6E000/1C95A999050892E0.yaml), v5, 1.5.5) | 🔴 |  |
| HOT WHEELS UNLEASHED | `0100AA60136D2000` | `F73C6504D378C38B` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA60136D2000/F73C6504D378C38B.yaml), v13, 1.0.13) | 🔵 | [LINK](Methodology/HOT%20WHEELS%20UNLEASHED) |
| HOT WHEELS UNLEASHED 2 | `01001BE01908C000` | `012294C1E2D28A79` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/012294C1E2D28A79.yaml), v1, 1.0.1) <br> `EBD417A7EB6B5486` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/EBD417A7EB6B5486.yaml), v4, 1.0.4) <br> `3973FB8AC2750BE4` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/3973FB8AC2750BE4.yaml), v5, 1.0.5) <br> `53E622E32DB8780F` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/53E622E32DB8780F.yaml), v6, 1.0.6) <br> `DF0F7D04FC02C9BB` ([✅](SaltySD/plugins/FPSLocker/patches/01001BE01908C000/DF0F7D04FC02C9BB.yaml), v7, 1.0.7) | 🔵 | [LINK](Methodology/HOT%20WHEELS%20UNLEASHED%202) |
| House Flipper | `0100CAE00EB02000` | `E137EF110988444F` (◯, v10, 1.10.0) | 🟢 |  |
| HYPERCHARGE: Unboxed | `0100A8B00F0B4000` | `92511355705EA8C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100A8B00F0B4000/92511355705EA8C5.yaml), v5, 0.1.2341.233) | 🔵 | [LINK](Methodology/HYPERCHARGE%20Unboxed) |
| Hyrule Warriors: Age of Calamity | `01002B00111A2000` | `C3CF52BF2B05D731` ([✅](SaltySD/plugins/FPSLocker/patches/01002B00111A2000/C3CF52BF2B05D731.yaml), v5, 1.3.0) | 🔴 |  |
| I Am Setsuna. | `0100849000BDA000` | `0BBA2167AED893BE` (◯, v1, 1.1.0) | 🟢 |  |
| Immortal Redneck | `01000F400435A000` | `DB367E57EDA9E84F` (◯, v1, 1.3.5) | 🟢 |  |
| Immortals Fenyx Rising | `01004A600EC0A000` | `70F3F6751D73C644` (❌, v11, 1.3.4) | 🔵 |  |
| In rays of the Light | `0100A760129A0000` | `AB4C861FD0C87F47` (◯, v2, 1.0.2) | 🟢 |  |
| In Sound Mind | `01006DF014682000` | `F0D0A9CC07EF507B` (❌, v3, 1.0.3) | 🔵 |  |
| INMOST | `0100F1401161E000` | `16CEFEA33FE6E24F` (❌, v6, 1.0.4.3) | 🔵 |  |
| Insomnis | `01001CF0190C2000` | `4C6727375D877B90` ([✅](SaltySD/plugins/FPSLocker/patches/01001CF0190C2000/4C6727375D877B90.yaml), v1, 1.01) | 🔵 | [LINK](Methodology/Insomnis) |
| Ion Fury | `010041C00D086000` | `9D2EFCF198F2247F` (◯, v4, 1.07.1) | 🔴 | [LINK](Methodology/Ion%20Fury) |
| Ironsmith: Medieval Simulator | `010025A01CD86000` | `D2A5A1FC6EEADF31` ([✅](SaltySD/plugins/FPSLocker/patches/010025A01CD86000/D2A5A1FC6EEADF31.yaml), v1, 1.1.0) | 🔵 |  |
| It Takes Two | `010092A0172E4000` | `C4067E8CB3258656` ([✅](SaltySD/plugins/FPSLocker/patches/010092A0172E4000/C4067E8CB3258656.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/It%20Takes%20Two) |
| Jojo's Bizarre Adventure: All-Star Battle R | `010017A0128C4000` | `B2FA8FF1240615F1` ([✅](SaltySD/plugins/FPSLocker/patches/010017A0128C4000/B2FA8FF1240615F1.yaml), v15, 2.3.0) <br> `3D4E3A9252AA6C63` ([✅](SaltySD/plugins/FPSLocker/patches/010017A0128C4000/3D4E3A9252AA6C63.yaml), v16, 2.3.3) | 🔴 |  |
| Jujutsu Kaisen Cursed Clash | `01002FC012548000` <br> `010085401A454000` | `372BF1E32FC51836` ([✅](SaltySD/plugins/FPSLocker/patches/01002FC012548000/372BF1E32FC51836.yaml), v1, 1.0.1) | 🔴 |  |
| JUMP FORCE | `010019D010F0E000` <br> `0100183010F12000` | `1667568420912C73` (❌, v7, 1.08) | 🟡 |  |
| Kao the Kangaroo | `0100956016464000` <br> `010078C01769A000` | `F9C83728910E28A4` ([✅](SaltySD/plugins/FPSLocker/patches/0100956016464000/F9C83728910E28A4.yaml), v5, 1.5) <br> `7BA282E94D34C620` ([✅](SaltySD/plugins/FPSLocker/patches/010078C01769A000/7BA282E94D34C620.yaml), v5, 1.5) | 🔵 | [LINK](Methodology/Kao%20The%20Kangaroo) |
| Katamari Damacy REROLL | `0100D7000C2C6000` | `B528B17AD9C71F41` (❌, v2, 1.2) | 🟡 |  |
| Kingdom Come: Deliverance | `0100650018FE0000` | `7A450848CFDEC18E` ([✅](SaltySD/plugins/FPSLocker/patches/0100650018FE0000/7A450848CFDEC18E.yaml), v2, 1.9.6H) | 🔴 |  |
| Kingdoms of Amalur: Re-Reckoning | `0100EF50132BE000` | `FA48B344ED72F24D` (◯, v7, 1.0.7) | 🟢 |  |
| Kitaria Fables | `0100F30013BFC000` | `220AA80516734F4C` (◯, v3, 1.0.3) | 🟢 |  |
| Kirby and the Forgotten Land | `01004D300C5AE000` | `D9BA7DB72FFAFECD` ([✅](SaltySD/plugins/FPSLocker/patches/01004D300C5AE000/D9BA7DB72FFAFECD.yaml), v0, 1.0.0) | 🔴 |  |
| Kirby Star Allies | `01007E3006DDA000` | `D55608916FA56C18`  ([✅](SaltySD/plugins/FPSLocker/patches/01007E3006DDA000/D55608916FA56C18.yaml), v5, 4.0.0) | 🔴 |  |
| Kirby's Dream Buffet | `0100A8E016236000` | `82AF4E16BBC0BEC8` ([✅](SaltySD/plugins/FPSLocker/patches/0100A8E016236000/82AF4E16BBC0BEC8.yaml), v0, 1.0.0) | 🔴 |  |
| L.A. Noire | `0100830004FB6000` | `40F973CE3B5EC8D7` ([✅](SaltySD/plugins/FPSLocker/patches/0100830004FB6000/40F973CE3B5EC8D7.yaml), v2, 1.2) | 🟡 | [LINK](Methodology/L.A.%20Noire) |
| LEGO 2K Drive | `0100739018020000` | `035715948447A762` ([✅](SaltySD/plugins/FPSLocker/patches/0100739018020000/035715948447A762.yaml), v4, 1.4) <br> `E93D49581521E084` ([✅](SaltySD/plugins/FPSLocker/patches/0100739018020000/E93D49581521E084.yaml), v7, 1.7) <br> `6DBC20263D224B3C` ([✅](SaltySD/plugins/FPSLocker/patches/0100739018020000/6DBC20263D224B3C.yaml), v13, 1.13) <br> `AA906741384B10CC` ([✅](SaltySD/plugins/FPSLocker/patches/0100739018020000/AA906741384B10CC.yaml), v14, 1.14) <br> `CE1D6113B65F2914` ([✅](SaltySD/plugins/FPSLocker/patches/0100739018020000/CE1D6113B65F2914.yaml), v16, 1.16) | 🔴 |  |
| LEGO City Undercover | `010085500130A000` | `32C590B064956546` (◯, v3, 1.0.3) | 🟢 |  |
| LEGO DC Super-Villains | `010070D009FEC000` | `711C52FC37605D45` (◯, v8, 1.0.8) | 🟢 |  |
| LEGO Jurassic World | `01001C100E772000` | `1B80403BE8882745` (◯, v1, 1.0.1) | 🟢 |  |
| LEGO MARVEL Super Heroes | `01006F600FFC8000` | `5D769ABCAD9F2743` (◯, v1, 1.0.1) | 🟢 |  |
| LEGO MARVEL Super Heroes 2 | `01007690040A0000` | `794534B11CF3BE40` (◯, v7, 1.0.7) | 🟢 |  |
| LEGO Star Wars: The Skywalker Saga | `010042D00D900000` | `C6901CE5426C704A` ([✅](SaltySD/plugins/FPSLocker/patches/010042D00D900000/C6901CE5426C704A.yaml), v8, 1.0.8) <br> `EC593A5F9552100A` ([✅](SaltySD/plugins/FPSLocker/patches/010042D00D900000/EC593A5F9552100A.yaml), v9, 1.10.0) | 🔵 | [LINK](Methodology/LEGO%20Star%20Wars%20The%20Skywalker%20Saga) |
| LEGO The Incredibles | `0100F19006E04000` | `414D247F3FD8084E` (◯, v2, 1.0.2) | 🟢 |  |
| LEGO Worlds | `0100838002AEA000` | `8174C89125B5404E` (◯, v10, 1.3.2) | 🟢 |  |
| Life is Strange | `0100DC301186A000` | `EE295EAAEA7D31E4` ([✅](SaltySD/plugins/FPSLocker/patches/0100DC301186A000/EE295EAAEA7D31E4.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Life%20is%20Strange) |
| Life is Strange 2 | `0100FD101186C000` | `BF0088C59D7E97C0`  ([✅](SaltySD/plugins/FPSLocker/patches/0100FD101186C000/BF0088C59D7E97C0.yaml), v1, 1.1.0) | 🔴 | [LINK](Methodology/Life%20is%20Strange%202) |
| Life is Strange: True Colors | `0100500012AB4000` | `118AA7B71E824B3B` ([✅](SaltySD/plugins/FPSLocker/patches/0100500012AB4000/118AA7B71E824B3B.yaml), v4, 1.0.4) | 🔴 | [LINK](Methodology/Life%20is%20Strange%20True%20Colors) |
| Little Noah: Scion of Paradise | `0100535014D76000` | `5BA1C162571DBD01` (◯, v6, 1.40) | 🟢 |  |
| Little Nightmares II | `010097100EDD6000` | `7F4216B6E784A4B2` ([✅](SaltySD/plugins/FPSLocker/patches/010097100EDD6000/7F4216B6E784A4B2.yaml), v4, 1.4) | 🔵 | [LINK](Methodology/Little%20Nightmares%20II/README.md) |
| Little Town Hero | `01000FB00AA90000` | `2BE4AF8B1A137445` (❌, v2, 1.2.0) | 🟡 |  |
| LIVE A LIVE | `0100CF801776C000` | `CF22083371DDACB2` (◯, v1, 1.0.1) | 🟢 |  |
| Lost In Random | `01005FE01291A000` | `416914C121775277` (◯, v1, 1.0.1) | 🟢 |  |
| LOST SPHEAR | `010077B0038B2000` | `641A9243BA35C638` (◯, v5, 1.3.1) | 🟢 |  |
| Luigi's Mansion 3 | `0100DCA0064A6000` | `79E5950FFA85ACF6` ([✅](SaltySD/plugins/FPSLocker/patches/0100DCA0064A6000/79E5950FFA85ACF6.yaml), v5, 1.4.0) | 🔴 |  |
| Maglam Lord | `01002C0015644000` | `3A3C781930CB8201` ([✅](SaltySD/plugins/FPSLocker/patches/01002C0015644000/3A3C781930CB8201.yaml), v0, 1.00) | 🔴 |  |
| Maquette | `0100861018480000` | `B0F09EE3E404D549` (❌, v0, 1.0.0) | 🔵 |  |
| Mario + Rabbids Kingdom Battle | `010067300059A000` | `3B39E0C06B8841F1` (◯, v9, 1.9.589692) | 🟢 |  |
| Mario + Rabbids Sparks of Hope | `0100317013770000` | `5B76A43B231E0640` (◯, v6, 1.6.2225577) | 🟢 |  |
| Mark of the Ninja: Remastered | `01009A700A538000` | `AE324830FE37FC72` (◯, v2, 1.0.2) | 🟢 |  |
| Marvel Ultimate Alliance 3: The Black Order | `010060700AC50000` | `E853C44FDF18B88F` ([✅](SaltySD/plugins/FPSLocker/patches/010060700AC50000/E853C44FDF18B88F.yaml), v8, 4.0.1) | 🔴 |  |
| Mary Skelter Finale | `0100530014438000` | `B1AFBB02475AD7E3` (❌, v1, 1.0.1) | 🔵 |  |
| Märchen Forest | `01001B2012D5E000` | `7A7C634CDAFE7D42` (◯, v7, 1.0.7) | 🟢 |  |
| Master Detective Archives: RAIN CODE | `01004800197F0000` <br> `0100149019460000` | `2058227F80E9B40C` ([✅](SaltySD/plugins/FPSLocker/patches/01004800197F0000/2058227F80E9B40C.yaml), v3, 1.3.0) <br> `6D722DED660CD6E3` ([✅](SaltySD/plugins/FPSLocker/patches/01004800197F0000/6D722DED660CD6E3.yaml), v5, 1.3.2) <br> `B1C54D7E3540577B` ([✅](SaltySD/plugins/FPSLocker/patches/01004800197F0000/B1C54D7E3540577B.yaml), v6, 1.3.3) <br> `B9E42653FB44EF2B` ([✅](SaltySD/plugins/FPSLocker/patches/0100149019460000/B9E42653FB44EF2B.yaml), v7, 1.4.0) <br> `F4685ACC91FEDB12` ([✅](SaltySD/plugins/FPSLocker/patches/01004800197F0000/F4685ACC91FEDB12.yaml), v7, 1.4.0) | 🔴 |  |
| Masters of Anima | `0100CC7009196000` | `B1C8B55EBD400E57` (◯, v1, 1.0.1) | 🟢 |  |
| Metal Gear Solid 2: Sons of Liberty | `0100A4301AA0C000` | `FA8A6B3A9E27FD33` (❌, v8, 1.5.0) | 🟡 |  |
| Metal Gear Solid 3: Snake Eater | `010047F01AA10000` | `BAFD3A1CA57EEAA9` (❌, v8, 1.5.0) | 🟡 |  |
| Metro 2033 Redux | `0100D4900E82C000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4900E82C000/85C362CC9790F0ED.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Metro%20Redux%20Collection) |
| Metro: Last Light Redux | `0100F0400E850000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100F0400E850000/85C362CC9790F0ED.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Metro%20Redux%20Collection) |
| Miitopia | `01003DA010E8A000` | `3378B75A3DD2ADA9` (❌, v3, 1.0.3) | 🟡 |  |
| Minecraft Dungeons | `01006C100EC08000` | `13F573E3017996E4` (◯, v27, 1.17.0.0) | 🟢 |  |
| Modern Combat Blackout | `0100D8700B712000` | `C56E6F514FADC5C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100D8700B712000/C56E6F514FADC5C5.yaml), v3, 1.1.9) | 🔴 |  |
| MONARK | `0100E4A01548C000` | `85EB6295023DD394` (◯, v1, 1.0.1) | 🟢 |  |
| Monster Hunter Generations Ultimate | `0100770008DD8000` <br> `0100C3800049C000` | `FB08F1D20FD1204F` (✝️, v4, 1.4.0) <br> `9D4C86E6EF74504A` (✝️, v5, 1.5.0) | 🟣 | [LINK](Methodology/Monster%20Hunter%20Generations%20Ultimate)
| Monster Hunter Rise | `0100B04011742000` <br> `0100559011740000` | `11C9CE3F0676EEFD` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/11C9CE3F0676EEFD.yaml), v29, 14.0.0) <br> `60EFBA0CB724E3FE` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/60EFBA0CB724E3FE.yaml), v30, 15.0.0) <br> `9B50DDD970E50DD5` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/9B50DDD970E50DD5.yaml), v31, 15.0.1) <br> `5CE1FFBE4B433343` ([✅](SaltySD/plugins/FPSLocker/patches/0100559011740000/5CE1FFBE4B433343.yaml), v31, 15.0.1) <br> `44C9289FBB51455F` ([✅](SaltySD/plugins/FPSLocker/patches/0100559011740000/44C9289FBB51455F.yaml), v32, 16.0.0) <br> `55D50CA1805E9C5B` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/55D50CA1805E9C5B.yaml), v33, 16.0.1) <br> `92DF51D37268A38C` ([✅](SaltySD/plugins/FPSLocker/patches/0100559011740000/92DF51D37268A38C.yaml), v33, 16.0.1) <br> `C9A3DD7702075ECD` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/C9A3DD7702075ECD.yaml), v34, 16.0.2) <br> `D2FD97779381FB9A` ([✅](SaltySD/plugins/FPSLocker/patches/0100559011740000/D2FD97779381FB9A.yaml), v34, 16.0.2) | 🔴 | [LINK](Methodology/Monster%20Hunter%20Rise) |
| Monster Jam Steel Titans | `010095C00F354000` | `8CA6136CF49F1A4F` (◯, v1, 1.0.1) | 🟢 |  |
| Monster Jam Steel Titans 2 | `010051B0131F0000` | `E0E9D0429A2458E1` ([✅](SaltySD/plugins/FPSLocker/patches/010051B0131F0000/E0E9D0429A2458E1.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/Monster%20Jam%20Steel%20Titans%202) |
| Monster Truck Championship | `0100D30010C42000` | `682F4A502035678D` ([✅](SaltySD/plugins/FPSLocker/patches/0100D30010C42000/682F4A502035678D.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/Monster%20Truck%20Championship) |
| Monster Train | `01006D9013894000` | `9DCA1A70C6414A49` (◯, v1, 2.2.0) | 🟢 |  |
| MotoGP 23 | `0100B750198C6000` | `CEE6B8B19D3A863E` ([✅](SaltySD/plugins/FPSLocker/patches/0100B750198C6000/CEE6B8B19D3A863E.yaml), v3, 1.0.3) <br> `FF0DDCCB9C3B9375` ([✅](SaltySD/plugins/FPSLocker/patches/0100B750198C6000/FF0DDCCB9C3B9375.yaml), v7, 1.0.7) | 🔵 |  |
| Moving Out | `0100C4C00E73E000` | `CB3172ED0C3BC646` (◯, v6, 1.0.6) | 🟢 |  |
| Moving Out 2 | `010065D018172000` | `C552B6464E7348A7` (◯, v5, 1.3.315) | 🟢 |  |
| My Time at Sandrock | `0100B63016916000` | `4B71E4BC46DC7F19` (◯, v6, 1.1.4.2) | 🟢 |  |
| Mythic Ocean | `0100F4F014108000` | `2284DFB25F387719` ([✅](SaltySD/plugins/FPSLocker/patches/0100F4F014108000/2284DFB25F387719.yaml), v1, 1.0.1) | 🔴 |  |
| NARUTO SHIPPUDEN:<br>Ultimate Ninja STORM 4<br>ROAD TO BORUTO | `01006CF00CF60000` | `D3016FC0C0402DFB` (❌, v3, 1.3.0) | 🔴 | [LINK](Methodology/Naruto%20Shippuuden%20Ultimate%20Ninja%20Storm%204%20Road%20to%20Boruto) |
| NARUTO X BORUTO Ultimate Ninja STORM CONNECTIONS | `01005A20190A6000` | `7CE9429D1FCBBD80` (❌, v3, 1.1.1) | 🔴 |  |
| NASCAR Heat | `0100DC7013938000` | `E0E11E95C0DE34D3` (◯, v5, 1.0.5) | 🟢 |  |
| NASCAR Rivals | `0100545016D5E000` | `71A1520B89DEC904` (◯, v5, 1.0.5) | 🟢 |  |
| NBA 2K23 | `0100ACA017E4E000` | `337DBCF525B7AC4E` (◯, v9, 1.0.9) | 🟢 |  |
| NBA 2K24 | `010006501A8D8000` | `3C37AD3626651C40` (◯, v4, 1.04) | 🟢 |  |
| Need For Speed Hot Pursuit | `010029B0118E8000` | `799D1061182C1302` ([✅](SaltySD/plugins/FPSLocker/patches/010029B0118E8000/799D1061182C1302.yaml), v3, 1.0.3) | 🔴 |  |
| Nelke & the Legendary Alchemists | `01006ED00BC76000` | `DBD272113FD196D5` (◯, v3, 1.0.3) | 🟢 |  |
| Neptunia x SENRAN KAGURA: Ninja Wars | `01008D0016AF4000` | `FB827BF029E0778A` ([✅](SaltySD/plugins/FPSLocker/patches/01008D0016AF4000/FB827BF029E0778A.yaml), v0, 1.0.0) | 🟡 | [LINK](Methodology/Neptunia%20x%20SENRAN%20KAGURA%20Ninja%20Wars) |
| Never Alone (Kisima Ingitchuna) | `0100A6B01712C000` | `B489970C5C8E79A7` (❌, v2, 1.0.2) | 🔵 |  |
| New Super Lucky's Tale | `010017700B6C2000` | `14872049185C584C` (◯, v3, 1.5.9) | 🟢 |  |
| New Tales from the Borderlands | `01002B7013440000` | `A19E113723E5C32E` ([✅](SaltySD/plugins/FPSLocker/patches/01002B7013440000/A19E113723E5C32E.yaml), v2, 1.0.2) | 🔴 | [LINK](Methodology/New%20Tales%20from%20the%20Borderlands) |
| Nickelodeon All-Star Brawl 2 | `010010701AFB2000` | `71DC7C0892FED6FE` (◯, v7, 1.7.0) | 🟢 |  |
| Ni no Kuni: Wrath of the White Witch | `0100E5600D446000` | `C32B29CB5FBA96D9` (✝️, v2, 1.0.2) | 🟣 | [LINK](Methodology/Ni%20no%20Kuni%20Wrath%20of%20the%20White%20Witch) |
| NieR:Automata | `0100B8E016F76000` <br> `010056B015FE8000` | `992787E2B5425994` (❌, v1, 1.0.2) <br> `E43525F22282A477` (❌, v1, 1.0.2) | 🔵 |  |
| Nights Of Azure 2: Bride of the New Moon | `0100628004BCE000` | `81DA4F9E1E961CA6` ([✅](SaltySD/plugins/FPSLocker/patches/0100628004BCE000/81DA4F9E1E961CA6.yaml), v1, 1.0.1) | 🔵 |  |
| Nine Parchments | `0100D03003F0E000` | `F7893E37FC10C803` (◯, v4, 1.1.1) | 🟢 |  |
| No Man's Sky | `0100853015E86000` | `35CB055482863ED9` (◯, v18, 4.2.2) <br> `DA7D68D91AB5FA3C` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/DA7D68D91AB5FA3C.yaml), v26, 4.4.5) <br> `A0C0DD9E26541179` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/A0C0DD9E26541179.yaml), v29, 4.4.7) <br> `BCC5B216CC47134F` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/BCC5B216CC47134F.yaml), v30, 4.5.0) <br> `591B871234DE6100` ([✅](SaltySD/plugins/FPSLocker/patches/0100853015E86000/591B871234DE6100.yaml), v32, 4.5.2) | 🔵 | [LINK](Methodology/No%20Man's%20Sky/README.md) |
| Oceanhorn 2: Knights of the Lost Realm | `01006CB010840000` | `9F2F187D1C6E44EC` ([✅](SaltySD/plugins/FPSLocker/patches/01006CB010840000/9F2F187D1C6E44EC.yaml), v2, 1.2) | 🔵 | [LINK](Methodology/Oceanhorn%202) |
| OCTOPATH TRAVELER | `010057D006492000` | `B88A8D8E5516DDE9` ([✅](SaltySD/plugins/FPSLocker/patches/010057D006492000/B88A8D8E5516DDE9.yaml), v4, 1.0.4) | 🔴 | [LINK](Methodology/OCTOPATH%20TRAVELER) |
| OCTOPATH TRAVELER II | `0100A3501946E000` | `BB891294DA55675E` ([✅](SaltySD/plugins/FPSLocker/patches/0100A3501946E000/BB891294DA55675E.yaml), v1, 1.0.2) | 🔴 | [LINK](Methodology/OCTOPATH%20TRAVELER%20II) |
| Oddworld: Soulstorm | `0100D210177C6000` | `9510D677DCCE4447` ([✅](SaltySD/plugins/FPSLocker/patches/0100D210177C6000/9510D677DCCE4447.yaml), v3, 1.1.3) | 🔵 |  |
| Off the Road Unleashed | `010045C0112F8000` | `5E8316D212D6D7BD` (◯, v1, 1.0.1) | 🟢 |  |
| Oninaki | `01001AF00CE54000` | `C949E2576F532C43` (◯, v2, 1.0.2) | 🟢 |  |
| Othercide | `0100E5900F49A000` | `A8BA2A8F93AAE647` ([✅](SaltySD/plugins/FPSLocker/patches/0100E5900F49A000/A8BA2A8F93AAE647.yaml), v3, 1.3.0.5) | 🔵 |  |
| Outer Wilds | `01003DC0144B6000` | `6D84C98833E0A849` (❌, v2, 1.1.14.856) | 🟡 | [LINK](Methodology/Outer%20Wilds) |
| Outlast | `01008D4007A1E000` | `C3D46BB3C7059DB1` ([✅](SaltySD/plugins/FPSLocker/patches/01008D4007A1E000/C3D46BB3C7059DB1.yaml), v1, 1.0.1) | 🔵 |  |
| Outlast 2 | `0100DE70085E8000` | `F18ACDA7A71CB287` ([✅](SaltySD/plugins/FPSLocker/patches/0100DE70085E8000/F18ACDA7A11CB287.yaml), v0, 1.0.0) | 🔵 |  |
| Overcooked! Special Edition | `01009B900401E000` | `41D554623A3F4341` (◯, v4, 1.1.1) | 🟢 |  |
| Overcooked 2 | `01006FD0080B2000` | `C305E9A71984424E` (◯, v16, 1.0.16) | 🟢 |  |
| Oxenfree II: Lost Signals | `010061F0176F6000` | `F722A80C29EF4275` (◯, v4, 1.4.8) | 🟢 |  |
| PAC-MAN WORLD Re-PAC | `0100D4401565E000` | `0058D033DAA48B17` (◯, v2, 1.0.2) | 🟢 |  |
| Paper Mario: The Origami King | `0100A3900C3E2000` | `E74395F066FD8CCB` (❌, v1, 1.0.1) | 🔴 |  |
| Paradise Killer | `01007FB010DC8000` | `D3744AF2C376CDC4` ([✅](SaltySD/plugins/FPSLocker/patches/01007FB010DC8000/D3744AF2C376CDC4.yaml), v7, 1.2.1) | 🔵 | [LINK](Methodology/Paradise%20Killer) |
| Paradise Lost | `010077A012A5C000` | `F5ECE696120B65B3` ([✅](SaltySD/plugins/FPSLocker/patches/010077A012A5C000/F5ECE696120B65B3.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Paradise%20Lost) |
| Pascal's Wager | `01009B9017D8E000` | `3F9A7276F039B226` (◯, v2, 2.0.0) | 🟢 |  | 
| Passpartout 2: The Lost Artist | `010094E01AA20000` | `43A930F90A36D248` (◯, v2, 1.1.0) | 🟢 |  | 
| PAW Patrol World | `0100273018D70000` | `54C42C73890100F1` (❌, v2, 1.0.2) | 🔴 |  |
| Peppa Pig: World Adventures | `0100FF1018E00000` | `696DE87363CDAED0` (◯, v1, 1.0.1) | 🟢 |  |
| Persona 5 Royal | `01005CA01580E000` | `D4B150B29A931CD3` (◯, v1, 1.0.2) | 🟢 |  |
| Persona 5 Scramble | `01001C400E9D8000` <br> `01009FE010876000` | `737E56D43D2C0B38` ([✅](SaltySD/plugins/FPSLocker/patches/01001C400E9D8000/737E56D43D2C0B38.yaml), v3, 1.0.3) <br> `407978D722447B25` ([✅](SaltySD/plugins/FPSLocker/patches/01009FE010876000/407978D722447B25.yaml), v1, 1.0.1) | 🔴 |  |
| Persona 5 Strikers | `0100801011C3E000` | `C4DF04F647BDC727` ([✅](SaltySD/plugins/FPSLocker/patches/0100801011C3E000/C4DF04F647BDC727.yaml), v0, 1.0.0) | 🔴 |  |
| Persona 5 Tactica | `010087701B092000` | `B6333790BE11542C` (◯, v4, 1.1.0) | 🟢 |  |
| Plants vs. Zombies: Battle for Neighborville | `0100C56010FD8000` | `82051A9C802D0A4C` (❌, v3, 1.0.3) | 🔵 | 
| Pokemon: Let's Go, Eevee! | `0100187003A36000` | `5831EC64D6B696FD` (❌, v2, 1.0.2) | 🟡 | [LINK](Methodology/Pokemon%20Let's%20Go%20Eevee) |
| Pokemon: Let's Go, Pikachu! | `010003F003A34000` | `C208DB6A4EF4361F` (❌, v2, 1.0.2) | 🟡 | [LINK](Methodology/Pokemon%20Let's%20Go%20Pikachu) |
| Pokemon Brilliant Diamond | `0100000011D90000` | `94CEAE325C205C4B` (◯, v6, 1.3.0) | 🟢 |  |
| Pokemon Legends: Arceus | `01001F5010DFA000` | `AEE8F150DDA1B5A8` (❌, v4, 1.1.1) | 🟡 | [LINK](Methodology/Pokemon%20Legends%20Arceus) |
| Pokemon Mystery Dungeon: Rescue Team DX | `01003D200BAA2000` | `3AB632DEE82D5944` (❌, v2, 1.0.2) | 🔵 | [LINK](Methodology/Pokemon%20Mystery%20Dungeon) |
| Pokemon Scarlet | `0100A3D008C5C000` | `421C5411B487EB4D` (❌, v11, 3.0.1) | 🟡 | [LINK](Methodology/Pokemon%20Scarlet) |
| Pokemon Shield | `01008DB008C2C000` | `A16802625E7826BF` (❌, v7, 1.3.2) | 🟡 | [LINK](Methodology/Pokemon%20Shield) |
| Pokemon Shining Pearl | `010018E011D92000` | `38F59CBDA2EB9C44` (◯, v6, 1.3.0) | 🟢 |  |
| Pokemon Sword | `0100ABF008968000` | `A3B75BCD3311385A` (❌, v7, 1.3.3) | 🟡 | [LINK](Methodology/Pokemon%20Sword) |
| Pokemon Violet | `01008F6008C5E000` | `709BFD6611529864` (❌, v11, 3.0.1) | 🟡 | [LINK](Methodology/Pokemon%20Violet) |
| Portal Knights | `0100437004170000` | `D59D81C06F923846` (❌, v8, 1.7.2) | 🔵 |  |
| Potion Permit | `010025F0126FE000` | `C7249836825D1750` (◯, v11, 1.0.11) | 🟢 |  |
| PowerWash Simulator | `0100926016012000` | `E44D9EFDB2F1D0A6` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/E44D9EFDB2F1D0A6.yaml), v5, 1.2.1) <br> `FCFC7462E8DC0E6D` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/FCFC7462E8DC0E6D.yaml), v10, 1.5.2) <br> `E71C3103420D9574` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/E71C3103420D9574.yaml), v11, 1.6.0) <br> `8EACFE3E9E92B0FE` ([✅](SaltySD/plugins/FPSLocker/patches/0100926016012000/8EACFE3E9E92B0FE.yaml), v12, 1.7.0) | 🔴 |  |
| Princess Peach Showtime! | `01007A3009184000` | `928EFE2954F68055` ([✅](SaltySD/plugins/FPSLocker/patches/01007A3009184000/928EFE2954F68055.yaml), v0, 1.0.0) | 🔵 |  |
| Prison Simulator | `010094C017B06000` | `56C709E1A63CF9EA` (◯, v0, 1.0.0) | 🟢 |  |
| Project Warlock | `0100BDB01150E000` | `D597DE8544D8ED4F` (◯, v3, 1.0.3) | 🟢 |  |
| Raccoo Venture | `0100C1E01CDEE000` | `7CDFB80365E4D30C` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1E01CDEE000/7CDFB80365E4D30C.yaml), v1, 1.0.1) <br> `5F0C6E385D6E3F8D` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1E01CDEE000/5F0C6E385D6E3F8D.yaml), v2, 1.0.2) <br> `27BB06DD145F39F5` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1E01CDEE000/27BB06DD145F39F5.yaml), v3, 1.0.3) | 🔴 |  |
| Rad Rogers: Radical Edition | `010000600CD54000` | `78885A1CA987C04C` ([✅](SaltySD/plugins/FPSLocker/patches/010000600CD54000/78885A1CA987C04C.yaml), v2, 1.2.0) | 🔴 | [LINK](Methodology/Rad%20Rogers) |
| Rain World | `010047600BF72000` | `BEC01A3CE1E33E93` (◯, v8, 1.9.13) | 🟢 |  |
| RAINBOW HIGH: RUNWAY RUSH | `010039E0182D8000` | `8ECB01C6E7E4F50C` (◯, v0, 1.0.0) | 🟢 |  |
| Raji: An Ancient Epic | `010010B00DDA2000` | `8A39E660F956BB00` ([✅](SaltySD/plugins/FPSLocker/patches/010010B00DDA2000/8A39E660F956BB00.yaml), v4, 1.0.4) | 🔵 | [LINK](Methodology/Raji%20An%20Ancient%20Epic) |
| realMyst: Masterpiece Edition | `0100E64010BAA000` | `31E49EEA600A6248` (◯, v3, 1.0.3) | 🟢 |  |
| Red Dead Redemption | `01007820196A6000` | `37531419DA7654EC` (◯, v4, 1.0.4) | 🟢 |  |
| Redemption Reapers | `010073F0197DA000` | `75960383063ABB4E` ([✅](SaltySD/plugins/FPSLocker/patches/010073F0197DA000/75960383063ABB4E.yaml), v6, 1.3.0) <br> `955DF07AA5F4497B` ([✅](SaltySD/plugins/FPSLocker/patches/010073F0197DA000/955DF07AA5F4497B.yaml), v7, 1.4.0) | 🔴 |  |
| Redout | `0100DA20021D0000` | `1C81D0BC78A01EE2` (◯, v2, 1.0.2) | 🟢 |  |
| Redout 2 | `0100664016D5C000` | `D45B9332B5742A70` ([✅](SaltySD/plugins/FPSLocker/patches/0100664016D5C000/D45B9332B5742A70.yaml), v6, 1.0.6) | 🔴 | [LINK](Methodology/Redout%202) |
| Remnant: From the Ashes | `010010F01418E000` | `49CF6B0B0A62F9E2` ([✅](SaltySD/plugins/FPSLocker/patches/010010F01418E000/49CF6B0B0A62F9E2.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Remnant%20From%20the%20Ashes) |
| RiME | `0100A62002042000` | `B426F56F027E8231` (◯, v2, 1.0.2) | 🟢 |  |
| Road 96 | `010031B0145B4000` | `EAF3511193618B2A` (◯, v5, 1.05) | 🟢 |  |
| Road 96: Mile 0 | `01008600180CE000` | `DF1EBBA8DE722A3B` (◯, v0, 1.00) | 🟢 |  |
| ROMANCE OF THE THREE KINGDOMS XIV | `0100ED7012DB2000` | `1A971CC40B6D5B3F` ([✅](SaltySD/plugins/FPSLocker/patches/0100ED7012DB2000/1A971CC40B6D5B3F.yaml), v10, 1.0.10) | 🔴 |  |
| Ruined King: A League of Legends Story | `0100947013122000` | `9FC46F388F6C684C` ([✅](SaltySD/plugins/FPSLocker/patches/0100947013122000/9FC46F388F6C684C.yaml), v7, 1.7) | 🔵 |  |
| Ruiner | `01006EC00F2CC000` | `F199FFD7D83F399E` ([✅](SaltySD/plugins/FPSLocker/patches/01006EC00F2CC000/F199FFD7D83F399E.yaml), v3, 1.3) | 🔵 | [LINK](Methodology/Ruiner) |
| Rune Factory 5 | `0100CDC013238000` | `D626F7A72AF54744` ([✅](SaltySD/plugins/FPSLocker/patches/0100CDC013238000/D626F7A72AF54744.yaml), v2, 1.0.2) | 🔵 |  |
| Sakuna: Of Rice and Ruin | `0100B1400E8FE000` | `A4F17AB0C365545B` (◯, v9, 1.0.9) | 🟢 |  |
| Samurai Bringer | `01007E30176E6000` | `20F6DC74F8FB9601` (◯, v4, 1.05.0) | 🟢 |  |
| Samurai Jack: Battle Through Time | `01006C600E46E000` | `6D5DB3434CCF63F2` ([✅](SaltySD/plugins/FPSLocker/patches/01006C600E46E000/6D5DB3434CCF63F2.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Samurai%20Jack%20Battle%20Through%20Time) |
| SAMURAI WARRIORS 5 | `0100B28014132000` | `810CBA3D7DB83EC0` ([✅](SaltySD/plugins/FPSLocker/patches/0100B28014132000/810CBA3D7DB83EC0.yaml), v3, 1.0.3) | 🔴 |  |
| SD GUNDAM BATTLE ALLIANCE | `01002BE016054000` | `751420FADE402804` ([✅](SaltySD/plugins/FPSLocker/patches/01002BE016054000/751420FADE402804.yaml), v7, 1.4.0) | 🔵 |  |
| SD シン・仮面ライダー 乱舞 | `0100CD40192AC000` | `651CF2EC3862B82B` (◯, v2, 1.0.2) | 🟢 |  |
| SENRAN KAGURA Peach Ball | `01004DC00D936000` | `31CDAD67EA25CC16` ([✅](SaltySD/plugins/FPSLocker/patches/01004DC00D936000/31CDAD67EA25CC16.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/SENRAN%20KAGURA%20Peach%20Ball) |
| Severed Steel | `0100E1C0148F8000` | `77C053D779EE97F6` ([✅](SaltySD/plugins/FPSLocker/patches/0100E1C0148F8000/77C053D779EE97F6.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/Severed%20Steel) |
| Session: Skate Sim | `010023001969A000` | `BF4126341134BFC7` ([✅](SaltySD/plugins/FPSLocker/patches/010023001969A000/BF4126341134BFC7.yaml), v3, 1.1.2) | 🔵 |  |
| Shadowverse: Champion's Battle | `01003B90136DA000` | `1F936E043FB8C349` (◯, v0, 1.3.0) | 🟢 |  |
| Shattered: Tale of the Forgotten King | `0100A0F0180D6000` | `4D42A2CA8232E8EB` (◯, v0, 1.0.0) | 🟢 |  |
| Sherlock Holmes The Awakened | `0100CA800F9B2000` | `32BF1643370F70AA` ([✅](SaltySD/plugins/FPSLocker/patches/0100CA800F9B2000/32BF1643370F70AA.yaml), v0, 1.0.0) <br> `A1E1EFBA68B846A9` ([✅](SaltySD/plugins/FPSLocker/patches/0100CA800F9B2000/A1E1EFBA68B846A9.yaml), v1, 1.0.1) | 🔴 | [LINK](Methodology/Sherlock%20Holmes%20The%20Awakened) |
| Sherlock Holmes: Crimes and Punishments | `0100651014DBA000` | `789C2939A757C0CD` (❌, v0, 1.0.0) | 🔴 |  |
| Sherlock Holmes: The Devil's Daughter | `010020F014DBE000` | `2B37ED2A971948F3` (❌, v0, 1.0.0) | 🔴 |  |
| Sherlock Holmes and The<br>Hound of The Baskervilles | `010003D018708000` | `4A06EBBB5A2E4FE4` (✝️, v2, 1.0.2) | 🟣 |  |
| Shin Megami Tensei III Nocturne | `01003B0012DC2000` | `F8098979DBC7F34E` (❌, v3, 1.0.3) | 🟡 | [LINK](Methodology/Shin%20Megami%20Tensei%20III) |
| SHIN MEGAMI TENSEI V | `0100B870126CE000` | `019FBFE7738EA314` ([✅](SaltySD/plugins/FPSLocker/patches/0100B870126CE000/019FBFE7738EA314.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/SHIN%20MEGAMI%20TENSEI%20V) |
| Ship Graveyard Simulator | `010018C01B106000` | `63B72CD5F2A90020` ([✅](SaltySD/plugins/FPSLocker/patches/010018C01B106000/63B72CD5F2A90020.yaml), v0, 1.0.0) | 🔴 |  |
| Ship of Fools | `010076901806C000` | `2C4700E500079C74` (◯, v5, 1.0.5) | 🟢 |  |
| Sifu | `01007B5017A12000` | `C56FA2C9627A26CF` ([✅](SaltySD/plugins/FPSLocker/patches/01007B5017A12000/C56FA2C9627A26CF.yaml), v3, 1.13_842) <br> `CE14D183190A44D2` ([✅](SaltySD/plugins/FPSLocker/patches/01007B5017A12000/CE14D183190A44D2.yaml), v5, 1.22_1197) <br> `4A5D86DA05A4E7BB` ([✅](SaltySD/plugins/FPSLocker/patches/01007B5017A12000/4A5D86DA05A4E7BB.yaml), v6, 0.1) | 🔵 | [LINK](Methodology/Sifu) |
| SIGNALIS | `0100307018934000` | `3A533EC563D74BE2` (◯, v3, 1.3) | 🟢 |  |
| SINNER: Sacrifice for Redemption | `0100B16009C10000` | `490D681909609015` ([✅](SaltySD/plugins/FPSLocker/patches/0100B16009C10000/490D681909609015.yaml), v3, 1.1.0319) | 🔴 | [LINK](Methodology/SINNER%20Sacrifice%20for%20Redemption) |
| Smurfs Kart | `01009790186FE000` | `7B09D23CFABD67E8` (◯, v3, 1.03.1) | 🟢 |  |
| Snake Pass | `0100C0F0020E8000` | `D0798521F563E6A7` ([✅](SaltySD/plugins/FPSLocker/patches/0100C0F0020E8000/D0798521F563E6A7.yaml), v5, 1.4) | 🔴 | [LINK](Methodology/Snake%20Pass) |
| Solar Ash | `010083501AB36000` | `0959D87753F9FED4` ([✅](SaltySD/plugins/FPSLocker/patches/010083501AB36000/0959D87753F9FED4.yaml), v1, 1.06.0) | 🔵 |  | 
| Sniper Elite 3 | `010075A00BA14000` | `6888027D61CF603D` ([✅](SaltySD/plugins/FPSLocker/patches/010075A00BA14000/6888027D61CF603D.yaml), v1, 1.0.1) | 🔵 |  | 
| Sniper Elite 4 | `010007B010FCC000` | `4EEA2970DF38ECE1` ([✅](SaltySD/plugins/FPSLocker/patches/010007B010FCC000/4EEA2970DF38ECE1.yaml), v3, 1.0.3) | 🔵 |  | 
| Sniper Elite V2 | `0100BB000A3AA000` | `B61F280560A937D2` ([✅](SaltySD/plugins/FPSLocker/patches/0100BB000A3AA000/B61F280560A937D2.yaml), v5, 1.0.5) | 🔵 | [LINK](Methodology/Sniper%20Elite%20V2) | 
| SnowRunner | `0100FBD013AB6000` | `D45BC89E992F23C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/D45BC89E992F23C5.yaml), v23, 1.0.23) <br> `2CD8707981B46DAF` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/2CD8707981B46DAF.yaml), v24, 1.0.28) <br> `2701FF0058D8C59C` ([✅](SaltySD/plugins/FPSLocker/patches/0100FBD013AB6000/2701FF0058D8C59C.yaml), v25, 1.0.29) | 🔵 |  |
| Snufkin: Melody of Moominvalley | `010085001A17C000` | `84F193B3B82589D9` (◯, v1, 0.2) | 🟢 |  |
| Song of Nunu: A League of Legends Story | `01004F401BEBE000` | `5507B771E68E9DB9` ([✅](SaltySD/plugins/FPSLocker/patches/01004F401BEBE000/5507B771E68E9DB9.yaml), v1, 1.0.1) <br> `DF2D64FB63F1BD00` ([✅](SaltySD/plugins/FPSLocker/patches/01004F401BEBE000/DF2D64FB63F1BD00.yaml), v2, 1.0.2) | 🔵 |
| Sonic Colours: Ultimate | `010040E0116B8000` | `957E1E19958193F9` (◯, v7, 1.0.9) | 🟢 |  |
| SONIC FORCES | `01001270012B6000` | `6D9EA94F8AAC00A8` ([✅](SaltySD/plugins/FPSLocker/patches/01001270012B6000/6D9EA94F8AAC00A8.yaml), v1, 1.1.0) | 🔴 |  |
| SONIC FORCES DIGITAL BONUS EDITION | `0100111004460000` | `6D9EA94F8AAC00A8` ([✅](SaltySD/plugins/FPSLocker/patches/0100111004460000/6D9EA94F8AAC00A8.yaml), v1, 1.1.0) | 🔴 |  |
| Sonic Frontiers | `01004AD014BF0000` | `D7A05D106FF46FC0` ([✅](SaltySD/plugins/FPSLocker/patches/01004AD014BF0000/D7A05D106FF46FC0.yaml), v7, 1.4.1) | 🔴 |  |
| Soundfall | `0100B7A01386E000` | `39F1BCCB912A12DF` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7A01386E000/39F1BCCB912A12DF.yaml), v3, 1.3.17957) | 🔵 | [LINK](Methodology/Soundfall) |
| South of the Circle | `0100E97016F60000` | `4FB83BAB154A2B56` (◯, v3, 1.0.3) | 🟢 |  |
| South Park: The Fractured But Whole | `01008F2005154000` | `DF15EDAAF603E00C` (❌, v5, 1.05) | 🔵 | [LINK](Methodology/South%20Park%20The%20Fractured%20But%20Whole) |
| South Park: The Stick Of Truth | `010095300B6A4000` <br> `010043600B6A6000` | `BB789D7392B165F5` (❌, v1, 1.01) <br> `5BEA90B5335C9B60` (❌, v1, 1.01) | 🔴 | [LINK](Methodology/South%20Park%20The%20Stick%20of%20Truth) |
| Space Tail: Every Journey Leads Home | `0100C37019BC2000` | `0CD7D5F5600CB448` (◯, v1, 1.0.1) | 🟢 |  |
| Speed Crew | `0100C1201A558000` | `998838513F72152F` (◯, v6, 1.2.0) | 🟢 |  |
| Spiritfarer | `0100BD400DC52000` | `482B575F4CCE512B` (◯, v15, 1.15) | 🟢 |  |
| Split | `010071801AB2A000` | `D008ADF7F5DA3315` (◯, v1, 1.1.0) | 🟢 |  |
| SpongeBob SquarePants: The Cosmic Shake | `01009FB0172F4000` | `F712547C68C66A0A` ([✅](SaltySD/plugins/FPSLocker/patches/01009FB0172F4000/F712547C68C66A0A.yaml), v7, 1.0.7) | 🔵 |  |
| Spyro Reignited Trilogy | `010077B00E046000` | `D2775FAFCF4835CB` ([✅](SaltySD/plugins/FPSLocker/patches/010077B00E046000/D2775FAFCF4835CB.yaml), v1, 1.01) | 🔴 |  |
| STAR OCEAN THE SECOND STORY R | `010065301A2E0000` | `7266AEB08847B0FA` (◯, v2, 1.0.2) | 🟢 |  |
| Starlink: Battle for Atlas | `01002CC003FE6000` | `13C816F2A273653C` (❌, v6, 1.0.6) | 🔵 |  |
| Strike Force 3 | `010060200F080000` | `8507336565D4C86B` (❌, v1, 1.1.0) | 🔵 |  |
| Subnautica | `0100429011144000` | `B3DB5A1EDAF8454F` (◯, v5, 1.21.71113) | 🟢 |  |
| Subnautica Below Zero | `010014C011146000` | `5B050C55B8264040` (◯, v8, 1.21.49397) | 🟢 |  |
| Super Crazy Rhythm Castle | `01005B7017828000` | `90B9B162B022DCBF` (◯, v0, 1.0.0.0) | 🟢 |  |
| Super Kirby Clash | `01003FB00C5A8000` | `DCDFA5A4AD9A175D`  ([✅](SaltySD/plugins/FPSLocker/patches/01003FB00C5A8000/DCDFA5A4AD9A175D.yaml), v1, 1.0.1) | 🔴 |  |
| SWORD ART ONLINE: FATAL BULLET | `01005DF00DC26000` | `029C2837B0EEE8A9` ([✅](SaltySD/plugins/FPSLocker/patches/01005DF00DC26000/029C2837B0EEE8A9.yaml), v2, 1.2.0) | 🔴 | [LINK](Methodology/Sword%20Art%20Online%20Fatal%20Bullet) |
| SWORD ART ONLINE: Hollow Realization | `01001B600D1D6000` | `0C356A98BCF20184` (❌, v2, 1.0.2) | 🔵 | [LINK](Methodology/Sword%20Art%20Online%20Hollow%20Realization) |
| SWORD ART ONLINE Alicization Lycoris | `010034501225C000` | `B6AF2C0FA614CC87` (❌, v8, 3.0.1) | 🔵 | [LINK](Methodology/Sword%20Art%20Online%20Alicization%20Lycoris/README.md) |
| SWORD OF THE VAGRANT | `0100BD000CB2C000` | `1F1363EC8CC83C73` ([✅](SaltySD/plugins/FPSLocker/patches/0100BD000CB2C000/1F1363EC8CC83C73.yaml), v1, 1.1) | 🔵 | [LINK](Methodology/SWORD%20OF%20THE%20VAGRANT) |
| SteamWorld Build | `01004E401B3EA000` | `844D7FE6058B6DFD` (◯, v10, 1.0.10) | 🟢 |  |
| Tails of Iron | `0100EF3013F60000` | `6A28EE5E39F76B6A` (◯, v4, 5) | 🟢 |  |
| Tales from the Borderlands | `0100F0C011A68000` | `818C98B885460561` (◯, v0, 1.0.0) | 🟢 |  |
| Tales of Symphonia Remastered | `0100A410169A4000` | `42673F5DE16DC698` (❌, v4, 1.3.1) | 🟡 |  |
| Taxi Chaos | `0100B76011DAA000` | `C5D73D3EDAADACB2` ([✅](SaltySD/plugins/FPSLocker/patches/0100B76011DAA000/C5D73D3EDAADACB2.yaml), v2, 1.0.3) | 🔴 |  |
| Team Sonic Racing | `010084B00B36E000` | `7D942261130F42A7` (◯, v3, 1.0.3) | 🟢 |  |
| Terraformers | `0100C1B01872A000` | `A01180885E696F91` (◯, v0, 1.1.55) | 🟢 |  |
| The Caligula Effect: Overdose | `010069100B7F0000` | `A953B35A45BEA33D` ([✅](SaltySD/plugins/FPSLocker/patches/010069100B7F0000/A953B35A45BEA33D.yaml), v1, 1.01) | 🔵 | [LINK](Methodology/The%20Caligula%20Effect%20Overdose) |
| The Caligula Effect 2 | `0100CC3014886000` | `9265FE6C4DE9600E` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC3014886000/9265FE6C4DE9600E.yaml), v1, 1.1.0) | 🟢 |  |
| The Dark Pictures Anthology: Little Hope | `010084F017B32000` | `2BFF5F7711EE6C9F` ([✅](SaltySD/plugins/FPSLocker/patches/010084F017B32000/2BFF5F7711EE6C9F.yaml), v0, 1.0.0) | 🔴 |  | 
| The Dark Pictures Anthology: Man of Medan | `0100711017B30000` | `D7D0827ABE36A00D` ([✅](SaltySD/plugins/FPSLocker/patches/0100711017B30000/D7D0827ABE36A00D.yaml), v0, 1.0.0) <br> `2C7A626BA5F25D5F` ([✅](SaltySD/plugins/FPSLocker/patches/0100711017B30000/2C7A626BA5F25D5F.yaml), v1, 1.0.1) | 🔴 |  | 
| The Elder Scrolls V: Skyrim | `01000A10041EA000` | `771BDFB65F8D0AF7` ([✅](SaltySD/plugins/FPSLocker/patches/01000A10041EA000/771BDFB65F8D0AF7.yaml), v4, 1.1.177.3285177) <br> `4F7995092FAA5DC0` ([✅](SaltySD/plugins/FPSLocker/patches/01000A10041EA000/4F7995092FAA5DC0.yaml), v5, 1.1.392.3925134) | 🔵 | [LINK](Methodology/The%20Elder%20Scrolls%20V%20Skyrim) |
| The Entropy Centre | `0100DDD01ACAA000` | `7AF502E140C13759` (❌, v1, 1.0.1) | 🔵 |  |
| The Forest Quartet | `010010A01BBF4000` | `C66F68F53A4A7053` ([✅](SaltySD/plugins/FPSLocker/patches/010010A01BBF4000/C66F68F53A4A7053.yaml), v1, 4.0.1) <br> `47A022F858BA09B1` ([✅](SaltySD/plugins/FPSLocker/patches/010010A01BBF4000/47A022F858BA09B1.yaml), v2, 4.0.2) | 🔵 |  |
| The Great Ace Attorney Chronicles | `010036E00FB20000` <br> `0100D7F00FB1A000` | `1DA748FC9499882F` ([✅](SaltySD/plugins/FPSLocker/patches/010036E00FB20000/1DA748FC9499882F.yaml), v0, 1.0.0) <br> `D871B992E95B71C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100D7F00FB1A000/D871B992E95B71C5.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/The%20Great%20Ace%20Attorney%20Chronicles) |
| The Knight Witch | `0100E8501816E000` | `9C09F15234A270E4` (◯, v5, 1.0.5) | 🟢 |  |
| The Last Worker | `0100ADC014CDE000` | `DAAADE43EA48F66B` (◯, v2, 1.0.4) | 🟢 |  |
| The Legend of Heroes: Trails into Reverie | `01008CB0156BC000` | `A3E80F5FE073639D` ([✅](SaltySD/plugins/FPSLocker/patches/01008CB0156BC000/A3E80F5FE073639D.yaml), v2, 1.0.2) <br> `BC3750610F6BCA5C` ([✅](SaltySD/plugins/FPSLocker/patches/01008CB0156BC000/BC3750610F6BCA5C.yaml), v3, 1.0.3) | 🔴 |  |
| The Legend of Heroes: Trails of Cold Steel III | `01005420101DA000` | `134EC3D8BE75126F` ([✅](SaltySD/plugins/FPSLocker/patches/01005420101DA000/134EC3D8BE75126F.yaml), v1, 1.0.1) | 🔴 |  |
| The Legend of Heroes: Trails of Cold Steel IV | `0100D3C010DE8000` | `59159483CF88330F` ([✅](SaltySD/plugins/FPSLocker/patches/0100D3C010DE8000/59159483CF88330F.yaml), v3, 1.0.3) | 🔴 |  |
| The Legend of Legacy HD Remastered | `010099F01C258000` | `F58DA3C8169D3593` (❌, v2, 1.0.2) | 🟡 |  |
| The Legend of Zelda: Breath of the Wild | `01007EF00011E000` | `8E9978D50BDD20B4` ([✅](SaltySD/plugins/FPSLocker/patches/01007EF00011E000/8E9978D50BDD20B4.yaml), v12, 1.6.0) | 🟡 |  |
| The Legend of Zelda: Tears of the Kingdom | `0100F2C0115B6000` | `9B4E43650501A4D4` ([✅](SaltySD/plugins/FPSLocker/patches/0100F2C0115B6000/9B4E43650501A4D4.yaml), v6, 1.2.1) | 🟡 | [LINK](Methodology/The%20Legend%20of%20Zelda%20Tears%20of%20The%20Kingdom/README.md) |
| The LEGO Movie 2 - Videogame | `0100A4400BE74000` | `BAC1309DDF75B14D` (◯, v3, 1.0.3) | 🟢 |  |
| The LEGO NINJAGO Movie Video Game | `01000CE002072000` | `346959B36CD9F14D` (◯, v3, 1.0.3) | 🟢 |  |
| The Outer Worlds | `0100626011656000` | `761CD556AB357C87` ([✅](SaltySD/plugins/FPSLocker/patches/0100626011656000/761CD556AB357C87.yaml), v5, 1.0.5) | 🔵 | [LINK](Methodology/The%20Outer%20Worlds) 
| The Settlers: New Allies | `0100F3200E7CA000` | `254DF6A118587EA0` ([✅](SaltySD/plugins/FPSLocker/patches/0100F3200E7CA000/254DF6A118587EA0.yaml), v0, 1.0.0) <br> `D87461C342CA071D` ([✅](SaltySD/plugins/FPSLocker/patches/0100F3200E7CA000/D87461C342CA071D.yaml), v5, 1.0.5) <br> `E80F9872CB44DDEE` ([✅](SaltySD/plugins/FPSLocker/patches/0100F3200E7CA000/E80F9872CB44DDEE.yaml), v6, 1.0.6) | 🔴 |  |
| The Sinking City | `010028D00BA1A000` | `85E49C169A8B988A` ([✅](SaltySD/plugins/FPSLocker/patches/010028D00BA1A000/85E49C169A8B988A.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/The%20Sinking%20City) |
| The Smurfs Mission Vileaf | `010040A01407E000` | `BBBBB9891F01415E` (◯, v4, 1.0.19.1) | 🟢 |  |
| The Smurfs 2: The Prisoner of the Green Stone | `010073C01B7FE000` | `F294A4EBE966E8A9` ([✅](SaltySD/plugins/FPSLocker/patches/010073C01B7FE000/F294A4EBE966E8A9.yaml), v3, 1.03.03) | 🔵 |  |
| The Stretchers | `0100AA400A238000` | `14D7D1537BD5A986` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA400A238000/14D7D1537BD5A986.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/The%20Stretchers) |
| The Survivalists | `0100EF200DA60000` | `69A45110D07F0442` (◯, v7, 1.0.7) | 🟢 |  |
| The Witcher 3 | `010039400E8D6000` <br> `01003D100E9C6000` <br> `0100BFE00E9CA000` <br> `010076F00E9C8000` <br> `010070A00E9CE000` <br> `010085500E9D0000` <br> `010019C00E9CC000` <br> `01000BB00E9D2000` <br> `0100A0800E9C4000` <br> `0100E67012924000` | `986CE0BB97D63CE6` (✝️, v0, 3.2) <br> `4FFB62F1CD9E17F8` ([✅](SaltySD/plugins/FPSLocker/patches/010039400E8D6000/4FFB62F1CD9E17F8.yaml), v4, 3.7) <br> `D27FD8A515077F34` ([✅](SaltySD/plugins/FPSLocker/patches/010039400E8D6000/D27FD8A515077F34.yaml), v7, 4.04b) <br> `4BC4A8A814FD46A4` ([✅](SaltySD/plugins/FPSLocker/patches/01003D100E9C6000/4BC4A8A814FD46A4.yaml), v7, 4.04b) <br> `B151A224A429F9A7` ([✅](SaltySD/plugins/FPSLocker/patches/0100E67012924000/B151A224A429F9A7.yaml), v4, 4.04b) | 🔴 | [LINK](Methodology/The%20Witcher%203) |
| Thronebreaker: The Witcher Tales | `0100E910103B4000` | `1BD046113635234D` (◯, v2, 1.0.2) | 🟢 |  |
| Thirsty Suitors | `0100982019374000` | `9DD9149968A0B8D3` ([✅](SaltySD/plugins/FPSLocker/patches/0100982019374000/9DD9149968A0B8D3.yaml), v0, NS27619.127559) | 🔵 |  |
| Tiny Troopers: Global Ops | `0100347013E4C000` | `63F1A8874A936747` (◯, v2, 1.0.0.2) | 🟢 |  |
| Tinykin | `0100A73016576000` | `4E2AA28721AFF2C1` ([✅](SaltySD/plugins/FPSLocker/patches/0100A73016576000/4E2AA28721AFF2C1.yaml), v4, 1.1.1) | 🔵 |  |
| Tokyo Mirage Sessions<br>#FE Encore | `0100A9400C9C2000` | `33463E11899166BB` (✝️, v0, 1.0.0) | 🟣 | [LINK](Methodology/Tokyo%20Mirage%20Sessions%20%23FE%20Encore) |
| Tony Hawk's Pro Skater 1 + 2 | `0100CC00102B4000` | `8AFCBE6A930CD42E` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC00102B4000/8AFCBE6A930CD42E.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Tony%20Hawk's%20Pro%20Skater%201%20%2B%202) |
| Train Life: A Railway Simulator | `0100FC101513E000` | `A9CE4E0196706EC8` (❌, v1, 1.0.1) | 🔵 |  |
| TRANSFORMERS: EARTHSPARK - Expedition | `010005001A8CA000` | `F87BEAF2C5CE13E3` ([✅](SaltySD/plugins/FPSLocker/patches/010005001A8CA000/F87BEAF2C5CE13E3.yaml), v5, 1.0.5) | 🔴 |  |
| Trek to Yomi | `0100D77019324000` | `A52C9938956331C9` ([✅](SaltySD/plugins/FPSLocker/patches/0100D77019324000/A52C9938956331C9.yaml), v3, 0.4) | 🔵 | [LINK](Methodology/Trek%20to%20Yomi) |
| Triangle Strategy | `0100CC80140F8000` | `2AA7F33234696651` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/2AA7F33234696651.yaml), v1, 1.0.2) <br> `F7C20294EFF7E6FA` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/F7C20294EFF7E6FA.yaml), v2, 1.0.3) <br> `9CB4490E8A718BAE` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/9CB4490E8A718BAE.yaml), v3, 1.1.0) | 🔵 | [LINK](Methodology/Triangle%20Strategy) |
| Trine 5: A Clockwork Conspiracy | `0100E2701A888000` | `1F0710E2B6C1DEAD` ([✅](SaltySD/plugins/FPSLocker/patches/0100E2701A888000/1F0710E2B6C1DEAD.yaml), v3, 1.0.3) <br> `8322528255D2CC63` ([✅](SaltySD/plugins/FPSLocker/patches/0100E2701A888000/8322528255D2CC63.yaml), v5, 1.0.5) | 🔵 |  |
| TT Isle of Man | `010099900CAB2000` | `F2F739A2F1CAFF72` ([✅](SaltySD/plugins/FPSLocker/patches/010099900CAB2000/F2F739A2F1CAFF72.yaml), v1, 1.1.0) | 🔵 | [LINK](Methodology/TT%20Isle%20of%20Man) |
| TT Isle of Man 3 | `0100FA2019AC2000` | `1DF30F9632347530` ([✅](SaltySD/plugins/FPSLocker/patches/0100FA2019AC2000/1DF30F9632347530.yaml), v2, 1.2.0) <br> `8A952C8A9BAB1375` ([✅](SaltySD/plugins/FPSLocker/patches/0100FA2019AC2000/8A952C8A9BAB1375.yaml), v5, 1.5.0) <br> `91CE601F6A7174CF` ([✅](SaltySD/plugins/FPSLocker/patches/0100FA2019AC2000/91CE601F6A7174CF.yaml), v7, 1.7.0) | 🔵 |  |
| TY the Tasmanian Tiger 2 | `0100BC701417A000` | `1F8808E4FC7516D2` (❌, v1, 1.0.1) | 🔵 | [LINK](Methodology/TY%20the%20Tasmanian%20Tiger%202) |
| Ultra Age | `01008D4015904000` | `CA77083E259D87A2` ([✅](SaltySD/plugins/FPSLocker/patches/01008D4015904000/CA77083E259D87A2.yaml), v7, 2.0.4) | 🔵 | [LINK](Methodology/Ultra%20Age) |
| Ultra Kaiju Monster Rancher | `01008E0019388000` | `53384CC3D2B4CA9F` (❌, v0, 1.0.1) | 🟡 | [LINK](Methodology/Ultra%20Kaiju%20Monster%20Rancher) |
| Undungeon | `0100CA3018EA4000` | `6A5B168E1D2C6647` (◯, v0, 0.002) | 🟢 |  |
| V-Rally 4 | `010064400B138000` | `EB8A679B5DDD0060` ([✅](SaltySD/plugins/FPSLocker/patches/010064400B138000/EB8A679B5DDD0060.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/V-Rally%204) |
| Valkyria Chronicles 4 | `01005C600AC68000` | `3758602AA47ADD37` (❌, v0, 1.0.0) | 🟡 | [LINK](Methodology/Valkyria%20Chronicles%204) |
| Vampire: The Masquerade – Swansong | `01007EE01318E000` | `36080563369C45D8` (◯, v0, 1.0.0) | 🟢 |  |
| Vampyr | `01000BD00CE64000` | `E417100FFEEFD1DE` ([✅](SaltySD/plugins/FPSLocker/patches/01000BD00CE64000/E417100FFEEFD1DE.yaml), v2, 0.4) | 🔵 | [LINK](Methodology/Vampyr) |
| Warhammer 40,000: Boltgun | `01005FD017E60000` | `448B5EEE940FF0B0` ([✅](SaltySD/plugins/FPSLocker/patches/01005FD017E60000/448B5EEE940FF0B0.yaml), v2, 1.0.0.2) <br> `7C992B6A003C599F` ([✅](SaltySD/plugins/FPSLocker/patches/01005FD017E60000/7C992B6A003C599F.yaml), v3, 1.0.0.3) | 🔴 |  |
| Warhammer 40000: Shootas, Blood & Teef | `010088B0155E2000` | `C9300E99B4975DCF` (◯, v3, 1.0.3_Switch) | 🟢 |  |
| WARRIORS OROCHI 4 | `010016A00AEC0000` | `5C9CCD358BE85FC9` ([✅](SaltySD/plugins/FPSLocker/patches/010016A00AEC0000/5C9CCD358BE85FC9.yaml), v8, 1.0.13) | 🔴 |  |
| We Love Katamari REROLL+ Royal Reverie | `0100E71018D1A000` | `8B1BC6D7B367605F` (❌, v3, 1.0.3) | 🟡 |  |
| What Remains of Edith Finch | `010038900DFE0000` | `E9578A470B175851` ([✅](SaltySD/plugins/FPSLocker/patches/010038900DFE0000/E9578A470B175851.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/What%20Remains%20of%20Edith%20Finch) |
| White Day: A Labirynth Named School | `010076601839C000` | `36D6740B3873CE4A` (◯, v1, 1.0.2) | 🟢 |  |
| Wolfenstein: Youngblood | `01003BD00CAAE000` | `8B40EBBA7244C94A` ([✅](SaltySD/plugins/FPSLocker/patches/01003BD00CAAE000/8B40EBBA7244C94A.yaml), v5, 1.5) | 🟡 | [LINK](Methodology/Wolfenstein%20Youngblood) |
| Wolfenstein II: The New Colossus | `01009040091E0000` | `F2FE5EF877839F4F` ([✅](SaltySD/plugins/FPSLocker/patches/01009040091E0000/F2FE5EF877839F4F.yaml), v2, 1.2) | 🟡 | [LINK](Methodology/Wolfenstein%202%20The%20New%20Colossus/README.md) |
| WORLD OF FINAL FANTASY MAXIMA | `010072000BD32000` | `5767FD44C331B44B` (❌, v1, 1.0.1) | 🟡 | [LINK](Methodology/WORLD%20OF%20FINAL%20FANTASY%20MAXIMA) |
| WRC10 | `01003E3014AFE000` | `69CACEEC5F01C41B` ([✅](SaltySD/plugins/FPSLocker/patches/01003E3014AFE000/69CACEEC5F01C41B.yaml), v1, 1.1.0) | 🔵 | [LINK](Methodology/WRC10) |
| WRC Generations | `0100041018810000` | `B8BE1CFAE53CAEBE` ([✅](SaltySD/plugins/FPSLocker/patches/0100041018810000/B8BE1CFAE53CAEBE.yaml), v4, 1.2.2) | 🔵 | [LINK](Methodology/WRC%20Generations) |
| Wreckfest | `0100DC0012E48000` | `7BCD694B69C98104` (◯, v2, 1.0.2) | 🟢 |  |
| WW2: Bunker Simulator | `01009A601B032000` | `0C2E9A763F9AB7A2` (◯, v0, 01.00) | 🟢 |  |
| WWE 2K18 | `010009800203E000` | `DEEE18D307C81634` (❌, v5, 1.04) | 🔵 |  |
| Xenoblade Chronicles: Definitive Edition | `0100FF500E34A000` | `92C78BB3DCBBC3F7` ([✅](SaltySD/plugins/FPSLocker/patches/0100FF500E34A000/92C78BB3DCBBC3F7.yaml), v3, 1.1.2) | 🔴 | [LINK](Methodology/Xenoblade%20Chronicles) |
| Xenoblade Chronicles 2 | `0100E95004038000` | `F77F1559371C0EC6` (❌, v15, 2.1.0) | 🔴 |  |
| Xenoblade Chronicles 3 | `010074F013262000` | `B76CD24AF02ACEA2` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/B76CD24AF02ACEA2.yaml), v6, 1.3.0) <br> `8E18600222CE90C2` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/8E18600222CE90C2.yaml), v7, 2.0.0) <br> `B6BE4A6B83D4F237` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/B6BE4A6B83D4F237.yaml), v8, 2.1.0) <br> `0AE74B263D8AC3CF` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/0AE74B263D8AC3CF.yaml), v9, 2.1.1) <br> `82D187FE9EF9BE92` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/82D187FE9EF9BE92.yaml), v10, 2.2.0) | 🔴 | [LINK](Methodology/Xenoblade%20Chronicles%203)  |
| Yooka-Laylee | `0100F110029C8000` | `6352FCBB7C75E478` (◯, v2, 1.2.0) | 🟢 |  |
| Young Souls | `010097900F550000` | `E43952D95F17FA48` (◯, v3, 1.0.3) | 🟢 |  |
| Ys VIII: Lacrimosa of DANA | `01007F200B0C0000` | `F7C4835FD8AE9D10`  (◯, v5, 1.05) | 🟢 |  |
| Ys IX: Monstrum Nox | `0100E390124D8000` | `4D33981B6DB6125A` (◯, v3, 1.0.3) | 🟢 |  |
| Zombie Army Trilogy | `0100C7300EEE4000` | `54211726D36A8D9C` ([✅](SaltySD/plugins/FPSLocker/patches/0100C7300EEE4000/54211726D36A8D9C.yaml), v2, 1.0.2) | 🔵 |  |
| Zombie Army 4: Dead War | `01000BF0152FA000` | `12024D08CCFD25EB` ([✅](SaltySD/plugins/FPSLocker/patches/01000BF0152FA000/12024D08CCFD25EB.yaml), v2, 1.1.1) | 🔵 |  | 
| Zomborg | `01006401D48A000` | `A371513D3E16409B` (◯, v0, 1.0.0) | 🟢 |  |
| 妖怪ウォッチ | `0100C0000CEEA000` | `B6E172353E696E65` ([✅](SaltySD/plugins/FPSLocker/patches/0100C0000CEEA000/B6E172353E696E65.yaml), v3, 1.3.0) | 🔴 |  |
| 妖怪ウォッチ4++ | `010086C00AF7C000` | `C7DAB27F22ACD2ED` ([✅](SaltySD/plugins/FPSLocker/patches/010086C00AF7C000/C7DAB27F22ACD2ED.yaml), v14, 2.2.0) | 🟡 |  |
| 英雄伝説 閃の軌跡I：改 -Thors Military Academy 1204- | `0100AD0014AB4000` | `AC8C8EC9DB1A8EF4` ([✅](SaltySD/plugins/FPSLocker/patches/0100AD0014AB4000/AC8C8EC9DB1A8EF4.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/The%20Legend%20of%20Heroes%20Trails%20of%20Cold%20Steel) |
| 英雄伝説 閃の軌跡II：改 -The Erebonian Civil War- | `0100906014C3C000` | `EAB1DC1D53E319F9` ([✅](SaltySD/plugins/FPSLocker/patches/0100906014C3C000/EAB1DC1D53E319F9.yaml), v5, 1.0.5) | 🔴 | [LINK](Methodology/The%20Legend%20of%20Heroes%20Trails%20of%20Cold%20Steel%20II) |
| ドラゴンクエストX　目覚めし五つの種族　オフライン | `0100E2E0152E4000` | `13F322A6161F787C` ([✅](SaltySD/plugins/FPSLocker/patches/0100E2E0152E4000/13F322A6161F787C.yaml), v4, 2.0.1) | 🔵 |  |
| 電車でＧＯ！！ はしろう山手線 | `0100BC501355A000` | `7C9F89C3743F202F` ([✅](SaltySD/plugins/FPSLocker/patches/0100BC501355A000/7C9F89C3743F202F.yaml), v3, 1.1.2) | 🔵 |  |
| 三國志14 with 威力加強版 | `0100CD4012DCA000` | `B067B077906C6208` ([✅](SaltySD/plugins/FPSLocker/patches/0100CD4012DCA000/B067B077906C6208.yaml), v10, 1.0.10) | 🔴 |  |

---

> Patches for games with unlocked framerates

| NAME | TITLE ID | BUILD ID (PATCH AVAILABLE, VERSION ID, VERSION) | DETAILS |
| --- | --- | --- | --- |
| Mortal Shell | `0100154019A7C000` | `BE2D1A84420113EC` ([✅](SaltySD/plugins/FPSLocker/patches/0100154019A7C000/BE2D1A84420113EC.yaml), v1, 1.0.1) <br> `6D9F6C7B79F5197F` ([✅](SaltySD/plugins/FPSLocker/patches/0100154019A7C000/BE2D1A84420113EC.yaml), v2, 1.2.0) | [LINK](Methodology/Mortal%20Shell) |
| RiMS Racing | `01003CD01299E000` | `4232D493269475B2` ([✅](SaltySD/plugins/FPSLocker/patches/01003CD01299E000/4232D493269475B2.yaml), v2, 1.2.0) | [LINK](Methodology/RiMS%20Racing) |
| TT Isle of Man 2 | `010000400F582000` | `02F2E5C8CBF5A92F` ([✅](SaltySD/plugins/FPSLocker/patches/010000400F582000/02F2E5C8CBF5A92F.yaml), v1, 1.0.1) | [LINK](Methodology/TT%20Isle%20of%20Man%202) |
| WRC8 | `010087800DCEA000` | `6B0B26802F0DAAAF` ([✅](SaltySD/plugins/FPSLocker/patches/010087800DCEA000/6B0B26802F0DAAAF.yaml), v4, 1.4.0) | [LINK](Methodology/WRC8) |
| WRC9 | `01001A0011798000` | `66B2DEA98B5CDF65` ([✅](SaltySD/plugins/FPSLocker/patches/01001A0011798000/66B2DEA98B5CDF65.yaml), v2, 1.2.0) | [LINK](Methodology/WRC9) |
