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
| Advance Wars 1+2: Re-Boot Camp | `0100300012F2A000` | `320A17744AEFD67F`  ([✅](SaltySD/plugins/FPSLocker/patches/0100300012F2A000/320A17744AEFD67F.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/Advance%20Wars%201%2B2) |
| American Fugitive | `010002B00C534000` | `375A0E11B2397340` (◯, v9, 1.1.1) | 🟢 |  |
| Ancestors Legacy | `01009EE0111CC000` | `EE20B8DD92B8F9B4` ([✅](SaltySD/plugins/FPSLocker/patches/01009EE0111CC000/EE20B8DD92B8F9B4.yaml)[➕](atmosphere/contents/01009EE0111CC000), v1, 1.1.0) | 🔴 | [LINK](Methodology/Ancestors%20Legacy) |
| Animal Crossing: New Horizons | `01006F8002326000` | `A31F81D41E1039C5` (✝️, v5, 1.1.4) | 🟡 | [LINK](Methodology/Animal%20Crossing%20New%20Horizons) |
| Alien: Isolation | `010075D00E8BA000` | `397C054A3D25D488` (✝️, v4, 1.1.4_60709) | 🟣 | [LINK](Methodology/Alien%20Isolation) |
| Batman - The Telltale Series | `0100011005D92000` | `A3A998AF3252D110` (❌, v3, 1.0.4) | 🔵 | [LINK](Methodology/Batman%20-%20The%20Telltale%20Series) |
| Batman: The Enemy Within | `0100E6300AA3A000` | `AAC6FB02E03062EF` (❌, v1, 1.0.3) | 🔵 | [LINK](Methodology/Batman%20The%20Enemy%20Within) |
| Bassmaster Fishing 2022 | `0100B8501771A000` | `78BF042012CF9EE8` ([✅](SaltySD/plugins/FPSLocker/patches/0100B8501771A000/78BF042012CF9EE8.yaml), v2, 1.02) | 🔵 | [LINK](Methodology/Bassmaster%20Fishing%202022%20Super%20Deluxe%20Edition) |
| BioShock Remastered | `0100AD10102B2000` | `D89FFAA2062E373D` ([✅](SaltySD/plugins/FPSLocker/patches/0100AD10102B2000/D89FFAA2062E373D.yaml), v1, 1.0.2) | 🔵 | [LINK](Methodology/BioShock%20Remastered) |
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
| CRISIS CORE -FINAL FANTASY VII- REUNION | `01004BC0166CC000` | `44D207EA6428E3F1` ([✅](SaltySD/plugins/FPSLocker/patches/01004BC0166CC000/44D207EA6428E3F1.yaml), v4, 1.0.4) | 🔴 | [LINK](Methodology/CRISIS%20CORE) |
| Dark Souls Remastered | `01004AB00A260000` | `DF3766A2BB651A3E` (✝️, v3, 1.0.3) | 🔴 | [LINK](Methodology/Dark%20Souls/README.md) |
| Darksiders II Deathinitive Edition | `010071800BA98000` | `173E2EDEA9E5D940` ([✅](SaltySD/plugins/FPSLocker/patches/010071800BA98000/173E2EDEA9E5D940.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Darksiders%202) |
| DC's Justice League: Cosmic Chaos | `0100157015DD8000` | `2BFC784E7E10DD89` (◯, v1, 1.0.1) | 🟢 |  |
| DEMON GAZE EXTRA | `0100FCC0168FC000` | `58EE9A90F6FE6D4B` (❌, v2, 1.0.2) | 🟡 |  |
| Destiny Connect: Tick-Tock Travelers | `010069500DD86000` | `5AD84EFD9D28FDDE` ([✅](SaltySD/plugins/FPSLocker/patches/010069500DD86000/5AD84EFD9D28FDDE.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Destiny%20Connect%20Tick-Tock%20Travelers) |
| DOOM | `0100416004C00000` | `01ACE43E724259C3` ([✅](SaltySD/plugins/FPSLocker/patches/0100416004C00000/01ACE43E724259C3.yaml), v3, 1.2) | 🟡 | [LINK](Methodology/DOOM) |
| DOOM Eternal | `0100B1A00D8CE000` | `5AF6F31EAC42DBC0` ([✅](SaltySD/plugins/FPSLocker/patches/0100B1A00D8CE000/5AF6F31EAC42D8C0.yaml), v13, 1.13) | 🟡 | [LINK](Methodology/DOOM%20Eternal) |
| Dragon's Dogma: Dark Arisen | `010032C00AC58000` <br> `010057E00AC56000` | `2CDB9B9D70010E88` ([✅](SaltySD/plugins/FPSLocker/patches/010032C00AC58000/2CDB9B9D70010E88.yaml), v1, 1.0.1) <br> `2D5B93C856CDF009` ([✅](SaltySD/plugins/FPSLocker/patches/010057E00AC56000/2D5B93C856CDF009.yaml), v1, 1.0.1) | 🔴 |  |
| Dredge | `01008CD0172D6000` | `68B7A194A9BF046A` (❌, v3, 1.0.3) | 🟡 |  |
| Dusk Diver | `0100B2B00E7AA000` | `FAD1AF4EDC6DB267` (❌, v6, 1.0.6) | 🔴 |  |
| Dusk Diver 2 | `01003980174BC000` | `217C9ECF258C0312` (❌, v1, 1.0.1) | 🔴 |  |
| Easy Come Easy Golf | `0100ECF01800C000` | `FA0A3A55243FAC21` (◯, v4, 1.9.1) | 🔵 |  |
| Eiyuden Chronicle: Rising | `010039B015CB6000` | `39DC785D9073C22B` (✝️, v4, 1.9.1) | 🔵 | [LINK](Methodology/Eiyuden%20Chronicle%20Rising) |
| Embr | `0100CC6013432000` | `473D222EB1BDAD47` (◯, v6, 1.0.6) | 🟢 |  |
| Everspace | `0100DCF0093EC000` | `71873FEB4648FA39` ([✅](SaltySD/plugins/FPSLocker/patches/0100DCF0093EC000/71873FEB4648FA39.yaml), v5, 1.0.5) | 🔴 | [LINK](Methodology/Everspace) |
| FAR: Changing Tides | `01008A0014A92000` | `7041BC78D64745A1` (◯, v2, 1.2.0) | 🟢 |  |
| FAR: Lone Sails | `010022700E7D6000` | `CE59C773211A1A49` (◯, v0, 1.0.0) | 🟢 |  |
| F.I.S.T.: Forged in Shadow Torch | `01009F8017F48000` | `69EE5F71F187EAA9` ([✅](SaltySD/plugins/FPSLocker/patches/01009F8017F48000/69EE5F71F187EAA9.yaml), v4, 1.0.4) | 🔵 | [LINK](Methodology/F.I.S.T) |
| Fate/EXTELLA | `010053E002EA2000` | `76EC789B99A25BA5` (❌, v0, 1.0.0) | 🔵 |  |
| Fate/EXTELLA LINK | `01001A700C832000` | `97FC79E063E26C9B` (❌, v2, 1.0.2) | 🔵 |  |
| Fe | `0100D2600736A000` | `4FF8F56B697A0949` (◯, v0, 1.0.0) | 🟢 |  |
| Figment 2: Creed Valley | `010098A016888000` | `16C2DB41CB7A7A31` (❌, v1, 1.0.5) | 🔴 |  |
| FINAL FANTASY XII THE ZODIAC AGE | `0100EB100AB42000` | `C2932C4D1C84ED7D` (❌, v1, 1.1.0) | 🟡 |  |
| Fire Emblem Engage | `0100A6301214E000` | `8C08B9719E085F91` (❌, v3, 1.0.3) | 🟡 |  |
| Fire Emblem: Three Houses | `010055D009F78000` | `89048449BA238C8C` (❌, v5, 1.2.0) | 🔵 |  |
| FROGUN DELUXE EDITION | `0100A0A018D3A000` | `7FA5168E6BEA2A40` (◯, v3, 1.3) | 🟢 |  |
| From Space | `010015F018C3C000` | `593BD545295A65FB` ([✅](SaltySD/plugins/FPSLocker/patches/010015F018C3C000/593BD545295A65FB.yaml), v2, 1.0.357) | 🔵 |  |
| FRONT MISSION 1st: Remake | `0100F200178F4000` | `A844899CE171F1CA` (◯, v4, 2.0.0) | 🟢 |  |
| Gamedec - Definitive Edition | `01002A501869E000` | `BFA92380757EF97D` ([✅](SaltySD/plugins/FPSLocker/patches/01002A501869E000/BFA92380757EF97D.yaml), v3, 1.3.0) | 🔴 | [LINK](Methodology/Gamedec) |
| Garfield Kart Furious Racing | `010061E00E8BE000` | `4A67AFB9EAC0DF44` (◯, v3, 1.0.3) | 🟢 |  |
| Gear.Club Unlimited 2 | `010072900AFF0000` | `FE757810B45C3444` (✝️, v14, 1.7.2) | 🔴 | [LINK](Methodology/Gear.Club%20Unlimited%202) |
| GetsuFumaDen: Undying Moon | `010042A013DB8000` | `8683E654CCD68852` (❌, v2, 1.1.1) | 🔵 | [LINK](Methodology/GetsuFumaDen) |
| Ghostrunner | `010090F012916000` | `D3DD5B220DCEB626` (❌, v8, 1.8) | 🔴 |
| Gigantosaurus The Game | `01002C400E526000` | `EF7B49570430043E` ([✅](SaltySD/plugins/FPSLocker/patches/01002C400E526000/EF7B49570430043E.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/Gigantosaurus%20The%20Game) |
| Gigantosaurus: Dino Kart | `01001890167FE000` | `5F7A2866D8E20BBA` ([✅](SaltySD/plugins/FPSLocker/patches/01001890167FE000/5F7A2866D8E20BBA.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/Gigantosaurus%20Dino%20Kart) |
| GO VACATION | `0100C1800A9B6000` | `174471C5192F8647` (❌, v0, 1.0.0) | 🔵 |  |
| GOD EATER 3 | `01001C700873E000` | `C0F144F5139F542E` (❌, v11, 2.5.1) | 🔵 |  |
| GOD WARS The Complete Legend | `0100F3D00B032000` | `3A0835D09F6D1544` (❌, v1, 1.1) | 🔵 | [LINK](Methodology/God%20Wars) |
| Gods Will Fall | `0100CFA0111C8000` | `2C22089ABC14264F` (◯, v4, 1.0.4) | 🟢 |  |
| Going Under | `01004D501113C000` | `3AC30B12FEAD3149` (◯, v4, 1.0.4) | 🟢 |  |
| Golazo 2 | `0100997014004000` | `8057D5A82615847E` (◯, v2, 1.2.3) | 🟢 |  |
| Good Job! | `0100B0500FE4E000` | `951D09EECE122A47` (◯, v0, 1.0.0) | 🟢 |  |
| Grand Theft Auto III | `0100C3C012718000` | `2CF52C8DA4468946` ([✅](SaltySD/plugins/FPSLocker/patches/0100C3C012718000/2CF52C8DA4468946.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20III) |
| Grand Theft Auto: San Andreas | `010065A014024000` | `6FB56071CCB321B6` ([✅](SaltySD/plugins/FPSLocker/patches/010065A014024000/6FB56071CCB321B6.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20San%20Andreas) |
| Grand Theft Auto: Vice City | `0100182014022000` | `56EEFA704373BDB3` ([✅](SaltySD/plugins/FPSLocker/patches/0100182014022000/56EEFA704373BDB3.yaml), v7, 1.0.7) | 🔴 | [LINK](Methodology/Grand%20Theft%20Auto%20Vice%20City) |
| Graveyard Keeper | `0100B6800B5C8000` | `9356531EDD2EC448` (◯, v6, 1.0.0.4633) | 🟢 |  |
| GRID Autosport | `0100DC800A602000` | `4264F9050557D760` (✝️, v8, 1.8.3_61741) | 🟣 | [LINK](Methodology/GRID%20Autosport) |
| HARVESTELLA | `0100521017B2A000` | `249EAB9BF046C5EA` ([✅](SaltySD/plugins/FPSLocker/patches/0100521017B2A000/249EAB9BF046C5EA.yaml), v2, 1.0.2) | 🔴 | [LINK](Methodology/HARVESTELLA) |
| Hellblade: Senua's Sacrifice | `010044500CF8E000` | `9B3DDF2FB9100E51` ([✅](SaltySD/plugins/FPSLocker/patches/010044500CF8E000/9B3DDF2FB9100E51.yaml), v1, 1.1.0) | 🔴 |  |
| Hoa | `010022E013A1A000` | `1A9DF794AC0099F3` (◯, v3, 1.0.3) | 🟢 |  |
| Hokko Life | `010022A016250000` | `D9D13603133F3D89` (◯, v5, 1.0.5) | 🟢 |  |
| HOT WHEELS UNLEASHED | `0100AA60136D2000` | `F73C6504D378C38B` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA60136D2000/F73C6504D378C38B.yaml), v13, 1.0.13) | 🔵 | [LINK](Methodology/HOT%20WHEELS%20UNLEASHED) |
| House Flipper | `0100CAE00EB02000` | `3AA24709AD26C14E` (◯, v7, 1.7.0) | 🟢 |  |
| HYPERCHARGE: Unboxed | `0100A8B00F0B4000` | `92511355705EA8C5` ([✅](SaltySD/plugins/FPSLocker/patches/0100A8B00F0B4000/92511355705EA8C5.yaml), v5, 0.1.2341.233) | 🔵 | [LINK](Methodology/HYPERCHARGE%20Unboxed) |
| Hyrule Warriors: Age of Calamity | `01002B00111A2000` | `C3CF52BF2B05D731` ([✅](SaltySD/plugins/FPSLocker/patches/01002B00111A2000/C3CF52BF2B05D731.yaml), v5, 1.3.0) | 🔴 |  |
| I Am Setsuna. | `0100849000BDA000` | `0BBA2167AED893BE` (◯, v1, 1.1.0) | 🟢 |  |
| Immortal Redneck | `01000F400435A000` | `DB367E57EDA9E84F` (❌, v1, 1.3.5) | 🟢 |  |
| Immortals Fenyx Rising | `01004A600EC0A000` | `70F3F6751D73C644` (✝️, v11, 1.3.4) | 🟣 | [LINK](Methodology/Immortals%20Fenyx%20Rising/README.md) |
| In rays of the Light | `0100A760129A0000` | `AB4C861FD0C87F47` (◯, v2, 1.0.2) | 🟢 |  |
| In Sound Mind | `01006DF014682000` | `DB367E57EDA9E84F` (❌, v1, 1.0.2) | 🟢 |  |
| INMOST | `0100F1401161E000` | `16CEFEA33FE6E24F` (❌, v6, 1.0.4.3) | 🔵 |  |
| Insomnis | `01001CF0190C2000` | `4C6727375D877B90` ([✅](SaltySD/plugins/FPSLocker/patches/01001CF0190C2000/4C6727375D877B90.yaml), v1, 1.01) | 🔵 | [LINK](Methodology/Insomnis) |
| Ion Fury | `010041C00D086000` | `9D2EFCF198F2247F` (◯, v4, 1.07.1) | 🔴 | [LINK](Methodology/Ion%20Fury) |
| It Takes Two | `010092A0172E4000` | `C4067E8CB3258656` ([✅](SaltySD/plugins/FPSLocker/patches/010092A0172E4000/C4067E8CB3258656.yaml)[➕](atmosphere/contents/010092A0172E4000/romfs/Nuts/Content/Paks/Nuts-Switch_p.pak), v2, 1.0.2) | 🔵 | [LINK](Methodology/It%20Takes%20Two) |
| Kao the Kangaroo | `0100956016464000` | `F9C83728910E28A4` ([✅](SaltySD/plugins/FPSLocker/patches/0100956016464000/F9C83728910E28A4.yaml), v5, 1.5) | 🔵 | [LINK](Methodology/Kao%20The%20Kangaroo) |
| Kingdoms of Amalur: Re-Reckoning | `0100EF50132BE000` | `F69D419BCF791019` (◯, v6, 1.0.6) | 🟢 |  |
| Kitaria Fables | `0100F30013BFC000` | `220AA80516734F4C` (◯, v3, 1.0.3) | 🟢 |  |
| Kirby and the Forgotten Land | `01004D300C5AE000` | `D9BA7DB72FFAFECD`  ([✅](SaltySD/plugins/FPSLocker/patches/01004D300C5AE000/D9BA7DB72FFAFECD.yaml), v0, 1.0.0) | 🔴 |  |
| Kirby Star Allies | `01007E3006DDA000` | `D55608916FA56C18`  ([✅](SaltySD/plugins/FPSLocker/patches/01007E3006DDA000/D55608916FA56C18.yaml), v5, 4.0.0) | 🔴 |  |
| Kirby's Dream Buffet | `0100A8E016236000` | `82AF4E16BBC0BEC8` ([✅](SaltySD/plugins/FPSLocker/patches/0100A8E016236000/82AF4E16BBC0BEC8.yaml), v0, 1.0.0) | 🔴 |  |
| L.A. Noire | `0100830004FB6000` | `40F973CE3B5EC8D7` ([✅](SaltySD/plugins/FPSLocker/patches/0100830004FB6000/40F973CE3B5EC8D7.yaml), v2, 1.2) | 🟡 | [LINK](Methodology/L.A.%20Noire) |
| LEGO City Undercover | `01008550013A000` | `32C590B064956546` (◯, v3, 1.0.3) | 🟢 |  |
| LEGO DC Super-Villains | `010070D009FEC000` | `711C52FC37605D45` (◯, v8, 1.0.8) | 🟢 |  |
| LEGO Jurassic World | `01001C100E772000` | `1B80403BE8882745` (◯, v1, 1.0.1) | 🟢 |  |
| LEGO MARVEL Super Heroes | `01006F600FFC8000` | `5D769ABCAD9F2743` (◯, v1, 1.0.1) | 🟢 |  |
| LEGO MARVEL Super Heroes 2 | `01007690040A0000` | `794534B11CF3BE40` (◯, v7, 1.0.7) | 🟢 |  |
| LEGO Star Wars: The Skywalker Saga | `010042D00D900000` | `C6901CE5426C704A` ([✅](SaltySD/plugins/FPSLocker/patches/010042D00D900000/C6901CE5426C704A.yaml), v8, 1.0.8) | 🔵 | [LINK](Methodology/LEGO%20Star%20Wars%20The%20Skywalker%20Saga) |
| LEGO The Incredibles | `0100F19006E04000` | `414D247F3FD8084E` (◯, v2, 1.0.2) | 🟢 |  |
| LEGO Worlds | `0100838002AEA000` | `8174C89125B5404E` (◯, v10, 1.3.2) | 🟢 |  |
| Life is Strange | `0100DC301186A000` | `EE295EAAEA7D31E4` ([✅](SaltySD/plugins/FPSLocker/patches/0100DC301186A000/EE295EAAEA7D31E4.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Life%20is%20Strange) |
| Life is Strange 2 | `0100FD101186C000` | `BF0088C59D7E97C0`  ([✅](SaltySD/plugins/FPSLocker/patches/0100FD101186C000/BF0088C59D7E97C0.yaml), v1, 1.1.0) | 🔴 | [LINK](Methodology/Life%20is%20Strange%202) |
| Life is Strange: True Colors | `0100500012AB4000` | `118AA7B71E824B3B` ([✅](SaltySD/plugins/FPSLocker/patches/0100500012AB4000/118AA7B71E824B3B.yaml), v4, 1.0.4) | 🔴 | [LINK](Methodology/Life%20is%20Strange%20True%20Colors) |
| Little Noah: Scion of Paradise | `0100535014D76000` | `5BA1C162571DBD01` (◯, v6, 1.40) | 🟢 |  |
| Little Nightmares II | `010097100EDD6000` | `7F4216B6E784A4B2` ([✅](SaltySD/plugins/FPSLocker/patches/010097100EDD6000/7F4216B6E784A4B2.yaml), v4, 1.4) | 🔵 | [LINK](Methodology/Little%20Nightmares%20II/README.md) |
| LIVE A LIVE | `0100CF801776C000` | `CF22083371DDACB2` (◯, v1, 1.0.1) | 🟢 |  |
| Lost In Random | `01005FE01291A000` | `416914C121775277` (◯, v1, 1.0.1) | 🟢 |  |
| LOST SPHEAR | `010077B0038B2000` | `641A9243BA35C638` (◯, v5, 1.3.1) | 🟢 |  |
| Luigi's Mansion 3 | `0100DCA0064A6000` | `79E5950FFA85ACF6` (✝️, v5, 1.4.0) | 🟣 | [LINK](Methodology/Luigi's%20Mansion%203) |
| Maglam Lord | `01002C0015644000` | `3A3C781930CB8201` ([✅](SaltySD/plugins/FPSLocker/patches/01002C0015644000/3A3C781930CB8201.yaml), v0, 1.00) | 🔴 |  |
| Mario + Rabbids Kingdom Battle | `010067300059A000` | `3B39E0C06B8841F1` (◯, v9, 1.9.589692) | 🟢 |  |
| Mario + Rabbids Sparks of Hope | `0100317013770000` | `553C2A1818237255` (◯, v3, 1.3.2145477) | 🟢 |  |
| Mark of the Ninja: Remastered | `01009A700A538000` | `AE324830FE37FC72` (◯, v2, 1.0.2) | 🟢 |  |
| Marvel Ultimate Alliance 3: The Black Order | `010060700AC50000` | `E853C44FDF18B88F` ([✅](SaltySD/plugins/FPSLocker/patches/010060700AC50000/E853C44FDF18B88F.yaml), v8, 4.0.1) | 🔴 |  |
| Mary Skelter Finale | `0100530014438000` | `B1AFBB02475AD7E3` (❌, v1, 1.0.1) | 🔵 |  |
| Märchen Forest | `01001B2012D5E000` | `7A7C634CDAFE7D42` (◯, v7, 1.0.7) | 🟢 |  |
| Masters of Anima | `0100CC7009196000` | `B1C8B55EBD400E57` (◯, v1, 1.0.1) | 🟢 |  |
| Metro 2033 Redux | `0100D4900E82C000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100D4900E82C000/85C362CC9790F0ED.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Metro%20Redux%20Collection) |
| Metro: Last Light Redux | `0100F0400E850000` | `85C362CC9790F0ED` ([✅](SaltySD/plugins/FPSLocker/patches/0100F0400E850000/85C362CC9790F0ED.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Metro%20Redux%20Collection) |
| Minecraft Dungeons | `01006C100EC08000` | `13F573E3017996E4` (◯, v27, 1.17.0.0) | 🟢 |  |
| MONARK | `0100E4A01548C000` | `85EB6295023DD394` (◯, v1, 1.0.1) | 🟢 |  |
| Monster Hunter Generations Ultimate | `0100770008DD8000` <br> `0100C3800049C000` | `FB08F1D20FD1204F` (✝️, v4, 1.4.0) <br> `9D4C86E6EF74504A` (✝️, v5, 1.5.0) | 🟣 | [LINK](Methodology/Monster%20Hunter%20Generations%20Ultimate)
| Monster Hunter Rise | `0100B04011742000` | `11C9CE3F0676EEFD` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/11C9CE3F0676EEFD.yaml), v29, 14.0.0) <br> `60EFBA0CB724E3FE` ([✅](SaltySD/plugins/FPSLocker/patches/0100B04011742000/60EFBA0CB724E3FE.yaml), v30, 15.0.0) | 🔴 | [LINK](Methodology/Monster%20Hunter%20Rise) |
| Monster Jam Steel Titans | `010095C00F354000` | `8CA6136CF49F1A4F` (◯, v1, 1.0.1) | 🟢 |  |
| Monster Jam Steel Titans 2 | `010051B0131F0000` | `E0E9D0429A2458E1` ([✅](SaltySD/plugins/FPSLocker/patches/010051B0131F0000/E0E9D0429A2458E1.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/Monster%20Jam%20Steel%20Titans%202) |
| Monster Truck Championship | `0100D30010C42000` | `682F4A502035678D` ([✅](SaltySD/plugins/FPSLocker/patches/0100D30010C42000/682F4A502035678D.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/Monster%20Truck%20Championship) |
| Monster Train | `01006D9013894000` | `9DCA1A70C6414A49` (◯, v1, 2.2.0) | 🟢 |  |
| Mortal Shell | `0100154019A7C000` | `BE2D1A84420113EC` ([✅](SaltySD/plugins/FPSLocker/patches/0100154019A7C000/BE2D1A84420113EC.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Mortal%20Shell) |
| Moving Out | `0100C4C00E73E000` | `CB3172ED0C3BC646` (◯, v6, 1.0.6) | 🟢 |  |
| Mythic Ocean | `0100F4F014108000` | `2284DFB25F387719` ([✅](SaltySD/plugins/FPSLocker/patches/0100F4F014108000/2284DFB25F387719.yaml), v1, 1.0.1) | 🔴 |  |
| NARUTO SHIPPUDEN:<br>Ultimate Ninja STORM 4<br>ROAD TO BORUTO | `01006CF00CF60000` | `D3016FC0C0402DFB` (✝️, v3, 1.3.0) | 🔴 | [LINK](Methodology/Naruto%20Shippuuden%20Ultimate%20Ninja%20Storm%204%20Road%20to%20Boruto) |
| NASCAR Heat | `0100DC7013938000` | `E0E11E95C0DE34D3` (◯, v5, 1.0.5) | 🟢 |  |
| NASCAR Rivals | `0100545016D5E000` | `E730CD3E70547C71` (◯, v4, 1.0.4) | 🟢 |  |
| NBA 2K23 | `0100ACA017E4E000` | `337DBCF525B7AC4E` (◯, v9, 1.0.9) | 🟢 |  |
| Need For Speed Hot Pursuit | `010029B0118E8000` | `799D1061182C1302` ([✅](SaltySD/plugins/FPSLocker/patches/010029B0118E8000/799D1061182C1302.yaml), v3, 1.0.3) | 🔴 |  |
| Neptunia x SENRAN KAGURA: Ninja Wars | `01008D0016AF4000` | `FB827BF029E0778A` (❌, v0, 1.0.0) | 🔵 | [LINK](Methodology/Neptunia%20x%20SENRAN%20KAGURA%20Ninja%20Wars) |
| Never Alone (Kisima Ingitchuna) | `0100A6B01712C000` | `B489970C5C8E79A7` (❌, v2, 1.0.2) | 🔵 |  |
| New Super Lucky's Tale | `010017700B6C2000` | `14872049185C584C` (◯, v3, 1.5.9) | 🟢 |  |
| New Tales from the Borderlands | `01002B7013440000` | `A19E113723E5C32E` ([✅](SaltySD/plugins/FPSLocker/patches/01002B7013440000/A19E113723E5C32E.yaml), v2, 1.0.2) | 🔴 | [LINK](Methodology/New%20Tales%20from%20the%20Borderlands) |
| No Man's Sky | `0100853015E86000` | `35CB055482863ED9` (◯, v18, 4.2.2) | 🟢 |  |
| Ni no Kuni: Wrath of the White Witch | `0100E5600D446000` | `C32B29CB5FBA96D9` (✝️, v2, 1.0.2) | 🟣 | [LINK](Methodology/Ni%20no%20Kuni%20Wrath%20of%20the%20White%20Witch) |
| NieR:Automata | `0100B8E016F76000` <br> `010056B015FE8000` | `992787E2B5425994` (◯, v1, 1.0.2) <br> `E43525F22282A477` (◯, v1, 1.0.2) | 🟢 |  |
| Nine Parchments | `0100D03003F0E000` | `F7893E37FC10C803` (◯, v4, 1.1.1) | 🟢 |  |
| Oceanhorn 2: Knights of the Lost Realm | `01006CB010840000` | `9F2F187D1C6E44EC` ([✅](SaltySD/plugins/FPSLocker/patches/01006CB010840000/9F2F187D1C6E44EC.yaml), v2, 1.2) | 🔵 | [LINK](Methodology/Oceanhorn%202) |
| OCTOPATH TRAVELER | `010057D006492000` | `B88A8D8E5516DDE9` ([✅](SaltySD/plugins/FPSLocker/patches/010057D006492000/B88A8D8E5516DDE9.yaml), v4, 1.0.4) | 🔴 | [LINK](Methodology/OCTOPATH%20TRAVELER) |
| OCTOPATH TRAVELER II | `0100A3501946E000` | `BB891294DA55675E` ([✅](SaltySD/plugins/FPSLocker/patches/0100A3501946E000/BB891294DA55675E.yaml), v1, 1.0.2) | 🔴 | [LINK](Methodology/OCTOPATH%20TRAVELER%20II) |
| Oddworld: Soulstorm | `0100D210177C6000` | `9510D677DCCE4447` ([✅](SaltySD/plugins/FPSLocker/patches/0100D210177C6000/9510D677DCCE4447.yaml), v3, 1.1.3) | 🔵 |  |
| Off the Road Unleashed | `010045C0112F8000` | `5E8316D212D6D7BD` (◯, v1, 1.0.1) | 🟢 |  |
| Oninaki | `01001AF00CE54000` | `C949E2576F532C43` (◯, v2, 1.0.2) | 🟢 |  |
| Othercide | `0100E5900F49A000` | `A8BA2A8F93AAE647` (✝️, v3, 1.3.0.5) | 🔵 | [LINK](Methodology/Othercide/README.md) |
| Outlast | `01008D4007A1E000` | `C3D46BB3C7059DB1` (❌, v1, 1.0.1) | 🔵 | [LINK](Methodology/Outlast/) |
| Outlast 2 | `0100DE70085E8000` | `F18ACDA7A71CB287` (❌, v0, 1.0.0) | 🔵 | [LINK](Methodology/Outlast%202) |
| Overcooked! Special Edition | `01009B900401E000` | `41D554623A3F4341` (◯, v4, 1.1.1) | 🟢 |  |
| Overcooked 2 | `01006FD0080B2000` | `C305E9A71984424E` (◯, v16, 1.0.16) | 🟢 |  |
| PAC-MAN WORLD Re-PAC | `0100D4401565E000` | `0058D033DAA48B17` (◯, v2, 1.0.2) | 🟢 |  |
| Paper Mario: The Origami King | `0100A3900C3E2000` | `E74395F066FD8CCB` (✝️, v1, 1.0.1) | 🔴 | [LINK](Methodology/Paper%20Mario%20The%20Origami%20King) |
| Paradise Killer | `01007FB010DC8000` | `D3744AF2C376CDC4` ([](SaltySD/plugins/FPSLocker/patches/01007FB010DC8000/D3744AF2C376CDC4.yaml), v7, 1.2.1) | 🔵 | [LINK](Methodology/Paradise%20Killer) |
| Paradise Lost | `010077A012A5C000` | `F5ECE696120B65B3` ([✅](SaltySD/plugins/FPSLocker/patches/010077A012A5C000/F5ECE696120B65B3.yaml), v0, 1.0.0) | 🔵 | [LINK](Methodology/Paradise%20Lost) |
| Pascal's Wager | `01009B9017D8E000` | `195F719B92A2C447` (◯, v1, 1.0.1) | 🟢 |  |
| Peppa Pig: World Adventures | `0100FF1018E00000` | `696DE87363CDAED0` (◯, v1, 1.0.1) | 🟢 |  |
| Persona 5 Royal | `01005CA01580E000` | `D4B150B29A931CD3` (◯, v1, 1.0.2) | 🟢 |  |
| Persona 5 Scramble | `01001C400E9D8000` <br> `01009FE010876000` | `737E56D43D2C0B38` ([✅](SaltySD/plugins/FPSLocker/patches/01001C400E9D8000/737E56D43D2C0B38.yaml), v3, 1.0.3) <br> `407978D722447B25` ([✅](SaltySD/plugins/FPSLocker/patches/01009FE010876000/407978D722447B25.yaml), v1, 1.0.1) | 🔴 |  |
| Persona 5 Strikers | `0100801011C3E000` | `C4DF04F647BDC727` ([✅](SaltySD/plugins/FPSLocker/patches/0100801011C3E000/C4DF04F647BDC727.yaml), v0, 1.0.0) | 🔴 |  |
| Pokemon: Let's Go, Eevee! | `0100187003A36000` | `5831EC64D6B696FD` (✝️, v2, 1.0.2) | 🟡 | [LINK](Methodology/Pokemon%20Let's%20Go%20Eevee) |
| Pokemon: Let's Go, Pikachu! | `010003F003A34000` | `C208DB6A4EF4361F` (✝️, v2, 1.0.2) | 🟡 | [LINK](Methodology/Pokemon%20Let's%20Go%20Pikachu) |
| Pokemon Brilliant Diamond | `0100000011D90000` | `94CEAE325C205C4B` (◯, v6, 1.3.0) | 🟢 |  |
| Pokemon Legends: Arceus | `01001F5010DFA000` | `AEE8F150DDA1B5A8` (✝️, v4, 1.1.1) | 🟡 | [LINK](Methodology/Pokemon%20Legends%20Arceus) |
| Pokemon Mystery Dungeon: Rescue Team DX | `01003D200BAA2000` | `3AB632DEE82D5944` (❌, v2, 1.0.2) | 🔵 | [LINK](Methodology/Pokemon%20Mystery%20Dungeon) |
| Pokemon Scarlet | `0100A3D008C5C000` | `6EE2D5E3216EBDA5` (✝️, v4, 1.3.0) | 🟡 | [LINK](Methodology/Pokemon%20Scarlet) |
| Pokemon Shield | `01008DB008C2C000` | `A16802625E7826BF` (✝️, v7, 1.3.2) | 🟡 | [LINK](Methodology/Pokemon%20Shield) |
| Pokemon Shining Pearl | `010018E011D92000` | `38F59CBDA2EB9C44` (◯, v6, 1.3.0) | 🟢 |  |
| Pokemon Sword | `0100ABF008968000` | `A3B75BCD3311385A` (✝️, v7, 1.3.3) | 🟡 | [LINK](Methodology/Pokemon%20Sword) |
| Pokemon Violet | `01008F6008C5E000` | `AC70E41BB699CB9F` (✝️, v4, 1.3.0) | 🟡 | [LINK](Methodology/Pokemon%20Violet) |
| Portal Knights | `0100437004170000` | `D59D81C06F923846` (❌, v8, 1.7.2) | 🔵 |  |
| Potion Permit | `010025F0126FE000` | `D0D456EE7DCF0FEE` (◯, v7, 1.0.7) | 🟢 |  |
| Project Warlock | `0100BDB01150E000` | `D597DE8544D8ED4F` (◯, v3, 1.0.3) | 🟢 |  |
| Rad Rogers: Radical Edition | `010000600CD54000` | `78885A1CA987C04C` ([✅](SaltySD/plugins/FPSLocker/patches/010000600CD54000/78885A1CA987C04C.yaml), v2, 1.2.0) | 🔴 | [LINK](Methodology/Rad%20Rogers) |
| Rain World | `010047600BF72000` | `83E5B9B8149CD349` (◯, v3, 1.0.3) | 🟢 |  |
| Raji: An Ancient Epic | `010010B00DDA2000` | `8A39E660F956BB00` ([✅](SaltySD/plugins/FPSLocker/patches/010010B00DDA2000/8A39E660F956BB00.yaml), v4, 1.0.4) | 🔵 | [LINK](Methodology/Raji%20An%20Ancient%20Epic) |
| realMyst: Masterpiece Edition | `0100E64010BAA000` | `31E49EEA600A6248` (◯, v3, 1.0.3) | 🟢 |  |
| Redemption Reapers | `010073F0197DA000` | `75960383063ABB4E` ([✅](SaltySD/plugins/FPSLocker/patches/010073F0197DA000/75960383063ABB4E.yaml), v6, 1.3.0) | 🔴 |  |
| Redout | `0100DA20021D0000` | `1C81D0BC78A01EE2` (◯, v2, 1.0.2) | 🟢 |  |
| Redout 2 | `0100664016D5C000` | `D45B9332B5742A70` ([✅](SaltySD/plugins/FPSLocker/patches/0100664016D5C000/D45B9332B5742A70.yaml), v6, 1.0.6) | 🔴 | [LINK](Methodology/Redout%202) |
| Remnant: From the Ashes | `010010F01418E000` | `49CF6B0B0A62F9E2` ([✅](SaltySD/plugins/FPSLocker/patches/010010F01418E000/49CF6B0B0A62F9E2.yaml), v1, 1.0.1) | 🔵 | [LINK](Methodology/Remnant%20From%20the%20Ashes) |
| RiME | `0100A62002042000` | `B426F56F027E8231` (◯, v2, 1.0.2) | 🟢 |  |
| Road 96 | `010031B0145B4000` | `EAF3511193618B2A` (◯, v4, 1.04) | 🟢 |  |
| Road 96: Mile 0 | `01008600180CE000` | `DF1EBBA8DE722A3B` (◯, v0, 1.00) | 🟢 |  |
| Ruined King: A League of Legends Story | `0100947013122000` | `9FC46F388F6C684C` ([✅](SaltySD/plugins/FPSLocker/patches/0100947013122000/9FC46F388F6C684C.yaml), v7, 1.7) | 🔵 |  |
| Ruiner | `01006EC00F2CC000` | `F199FFD7D83F399E` ([✅](SaltySD/plugins/FPSLocker/patches/01006EC00F2CC000/F199FFD7D83F399E.yaml), v3, 1.3) | 🔵 | [LINK](Methodology/Ruiner) |
| Rune Factory 5 | `0100CDC013238000` | `D626F7A72AF54744` ([✅](SaltySD/plugins/FPSLocker/patches/0100CDC013238000/D626F7A72AF54744.yaml), v2, 1.0.2) | 🔵 |  |
| Sakuna: Of Rice and Ruin | `0100B1400E8FE000` | `A4F17AB0C365545B` (◯, v9, 1.0.9) | 🟢 |  |
| Samurai Bringer | `01007E30176E6000` | `20F6DC74F8FB9601` (◯, v4, 1.05.0) | 🟢 |  |
| Samurai Jack: Battle Through Time | `01006C600E46E000` | `6D5DB3434CCF63F2` ([✅](SaltySD/plugins/FPSLocker/patches/01006C600E46E000/6D5DB3434CCF63F2.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Samurai%20Jack%20Battle%20Through%20Time) |
| SD GUNDAM BATTLE ALLIANCE | `01002BE016054000` | `4F075A26209A5FF1` (❌, v6, 1.3.1) | 🔵 | [LINK](Methodology/SD%20GUNDAM%20BATTLE%20ALLIANCE) |
| SENRAN KAGURA Peach Ball | `01004DC00D936000` | `31CDAD67EA25CC16` ([✅](SaltySD/plugins/FPSLocker/patches/01004DC00D936000/31CDAD67EA25CC16.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/SENRAN%20KAGURA%20Peach%20Ball) |
| Severed Steel | `0100E1C0148F8000` | `77C053D779EE97F6` ([✅](SaltySD/plugins/FPSLocker/patches/0100E1C0148F8000/77C053D779EE97F6.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/Severed%20Steel) |
| Session: Skate Sim | `010023001969A000` | `BF4126341134BFC7` (❌, v3, 1.1.2) | 🔵 |  |
| Shadowverse: Champion's Battle | `01003B90136DA000` | `1F936E043FB8C349` (◯, v0, 1.3.0) | 🟢 |  |
| Shattered: Tale of the Forgotten King | `0100A0F0180D6000` | `4D42A2CA8232E8EB` (◯, v0, 1.0.0) | 🟢 |  |
| Sherlock Holmes: Crimes and Punishments | `0100651014DBA000` | `789C2939A757C0CD` (❌, v0, 1.0.0) | 🔴 |  |
| Sherlock Holmes: The Devil's Daughter | `010020F014DBE000` | `2B37ED2A971948F3` (❌, v0, 1.0.0) | 🔴 |  |
| Sherlock Holmes and The<br>Hound of The Baskervilles | `010003D018708000` | `4A06EBBB5A2E4FE4` (✝️, v1, 1.0.1) | 🟣 |  |
| Shin Megami Tensei III Nocturne | `01003B0012DC2000` | `F8098979DBC7F34E` (❌, v3, 1.0.3) | 🟡 | [LINK](Methodology/Shin%20Megami%20Tensei%20III) |
| SHIN MEGAMI TENSEI V | `0100B870126CE000` | `019FBFE7738EA314` ([✅](SaltySD/plugins/FPSLocker/patches/0100B870126CE000/019FBFE7738EA314.yaml), v2, 1.0.2) | 🔵 | [LINK](Methodology/SHIN%20MEGAMI%20TENSEI%20V) |
| Ship of Fools | `010076901806C000` | `6AC1BB9A37B0EC43` (◯, v3, 1.0.3) | 🟢 |  |
| Sifu | `01007B5017A12000` | `C56FA2C9627A26CF` ([✅](SaltySD/plugins/FPSLocker/patches/01007B5017A12000/C56FA2C9627A26CF.yaml), v3, 1.13_842) | 🔵 | [LINK](Methodology/Sifu) |
| SIGNALIS | `0100307018934000` | `3A533EC563D74BE2` (◯, v3, 1.3) | 🟢 |  |
| SINNER: Sacrifice for Redemption | `0100B16009C10000` | `490D681909609015` ([✅](SaltySD/plugins/FPSLocker/patches/0100B16009C10000/490D681909609015.yaml), v3, 1.1.0319) | 🔴 | [LINK](Methodology/SINNER%20Sacrifice%20for%20Redemption) |
| Smurfs Kart | `01009790186FE000` | `8915848314513CBD` (◯, v2, 1.02.0) | 🟢 |  |
| Snake Pass | `0100C0F0020E8000` | `D0798521F563E6A7` ([✅](SaltySD/plugins/FPSLocker/patches/0100C0F0020E8000/D0798521F563E6A7.yaml), v5, 1.4) | 🔴 | [LINK](Methodology/Snake%20Pass) |
| Sniper Elite 3 | `010075A00BA14000` | `6888027D61CF603D` ([✅](SaltySD/plugins/FPSLocker/patches/010075A00BA14000/6888027D61CF603D.yaml), v1, 1.0.1) | 🔵 |  | 
| Sniper Elite 4 | `010007B010FCC000` | `4EEA2970DF38ECE1` ([✅](SaltySD/plugins/FPSLocker/patches/010007B010FCC000/4EEA2970DF38ECE1.yaml), v3, 1.0.3) | 🔵 |  | 
| Sniper Elite V2 | `0100BB000A3AA000` | `B61F280560A937D2` ([✅](SaltySD/plugins/FPSLocker/patches/0100BB000A3AA000/B61F280560A937D2.yaml), v5, 1.0.5) | 🔵 | [LINK](Methodology/Sniper%20Elite%20V2) | 
| SnowRunner | `0100FBD013AB6000` | `84E92A9A50DF4644` (❌, v16, 1.0.16) | 🔵 | [LINK](Methodology/SnowRunner) |
| Sonic Colours: Ultimate | `010040E0116B8000` | `957E1E19958193F9` (◯, v7, 1.0.9) | 🟢 |  |
| SONIC FORCES | `0100111004460000` <br> `01001270012B6000` | `6D9EA94F8AAC00A8` (❌, v1, 1.1.0) | 🔴 | [LINK](Methodology/SONIC%20FORCES/README.md) |
| Sonic Frontiers | `01004AD014BF0000` | `AE548A35FD9DF5DA` (✝️, v4, 1.2.0) | 🔴 | [LINK](Methodology/SONIC%20FRONTIERS) |
| Soundfall | `0100B7A01386E000` | `39F1BCCB912A12DF` ([✅](SaltySD/plugins/FPSLocker/patches/0100B7A01386E000/39F1BCCB912A12DF.yaml), v3, 1.3.17957) | 🔵 | [LINK](Methodology/Soundfall) |
| South of the Circle | `0100E97016F60000` | `4FB83BAB154A2B56` (◯, v3, 1.0.3) | 🟢 |  |
| South Park: The Fractured But Whole | `01008F2005154000` | `DF15EDAAF603E00C` (❌, v5, 1.05) | 🔵 |  |
| South Park: The Stick Of Truth | `010095300B6A4000` | `BB789D7392B165F5` (❌, v1, 1.01) | 🔴 |  |
| Space Tail: Every Journey Leads Home | `0100C37019BC2000` | `0CD7D5F5600CB448` (◯, v1, 1.0.1) | 🟢 |  |
| Spiritfarer | `0100BD400DC52000` | `482B575F4CCE512B` (◯, v15, 1.15) | 🟢 |  |
| Spyro Reignited Trilogy | `010077B00E046000` | `D2775FAFCF4835CB` ([✅](SaltySD/plugins/FPSLocker/patches/010077B00E046000/D2775FAFCF4835CB.yaml), v1, 1.01) | 🔴 |  |
| Starlink: Battle for Atlas | `01002CC003FE6000` | `13C816F2A273653C` (❌, v6, 1.0.6) | 🔵 |  |
| Subnautica | `0100429011144000` | `B3DB5A1EDAF8454F` (◯, v5, 1.21.71113) | 🟢 |  |
| Subnautica Below Zero | `010014C011146000` | `5B050C55B8264040` (❌, v8, 1.21.49397) | 🟢 |  |
| Super Kirby Clash | `01003FB00C5A8000` | `DCDFA5A4AD9A175D`  ([✅](SaltySD/plugins/FPSLocker/patches/01003FB00C5A8000/DCDFA5A4AD9A175D.yaml), v1, 1.0.1) | 🔴 |  |
| SWORD ART ONLINE: FATAL BULLET | `01005DF00DC26000` | `029C2837B0EEE8A9` ([✅](SaltySD/plugins/FPSLocker/patches/01005DF00DC26000/029C2837B0EEE8A9.yaml), v2, 1.2.0) | 🔴 | [LINK](Methodology/Sword%20Art%20Online%20Fatal%20Bullet) |
| SWORD ART ONLINE: Hollow Realization | `01001B600D1D6000` | `0C356A98BCF20184` (❌, v2, 1.0.2) | 🔵 | [LINK](Methodology/Sword%20Art%20Online%20Hollow%20Realization) |
| SWORD ART ONLINE Alicization Lycoris | `010034501225C000` | `B6AF2C0FA614CC87` (❌, v8, 3.0.1) | 🔵 | [LINK](Methodology/Sword%20Art%20Online%20Alicization%20Lycoris/README.md) |
| SWORD OF THE VAGRANT | `0100BD000CB2C000` | `1F1363EC8CC83C73` ([✅](SaltySD/plugins/FPSLocker/patches/0100BD000CB2C000/1F1363EC8CC83C73.yaml), v1, 1.1) | 🔵 | [LINK](Methodology/SWORD%20OF%20THE%20VAGRANT) |
| Tails of Iron | `0100EF3013F60000` | `AD8FA9F610DB1015` (◯, v3, 4) | 🟢 |  |
| Tales from the Borderlands | `0100F0C011A68000` | `818C98B885460561` (◯, v0, 1.0.0) | 🟢 |  |
| Tales of Symphonia Remastered | `0100A410169A4000` | `BCFDC7A6A7181E9F` (❌, v1, 1.1) | 🟡 |  |
| Team Sonic Racing | `01008400B36E0000` | `7D942261130F42A7` (◯, v3, 1.0.3) | 🟢 |  |
| The Caligula Effect: Overdose | `010069100B7F0000` | `A953B35A45BEA33D` ([✅](SaltySD/plugins/FPSLocker/patches/010069100B7F0000/A953B35A45BEA33D.yaml), v1, 1.01) | 🔵 | [LINK](Methodology/The%20Caligula%20Effect%20Overdose) |
| The Caligula Effect 2 | `0100CC3014886000` | `094BD2CDF388A1DB` (◯, v0, 1.0.0) | 🟢 |  |
| The Elder Scrolls V: Skyrim | `01000A10041EA000` | `771BDFB65F8D0AF7` ([✅](SaltySD/plugins/FPSLocker/patches/01000A10041EA000/771BDFB65F8D0AF7.yaml), v4, 1.1.177.3285177) | 🔵 | [LINK](Methodology/The%20Elder%20Scrolls%20V%20Skyrim) |
| The Great Ace Attorney Chronicles | `010036E00FB20000` | `1DA748FC9499882F` ([✅](SaltySD/plugins/FPSLocker/patches/010036E00FB20000/1DA748FC9499882F.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/The%20Great%20Ace%20Attorney%20Chronicles) |
| The Knight Witch | `0100E8501816E000` | `9C09F15234A270E4` (◯, v5, 1.0.5) | 🟢 |  |
| The Legend of Heroes: Trails of Cold Steel III | `01005420101DA000` | `134EC3D8BE75126F` (✝️, v1, 1.0.1) | 🔴 | [LINK](Methodology/Trails%20of%20Cold%20Steel%203) |
| The Legend of Heroes: Trails of Cold Steel IV | `0100D3C010DE8000` | `59159483CF88330F` (✝️, v3, 1.0.3) | 🔴 | [LINK](Methodology/Trails%20of%20Cold%20Steel%204) |
| The LEGO Movie 2 - Videogame | `0100A4400BE74000` | `BAC1309DDF75B14D` (◯, v3, 1.0.3) | 🟢 |  |
| The LEGO NINJAGO Movie Video Game | `01000CE002072000` | `346959B36CD9F14D` (◯, v3, 1.0.3) | 🟢 |  |
| The Outer Worlds | `0100626011656000` | `761CD556AB357C87` ([✅](SaltySD/plugins/FPSLocker/patches/0100626011656000/761CD556AB357C87.yaml), v5, 1.0.5) | 🔵 | [LINK](Methodology/The%20Outer%20Worlds) |
| The Sinking City | `010028D00BA1A000` | `85E49C169A8B988A` ([✅](SaltySD/plugins/FPSLocker/patches/010028D00BA1A000/85E49C169A8B988A.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/The%20Sinking%20City) |
| The Smurfs Mission Vileaf | `010040A01407E000` | `BBBBB9891F01415E` (◯, v4, 1.0.19.1) | 🟢 |  |
| The Stretchers | `0100AA400A238000` | `14D7D1537BD5A986` ([✅](SaltySD/plugins/FPSLocker/patches/0100AA400A238000/14D7D1537BD5A986.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/The%20Stretchers) |
| The Survivalists | `0100EF200DA60000` | `69A45110D07F0442` (◯, v7, 1.0.7) | 🟢 |  |
| The Witcher 3 | `010039400E8D6000` <br> `01003D100E9C6000` <br> `0100BFE00E9CA000` <br> `010076F00E9C8000` <br> `010070A00E9CE000` <br> `010085500E9D0000` <br> `010019C00E9CC000` <br> `01000BB00E9D2000` <br> `0100A0800E9C4000` <br> | `4FFB62F1CD9E17F8` ([✅](SaltySD/plugins/FPSLocker/patches/010039400E8D6000/4FFB62F1CD9E17F8.yaml), v4, 3.7) <br> `986CE0BB97D63CE6` (✝️, v0, 3.2) | 🔴 | [LINK](Methodology/The%20Witcher%203) |
| Thronebreaker: The Witcher Tales | `0100E910103B4000` | `1BD046113635234D` (◯, v2, 1.0.2) | 🟢 |  |
| Tiny Troopers: Global Ops | `0100347013E4C000` | `A3EE277B20160F49` (◯, v0, 1.0.0.0) | 🟢 |  |
| Tinykin | `0100A73016576000` | `4E2AA28721AFF2C1` ([✅](SaltySD/plugins/FPSLocker/patches/0100A73016576000/4E2AA28721AFF2C1.yaml), v3, 1.1.0) | 🔵 |  |
| Tokyo Mirage Sessions<br>#FE Encore | `0100A9400C9C2000` | `33463E11899166BB` (✝️, v0, 1.0.0) | 🟣 | [LINK](Methodology/Tokyo%20Mirage%20Sessions%20%23FE%20Encore) |
| Tony Hawk's Pro Skater 1 + 2 | `0100CC00102B4000` | `8AFCBE6A930CD42E` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC00102B4000/8AFCBE6A930CD42E.yaml), v3, 1.0.3) | 🔴 | [LINK](Methodology/Tony%20Hawk's%20Pro%20Skater%201%20%2B%202) |
| Train Life: A Railway Simulator | `0100FC101513E000` | `A9CE4E0196706EC8` (❌, v1, 1.0.1) | 🔵 |  |
| Trek to Yomi | `0100D77019324000` | `A52C9938956331C9` ([✅](SaltySD/plugins/FPSLocker/patches/0100D77019324000/A52C9938956331C9.yaml), v3, 0.4) | 🔵 | [LINK](Methodology/Trek%20to%20Yomi) |
| Triangle Strategy | `0100CC80140F8000` | `2AA7F33234696651` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/2AA7F33234696651.yaml), v1, 1.0.2) <br> `F7C20294EFF7E6FA` ([✅](SaltySD/plugins/FPSLocker/patches/0100CC80140F8000/F7C20294EFF7E6FA.yaml), v2, 1.0.3) | 🔵 | [LINK](Methodology/Triangle%20Strategy) |
| TT Isle of Man | `010099900CAB2000` | `F2F739A2F1CAFF72` ([✅](SaltySD/plugins/FPSLocker/patches/010099900CAB2000/F2F739A2F1CAFF72.yaml), v1, 1.1.0) | 🔵 | [LINK](Methodology/TT%20Isle%20of%20Man) |
| TY the Tasmanian Tiger 2 | `0100BC701417A000` | `1F8808E4FC7516D2` (❌, v1, 1.0.1) | 🔵 | [LINK](Methodology/TY%20the%20Tasmanian%20Tiger%202) |
| Ultra Age | `01008D4015904000` | `CA77083E259D87A2` ([✅](SaltySD/plugins/FPSLocker/patches/01008D4015904000/CA77083E259D87A2.yaml), v7, 2.0.4) | 🔵 | [LINK](Methodology/Ultra%20Age) |
| Ultra Kaiju Monster Rancher | `01008E0019388000` | `53384CC3D2B4CA9F` (❌, v0, 1.0.1) | 🟡 | [LINK](Methodology/Ultra%20Kaiju%20Monster%20Rancher) |
| Undungeon | `0100CA3018EA4000` | `6A5B168E1D2C6647` (◯, v0, 0.002) | 🟢 |  |
| V-Rally 4 | `010064400B138000` | `EB8A679B5DDD0060` ([✅](SaltySD/plugins/FPSLocker/patches/010064400B138000/EB8A679B5DDD0060.yaml), v2, 1.2.0) | 🔵 | [LINK](Methodology/V-Rally%204) |
| Valkyria Chronicles 4 | `01005C600AC68000` | `3758602AA47ADD37` (❌, v0, 1.0.0) | 🟡 | [LINK](Methodology/Valkyria%20Chronicles%204) |
| Vampyr | `01000BD00CE64000` | `E417100FFEEFD1DE` ([✅](SaltySD/plugins/FPSLocker/patches/01000BD00CE64000/E417100FFEEFD1DE.yaml), v2, 0.4) | 🔵 | [LINK](Methodology/Vampyr) |
| Warhammer 40000: Shootas, Blood & Teef | `010088B0155E2000` | `C9300E99B4975DCF` (◯, v3, 1.0.3_Switch) | 🟢 |  |
| WARRIORS OROCHI 4 | `010016A00AEC0000` | `5C9CCD358BE85FC9` ([✅](SaltySD/plugins/FPSLocker/patches/010016A00AEC0000/5C9CCD358BE85FC9.yaml), v8, 1.0.13) | 🔴 |  |
| What Remains of Edith Finch | `010038900DFE0000` | `E9578A470B175851` ([✅](SaltySD/plugins/FPSLocker/patches/010038900DFE0000/E9578A470B175851.yaml), v0, 1.0.0) | 🔴 | [LINK](Methodology/What%20Remains%20of%20Edith%20Finch) |
| White Day: A Labirynth Named School | `010076601839C000` | `36D6740B3873CE4A` (◯, v1, 1.0.2) | 🟢 |  |
| Wolfenstein: Youngblood | `01003BD00CAAE000` | `8B40EBBA7244C94A` ([✅](SaltySD/plugins/FPSLocker/patches/01003BD00CAAE000/8B40EBBA7244C94A.yaml), v5, 1.5) | 🟡 | [LINK](Methodology/Wolfenstein%20Youngblood) |
| Wolfenstein II: The New Colossus | `01009040091E0000` | `F2FE5EF877839F4F` ([✅](SaltySD/plugins/FPSLocker/patches/01009040091E0000/F2FE5EF877839F4F.yaml), v2, 1.2) | 🟡 | [LINK](Methodology/Wolfenstein%202%20The%20New%20Colossus/README.md) |
| WORLD OF FINAL FANTASY MAXIMA | `010072000BD32000` | `5767FD44C331B44B` (❌, v1, 1.0.1) | 🟡 | [LINK](Methodology/WORLD%20OF%20FINAL%20FANTASY%20MAXIMA) |
| WRC10 | `01003E3014AFE000` | `69CACEEC5F01C41B` ([✅](SaltySD/plugins/FPSLocker/patches/01003E3014AFE000/69CACEEC5F01C41B.yaml), v1, 1.1.0) | 🔵 | [LINK](Methodology/WRC10) |
| WRC Generations | `0100041018810000` | `B8BE1CFAE53CAEBE` ([✅](SaltySD/plugins/FPSLocker/patches/0100041018810000/B8BE1CFAE53CAEBE.yaml), v4, 1.2.2) | 🔵 | [LINK](Methodology/WRC%20Generations) |
| Wreckfest | `0100DC0012E48000` | `7BCD694B69C98104` (◯, v2, 1.0.2) | 🟢 |  |
| Xenoblade Chronicles: Definitive Edition | `010074F013262000` | `92C78BB3DCBBC3F7` ([✅](SaltySD/plugins/FPSLocker/patches/0100FF500E34A000/92C78BB3DCBBC3F7.yaml), v6, 1.1.2) | 🔴 | [LINK](Methodology/Xenoblade%20Chronicles) |
| Xenoblade Chronicles 3 | `010074F013262000` | `B76CD24AF02ACEA2` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/B76CD24AF02ACEA2.yaml), v6, 1.3.0) <br> `8E18600222CE90C2` ([✅](SaltySD/plugins/FPSLocker/patches/010074F013262000/8E18600222CE90C2.yaml), v7, 2.0.0) | 🔴 | [LINK](Methodology/Xenoblade%20Chronicles%203)  |
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
