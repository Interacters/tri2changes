import random, json, os, fcntl
from flask import current_app

performance_jokes = [
    {"category": "Grammar", "joke": "I before E, except when you feisty neighbor Keith receives eight counterfeit beige sleighs from caffeinated weightlifters. Weird.", "level": 1},
    {"category": "Writing", "joke": "Why did the writer break up with their outline? It wasn't their type!", "level": 2},
    {"category": "Reading", "joke": "I told my book I needed space. Now it won't stop giving me margins.", "level": 3},
    {"category": "Vocabulary", "joke": "What's a thesaurus's favorite dessert? Synonym rolls!", "level": 1},
    {"category": "Essays", "joke": "My essay and I are in a complicated relationship. It has too many issues.", "level": 2},
    {"category": "Analysis", "joke": "Why don't English teachers trust atoms? Because they make up everything!", "level": 3},
    {"category": "Citations", "joke": "I cited Wikipedia once. My teacher said that's not a proper source. I cited my disappointment.", "level": 2},
    {"category": "Editing", "joke": "Editing is like doing your own dental work - painful but necessary.", "level": 1},
    {"category": "Research", "joke": "99% of research is finding credible sources. The other 1% is remembering where you found them.", "level": 4},
    {"category": "Critical Thinking", "joke": "I think critically, therefore I am... confused.", "level": 5},
    {"category": "Punctuation", "joke": "A comma splice walks into a bar, it has a drink and then leaves.", "level": 1},
    {"category": "Shakespeare", "joke": "What's Shakespeare's favorite breakfast? Omelette! (Hamlet)", "level": 3},
    {"category": "Poetry", "joke": "Roses are red, violets are blue, poems are hard, and essays are too.", "level": 2},
    {"category": "Grammar", "joke": "Why was the comma feeling lonely? It was between two independent clauses!", "level": 1},
    {"category": "Writing", "joke": "Writer's block: when your brain and your hands hold separate meetings.", "level": 2}
]

def get_jokes_file():
    data_folder = current_app.config['DATA_FOLDER']
    return os.path.join(data_folder, 'performance_jokes.json')

def _read_jokes_file():
    JOKES_FILE = get_jokes_file()
    if not os.path.exists(JOKES_FILE):
        return []
    with open(JOKES_FILE, 'r') as f:
        fcntl.flock(f, fcntl.LOCK_SH)
        try:
            data = json.load(f)
        except Exception:
            data = []
        fcntl.flock(f, fcntl.LOCK_UN)
    return data

def _write_jokes_file(data):
    JOKES_FILE = get_jokes_file()
    with open(JOKES_FILE, 'w') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        json.dump(data, f)
        fcntl.flock(f, fcntl.LOCK_UN)

def initPerformanceJokes():
    JOKES_FILE = get_jokes_file()
    if os.path.exists(JOKES_FILE):
        return
    jokes_data = []
    item_id = 0
    for item in performance_jokes:
        jokes_data.append({
            "id": item_id, 
            "category": item["category"],
            "joke": item["joke"], 
            "level": item["level"],
            "haha": 0, 
            "boohoo": 0
        })
        item_id += 1
    # Prime some responses
    for i in range(10):
        id = random.randint(0, len(jokes_data) - 1)
        jokes_data[id]['haha'] += 1
    for i in range(3):
        id = random.randint(0, len(jokes_data) - 1)
        jokes_data[id]['boohoo'] += 1
    _write_jokes_file(jokes_data)

def getJokes():
    return _read_jokes_file()

def getJoke(id):
    jokes = _read_jokes_file()
    return jokes[id] if id < len(jokes) else None

def getJokesByLevel(level):
    jokes = _read_jokes_file()
    return [joke for joke in jokes if joke['level'] == level]

def getRandomJoke():
    jokes = _read_jokes_file()
    return random.choice(jokes) if jokes else None

def favoriteJoke():
    jokes = _read_jokes_file()
    best = 0
    bestID = -1
    for joke in jokes:
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return jokes[bestID] if bestID != -1 else None

def _vote_joke(id, field):
    JOKES_FILE = get_jokes_file()
    with open(JOKES_FILE, 'r+') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        jokes = json.load(f)
        if id < len(jokes):
            jokes[id][field] += 1
        f.seek(0)
        json.dump(jokes, f)
        f.truncate()
        fcntl.flock(f, fcntl.LOCK_UN)
    return jokes[id][field] if id < len(jokes) else 0

def addJokeHaHa(id):
    return _vote_joke(id, 'haha')

def addJokeBooHoo(id):
    return _vote_joke(id, 'boohoo')

def countJokes():
    jokes = _read_jokes_file()
    return len(jokes)