# Εισαγωγή στην JSON (JavaScript Object Notation)

# Download and Install the Requests Module
# > pip install requests
import json

### Απο JSON σε Python ###

data = '''
[
    { 
        "id" : "001",
        "lang" : "Python",
        "name" : "Alex"
    },
    { 
        "id" : "002",
        "lang" : "TKinter",
        "name" : "Nick"
    },
    { 
        "id" : "003",
        "lang" : "JavaScript",
        "name" : "George"
    }
]'''

# Μετατροπή από JSON σε Dictionary
info = json.loads(data)

# Εκτύπωση αριθμού εγγραφών
print('User count:', len(info))
print('\n----------------\n')

# Εκτύπωση στοιχειων
for people in info:
    print('Name', people['name'])
    print('Id', people['id'])
    print('Language', people['lang'])
    print('\n----------------\n')


### Απο Python σε JSNO ###

# a Python Dictionary:
myfriend = {
  "name": "Nicolas",
  "age": 3,
  "city": "Faliro mou"
}

# Μεταγραφή σε JSON:
friend = json.dumps(myfriend)
print(friend)


### Ένα μικρό παράδειγμα ###
print('\n--- My API ---\n')

# επιτρέπει να στέλνουμε αιτήματα HTTP χρησιμοποιώντας την Python
import requests

jokes = requests.get('https://api.chucknorris.io/jokes/random')
jokes =jokes.text

myjoke = json.loads(jokes)

# Δημιουργία Dictionary:
print(myjoke["value"])
