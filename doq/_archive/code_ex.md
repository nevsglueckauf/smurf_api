# Beispiele in Codes

## Abfrage der API 

```python
import pyquiz.api

api = pyquiz.api.OTDBApi()
# Hole 8 Fragen ('zufällig' - ohne weitere Parametrisierung)
api.get_questions_raw(8)
```

```
{   'category': 'Entertainment: Music',
    'correct_answer': 'Thriller',
    'difficulty': 'hard',
    'incorrect_answers': ['Dangerous', 'Bad', 'Off the Wall'],
    'question': 'Which of Michael Jackson&#039;s albums sold the most copies?',
    'type': 'multiple'}
```



## Fragenkatalog filtern

```python
df_fil = df.filter_by('Category').equals('History')
```