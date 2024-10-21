# RelatusEngine

A barebone and adaptable game engine for creating dynamic role-playing games (RPGs) that focus on the dynamic relationships between players and NPCs. The engine provides flexibility for developers to build immersive stories where the personality, attributes, and interactions of characters evolve over time, enabling relationship tracking that affects gameplay.

## Features

- Dynamic Player-NPC Interactions: Track and adapt relationships between players and NPCs based on customizable personality traits.
- Customizable Environment and Quests: Easily define game environments, locations, quests, and objectives.
- Extensible Design: The engine is built with flexibility in mind, allowing developers to easily extend or modify behavior to fit their specific game world.
- Story-Driven Quests: Build interactive and multi-stage quests where player actions and decisions influence the outcome.

## Getting Started
### Prerequisites

- Python 3.x

All other dependencies are listed in the `requirements.txt` file.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AshtonBenson/RelatusEngine.git
cd RelatusEngine
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

### Running the Game
An example run_game.py script is provided to demonstrate how to set up and run the game using the engine.

To run the example:
```bash
python examples/run_game.py
```

This script sets up a basic RPG scenario involving the player and NPCs such as Zeus, Athena, and Poseidon, along with defined locations and quests.

### Game Setup
The game consists of several main components:

1. Player: Represents the main character controlled by the player. Personality traits such as trust, loyalty, aggression, and attributes like strength, health, and speed can be customized.

**Example**:
```python
player = Player(
    name="Percy Jackson",
    personality={
        "trust": 0.7,
        "loyalty": 0.9,
        "kindness": 0.6,
        "aggression": 0.4,
        "empathy": 0.8,
        "cynicism": 0.2
    },
    attributes={
        "strength": 7,
        "health": 120,
        "defense": 6,
        "mana": 80,
        "speed": 5,
        "experience": 150,
        "level": 3,
        "next_level_xp": 300,
        "inventory": ["Riptide", "Ambrosia", "Health Potion"]
    }
)
```

2. NPCs: Non-player characters (NPCs) who interact with the player. Each NPC can have personality traits and attributes similar to the player.

**Example**:
```python
zeus = NPC(
name="Zeus",
    personality={
        "trust": 0.4,
        "loyalty": 0.6,
        "kindness": 0.5,
        "aggression": 0.8,
        "empathy": 0.3,
        "cynicism": 0.6
    },
    attributes={
        "strength": 10,
        "defense": 9,
        "health": 150,
        "mana": 100,
        "speed": 6
    }
)
```

3. Environment: Contains the various locations where the game takes place. Each location can host NPCs, items, and be part of quests.

**Example**:
```python
mtOlympus = Location(
    name="Mt. Olympus",
    description="Home of the Greek gods...",
    items=[],
    npcs=[zeus, athena, poseidon],
    weather="Sunny"
)
```

4. Story and Quests: Define the narrative and objectives of the game. Quests consist of multiple objectives, which the player must complete to progress.

**Example**:
```python
quest1 = Quest(
    name="Zeus' Favor",
    description="Gain the favor of Zeus by interacting with him.",
    objectives=[Objective(description="Speak with Zeus", completionStatus=False)]
)
```

## Example Usage
An example of the main game loop is included in run_game.py. This script demonstrates how to:
1. Create the player and NPCs.
2. Set up the environment (locations, NPCs).
3. Define a storyline with quests.
4. Run the game using the Game class's main_loop() method.

## Folder Structure

`examples/`: This directory contains example scripts demonstrating how to use the engine.
- `run_game.py`: Example script for setting up and running a game.

`RelatusEngine/`: This directory contains the core engine code.
- `__init__.py`: Initialization file for the RelatusEngine package.
- `environment.py`: Handles the game’s locations, weather, and environmental setup.
- `game.py`: Contains the core game logic and the main game loop.
- `nlp.py`: Uses TextBlob for sentiment analysis, analyzing player input and adjusting NPC mood and responses accordingly based on the sentiment score (e.g., positive or negative dialogue influencing NPC trust or aggression).
- `npc.py`: Defines NPC attributes and personality traits.
- `player.py`: Defines the player’s attributes and personality.
- `story.py`: Manages quests, objectives, and overall story progression.
- `utils.py`: Helper functions for various game tasks.

`tests/`: This directory contains test scripts for verifying functionality.

`README.md`: The documentation file you're reading.

`requirements.txt`: Lists the dependencies required for the project.

`setup.py`: Python setup file for packaging the project.

`LICENSE`: License file that specifies the terms under which the project is distributed.

## Running Tests
To run the test suite, use the following command:
```bash
py -m pytest
```

## Future Plans
1. **Simplified Event System**
- **Elaboration**: Introduce a minimal event system where player actions can trigger specific events (e.g., dialogue responses, environmental changes, quest updates). This will allow developers to set simple triggers and conditions without needing to write complex logic.
2. **Relationship Decay and Influence**
- **Elaboration**: Implement a basic relationship decay system, where NPC relationships with the player change over time based on interaction frequency and decisions. Add a simple influence system where NPCs can affect each other's relationships with the player.
3. **Environmental Effects on Combat/Dialogue**
- **Elaboration**: Add simple environmental modifiers that can influence combat or dialogue. For example, if the player is in a dark room and doesn’t have a torch, they may suffer a combat penalty or receive dialogue penalties when interacting with NPCs.
4. **Simple AI Behavior Customization**
- **Elaboration**: Allow developers to define basic AI behaviors for NPCs, such as following or attacking the player based on mood, relationship, or quest state. This would add more dynamism to NPC actions based on the game state.

## Contributing
1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Submit a pull request for review.

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.
