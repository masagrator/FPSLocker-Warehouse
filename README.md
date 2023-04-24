# FPSLocker Warehouse

Here you will a find list with 30 FPS locked games, if they have FPSLocker patches that allow going above 30 FPS, tweak dynamic resolution frame timing for better performance, etc. At the end of README you can also find a separate list of patches for games that are targeting 30 FPS even though they ahave unlocked framerate.

Remember that NX-FPS plugin is limited by SaltyNX capabilities. 
Read SaltyNX readme to check which games are not compatible with the plugin.

---

> To download all patches click [here](https://github.com/masagrator/FPSLocker-Warehouse/archive/refs/heads/main.zip), unpack it and copy the `SaltySD` folder to root of your sdcard.

---

Column with colors stores info if the plugin is enough to go above 30 FPS or it requires additional patches.<br>
Patches status concern only FPSLocker "LOCK" patch format. There may exist cheat/IPS patch/mod that unlocks 60 FPS already.<br>
As the list is filled by community, it may not be up to date.

🟢 - Plugin alone is enough<br>
🔵 - Plugin alone allows going above 30 FPS, but it requires patch to fix non-breaking gameplay elements (f.e. dynamic resolution frame time to improve performance, adjust lipsync, remove double buffer)<br>
🟡 - Plugin alone allows going above 30 FPS, but it requires patch to fix breaking gameplay elements (f.e. game speed or physics)<br>
🔴 - Plugin alone is not enough, patches are required<br>
🟣 - Game is not compatible with the plugin

PATCH AVAILABILITY<br>
✝️ - patch is not possible to create<br>
❌ - patch not available<br>
✅ - patch available (click on it for file).<br>
➕ - Mod installation is required (or advised if it's next to ✅/◯). Read DETAILS.<br>
◯ - this version doesn't need a patch

---

DETAILS contains links to documents explaining why patch is necessary, possible issues with using FPSLocker in this game and how to update patch yourself for any version (It won't explain how to use IDA/Ghidra/Edizon-SE/GDB or how it was determined that those offsets are correct).

---

| NAME | TITLE ID | BUILD ID (PATCH AVAILABLE, VERSION ID, VERSION) |  | DETAILS |
| --- | --- | --- | --- | --- |
| A Hat in Time | `010056E00853A000` | `746F0D697EEEE2DD` ([✅](SaltySD/plugins/FPSLocker/patches/010056E00853A000/746F0D697EEEE2DD.yaml), v4, 1.0.4) | 🔴 |  |
| ABZU | `0100C1300BBC6000` | `59719CFCD1671B98` ([✅](SaltySD/plugins/FPSLocker/patches/0100C1300BBC6000/59719CFCD1671B98.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/ABZU) |
| American Fugitive | `010002B00C534000` | `375A0E11B2397340` (◯, v9, 1.1.1) | 🟢 |  |
| Ancestors Legacy | `01009EE0111CC000` | `EE20B8DD92B8F9B4` ([✅](SaltySD/plugins/FPSLocker/patches/01009EE0111CC000/EE20B8DD92B8F9B4.yaml)[➕](atmosphere/contents/01009EE0111CC000), v1, 1.1.0) | 🔴 | [LINK](Methodology/Ancestors%20Legacy) |
| Animal Crossing: New Horizons | `01006F8002326000` | `A31F81D41E1039C5` (✝️, v5, 1.1.4) | 🟡 | [LINK](Methodology/Animal%20Crossing%20New%20Horizons) |
| Alien: Isolation | `010075D00E8BA000` | `397C054A3D25D488` (✝️, v4, 1.1.4_60709) | 🟣 | [LINK](Methodology/Alien%20Isolation) |
| Bassmaster Fishing 2022 | `0100B8501771A000` | `78BF042012CF9EE8` ([✅](SaltySD/plugins/FPSLocker/patches/0100B8501771A000/78BF042012CF9EE8.yaml), v2, 1.02) | 🔵 | [LINK](Methodology/Bassmaster%20Fishing%202022%20Super%20Deluxe%20Edition) |
| BioShock Remastered | `0100AD10102B2000` | `D89FFAA2062E373D` ([✅](SaltySD/plugins/FPSLocker/patches/0100AD10102B2000/D89FFAA2062E373D.yaml), v1, 1.0.2) | 🔵 | [LINK](https://github.com/masagrator/FPSLocker-Warehouse/tree/bioshock/Methodology/BioShock%20Remastered) |
| BioShock 2 Remastered | `01002620102C6000` | `7D1714279435589C` ([✅](SaltySD/plugins/FPSLocker/patches/01002620102C6000/7D1714279435589C.yaml), v1, 1.0.2) | 🔵 | [LINK](Methodology/BioShock%202%20Remastered) |
| BioShock Infinite | `0100D560102C8000` | `48681F1D90704F6C` ([✅](SaltySD/plugins/FPSLocker/patches/48681F1D90704F6C.yaml), v1, 1.0.2) | 🔵 | [LINK](Methodology/BioShock%20Infinite) |
| Blade Assault | `0100EA1018A2E000` | `0DF84BFE1556A443` (◯, v1, 1.0.1) | 🟢 |  |
| Blair Witch | `01006CC01182C000` | `C31E59266A218855` ([✅](SaltySD/plugins/FPSLocker/patches/01006CC01182C000/C31E59266A218855.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Blair%20Witch) |
| Borderlands | `010064800F66A000` | `1C37C3673E0E4E7A` (◯, v2, 1.0.2) | 🟢 |  |
| Borderlands 2 | `010096F00FF22000` | `F7C233469F20EE3F` (◯, v2, 1.0.2) | 🟢 |  |
| Borderlands: The Pre-Sequel | `010007400FF24000` | `090B1F7F7AF35D00` (◯, v1, 1.0.1) | 🟢 |  |
| BRAVELY DEFAULT II | `01006DC010326000` | `05DE5A7F20BD1532` ([✅](SaltySD/plugins/FPSLocker/patches/01006DC010326000/05DE5A7F20BD1532.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/Bravely%20Default%202) |
| Bulletstorm | `01003DD00D658000` | `32FC35DF1C50E1F1` (◯, v0, 1.0.0) | 🟢 |  |
| Call of Juarez: Gunslinger | `0100B4700BFC6000` | `EBF7DE558D554C7E` (◯, v5, 1.0.5) | 🟢 |  |
| Candleman | `010034400CB5E000` | `55AA8D007FAEC044` (◯, v1, 1.0.1) | 🟢 |  |
| Chef Life - A Restaurant Simulator | `0100F24014280000` | `8BC03B559A77C4CE` (◯, v2, 1.2.0) | 🟢 |  |
| Crash Team Racing Nitro-Fueled | `0100F9F00C696000` | `1C68951840693051` (◯, v15, 1.0.15) | 🟢 |  |
| Dark Souls Remastered | `01004AB00A260000` | `DF3766A2BB651A3E` (✝️, v3, 1.0.3) | 🔴 | [LINK](Methodology/Dark%20Souls/README.md) |
| Darksiders II Deathinitive Edition | `010071800BA98000` | `173E2EDEA9E5D940` ([✅](SaltySD/plugins/FPSLocker/patches/010071800BA98000/173E2EDEA9E5D940.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Darksiders%202) |
| DC's Justice League: Cosmic Chaos | `0100157015DD8000` | `2BFC784E7E10DD89` (◯, v1, 1.0.1) | 🟢 |  |
| DEMON GAZE EXTRA | `0100FCC0168FC000` | `58EE9A90F6FE6D4B` (❌, v2, 1.0.2) | 🟡 |  |
| Destiny Connect: Tick-Tock Travelers | `010069500DD86000` | `5AD84EFD9D28FDDE` ([✅](SaltySD/plugins/FPSLocker/patches/010069500DD86000/5AD84EFD9D28FDDE.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Destiny%20Connect%20Tick-Tock%20Travelers) |
| DOOM | `0100416004C00000` | `01ACE43E724259C3` ([✅](SaltySD/plugins/FPSLocker/patches/0100416004C00000/01ACE43E724259C3.yaml), v3, 1.2) | 🟡 | [LINK](Methodology/DOOM) |
| DOOM Eternal | `0100B1A00D8CE000` | `5AF6F31EAC42DBC0` ([✅](SaltySD/plugins/FPSLocker/patches/0100B1A00D8CE000/5AF6F31EAC42D8C0.yaml), v13, 1.13) | 🟡 | [LINK](Methodology/DOOM%20Eternal) |
| Dragon's Dogma: Dark Arisen | `010032C00AC58000` <br> `010057E00AC56000` | `2CDB9B9D70010E88` ([✅](SaltySD/plugins/FPSLocker/patches/010032C00AC58000/2CDB9B9D70010E88.yaml), v1, 1.0.1) <br> `2D5B93C856CDF009` ([✅](SaltySD/plugins/FPSLocker/patches/010057E00AC56000/2D5B93C856CDF009.yaml), v1, 1.0.1) | 🔴 |  |
| Dredge | `01008CD0172D6000` | `68B7A194A9BF046A` (❌, v3, 1.0.3) | 🟡 |  |
| Everspace | `0100DCF0093EC000` | `71873FEB4648FA39` ([✅](SaltySD/plugins/FPSLocker/patches/0100DCF0093EC000/71873FEB4648FA39.yaml), v5, 1.0.5) | 🔴 | [LINK](Methodology/Everspace) |
| Fe | `0100D2600736A000` | `4FF8F56B697A0949` (◯, v0, 1.0.0) | 🟢 |  |
| Figment 2: Creed Valley | `010098A016888000` | `16C2DB41CB7A7A31` (❌, v1, 1.0.5) | 🔴 |  |
| Fire Emblem: Three Houses | `010055D009F78000` | `89048449BA238C8C` (❌, v5, 1.2.0) | 🔵 |  |
| Garfield Kart Furious Racing | `010061E00E8BE000` | `4A67AFB9EAC0DF44` (◯, v3, 1.0.3) | 🟢 |  |
| Gear.Club Unlimited 2 | `010072900AFF0000` | `FE757810B45C3444` (✝️, v14, 1.7.2) | 🔴 | [LINK](Methodology/Gear.Club%20Unlimited%202) |
| GOD WARS The Complete Legend | `0100F3D00B032000` | `3A0835D09F6D1544` (❌, v1, 1.1) | 🔵 | [LINK](Methodology/God%20Wars) |
| Grand Theft Auto III | `0100C3C012718000` | `2CF52C8DA4468946` ([✅](SaltySD/plugins/FPSLocker/patches/0100C3C012718000/2CF52C8DA4468946.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20III) |
| Grand Theft Auto: San Andreas | `010065A014024000` | `6FB56071CCB321B6` ([✅](SaltySD/plugins/FPSLocker/patches/010065A014024000/6FB56071CCB321B6.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20San%20Andreas) |
| Grand Theft Auto: Vice City | `0100182014022000` | `56EEFA704373BDB3` ([✅](SaltySD/plugins/FPSLocker/patches/0100182014022000/56EEFA704373BDB3.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20Vice%20City) |
| GRID Autosport | `0100DC800A602000` | `4264F9050557D760` (✝️, v8, 1.8.3_61741) | 🟣 | [LINK](Methodology/GRID%20Autosport) |
| Hokko Life | `010022A016250000` | `D9D13603133F3D89` (◯, v5, 1.0.5) | 🟢 |  |
| I Am Setsuna. | `0100849000BDA000` | `0BBA2167AED893BE` (◯, v1, 1.1.0) | 🟢 |  |
| L.A. Noire | `0100830004FB6000` | `40F973CE3B5EC8D7` ([✅](SaltySD/plugins/FPSLocker/patches/0100830004FB6000/40F973CE3B5EC8D7.yaml), v2, 1.2) | 🟡 | [LINK](Methodology/L.A.%20Noire) |
| Little Nightmares II | `010097100EDD6000` | `7F4216B6E784A4B2` ([✅](SaltySD/plugins/FPSLocker/patches/010097100EDD6000/7F4216B6E784A4B2.yaml), v4, 1.4) | 🔵 | [LINK](Methodology/Little%20Nightmares%20II/README.md) |
| LOST SPHEAR | `010077B0038B2000` | `641A9243BA35C638` (◯, v5, 1.3.1) | 🟢 |  |
| Luigi's Mansion 3 | `0100DCA0064A6000` | `79E5950FFA85ACF6` (✝️, v5, 1.4.0) | 🟣 | [LINK](Methodology/Luigi's%20Mansion%203) |
| Metro 2033 Redux | `0100D4900E82C000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4900E82C000/85C362CC9790F0ED.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Metro%20Redux%20Collection) |
| Metro: Last Light Redux | `0100F0400E850000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100F0400E850000/85C362CC9790F0ED.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Metro%20Redux%20Collection) |
| Minecraft Dungeons | `01006C100EC08000` | `13F573E3017996E4` (◯, v27, 1.17.0.0) | 🟢 |  |
| Monster Hunter Generations Ultimate | `0100770008DD8000` <br> `0100C3800049C000` | `FB08F1D20FD1204F` (✝️, v4, 1.4.0) <br> `9D4C86E6EF74504A` (✝️, v5, 1.5.0) | 🟣 | [LINK](Methodology/Monster%20Hunter%20Generations%20Ultimate)
| Monster Hunter Rise | `0100B04011742000` | `11C9CE3F0676EEFD` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/11C9CE3F0676EEFD.yaml), v29, 14.0.0) <br> `60EFBA0CB724E3FE` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/60EFBA0CB724E3FE.yaml), v30, 15.0.0) | 🔴 | [LINK](Methodology/Monster%20Hunter%20Rise) |
| Monster Jam Steel Titans | `010095C00F354000` | `8CA6136CF49F1A4F` (◯, v1, 1.0.1) | 🟢 |  |
| Monster Jam Steel Titans 2 | `010051B0131F0000` | `E0E9D0429A2458E1` ([✅](SaltySD/plugins/FPSLocker/patches/010051B0131F0000/E0E9D0429A2458E1.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/Monster%20Jam%20Steel%20Titans%202) |
| Monster Truck Championship | `0100D30010C42000` | `682F4A502035678D` ([✅](SaltySD/plugins/FPSLocker/patches/0100D30010C42000/682F4A502035678D.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/Monster%20Truck%20Championship) |
| NARUTO SHIPPUDEN:<br>Ultimate Ninja STORM 4<br>ROAD TO BORUTO | `01006CF00CF60000` | `D3016FC0C0402DFB` (✝️, v3, 1.3.0) | 🔴 | [LINK](Methodology/Naruto%20Shippuuden%20Ultimate%20Ninja%20Storm%204%20Road%20to%20Boruto) |
| Neptunia x SENRAN KAGURA: Ninja Wars | `01008D0016AF4000` | `FB827BF029E0778A` (❌, v0, 1.0.0) | 🔵 | [LINK](Methodology/Neptunia%20x%20SENRAN%20KAGURA%20Ninja%20Wars) |
| Ni no Kuni: Wrath of the White Witch | `0100E5600D446000` | `C32B29CB5FBA96D9` (✝️, v2, 1.0.2) | 🟣 | [LINK](Methodology/Ni%20no%20Kuni%20Wrath%20of%20the%20White%20Witch) |
| NieR:Automata | `0100B8E016F76000` <br> `010056B015FE8000` | `992787E2B5425994` (◯, v1, 1.0.2) <br> `E43525F22282A477` (◯, v1, 1.0.2) | 🟢 |  |
| Oninaki | `01001AF00CE54000` | `C949E2576F532C43` (◯, v2, 1.0.2) | 🟢 |  |
| Othercide | `0100E5900F49A000` | `A8BA2A8F93AAE647` (✝️, v3, 1.3.0.5) | 🔵 | [LINK](Methodology/Othercide/README.md) |
| Outlast | `01008D4007A1E000` | `C3D46BB3C7059DB1` (❌, v1, 1.0.1) | 🔵 | [LINK](Methodology/Outlast/) |
| Outlast 2 | `0100DE70085E8000` | `F18ACDA7A71CB287` (❌, v0, 1.0.0) | 🔵 | [LINK](Methodology/Outlast%202) |
| Overcooked! Special Edition | `01009B900401E000` | `41D554623A3F4341` (◯, v4, 1.1.1) | 🟢 |  |
| Paper Mario: The Origami King | `0100A3900C3E2000` | `E74395F066FD8CCB` (✝️, v1, 1.0.1) | 🔴 | [LINK](Methodology/Paper%20Mario%20The%20Origami%20King) |
| Paradise Lost | `010077A012A5C000` | `F5ECE696120B65B3` ([✅](SaltySD/plugins/FPSLocker/patches/010077A012A5C000/F5ECE696120B65B3.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Paradise%20Lost) |
| Peppa Pig: World Adventures | `0100FF1018E00000` | `696DE87363CDAED0` (◯, v1, 1.0.1) | 🟢 |  |
| Persona 5 Scramble | `01001C400E9D8000` <br> `01009FE010876000` | `737E56D43D2C0B38` ([✅](SaltySD/plugins/FPSLocker/patches/01001C400E9D8000/737E56D43D2C0B38.yaml), v3, 1.0.3) <br> `407978D722447B25` ([✅](SaltySD/plugins/FPSLocker/patches/01009FE010876000/407978D722447B25.yaml), v1, 1.0.1) | 🔴 |  |
| Persona 5 Strikers | `0100801011C3E000` | `C4DF04F647BDC727` ([✅](SaltySD/plugins/FPSLocker/patches/0100801011C3E000/C4DF04F647BDC727.yaml), v0, 1.0.0) | 🔴 |  |
| Pokemon Mystery Dungeon: Rescue Team DX | `01003D200BAA2000` | `3AB632DEE82D5944` (❌, v2, 1.0.2) | 🔵 | [LINK](Methodology/Pokemon%20Mystery%20Dungeon) |
| Rain World | `010047600BF72000` | `83E5B9B8149CD349` (◯, v3, 1.0.3) | 🟢 |  |
| Redout | `0100DA20021D0000` | `1C81D0BC78A01EE2` (◯, v2, 1.0.2) | 🟢 |  |
| Redout 2 | `0100664016D5C000` | `D45B9332B5742A70` ([✅](SaltySD/plugins/FPSLocker/patches/0100664016D5C000/D45B9332B5742A70.yaml), v6, 1.0.6) | 🔴 | [LINK](Methodology/Redout%202) |
| Remnant: From the Ashes | `010010F01418E000` | `49CF6B0B0A62F9E2` ([✅](SaltySD/plugins/FPSLocker/patches/010010F01418E000/49CF6B0B0A62F9E2.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Remnant%20From%20the%20Ashes) |
| Ruiner | `01006EC00F2CC000` | `F199FFD7D83F399E` ([✅](SaltySD/plugins/FPSLocker/patches/01006EC00F2CC000/F199FFD7D83F399E.yaml), v3, 1.3) | 🔵 | [LINK](Methodology/Ruiner) |
| SENRAN KAGURA Peach Ball | `01004DC00D936000` | `31CDAD67EA25CC16` ([✅](SaltySD/plugins/FPSLocker/patches/01004DC00D936000/31CDAD67EA25CC16.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/SENRAN%20KAGURA%20Peach%20Ball) |
| Session: Skate Sim | `010023001969A000` | `BF4126341134BFC7` (❌, v3, 1.1.2) | 🔵 |  |
| Sherlock Holmes: Crimes and Punishments | `0100651014DBA000` | `789C2939A757C0CD` (❌, v0, 1.0.0) | 🔴 |  |
| Sherlock Holmes: The Devil's Daughter | `010020F014DBE000` | `2B37ED2A971948F3` (❌, v0, 1.0.0) | 🔴 |  |
| Sherlock Holmes and The<br>Hound of The Baskervilles | `010003D018708000` | `4A06EBBB5A2E4FE4` (✝️, v1, 1.0.1) | 🟣 |  |
| SINNER: Sacrifice for Redemption | `0100B16009C10000` | `490D681909609015` ([➕](atmosphere/contents/0100B16009C10000/romfs/blackstar_switch/Content/Paks/blackstar_switch-Switch_p.pak), v3, 1.1.0319) | 🔴 | [LINK](Methodology/SINNER%20Sacrifice%20for%20Redemption) |
| Snake Pass | `0100C0F0020E8000` | `D0798521F563E6A7` ([✅](SaltySD/plugins/FPSLocker/patches/0100C0F0020E8000/D0798521F563E6A7.yaml), v5, 1.4) | 🔴 | [LINK](Methodology/Snake%20Pass) |
| Sniper Elite 3 | `010075A00BA14000` | `6888027D61CF603D` ([✅](SaltySD/plugins/FPSLocker/patches/010075A00BA14000/6888027D61CF603D.yaml), v1, 1.0.1) | 🔵 |  | 
| Sniper Elite 4 | `010007B010FCC000` | `4EEA2970DF38ECE1` ([✅](SaltySD/plugins/FPSLocker/patches/010007B010FCC000/4EEA2970DF38ECE1.yaml), v3, 1.0.3) | 🔵 |  | 
| Sniper Elite V2 | `0100BB000A3AA000` | `B61F280560A937D2` ([✅](SaltySD/plugins/FPSLocker/patches/0100BB000A3AA000/B61F280560A937D2.yaml), v5, 1.0.5) | 🔵 | [LINK](Methodology/Sniper%20Elite%20V2) | 
| SnowRunner | `0100FBD013AB6000` | `84E92A9A50DF4644` (❌, v16, 1.0.16) | 🔵 | [LINK](Methodology/SnowRunner) |
| SONIC FORCES | `0100111004460000` <br> `01001270012B6000` | `6D9EA94F8AAC00A8` (❌, v1, 1.1.0) | 🔴 | [LINK](Methodology/SONIC%20FORCES/README.md) |
| SWORD ART ONLINE: FATAL BULLET | `01005DF00DC26000` | `029C2837B0EEE8A9` ([✅](SaltySD/plugins/FPSLocker/patches/01005DF00DC26000/029C2837B0EEE8A9.yaml), v2, 1.2.0) | 🔴 | [LINK](Methodology/Sword%20Art%20Online%20Fatal%20Bullet) |
| SWORD ART ONLINE: Hollow Realization | `01001B600D1D6000` | `0C356A98BCF20184` (❌, v2, 1.0.2) | 🔵 | [LINK](Methodology/Sword%20Art%20Online%20Hollow%20Realization) |
| SWORD ART ONLINE Alicization Lycoris | `010034501225C000` | `B6AF2C0FA614CC87` (❌, v8, 3.0.1) | 🔵 | [LINK](Methodology/Sword%20Art%20Online%20Alicization%20Lycoris/README.md) |
| Team Sonic Racing | `01008400B36E0000` | `7D942261130F42A7` (◯, v3, 1.0.3) | 🟢 |  |
| The Caligula Effect: Overdose | `010069100B7F0000` | `A953B35A45BEA33D` ([✅](SaltySD/plugins/FPSLocker/patches/010069100B7F0000/A953B35A45BEA33D.yaml), v1, 1.01) | 🔵 | [LINK](Methodology/The%20Caligula%20Effect%20Overdose) |
| The Caligula Effect 2 | `0100CC3014886000` | `094BD2CDF388A1DB` (◯, v0, 1.0.0) | 🟢 |  |
| The Smurfs Mission Vileaf | `010040A01407E000` | `BBBBB9891F01415E` (◯, v4, 1.0.19.1) | 🟢 |  |
| The Stretchers | `0100AA400A238000` | `14D7D1537BD5A986` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA400A238000/14D7D1537BD5A986.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/The%20Stretchers) |
| The Witcher 3 | `010039400E8D6000` <br> `01003D100E9C6000` <br> `0100BFE00E9CA000` <br> `010076F00E9C8000` <br> `010070A00E9CE000` <br> `010085500E9D0000` <br> `010019C00E9CC000` <br> `01000BB00E9D2000` <br> `0100A0800E9C4000` <br> | `4FFB62F1CD9E17F8` ([✅](SaltySD/plugins/FPSLocker/patches/010039400E8D6000/4FFB62F1CD9E17F8.yaml), v4, 3.7) <br> `986CE0BB97D63CE6` (✝️, v0, 3.2) | 🔴 | [LINK](Methodology/The%20Witcher%203) |
| Thronebreaker: The Witcher Tales | `0100E910103B4000` | `1BD046113635234D` (◯, v2, 1.0.2) | 🟢 |  |
| Tiny Troopers: Global Ops | `0100347013E4C000` | `A3EE277B20160F49` (◯, v0, 1.0.0.0) | 🟢 |  |
| Tokyo Mirage Sessions<br>#FE Encore | `0100A9400C9C2000` | `33463E11899166BB` (✝️, v0, 1.0.0) | 🟣 | [LINK](Methodology/Tokyo%20Mirage%20Sessions%20%23FE%20Encore) |
| Tony Hawk's Pro Skater 1 + 2 | `0100CC00102B4000` | `8AFCBE6A930CD42E` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC00102B4000/8AFCBE6A930CD42E.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Tony%20Hawk's%20Pro%20Skater%201%20%2B%202) |
| Train Life: A Railway Simulator | `0100FC101513E000` | `A9CE4E0196706EC8` (❌, v1, 1.0.1) | 🔵 |  |
| Triangle Strategy | `0100CC80140F8000` | `2AA7F33234696651` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/2AA7F33234696651.yaml), v1, 1.0.2) <br> `F7C20294EFF7E6FA` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/F7C20294EFF7E6FA.yaml), v2, 1.0.3) | 🔵 | [LINK](Methodology/Triangle%20Strategy) |
| TT Isle of Man | `010099900CAB2000` | `F2F739A2F1CAFF72` ([✅](SaltySD/plugins/FPSLocker/patches/010099900CAB2000/F2F739A2F1CAFF72.yaml), v1, 1.1.0) | 🔵 | [LINK](Methodology/TT%20Isle%20of%20Man) |
| V-Rally 4 | `010064400B138000` | `EB8A679B5DDD0060` ([✅](SaltySD/plugins/FPSLocker/patches/010064400B138000/EB8A679B5DDD0060.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/V-Rally%204) |
| Vampyr | `01000BD00CE64000` | `E417100FFEEFD1DE` ([✅](SaltySD/plugins/FPSLocker/patches/01000BD00CE64000/E417100FFEEFD1DE.yaml), v2, 0.4) | 🔵 | [LINK](Methodology/Vampyr) |
| Warhammer 40000: Shootas, Blood & Teef | `010088B0155E2000` | `C9300E99B4975DCF` (◯, v3, 1.0.3_Switch) | 🟢 |  |
| What Remains of Edith Finch | `010038900DFE0000` | `E9578A470B175851` ([✅](SaltySD/plugins/FPSLocker/patches/010038900DFE0000/E9578A470B175851.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/What%20Remains%20of%20Edith%20Finch) |
| White Day: A Labirynth Named School | `010076601839C000` | `36D6740B3873CE4A` (◯, v1, 1.0.2) | 🟢 |  |
| Wolfenstein: Youngblood | `01003BD00CAAE000` | `8B40EBBA7244C94A` ([✅](SaltySD/plugins/FPSLocker/patches/01003BD00CAAE000/8B40EBBA7244C94A.yaml), v5, 1.5) | 🟡 | [LINK](Methodology/Wolfenstein%20Youngblood) |
| Wolfenstein II: The New Colossus | `01009040091E0000` | `F2FE5EF877839F4F` ([✅](SaltySD/plugins/FPSLocker/patches/01009040091E0000/F2FE5EF877839F4F.yaml), v2, 1.2) | 🟡 | [LINK](Methodology/Wolfenstein%202%20The%20New%20Colossus/README.md) |
| WRC10 | `01003E3014AFE000` | `69CACEEC5F01C41B` ([✅](SaltySD/plugins/FPSLocker/patches/01003E3014AFE000/69CACEEC5F01C41B.yaml), v1, 1.1.0) | 🔵 | [LINK](Methodology/WRC10) |
| WRC Generations | `0100041018810000` | `B8BE1CFAE53CAEBE` ([✅](SaltySD/plugins/FPSLocker/patches/0100041018810000/B8BE1CFAE53CAEBE.yaml), v4, 1.2.2) | 🔵 | [LINK](Methodology/WRC%20Generations) |
| Wreckfest | `0100DC0012E48000` | `7BCD694B69C98104` (◯, v2, 1.0.2) | 🟢 |  |
| Xenoblade Chronicles: Definitive Edition | `010074F013262000` | `92C78BB3DCBBC3F7` ([✅](SaltySD/plugins/FPSLocker/patches/0100FF500E34A000/92C78BB3DCBBC3F7.yaml), v6, 1.1.2) | 🔴 | [LINK](Methodology/Xenoblade%20Chronicles) |
| Xenoblade Chronicles 3 | `010074F013262000` | `B76CD24AF02ACEA2` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/B76CD24AF02ACEA2.yaml), v6, 1.3.0) | 🔴 | [LINK](Methodology/Xenoblade%20Chronicles%203)  |
| Yooka-Laylee | `0100F110029C8000` | `6352FCBB7C75E478` (◯, v2, 1.2.0) | 🟢 |  |
| Young Souls | `010097900F550000` | `E43952D95F17FA48` (◯, v3, 1.0.3) | 🟢 |  |
| Ys VIII: Lacrimosa of DANA | `01007F200B0C0000` | `F7C4835FD8AE9D10`  (◯, v5, 1.05) | 🟢 |  |
| Ys IX: Monstrum Nox | `0100E390124D8000` | `4D33981B6DB6125A`  (◯, v3, 1.0.3) | 🟢 |  |
| Zombie Army Trilogy | `0100C7300EEE4000` | `54211726D36A8D9C` ([✅](SaltySD/plugins/FPSLocker/patches/0100C7300EEE4000/54211726D36A8D9C.yaml), v2, 1.0.2) | 🔵 |  |
| Zombie Army 4: Dead War | `01000BF0152FA000` | `12024D08CCFD25EB` ([✅](SaltySD/plugins/FPSLocker/patches/01000BF0152FA000/12024D08CCFD25EB.yaml), v2, 1.1.1) | 🔵 |  | 
| 英雄伝説 閃の軌跡I：改 -Thors Military Academy 1204- | `0100AD0014AB4000` | `AC8C8EC9DB1A8EF4` ([✅](SaltySD/plugins/FPSLocker/patches/0100AD0014AB4000/AC8C8EC9DB1A8EF4.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/The%20Legend%20of%20Heroes%20Trails%20of%20Cold%20Steel) |
| 英雄伝説 閃の軌跡II：改 -The Erebonian Civil War- | `0100906014C3C000` | `EAB1DC1D53E319F9` ([✅](SaltySD/plugins/FPSLocker/patches/0100906014C3C000/EAB1DC1D53E319F9.yaml), v5, 1.0.5) | 🔴 | [LINK](Methodology/The%20Legend%20of%20Heroes%20Trails%20of%20Cold%20Steel%20II) |

---

> Patches for games with unlocked framerates

| NAME | TITLE ID | BUILD ID (PATCH AVAILABLE, VERSION ID, VERSION) | DETAILS |
| --- | --- | --- | --- |
| RiMS Racing | `01003CD01299E000` | `4232D493269475B2` ([✅](SaltySD/plugins/FPSLocker/patches/01003CD01299E000/4232D493269475B2.yaml), v2, 1.2.0) | [LINK](Methodology/RiMS%20Racing) |
| TT Isle of Man 2 | `010000400F582000` | `02F2E5C8CBF5A92F` ([✅](SaltySD/plugins/FPSLocker/patches/010000400F582000/02F2E5C8CBF5A92F.yaml), v1, 1.0.1) | [LINK](Methodology/TT%20Isle%20of%20Man%202) |
| WRC8 | `010087800DCEA000` | `6B0B26802F0DAAAF` ([✅](SaltySD/plugins/FPSLocker/patches/010087800DCEA000/6B0B26802F0DAAAF.yaml), v4, 1.4.0) | [LINK](Methodology/WRC8) |
| WRC9 | `01001A0011798000` | `66B2DEA98B5CDF65` ([✅](SaltySD/plugins/FPSLocker/patches/01001A0011798000/66B2DEA98B5CDF65.yaml), v2, 1.2.0) | [LINK](Methodology/WRC9) |
