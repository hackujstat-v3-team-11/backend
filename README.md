# Team Eleven
---
#### Statistika hrou je platforma pro prezentaci dat zábavným interaktivním způsobem. Má formu chatbota napojitelného na facebook Messenger i vlastní dialog-flow web aplikaci. Tímto designem získává potenciál oslovit skrze sociální sítě. 

ChatBot po zahájení konverzace zprávou "čau" vyzve hráče k zadání okresu v ČR. Z reálií zvoleného místa pak formuluje otázky kvízu. Hráč se tak seznamuje s nejrůznějšími statistickými daty daného regionu.

---
## Datové sady
  - Repozitář obahuje několik datových sad, pro demostraci možností systému.
### Zdroje čerpání dat
- [Český Sociálněvědní Datový Archív](http://nesstar.soc.cas.cz/webview/)
	- České panelové šetření domácností (CHPS)
		- [spokojenost s životem](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/people/zivot_spokojenost.json) 
		- [spokojenost se zaměstnáním](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/people/zamestnani_spokojenost.json)
		- [spokojenost ve vztahu](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/people/vztah_spokojenost.json)
		- [pocit štěstí](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/people/pocit_stesti.json) 
		- [míra kouření](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/people/smoke.json) 
		- [průměrný věk](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/people/age.json)
- [Český Statistický Úřad](https://www.czso.cz/)
    - [Hospářská zvířata podle krajů](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/hospodarska_zvirata/270230-19data053119.csv)
    - [Sklizeň zemědělských plodin podle krajů](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/sklizen_zemedelskych_plodin/270229-19data043019.csv)
    - [Populace](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/populace/DEM07D.csv)
    - [Hosté a přenocování v hromadných ubytovacích zažízeních podle zemí](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/foreign_tourists/020063-19data080819.csv)
    - [Naděje dožití v okresech a správních obvodech ORP](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/life_expectancy/130140-19data080519.csv)
- [Ministerstvo zdravotnictví České republiky](https://www.mzcr.cz)
    - [Národní registr poskytovatelů zdravotních služeb](https://github.com/hackujstat-v3-team-11/backend/blob/master/question_modules/medical_facilities/narodni-registr-poskytovatelu-zdravotnich-sluzeb.csv)
- [Český úřad zeměměřický a katastrální](https://www.cuzk.cz/Uvod.aspx)
    - [číselníky katastrů]()