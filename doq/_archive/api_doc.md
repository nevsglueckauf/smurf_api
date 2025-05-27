# Beschreibung der <var>Open Trivia API</var>


## Session Tokens

- Benutzen: ```https://opentdb.com/api.php?amount=10&token=YOURTOKENHERE```

- Erhalten: ``` https://opentdb.com/api_token.php?command=request```

- Reset: ```https://opentdb.com/api_token.php?command=reset&token=YOURTOKENHERE```

## Response Codes


 -   Code 0: Success Returned results successfully.
 -   Code 1: No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
 -   Code 2: Invalid Parameter Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)
 -   Code 3: Token Not Found Session Token does not exist.
 -   Code 4: Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.
 -   Code 5: Rate Limit Too many requests have occurred. Each IP can only access the API once every 5 seconds.

## Encoding 
 -   Default Encoding (HTML Codes):
 -   Legacy URL Encoding:
 -   URL Encoding (RFC 3986):
 -   Base64 Encoding:

## API Tools

### Category Lookup:

```https://opentdb.com/api_category.php```

### Category Question Count Lookup: 

```https://opentdb.com/api_count.php?category=CATEGORY_ID_HERE```

#### Global Question Count Lookup: 

```https://opentdb.com/api_count_global.php```



 HINT:  
  - Only 1 Category can be requested per API Call. To get questions from any category, don't specify a category.
  - A Maximum of 50 Questions can be retrieved per call.

## Sequenzdiagramm API-Request bis Nutzung in der App

## Beispiel Response

### Ausschnitt JSON
```json
{
    "type":"multiple",
    "difficulty":"hard",
    "category":"Science &amp; Nature",
    "question":"What nucleotide pairs with guanine?",
    "correct_answer":"Cytosine",
    "incorrect_answers":["Thymine","Adenine","Uracil"]
}
```

### Behandlung der Response

1. Texte sind HTML kodiert und enthalten sog. HTML Entities (im Beispiel ```&amp;``` für <var>Ampersand</var> (```&```))
2. Korrekte und nicht korrekte Antworten sind getrennt

- ad 1: Verwendung von ```html.unescape()```
- ad 2: - Mergen der Antworten
        - Randomisierung der Reihenfolge

### Pythonische Therapie der Response
In <var>question</var> steht obige <var>JSON</var> Datenstruktur als <kbd>Dict</kbd>

Die Code Kommentare aus den Python-Quellen {hier: ```pyquiz/entity.py```} sind (wie immer) auf englisch.

```python
import random
import html
# ...
question["question"] = html.unescape(question["question"])

question["answers"] = question["incorrect_answers"]
question["answers"].append(question["correct_answer"])
question["question"] = html.unescape(question["question"])
# Unescape all answers
question["answers"] = list(map(lambda x: html.unescape(x), question["answers"]))
random.shuffle(question["answers"])  # get questions in a randomized order

```
So sieht die Datenstruktur (```dict```) nach der Kontextbehandlung aus:

```python
{
    'type': 'multiple', 
    'difficulty': 'hard', 
    'category': 'Science & Nature', 
    'question': 'What nucleotide pairs with guanine?', 
    'answer': 'Cytosine', 
    'incorrect_answers': ['Thymine', 'Adenine', 'Uracil']
    'answers': ['Adenine', 'Cytosine', 'Uracil', 'Thymine']
}
```