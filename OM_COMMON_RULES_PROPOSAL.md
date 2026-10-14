# OM — Common Project Rules Proposal

Klasifikace: TLP CRA GREEN (návrh; neobsahuje osobní údaje ani secrets, obsah se týká procesu vývoje)

**Status:** DEVELOPMENT PROPOSAL / NON-CANONICAL
**Target:** OM 2.4.0 (navrhovaná minor verze; číslo určí vlastník OM)
**Origin:** analýza `.project/DEVELOPMENT_RULES.md` projektu CRA Business Mapping (OM 2.3.0, DEV, solo), 2026-10-14
**Stav návrhu:** k revizi uživatelem. Nic nebylo změněno v repozitáři OM.

## 1. Problém

OM 2.3.0 nemá mechanismus společných pravidel pro projekt. DEV profil (bod 3) označuje `DEVELOPMENT_RULES.md` jako volitelný („conditional, not mandatory“) a šablona obsahuje jen placeholder. Projekt, který chce provozní pravidla nad rámec profilu, je proto celá píše a udržuje sám. V projektu CRA Business Mapping vznikla sada 14 pravidel; asi polovina je obecná a každý další projekt by ji kopíroval nebo znovu vymýšlel.

## 2. Návrh

Zavést **společnou vrstvu pravidel** a ponechat `DEVELOPMENT_RULES.md` jako doplněk, ne náhradu.

Vrstvy a priorita (od nejvyšší):

1. OM jádro a profil (`CORE.md`, `profiles/DEV.md`): invarianty z oddílu 6, které nelze oslabit v žádné nižší vrstvě.
2. **Pravidla organizace** (např. CRA), **volitelná vrstva**. Pokud existuje, je nadřazená OM Common Rules: smí je zpřesnit, specializovat a zpřísnit.
3. **OM Common Rules** (nové): obecný základ vydávaný s OM, bez obsahu specifického pro organizaci nebo projekt. Platí, pokud organizační vrstva neexistuje, a doplňuje ji všude, kde s ní není v rozporu.
4. `DEVELOPMENT_RULES.md` projektu: jen to, co je pro projekt specifické, a výslovné výjimky.

Pravidlo rozporu: při rozporu vyhrává vyšší vrstva, s výjimkou invariantů vrstvy 1. Pravidlo, které organizační vrstva neřeší, se doplní z OM Common Rules.

Projekt společná pravidla přijímá odkazem na pevnou revizi OM (už připnutou v `governance.operating_model`). Nepřijímá je kopií. Výjimka ze společného pravidla musí být zapsána v `DEVELOPMENT_RULES.md` s důvodem.

## 3. Obsah Common Rules (povýšení z projektu CRA)

Číslování = pravidla v `DEVELOPMENT_RULES.md` CRA Business Mapping.

| # | Pravidlo | Návrh formy v OM | Poznámka |
|---|---|---|---|
| 14 | AI review a audit | nový playbook `AI_REVIEW_AUDIT.md`, navazuje na SOLO 4–5 a AI loop 6 | viz 3.1 |
| 12 | Repozitář je jediný zdroj stavu, paměť agenta je jen pomůcka | doplnění DEV 20 a 22 | rozhodnutí a otevřené body se zapisují v session, kde vznikly |
| 10 | Životní cyklus pracovní jednotky (vlny) | volitelný vzor v AI loop | viz 3.2 |
| 1–4 | Lokální kompenzace bez platformy | nová platforma `platforms/git_local/` | viz 3.3 |
| 7 | Osobní údaje: nevkládat do repozitáře, dokumentů, evidence, testů ani externích služeb; agent pracuje s ID, počty a pseudonymy; fixtures jen syntetické | obecný základ v OM Common Rules | bez CRA specifik (pověřenec, konkrétní soubory); organizace smí zpřísnit |
| 8 | Secrets: žádné credentials a tokeny ve zdrojích, dokumentech a commitech | obecný základ v OM Common Rules | úložiště tajemství a postup při úniku určí organizace |
| 13 | Git: commit, tag a push po souhlasu uživatele; push jen do schváleného hostingu | obecný základ v OM Common Rules | jazyk commit messages a konkrétní hosting určí organizace nebo projekt |
| 9 | Závislosti: zamčené verze, zdůvodnění nové | doplnění DEV 25 | zákaz CDN zůstává projektový |
| 11 | Neúspěšná jednotka se nepřepisuje | beze změny OM | už pokrývá DEV 8; vzor jen mapovat na DEV 8 |

### 3.1 Playbook AI review a audit

Spouštěč: `assurance.mode: solo` a materiální změna, nebo kdykoli profil vyžaduje nezávislou analytickou kontrolu.

