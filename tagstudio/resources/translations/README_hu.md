# TagStudio: Egy felhasználóközpontú dokumentumkezelő rendszer

<details>
    <summary>🌐 Nyelv</summary>
    <br>
    <div align="left">
        <table align="left">
            <tr>
                <td>🌎 <a href="/#:Rr9ab:">angol</a></td>
                <td><a href="https://github.com/Nginearing/TagStudioTesting/blob/main/CONTRIBUTING.md">Új nyelv</a></td>
            </tr>
        </table>
    </div>
</details>
<br>
<br>

<p align="center">
  <img width="60%" src="/docs/assets/github_header.png">
</p>

A TagStudio egy fénykép- és fájlrendszerező alkalmazás, ami a felhasználó szabadságára és rugalmasságára helyezi a hangsúlyt. A TagStudio köreiben nincsenek jogvédett programok és fájlformátumok, széthullajtott oldalkocsifájlok és nem fordítja a feje tetejére a létező fájlrendszert. **A dokumentációt megtalálja a [docs.tagstud.io](https://docs.tagstud.io)-honlapon.**

> [!CAUTION]
> **A [#332](https://github.com/TagStudioDev/TagStudio/pull/332). (SQLite Migration) lekérési kérelemtől fogva a program `main` ága egy nyílt próbaverzió, amelyen a teljes JSON–SQL-funkcióparitást próbáljuk elérni.** A létező TagStudio-könyvtárak még nem kompatibilisek a változtatásokkal, viszont az ezekkel a verziókkal történő megnyitásuk **NEM jár a könyvtárak sérülésével vagy törlésével**. Ezt a figyelmeztetést el fogjuk távolítani, ha elérjük a paritást és befejezzük a könyvtárkonvertáló kifejlesztését.
>
> A legújabb stabil verzióhoz ld.: [`Alpha-v9.4` ág](https://github.com/TagStudioDev/TagStudio/tree/Alpha-v9.4). A 9.4-es verzió új funkcióit jelenleg ültetjük át az SQL-izált `main` ágba. [Ha tud velünk angolul kommunikálni, örömmel vennénk a segítséget!](/CONTRIBUTING.md)

> [!NOTE]
> Ez a projekt jelenleg még egy nagyon korai fázisban van. A teljesítmény és az élmény nem ideális, és elvétve furcsaságokkal és döcögős munkamenetekkel is találkozhat. Általánosságban elmondható, hogy a könyvtárfájlok biztonsági a mentése a program állapotától függetlenül **mindig** fontos.
>
> Mindezek mellett azt megjegyeznénk, hogy a TagStudio _NEM_:
>
> - fog akármilyen módon érinteni, áthelyezni vagy egyéb módon fájlokat módosítani _(kivéve, ha a fájltörlő funkciót használja, ami egy megerősítő párbeszédablak mögé van zárva)_;
> - fog frissítések után könyvtárakat alaphelyzetbe állítani és Öntől elvárni, hogy ezeket újra létrehozza – az adatok biztonságos verziók közötti frissítése és átvitele számunkra a legfőbb szempont;
> - teszi lehetővé Ön számára, hogy észben tarthassa azt a 10 billió letöltött képet, amelyeket még valószínűleg nem is tekintett meg első kézből – az irányítás az Ön kezében van, de még a gépi tanulás alapján fejlesztett eszközöket is emberi szemmel kell ellenőrizni, mielőtt azokat pontosnak kiálthatnánk ki.

<figure align="center">
  <img width="80%" src="/docs/assets/screenshot.jpg" alt="TagStudio Screenshot" align="center">

  <figcaption><i>A TagStudio 9.1.0-s alfaverziója Windows 10-en.</i></figcaption>
</figure>

## Tartalom

- [Célok](#célok)
- [Prioritások](#prioritások)
- [Jelenlegi képességek](#jelenlegi-képességek)
- [Közreműködés](#közreműködés)
  - [Fejlesztői környezet felállítása](#fejlesztői-környezet-felállítása)
- [Használat](#használat)
- [GY.I.K.](#GY.I.K.)

## Célok

- Egy hordozható, biztonságos, nyitott, kiterjeszthető és funkciógazdag fájlrendszerező és -újrafelfedező-rendszer létrehozása.
- A rendszerezés sokoldalú lehetővé tétele, elsősorban a címkekompozíció, avagy a „címkézhető címkék” kínálata.
- Egy olyan rendszer létrehozása, amely ellenálló a felhasználó programon kívüli cselekedeteivel szemben (fájlok módosítása, áthelyezése, átnevezése), olyan módon, hogy ne terhelje őt kötelező oldalkocsifájlok tárolásával vagy a létező fájlstruktúrák és munkamenetek megváltoztatásával.
- Sokféle felhasználó támogatása különböző platformokon, többfelhasználós felállásban, nagy (több terabájtos) könyvtárakkal.
- Mindezt úgy elérni, hogy a program ki is nézzen valahogy – elvégre 2024 van, nem pedig 1994.

## Prioritások

1. **Az ötlet.** Még ha a TagStudio, mint program, el is bukna, szeretném hogy az ötlete tovább éljen egy jobb projektben. A fent körvonalazott [célok](#célok) nem a TagStudiót testesítik meg – a _TagStudio_ testesíti meg a _célokat_.
2. **A rendszer.** Az előterek és implementációk változatosak és ez így is van rendjén. A központi metaadatkezelő-rendszernek viszont előtértől, programtól és operációs rendszertől függetlenül működnie kell. A fejlesztés során ki fog alakulni egy szabványos implementáció – ez megnyitja majd az utat jobb és változatosabb kliensek, külsős alkalmazásokkal való kompatibilitás és még több előtt.
3. **Az alkalmazás.** Alaphangon a TagStudio lesz ennek a metaadatkezelő-rendszernek az első (és eddig egyetlen) implementációja. Emiatt rá esik a felelősség az ötlet helyes megtestesítése iránt, és hogy megmutassa, mit is tesz lehetővé a fájlkezelés ezen módja.
4. (A név.) Úgy gondolom, hogy ez egy egész jó név egy alkalmazásnak, de nem illik túlságosan egy rendszerhez vagy szabványhoz. Majd meglátjuk, hogy mi lesz belőle.

## Jelenlegi képességek

- A rendszer egy mappájának alapjára épített könyvtárak. Ezek a könyvtárak tételeket tartalmaznak, amelyek a fájlok képviselői metaadatmezőkkel kiegészítve. Minden tétel egy fájlt testesít meg és annak az elérési útjával van összekapcsolva.
- Metaadatok létrehozása a könyvtár tételeiben. Többek között:
  - cím, szerző, előadó (egysoros szövegmezők);
  - leírás, jegyzetek (többsoros szövegmezők);
  - címkék, metacímkék, tartalomcímkék (címkemezők).
- Sokoldalú címkék létrehozása, amelyek tartalmazhatnak egy elnevezést, áljeleket és „alcímkéket” – ezek olyan címkék, amelyek a szülőcímkéiktől vesznek át értékeket.
- Tételek közötti keresés címkék, ~~metaadatok~~ (a későbbiekben) vagy fájlnevek/-típusok (`filename: <keresési kifejezés>`) alapján.
- Különleges keresési esetek: `untagged`/`no tags` (címke nélküli) és `empty`/`no fields` (mező nélküli).

> [!NOTE]
> További információért ld.: [GY.I.K](#gy.i.k.), [Dokumentáció](/docs/index.md).

## Közreműködés

Ha szeretne közreműködni a TagStudio fejlesztésében és tud velünk angolul kommunikálni, kérjük böngéssze át a [közreműködési segédletet](/CONTRIBUTING.md) _(angol nyelven)_!

A projekt fordítását a [Weblate](https://hosted.weblate.org/projects/tagstudio/)-en végezzük.

### Fejlesztői környezet felállítása

<details>
<summary>Részletek</summary>

#### Követelmények

- [Python](https://www.python.org/downloads/) 3.12
- [Ruff](https://github.com/astral-sh/ruff) (A `requirements-dev.txt` tartalma)
- [Mypy](https://github.com/python/mypy) (A `requirements-dev.txt` tartalma)
- [PyTest](https://docs.pytest.org) (A `requirements-dev.txt` tartalma)

#### A Python virtuális környezet felállítása

Ha a TagStudio forráskód-verzióját a fejlesztőkörnyezetén kívül kívánja futtatni:

> [!IMPORTANT]
> A Pythont előhívó parancs a rendszertől függően lehet `python`, `py`, `python3` vagy `py3`. Az egységesítés érdekében ezek mind a `python3` áljelet használják. A rendszer által használt áljelet a `python3 --version` parancssal lehet előhívni a parancssorból (egyéb áljelek esetén is).

> [!TIP]
> Linuxon és macOS-en a `tagstudio.sh` fájl futtatásával ki lehet hagyni az alábbi részt, a `requirements-dev.txt`-s részt leszámítva. _A program forráskódból való futtatásához elég ez a parancsfájl._

1. Hozzon létre egy Python virtuális környezetet a projekt adattárának gyökérmappájában:
   `python3 -m venv .venv`
2. Aktiválja a környezetet:

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Windows (Parancssor): `.venv\Scripts\activate.bat`
- Linux/macOS: `source .venv/bin/activate`

3. Telepítse a szükséges csomagokat:

- `pip install -r requirements.txt`
- Fejlesztés esetén (tartalmazza a Ruffot és Mypyt is): `pip install -r requirements-dev.txt`

_További információt egy virtuális környezet felállításáról [itt olvashat](https://docs.python.org/3/tutorial/venv.html)_ (angol nyelven)_._

#### Kézi indítás (fejlesztői környezeten kívül)

- **Windows** (start_win.bat)

  - A TagStudio indításához futtassa a `start_win.bat` fájlt. Ha szeretné, szerkesztheti ezt a kötegfájlt vagy létrehozhat egy parancsikont argumentumokkal.
  
- **Linux/macOS** (TagStudio.sh)

  - Egyszerűen futtassa a `TagStudio.sh` fájlt. (Linuxon ne felejtse el futtathatóvá tenni a parancsfájlt!) Megjegyzés: Ha terminálon kívülről futtatja a programot, akkor a hibakeresési és összeomlási információkat tartalmazó terminálablak nem fog megjelenni. Ha szeretné látni ezeket az információkat, akkor futtassa a parancsfájlt terminálból, a `./TagStudio.sh` paranccsal.
  
  - **NixOS** (Nix Flake)
    > [!WARNING]
	> A NixOS-támogatás még kidolgozás alatt van.
	- Hozzon létre és lépjen be egy munkakörnyezetbe a projektben található [Flake](https://nixos.wiki/wiki/Flakes) felhasználásával, a `nix develop` parancs futtatásával. Ezután a gyökérmappából futtassa a programot a `python3 tagstudio/tag_studio.py` paranccsal.
	
- **Bármilyen környezet** (Parancsfájlok nélkül)

  - Ezen kívül a virtuális környezetből egyszerűen futtathatja a `tagstudio\tag_studio.py` Python-fájlt is. Ha a gyökérmappában van, használja a `python3 tagstudio/tag_studio.py` parancsot.
</details> 

## Telepítés

