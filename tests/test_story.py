import pytest
from RelatusEngine.story import Story, Quest

class MockObjective:
    def __init__(self, completed=False):
        self.completed = completed

    def is_completed(self, player):
        return self.completed

class MockPlayer:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def player():
    return MockPlayer(name="TestPlayer")

@pytest.fixture
def story():
    return Story()

def test_quest_initialization():
    objective1 = MockObjective(completed=False)
    quest = Quest(name="Find the Sword", description="Retrieve the legendary sword.", objectives=[objective1])
    
    assert quest.name == "Find the Sword"
    assert quest.description == "Retrieve the legendary sword."
    assert len(quest.objectives) == 1
    assert not quest.completed

def test_quest_completion(player):
    objective1 = MockObjective(completed=False)
    objective2 = MockObjective(completed=True)
    quest = Quest(name="Test Quest", description="Complete objectives.", objectives=[objective1, objective2])
    
    assert not quest.check_completion(player)
    assert not quest.completed

    objective1.completed = True
    
    assert quest.check_completion(player)
    assert quest.completed

def test_story_progression(player, story):
    objective1 = MockObjective(completed=True)
    objective2 = MockObjective(completed=False)
    quest1 = Quest(name="First Quest", description="First test quest", objectives=[objective1])
    quest2 = Quest(name="Second Quest", description="Second test quest", objectives=[objective2])

    story.add_quest(quest1)
    story.add_quest(quest2)

    assert len(story.active_quests) == 2
    assert quest1 in story.active_quests
    assert quest2 in story.active_quests

    story.progress_story(player)
    
    assert len(story.completed_quests) == 1
    assert quest1 in story.completed_quests
    assert quest2 in story.active_quests

    objective2.completed = True
    story.progress_story(player)

    assert len(story.completed_quests) == 2
    assert quest2 in story.completed_quests
    assert len(story.active_quests) == 0

def test_trigger_event(story):
    event_name = "npc_joined_party"
    story.trigger_event(event_name)
