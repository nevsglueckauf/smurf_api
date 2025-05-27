# Setup Beispiel 

Komplett für  UNIX like OS (MacOS, Linux, Solaris etc.) -> für Wintendo Boxen mit Hinweisen

## Repo clonen

<kbd>git clone https://github.com/nevsglueckauf/pyquiz </kbd>

<kbd>cd pyquiz</kbd>



## VENV

### Virtuelle Umgebung einrichten
<code>sven@Thanos pyquiz % </code><kbd>python3 -m venv .venv</kbd>

### Virtuelle Umgebung aktivieren
<code>sven@Thanos pyquiz % </code><kbd>source .venv/bin/activate</kbd>

<code><span style="color:green">(.venv)</span> sven@Thanos pyquiz % </code>

Für Wintendo Boxen:

```PS
.venv\Scripts\activate
```

## Dependencies AUFLÖSEN

<code><span style="color:green">(.venv)</span> sven@Thanos pyquiz % </code><kbd>pip -r req.txt</kbd>

## Web App starten
Bootstrap starten mit Umlenkung von ```STDIN``` und ```STDOUT``` nach ```dev/null```

```sh
(.venv) svenschrodt@Thanos pyquiz % python -m streamlit run Home.py  > /dev/null  2>&1 &
```

## 