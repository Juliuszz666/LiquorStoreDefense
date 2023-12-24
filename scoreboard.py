import json

def update_scoreboard(user_score):
    try:
        with open('scoreboard.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
        
    new_entry = {'USER': "Julian", 'SCORE': user_score}
    data.append(new_entry)

    with open('scoreboard.json', 'w') as file:
        json.dump(data, file, indent=2)
        
def load_scoreboard():
    try:
        with open('scoreboard.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data