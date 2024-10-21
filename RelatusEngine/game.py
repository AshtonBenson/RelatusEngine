from RelatusEngine.environment import Environment, Location
from RelatusEngine.story import Story
from RelatusEngine.player import Player

class Game:
    def __init__(self):
        self.player = None
        self.environment = None
        self.story = None
        self.running = True

    def initialize_game(self, player, environment, story):
        self.player = player
        self.environment = environment
        self.story = story
        print("Game initialized. Ready to start!")
        self.environment.move_player(player, list(self.environment.locations.keys())[0]) 
    
    def main_loop(self):
        while self.running:
            action = self.get_player_input()
            self.process_input(action)
            self.story.progress_story(self.player)
    
    def get_player_input(self):
        return input("Enter action: (explore/move/talk/quit): ")
    
    def process_input(self, action):
        if action == "explore":
            current_location = self.environment.get_current_location(self.player)
            result = current_location.explore(self.player)
            print(result)
        elif action == "move":
            location_name = input("Where do you want to move? ")
            self.environment.move_player(self.player, location_name)
        elif action == "talk":
            npc_name = input("Who do you want to talk to? ")
            npc = self.environment.get_npc_in_location(self.player, npc_name)
            if npc:
                dialogue = input(f"What do you want to say to {npc_name}? ")
                npc_response = npc.sayTo(dialogue)
                print(f"{npc.name} responds: {npc_response['mood']}")
                print(f"Suggested action: {npc_response['suggested_action']}")
            else:
                print(f"No such NPC named {npc_name} here.")
        elif action == "quit":
            self.quit_game()
        else:
            print("Invalid action.")

    
    def quit_game(self):
        self.running = False
        print("Game ended.")