- Review provádí subagent s čistým kontextem, bez konverzace z implementace. Pokud je dostupný, použije se jiný model než implementace.
- Zadání je pevný dokument projektu (`REVIEW_BRIEF.md`). Implementující agent ho pro konkrétní práci nezužuje a mění se jen se souhlasem uživatele.
- Rozsah určuje rozdíl proti poslednímu přijatému bodu (commity, necommitnuté i nové soubory), ne implementující agent.
- Subagent je read-only: nic nemění, necommituje a nepřistupuje ke vzdáleným systémům.
- Výstup se ukládá beze změny, dříve než na něj implementace reaguje. Každý nález dostane rozhodnutí (opraveno / odmítnuto s důvodem / převedeno), které schvaluje člověk. Žádný nález se nevypouští.
- Evidence uvádí model, rozsah, počty podle závažnosti, odkaz a údaj „lidská self-review diffu: ano/ne“.
- Po materiální opravě se review opakuje.
- Záznam je „AI review“. Nenahrazuje lidské přijetí (SOLO 2, 4, 7).

### 3.2 Pracovní jednotka a session (volitelný vzor)

OM 22 říká, že změna session sama nevytváří stav. Proto vzor nic nepředepisuje, jen nabízí volitelnou konvenci:

1. Nová session začíná recovery (PROJECT → ACTIVE_STATE → podmíněné čtení).
2. Plán jednotky se předloží a čeká se na souhlas, bez souhlasu se neimplementuje.
3. Evidence jednotky, review, přijetí člověkem, pak commit, tag a aktualizace ACTIVE_STATE, vše po souhlasu.
4. Na konci jednotky agent **doporučí**, zda pokračovat ve stejné session, nebo začít novou. Není to požadavek. Podle principů OM (průběžné ukládání stavu, načítání minimálního kontextu, discover) je přechod do nové session z hlediska správnosti lhostejný. Rozhoduje praktická stránka: délka kontextu (náklady na tokeny a kvalita), a že jsou stav, evidence a další kroky zapsané v repozitáři. Rozhodnutí uživatele z 2026-10-14; nahrazuje tvrdé „jedna vlna = jedna session“ z pravidla 10 projektu CRA Business Mapping.

Pojmy „vlna“ a roadmapa zůstávají projektové. OM používá neutrální „pracovní jednotka“.

### 3.3 Platforma `git_local` (lokální vynucení)

Pro projekty bez platformního vynucení (DEV 24):

- vzorový `reference-transaction` hook, který odmítne přesun nebo smazání přijímacích tagů,
- vzorový `pre-commit` hook, který validuje staged `.project/*.yaml` proti schématům na přesné OM revizi a ověří shodu `ref` a `commit`,
- projekt doplní jen seznam zakázaných cest a přípon,
- záloha ověřeným `git bundle` všech refů se součtem SHA256, bez přepisování a mazání existujících záloh,
- procedurální kontroly (build, testy) nahrazující chybějící CI se výslovně zapisují jako kompenzace.

## 4. Změna v OM mimo pravidla

- **Validátor bez Pythonu.** OM validátor dnes vyžaduje Python. CRA Business Mapping ho kvůli tomu nahrazuje vlastním validátorem v Node (pravidlo 3). Doporučení: OM poskytne validátor bez závislosti na Pythonu, nebo referenční implementaci nezávislou na prostředí. Tím vlastní validátory v projektech odpadnou.
- **Šablona.** `templates/DEV/.project/DEVELOPMENT_RULES.md` nahradit kostrou s oddíly „Přijatá společná pravidla (revize OM)“, „Výjimky“ a „Specifická pravidla projektu“.

## 5. Co v OM nepatří (zůstává mimo)

- Obsah specifický pro organizaci CRA v pravidlech 7, 8 a 13: pověřenec, CRA Vault, konkrétní soubory s osobními údaji, jazyk commit messages, firemně schválený hosting. OM obsahuje jen obecné znění, konkrétní podobu doplní organizace.
- Obsah projektu: zdroje dat (6), zadání (5), zálohy do konkrétního SharePointu (4), zákaz CDN (9), seznam zakázaných souborů (2).

## 6. Invarianty

Společná vrstva nesmí oslabit: autoritu control plane, historickou integritu, fail-closed autorizaci, přesnou identitu cíle, destruktivní a produkční autorizaci, ani explicitní lidský souhlas. Projektová výjimka ze společného pravidla nikdy nesmí zrušit nic z tohoto seznamu.

## 7. Dopad na projekty

- Existující projekty se nemění, dokud nepřijmou novou revizi OM (`PROJECT.yaml` je pevně připnutý).
- Přijetí společné vrstvy je změna `governance.operating_model` na novou revizi a redukce `DEVELOPMENT_RULES.md` na specifika. Zpětná kompatibilita je zachována, protože projektové pravidlo smí být přísnější než společné.

## 8. Otevřené otázky

**Rozhodnuto uživatelem (2026-10-14):** invarianty OM (oddíl 6) nesmí oslabit žádná nižší vrstva, včetně nadřazené organizační. Organizační vrstva smí společná pravidla jen zpřesnit nebo zpřísnit.

