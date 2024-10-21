import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RelatusEngine.game import Game
from RelatusEngine.player import Player
from RelatusEngine.environment import Environment, Location
from RelatusEngine.story import Story, Quest, Objective
from RelatusEngine.npc import NPC

def main():
    player = Player(
        name="Percy Jackson",
        personality={
            "trust": 0.7,  # Percy tends to trust his close friends
            "loyalty": 0.9,  # Very loyal to those he cares about
            "kindness": 0.6,  # Percy has a good heart
            "aggression": 0.4,  # He can get aggressive in battles, but it's not his default nature
            "empathy": 0.8,  # He's empathetic to others’ struggles
            "cynicism": 0.2  # Not too cynical, usually hopeful
        },
        attributes={
            "strength": 7,  # Percy is physically strong due to his demigod nature
            "health": 120,  # Higher than average health
            "defense": 6,  # Decent defense in battles
            "mana": 80,  # This could represent his water-based abilities
            "speed": 5,  # Quick in battle
            "experience": 150,  # He's been through a lot of quests
            "level": 3,  # Percy's level in your game can be relatively advanced
            "next_level_xp": 300,  # XP needed to level up
            "inventory": ["Riptide", "Ambrosia", "Health Potion"]  # Items Percy carries
        }
    )
    zeus = NPC(
    name="Zeus",
    personality={
        "trust": 0.4,  # Zeus can be suspicious of others
        "loyalty": 0.6,  # Loyal to Olympus and his fellow gods
        "kindness": 0.5,  # Zeus can be just, but unpredictable
        "aggression": 0.8,  # Quick to anger and assert dominance
        "empathy": 0.3,  # Less empathetic to mortals
        "cynicism": 0.6  # Zeus tends to be cynical due to his experiences
    },
    attributes={
        "strength": 10,  # Zeus is incredibly powerful
        "defense": 9,  # Well defended, given his godly stature
        "health": 150,  # High health due to divine nature
        "mana": 100,  # Magical abilities representing thunderbolts
        "speed": 6  # Quick but not the fastest god
    }
)

    athena = NPC(
        name="Athena",
        personality={
            "trust": 0.8,  # Trusts wise and just people
            "loyalty": 0.9,  # Deeply loyal to her ideals and justice
            "kindness": 0.7,  # Kind and fair in her judgment
            "aggression": 0.3,  # Rarely aggressive, only in battle for justice
            "empathy": 0.9,  # Highly empathetic to those in need of wisdom
            "cynicism": 0.2  # Not cynical, believes in the power of wisdom
        },
        attributes={
            "strength": 7,  # Strong, but more mentally than physically
            "defense": 8,  # Strong defenses
            "health": 120,  # High, but not the highest
            "mana": 90,  # Uses magical abilities and wisdom in combat
            "speed": 5  # More focused on strategy than speed
        }
    )

    poseidon = NPC(
        name="Poseidon",
        personality={
            "trust": 0.5,  # Trusts, but can be volatile
            "loyalty": 0.8,  # Loyal to family but often has his own agenda
            "kindness": 0.6,  # Can be kind but is also easily angered
            "aggression": 0.7,  # Tends to be aggressive in battles, especially at sea
            "empathy": 0.4,  # Empathetic, but not overly so
            "cynicism": 0.5  # Slightly cynical due to rivalry with other gods
        },
        attributes={
            "strength": 9,  # Strong due to his control of the sea
            "defense": 8,  # Well defended by the power of the ocean
            "health": 140,  # Strong health
            "mana": 95,  # Uses water-based abilities
            "speed": 6  # Agile in water
        }
    )

    mtOlympus = Location(
        name="Mt. Olympus",
        description="Perched high above the mortal world, Mount Olympus is the home of the Greek gods. Towering clouds surround its shimmering peaks, hiding the entrance to the gods' domain. The air here is filled with divine energy, and the towering gates of the Olympian palace gleam in gold and marble. Statues of the gods line the grand hallways, each radiating power and presence.",
        items = [],
        npcs = [zeus, poseidon, athena],
        weather = "Sunny"
    )
    environment = Environment()
    environment.add_location(mtOlympus)

    story = Story()

    quest1_objective1 = Objective(description="Speak with Zeus", completionStatus=False)
    quest1_objective2 = Objective(description="Gain Zeus' favor", completionStatus=False)
    quest2_objective1 = Objective(description="Speak with Poseidon", completionStatus=False)

    quest1 = Quest(
        name="Zeus' Favor",
        description="Gain the favor of Zeus by interacting with him.",
        objectives=[quest1_objective1, quest1_objective2]
    )
    
    quest2 = Quest(
        name="Poseidon's Test",
        description="Speak with Poseidon and pass his test of strength.",
        objectives=[quest2_objective1]
    )

    story.add_quest(quest1)
    story.add_quest(quest2)

    game = Game()
    
    game.initialize_game(player, environment, story)
    game.main_loop()

if __name__ == "__main__":
    main()
