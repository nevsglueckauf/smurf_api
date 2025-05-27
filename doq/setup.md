# Setup Beispiel 

Komplett für  UNIX like OS (MacOS, Linux, Solaris etc.) -> für Wintendo Boxen mit Hinweisen

## Repo clonen

<kbd>git clone https://github.com/nevsglueckauf/smurf_api </kbd>

<kbd>cd smurf_api</kbd>



## VENV

### Virtuelle Umgebung einrichten
<code>sven@Thanos smurf_api % </code><kbd>python3 -m venv .venv</kbd>

### Virtuelle Umgebung aktivieren
<code>sven@Thanos smurf_api % </code><kbd>source .venv/bin/activate</kbd>

<code><span style="color:green">(.venv)</span> sven@Thanos smurf_api % </code>

Für Wintendo Boxen:

```PS
.venv\Scripts\activate
```

## Dependencies AUFLÖSEN

<code><span style="color:green">(.venv)</span> sven@Thanos smurf_api % </code><kbd>pip -r req.txt</kbd>

## FastAPI DEV App starten
Bootstrap starten mit Umlenkung von ```STDIN``` und ```STDOUT``` nach ```dev/null```

```sh
(.venv) svenschrodt@Thanos smurf_api % fastapi dev main.py  
#> /dev/null  2>&1 &
```

## 