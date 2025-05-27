# Design & Architecture Dossier

In diesem Dokument wird die technische Umsetzung des Projektes beschrieben

Der Python-spezifische Teil findet sich hier: [PyDesgin](pydesign.md)

## Persistenzschicht

- RDBMS (SQLITE, oder ???)
- Filesystem als JSON
- Filesystem als XML ???
- Filesystem als ```__pycache__``` ???


## Zur Dokumentation Allgemein

### Tools

Markdown (insbes. Mermaid) wegen der hervorragenden Unterstützung durch github

### User Interfaces

#### Shell / Terminal / Plaintext

#### GUI

#### Web

#### Sequenzdiagramm: Abruf der Fragen

```mermaid
sequenceDiagram
    autonumber
    User->Python : Starte APP
    Python->>Webserver: Sende Request an: https://opentdb.com/api.php?amount={$FOO} 
    Webserver->>Python: Sende Response als JSON: {"response_code":0,"results":[...] }
    Python->>Python: Parse Response
    Note over User,Webserver: Führe Kontextbehandlung durch, Mische Inkorr. und korrekte Antworten, Randomisiere Reihenfolge
    Python->>Python:  Generiere View für User Interface
    alt ist graphical user interface
        Python->>TTK_GUI: Starte GUI 
        TTK_GUI->>User: Zeige Daten in GUI 
    else ist web
        Python->Streamlit: LISTEN (HTTP auf Port 8023)
        User-Agent->Streamlit: Sende Request an: https://thanos:8023/trivia_game?amount={$FOO} 
        Streamlit->>User-Agent: Sende Response zurück
        User-Agent->>User: Rendere Daten (Ansicht im Browser)
    end
    opt CLI
        Python->>User: Zeige Daten in Shell/Terminal
    end
```

 

