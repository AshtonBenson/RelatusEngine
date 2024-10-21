import pytest
from RelatusEngine.player import Player
from RelatusEngine.npc import NPC 

@pytest.fixture
def player():
    personality = {
        'kindness': 0.5,
        'aggression': 0.2,
        'trust': 0.5,
        'empathy': 0.3,
        'loyalty': 0.3
    }
    attributes = {
        'strength': 5,
        'defense': 3,
        'health': 100,
        'experience': 50,
        'next_level_xp': 100,
        'inventory': []
    }
    return Player(name="Legolas", personality=personality, attributes=attributes)

@pytest.fixture
def npc():
    personality = {
        'kindness': 0.3,
        'aggression': 0.5,
        'trust': 0.3,
        'cynicism': 0.4,
        'loyalty': 0.2
    }
    attributes = {
        'strength': 3,
        'defense': 2,
        'health': 100
    }
    return NPC(name="Sauron", personality=personality, attributes=attributes)

def test_relationshipTo(player, npc):
    relationship = player.relationshipTo(npc.personality)
    assert relationship == "strained relationship"

def test_speak(player, npc):
    mood, npc_personality = player.speak("Hello there!", npc)
    assert mood == "neutral"  
    assert isinstance(npc_personality, dict)

def test_attack(player, npc):
    result = player.attack(npc)
    assert result['remaining_health'] < 100
    assert result['mood'] == "neutral" or result['mood'] == "angry"
    assert result['personality']['aggression'] > 0.5 

def test_defend(player, npc):
    damage = 10
    result = player.defend(npc, damage)
    assert result['remaining_health'] < 100
    assert player.attributes['health'] > 0

def test_add_to_inventory(player):
    player.add_to_inventory("health_potion")
    assert "health_potion" in player.attributes['inventory']

def test_use_item(player):
    player.add_to_inventory("health_potion")
    player.attributes['health'] = 50
    result = player.use_item("health_potion")
    assert player.attributes['health'] == 70
    assert result == "Used health_potion"

def test_use_item_not_in_inventory(player):
    result = player.use_item("mana_potion")
    assert result == "mana_potion not found in inventory"

def test_level_up(player):
    result = player.level_up(60) 
    assert player.attributes['level'] == 2 
    assert player.attributes['strength'] == 6
    assert player.attributes['health'] == 100
    assert "Level up!" in result

def test_speak_with_tone(player, npc):
    mood, npc_personality = player.speak_with_tone("Hello!", npc, 'friendly')
    assert mood == "friendly" or mood == "neutral"