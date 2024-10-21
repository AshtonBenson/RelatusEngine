class Objective:
    def __init__(self, description, completionStatus):
        self.description = description
        self.completionStatus = completionStatus
    
    def is_completed(self, player):
        return self.completionStatus

class Quest:
    def __init__(self, name, description, objectives):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.completed = False
    
    def check_completion(self, player):
        for objective in self.objectives:
            if not objective.is_completed(player):
                return False
        self.completed = True
        return True

class Story:
    def __init__(self):
        self.active_quests = []
        self.completed_quests = []
    
    def add_quest(self, quest):
        self.active_quests.append(quest)
    
    def progress_story(self, player):
        for quest in self.active_quests:
            if quest.check_completion(player):
                self.complete_quest(quest)
    
    def complete_quest(self, quest):
        self.active_quests.remove(quest)
        self.completed_quests.append(quest)
        print(f"Quest {quest.name} completed!")
    
    def trigger_event(self, event_name):
        # Developers can create custom story events that occur based on player actions
        print(f"Story event triggered: {event_name}")
