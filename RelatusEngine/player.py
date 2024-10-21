import RelatusEngine.npc as npc
import json

class Player:
    def __init__(self, name, personality, attributes, currentLocation = None):
        self.name = name
        self.personality = personality
        self.attributes = attributes 
        self.currentLocation = currentLocation

    def relationshipTo(self, extCharacter):
        relationship_value = 0
        if self.personality['trust'] > 0.7 and extCharacter['trust'] > 0.7:
            relationship_value += 10
        if self.personality['loyalty'] > 0.5 and extCharacter['loyalty'] > 0.5:
            relationship_value += 5
        if extCharacter['aggression'] > 0.5:
            relationship_value -= 3
        if extCharacter['cynicism'] > 0.5:
            relationship_value -= 2
        if relationship_value > 10:
            return "strong relationship"
        elif relationship_value > 5:
            return "neutral relationship"
        else:
            return "strained relationship"
    
    def speak(self, dialogue, npc):
        npc_response = npc.sayTo(dialogue)
        return npc_response['mood'], npc_response['personality']
    
    def attack(self, npc, damageModifier=0):

        player_strength = self.attributes.get('strength', 1)
        npc_defense = npc.attributes.get('defense', 0)
        
        damage = (2 + player_strength + damageModifier) - npc_defense
        damage = max(1, damage)  


        npc.attributes['health'] = max(npc.attributes.get('health', 100) - damage, 0)

        npc.personality['aggression'] = min(npc.personality.get('aggression', 0) + 0.3, 1.0)

        npc.personality['trust'] = max(npc.personality.get('trust', 0) - 0.2, 0)

        if npc.personality['aggression'] > 0.7:
            npc.mood = "angry"
        else:
            npc.mood = "neutral"

        return {
            'mood': npc.mood,
            'personality': npc.personality,
            'remaining_health': npc.attributes['health']
        }
    
    def defend(self, npc, damage):
        player_defense = self.attributes.get('defense', 0)
        total_damage = max(damage - player_defense, 1)

        self.attributes['health'] = max(self.attributes.get('health', 100) - total_damage, 0)

        self.personality['aggression'] = min(self.personality.get('aggression', 0) + 0.1, 1.0)

        if self.attributes['health'] <= 0:
            return "Player has been defeated"
        return {
            'remaining_health': self.attributes['health']
        }
    
    def add_to_inventory(self, item):
        if 'inventory' not in self.attributes:
            self.attributes['inventory'] = []
        self.attributes['inventory'].append(item)

    def use_item(self, item):
        if item in self.attributes.get('inventory', []):
            if item == 'health_potion':
                self.attributes['health'] = min(self.attributes.get('health', 100) + 20, 100)
            if item == 'mana_potion':
                self.attributes['mana'] = min(self.attributes.get('mana', 100) + 30, 100)
            if item == 'stamina_potion':
                self.attributes['stamina'] = min(self.attributes.get('stamina', 100) + 25, 100)
            if item == 'strength_booster':
                self.attributes['strength'] += 2
            if item == 'defense_elixir':
                self.attributes['defense'] = min(self.attributes.get('defense', 50) + 5, 50)
            if item == 'speed_potion':
                self.attributes['speed'] = min(self.attributes.get('speed', 50) + 5, 50)
            if item == 'lockpick':
                return "Used lockpick to open a door or chest"
            if item == 'torch':
                return "You light the torch and can now see your surroundings"            
            self.attributes['inventory'].remove(item)
            return f"Used {item}"
        return f"{item} not found in inventory"

    def level_up(self, xp_earned):
        self.attributes['experience'] = self.attributes.get('experience', 0) + xp_earned

        if self.attributes['experience'] >= self.attributes.get('next_level_xp', 100):
            self.attributes['level'] = self.attributes.get('level', 1) + 1
            self.attributes['strength'] = self.attributes.get('strength', 1) + 1
            self.attributes['health'] = min(self.attributes.get('health', 100) + 10, 100)
            self.attributes['next_level_xp'] = self.attributes['next_level_xp'] * 1.5
            return f"Level up! You are now level {self.attributes['level']}"
        return "XP added"

    def speak_with_tone(self, dialogue, npc, tone):
        if tone == 'friendly':
            sentiment_modifier = 0.2
        elif tone == 'aggressive':
            sentiment_modifier = -0.35
        elif tone == 'sarcastic':
            sentiment_modifier = -0.25
        elif tone == 'extremelyAggressive':
            sentiment_modifier = -0.9
        else:
            sentiment_modifier = 0
        npc_response = npc.sayTo(dialogue, sentiment_modifier=sentiment_modifier)
        return npc_response['mood'], npc_response['personality']
    
    def save(self, filepath):
        with open(filepath, 'w') as file:
            json.dump(self.attributes, file)
        return "Player state saved!"

    def load(self, filepath):
        with open(filepath, 'r') as file:
            self.attributes = json.load(file)
        return "Player state loaded!"
