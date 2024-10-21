from RelatusEngine.environment import Environment, Location
from RelatusEngine.npc import NPC
import pytest

class MockPlayer:
    def __init__(self):
        self.inventory = []
        self.currentLocation = None

    def add_to_inventory(self, item):
        self.inventory.append(item)

@pytest.fixture
def environment():
    return Environment()

@pytest.fixture
def location():
    gandalf_personality = {'kindness': 0.8, 'aggression': 0.2, 'trust': 0.5}
    gandalf = NPC(name="Gandalf", personality=gandalf_personality, attributes={'health': 100, 'strength': 5})
    
    return Location(
        name="Forest", 
        description="A dense and mysterious forest", 
        items=["sword", "shield"], 
        npcs=[gandalf], 
        weather="Sunny"
    )

@pytest.fixture
def player():
    return MockPlayer()

def test_add_location(environment, location):
    environment.add_location(location)
    assert "Forest" in environment.locations
    assert environment.get_location("Forest") == location

def test_get_location_not_found(environment):
    assert environment.get_location("NonExistent") is None

def test_enter_location(location, player):
    location.enter(player)
    assert player.currentLocation == "Forest"

def test_explore_location_with_items(location, player):
    result = location.explore(player)
    assert result == "Found sword in Forest!"
    assert "sword" in player.inventory
    result = location.explore(player)
    assert result == "Found shield in Forest!"
    assert "shield" in player.inventory

def test_explore_location_no_items(location, player):
    location.explore(player)
    location.explore(player)
    result = location.explore(player)
    assert result == "Nothing found here."

def test_add_remove_npc(location):
    assert any(npc.name == "Gandalf" for npc in location.npcs)
    
    frodo_personality = {'kindness': 0.7, 'aggression': 0.1, 'trust': 0.6}
    frodo = NPC(name="Frodo", personality=frodo_personality, attributes={'health': 80, 'strength': 3})
    
    location.add_npc(frodo)
    assert any(npc.name == "Frodo" for npc in location.npcs)

    location.remove_npc(location.npcs[0]) 
    assert not any(npc.name == "Gandalf" for npc in location.npcs)

def test_set_get_weather(location):
    assert location.get_weather() == "Sunny"
    result = location.set_weather("Rainy")
    assert result == "Set weather at Forest to Rainy."
    assert location.get_weather() == "Rainy"
