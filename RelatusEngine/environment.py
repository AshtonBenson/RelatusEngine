import RelatusEngine.player as Player

class Environment:
    def __init__(self):
        self.locations = {}
    
    def add_location(self, location):
        self.locations[location.name] = location

    def get_location(self, name):
        return self.locations.get(name, None)

    def get_current_location(self, player):
        return self.get_location(player.currentLocation)
    
    def move_player(self, player, location_name):
        location = self.get_location(location_name)
        if location:
            location.enter(player)
            print(f"Moved to {location_name}")
        else:
            print(f"Location {location_name} does not exist.")

    def get_npc_in_location(self, player, npc_name):
        current_location = self.get_current_location(player)
        for npc in current_location.npcs:
            if npc.name == npc_name:
                return npc
        return None

class Location:
    def __init__(self, name, description, items=None, npcs=None, weather=None):
        self.name = name
        self.description = description
        self.items = items
        self.npcs = npcs
        self.weather = weather
    
    def enter(self, player):
        npc_names = [npc.name for npc in self.npcs]
        print(f"Player enters {self.name}. {self.description} NPCs in this location: {', '.join(npc_names)}.")
        player.currentLocation = self.name
    
    def explore(self, player):
        if self.items:
            found_item = self.items.pop(0)
            player.add_to_inventory(found_item)
            return f"Found {found_item} in {self.name}!"
        return "Nothing found here."
    
    def add_npc(self, npc):
        self.npcs.append(npc)
    
    def remove_npc(self, npc):
        self.npcs.remove(npc)

    def get_weather(self):
        return self.weather
    
    def set_weather(self, weather):
        self.weather = weather
        return f"Set weather at {self.name} to {weather}."