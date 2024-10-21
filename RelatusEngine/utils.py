def calculate_damage(strength, defense, modifier=0):
    return max(1, (strength + modifier) - defense)

def log_event(event):
    print(f"[LOG]: {event}")

def save_to_file(data, filepath):
    import json
    with open(filepath, 'w') as file:
        json.dump(data, file)

def load_from_file(filepath):
    import json
    with open(filepath, 'r') as file:
        return json.load(file)