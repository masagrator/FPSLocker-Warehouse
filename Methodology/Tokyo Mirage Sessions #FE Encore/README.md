# Tokyo Mirage Sessions™ #FE Encore

> Game info

TitleID: `0100A9400C9C2000`<br>
Explanation based on:
- Internal version: `1.0.0`, 
- Nintendo version ID: `v0`
- BID: `33463E11899166BB`
- Engine: Atlus proprietary engine

> Details

SaltyNX doesn't support 32-bit games. It requires strict testing what is broken and not, because it uses different 1/30 floats for different things, some must be changed, some are breaking gameplay if changed. UI doesn't use this float to change speed. Game uses double buffer and is fairly easy to unlock triple buffer.
