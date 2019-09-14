# Team Eleven
---
#### Tento projekt je univerzální datová platfotma pro zpracování dat a následné zprostředkování na sociální síť ve formě    ChatBota, který má za úkol přiblížit obyvatelstvu některá vybraná data formou zábavného chat kvízu. 
---
## Datové sady
  - Repozitář obahuje několik datových sad, pro demostraci.
### Zdroje čerpání dat
- [Český Sociálněvědní Datový Archív](http://nesstar.soc.cas.cz/webview/)
	- České panelové šetření domácností (CHPS)
		- [spokojenost s životem](https://github.com/teams91/13/blob/master/datove_sloupce/zamestnani_spokojenost.json) 
		- [spokojenost se zaměstnáním](https://github.com/teams91/13/blob/master/datove_sloupce/zamestnani_spokojenost.json)
		- [spokojenost ve vztahu](https://github.com/teams91/13/blob/master/datove_sloupce/vztah_spokojenost.json)
		- [pocit štěstí](https://github.com/teams91/13/blob/master/datove_sloupce/pocit_stesti.json) 
		- [míra kouření](https://github.com/teams91/13/blob/master/datove_sloupce/smoke.json) 
		- [míra konzumace alkoholu](https://github.com/teams91/13/blob/master/datove_sloupce/konzumace_alkoholu.json) 
		- [průměrný věk](https://github.com/teams91/13/blob/master/datove_sloupce/age.json)
- [Český Statistický Úřad](https://www.czso.cz/)
	-  [Bytová výstavba](https://www.czso.cz/csu/czso/dokoncene-byty-v-obcich) *(Možno sledovat od 1997 - 2016*)
	-  [Zemřelí podle příčin smrti](https://www.czso.cz/csu/czso/zemreli-podle-pricin-smrti-a-pohlavi-v-cr-krajich-a-okresech)

### Formáty dat

1) Data měřená agregovanou hodnotou nad jednotlivými částmi mapy, jsou reprezentovány jednoduchým JSON formátem. 
*Příklad*:
`{"CZ0712":71, "CZ0635":76, "CZ0514":76, "CZ0316":70}`
`"CZ0712":71` = "Kód okresu":Velikost měřené hodnoty

	Kódy okresů jsou převáděné [číselníky](https://github.com/teams91/13/blob/master/czso-okresy-ciselnik.json) [Státní správy zeměměřictví a katastru](http://atom.cuzk.cz/)
