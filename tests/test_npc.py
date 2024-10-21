from RelatusEngine.npc import NPC

def test_npc_with_high_kindness():
    personality = {
        'kindness': 0.8,
        'aggression': 0.2,
        'trust': 0.5
    }
    attributes = {
        'health': 100,
        'strength': 5,
        'defense': 3
    }
    npc = NPC(name="Gandalf", personality=personality, attributes=attributes)

    response = npc.interpret_sentiment(0.5)
    assert response['mood'] == "friendly"

    response = npc.interpret_sentiment(-0.5)
    assert response['mood'] == "neutral"

def test_npc_with_high_aggression():
    personality = {
        'kindness': 0.2,
        'aggression': 0.9,
        'trust': 0.3
    }
    attributes = {
        'health': 100,
        'strength': 7,
        'defense': 2
    }
    npc = NPC(name="Sauron", personality=personality, attributes=attributes)

    response = npc.interpret_sentiment(-0.5)
    assert response['mood'] == "angry"

    response = npc.interpret_sentiment(0.5)
    assert response['mood'] == "neutral"

def test_npc_with_high_trust():
    personality = {
        'kindness': 0.4,
        'aggression': 0.1,
        'trust': 0.9
    }
    attributes = {
        'health': 80,
        'strength': 3,
        'defense': 4
    }
    npc = NPC(name="Arwen", personality=personality, attributes=attributes)

    response = npc.interpret_sentiment(0.0)
    assert response['mood'] == "friendly"

    response = npc.interpret_sentiment(-0.3)
    assert response['mood'] == "neutral"

def test_npc_with_high_cynicism():
    personality = {
        'kindness': 0.3,
        'aggression': 0.2,
        'cynicism': 0.8
    }
    attributes = {
        'health': 90,
        'strength': 4,
        'defense': 2
    }
    npc = NPC(name="Saruman", personality=personality, attributes=attributes)

    response = npc.interpret_sentiment(0.7)
    assert response['mood'] == "neutral"

    response = npc.interpret_sentiment(0.0)
    assert response['mood'] == "neutral"

def test_npc_with_high_empathy():
    personality = {
        'kindness': 0.7,
        'empathy': 0.9,
        'aggression': 0.1
    }
    attributes = {
        'health': 85,
        'strength': 3,
        'defense': 3
    }
    npc = NPC(name="Frodo", personality=personality, attributes=attributes)

    response = npc.interpret_sentiment(-0.8)
    assert response['mood'] == "neutral"

    response = npc.interpret_sentiment(0.5)
    assert response['mood'] == "friendly"

def test_npc_sayTo_updates_personality():
    personality = {
        'kindness': 0.5,
        'aggression': 0.2,
        'trust': 0.5,
        'empathy': 0.3,
        'loyalty': 0.3
    }
    attributes = {
        'health': 100,
        'strength': 5,
        'defense': 3
    }
    npc = NPC(name="Legolas", personality=personality, attributes=attributes)

    dialogue = "You are amazing, Legolas!"
    initial_trust = npc.personality['trust']
    initial_loyalty = npc.personality['loyalty']
    
    response = npc.sayTo(dialogue)

    assert response['mood'] == "friendly"
    assert npc.personality['trust'] > initial_trust 
    assert npc.personality['loyalty'] > initial_loyalty 

    dialogue = "I hate you."
    initial_trust = npc.personality['trust']
    initial_loyalty = npc.personality['loyalty']
    
    response = npc.sayTo(dialogue)

    assert response['mood'] == "neutral" 
    assert npc.personality['trust'] < initial_trust 
    assert npc.personality['loyalty'] < initial_loyalty 
