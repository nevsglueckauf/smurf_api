# Python 

## Package

Das <var>Main Package</var> heißt ```pyquiz```

### pyquiz.app

Sub-Package für die Steuerung der Apps (Shell, GUI, Web)


### pyquiz.api

Sub-Package für den Zugriff auf die HTTP RESTful API von Open Trivia DB



### pyquiz.mock

Sub-Package für den Zugriff auf Daten aus dem lokalen Cache (in der APP und für Tests)


### pyquiz.persist

Sub-Package für den Zugriff auf persistierte Daten allgemein


### pyquiz.entity

Sub-Package für die Repräsentation der Daten als Entity-Instanzen



## UML - Klassendiagramme [^1]

```mermaid
classDiagram
    Controller *-- ViewHelper
    Controller *-- OTDBApi
    OTDBApi *-- Endpoints
    Runner <|-- CliRunner
    QuestionList "1" --> "*" Question

    class Controller{
        + __ init__(self, st: streamlit)
        + meta(self, title: str = "", icon: str = "")
        + save_success(self, msg="Daten gespeichert 💾")
    }

    class ViewHelper{
        + + __ init__(self, st:streamlit)
        + + cats(self)
        + + amount(self)
        + + diff(self)
    }


    class OTDBApi{
        + __ init__(self)
        + get_questions_raw(self, number: int = 10)
    }

    class Endpoints{
    }
 
    class Runner{
        + __ init__(self)
        + render(self, question:Question)
    }

    class CliRunner{
        + __ init__(self)
        + render(self, question:Question)
    }

    class App{
        + __ init__(self)
    }

    class QuestionList{
         + __ init__(self)
         + filter_by()
         + equals()
    }

    class Question{
         + __ init__(self)
         +  + solve(self):
         + __getattr__(self, key):
         + __str__(self) -> str:
         + __sanitize_key(self, key: str):
         + __sanitize_answer(self, input):
    }

    class QDFA{
        + __ init__(self):
        + n(self):
        + sf(self, sfx: str = ".json") -> Self:
        + pf(self, pfx: str = "qd_") -> Self:
        + w(self, txt:str='', fn:str='::auto::', mode:str='a') -> Self:
        + r(self, fn:str='::auto::') -> str:
    }

    
```
## Datenstrukturen

Die generelle Datenstruktur welche hier Verwendung findet ist [```pandas.DataFrame```](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

Aus den JSON-Ressourcen (andere: tbd.) von Open Trivia DB werden ```DataFrames``` erzeugt.

### Motivation

- Robuste und performante Operationen auf (Pandas)- Datenstrukturen gewährleisten



--- 
[^1]: Dunder- Methoden enthalten hier <var>Space</var> im Namen nach "__", damit der Text nicht als __Fett__ markiert wird : 