Stav otázek 1, 2 a 4: posouzeno, doporučení čeká na rozhodnutí uživatele. Otázka 3 zůstává otevřená.

1. **Schéma `om.project/v2`: posouzeno.**
   - `PROJECT.v2.schema.json` má `additionalProperties: false` na všech úrovních včetně `governance`. Nové pole v `PROJECT.yaml` by proto bylo změnou schématu a starší validátor by projekt s tímto polem odmítl.
   - Pole **pro přijetí Common Rules není potřeba.** Pravidla jsou součástí vydání OM, které projekt už připíná přes `governance.operating_model` (`ref`, `commit`).
   - **Organizační vrstva** pole potřebuje, ale existuje obejití bez změny schématu. `governance.project_rules.locator` smí být URI (validátor `validate_project_bootstrap.py` při `://` existenci souboru nekontroluje) a projektový soubor pravidel může organizační vrstvu odkazovat pevnou revizí.
   - Doporučení: Common Rules **bez změny schématu**. Pro organizační vrstvu volitelně přidat `governance.organization_rules` (`repository`, `ref`, `commit`) jako zpětně nekompatibilní rozšíření schémat v2 v příští minor verzi OM. Do rozhodnutí o vlastníkovi vrstvy (otázka 3) použít obejití přes `project_rules`.
2. **Povinnost a verzování: posouzeno.**
   - OM pro DEV už dnes některá pravidla stanoví jako „shall“ (např. DEV 25, SOLO 4 až 5). Společná pravidla jsou jejich zpřesněním, ne novým břemenem.
   - Doporučení: Common Rules jsou **součástí vydání OM** (ne samostatně verzovaná) a pro DEV **povinná se zdůvodněnou výjimkou** zapsanou v `DEVELOPMENT_RULES.md`. Výjimka nesmí zasáhnout invarianty z oddílu 6.
   - Pravidla, která jsou volitelným vzorem (pracovní jednotka a session, 3.2), jsou označena jako „may“, ne „shall“.
   - Důvod doporučení: bez povinnosti by se vrstva nepoužívala a každý projekt by pravidla dál psal sám. Samostatné verzování by znamenalo druhou připínací dimenzi v `PROJECT.yaml` bez přínosu.
3. **Vlastník organizační vrstvy.** Vlastník CRA vrstvy zatím není znám. Vrstva je volitelná a bez ní platí OM Common Rules, otázka tedy neblokuje. Zůstává otevřené, zda a kde bude CRA vrstva vznikat (např. samostatný repozitář odkazovaný z `PROJECT.yaml`).
4. **Použitelnost pro ostatní profily: posouzeno z textu profilů DEV, SOLUTION, DOCUMENT, EXPERIMENT a LIGHT.**

   | Pravidlo / prvek | DEV | SOLUTION | DOCUMENT | EXPERIMENT | LIGHT |
   |---|---|---|---|---|---|
   | 7 osobní údaje, 8 secrets | ano | ano | ano | ano | ano |
   | 13 souhlas před commit/tag/push | ano | ano | ano | ano | ano, jen kde je Git |
   | 14 AI review a audit (solo) | ano | ano, doplňuje SOLUTION 6 | ano, doplňuje DOCUMENT 6 | volitelně | volitelně |
   | 12 repozitář je zdroj stavu | ano (DEV 20) | ano (SOLUTION 3) | ano (DOCUMENT 3) | ano (EXPERIMENT 3) | ano (LIGHT 2) |
   | 1 až 4 `git_local` | ano | jen s Git control plane | jen s Git control plane | ne | ne |
   | 9 závislosti | ano | ne | ne | volitelně | ne |
   | 10 pracovní jednotka a session | volitelně | volitelně | volitelně | ne | ne |

   - Playbook AI review a audit je navázaný na `assurance.mode: solo` (SOLO_ASSURANCE je nezávislý na profilu). Proto platí napříč profily, kde je solo režim.
   - Zdůvodnění „ne“ u LIGHT: LIGHT 10 výslovně nechce přechodové balíčky na konci session. Pracovní jednotka a session by byla v rozporu s duchem profilu.
   - Doporučení: Common Rules rozdělit na **univerzální** (7, 8, 12, 13, AI review pro solo), **DEV** (9, 10) a **Git** (1 až 4), přičemž každý profil odkazuje jen na relevantní oddíl.

## 9. Další kroky (vyžadují souhlas)

1. Revize tohoto návrhu uživatelem.
2. Rozhodnutí o doporučeních k otázkám 1, 2 a 4 a o otázce 3 (vlastník organizační vrstvy).
3. Případné založení větve v repozitáři OM a převedení návrhu do kandidátních souborů (`playbooks/AI_REVIEW_AUDIT.md`, `platforms/git_local/`, šablona).
4. Teprve pak úprava `DEVELOPMENT_RULES.md` CRA Business Mapping.
