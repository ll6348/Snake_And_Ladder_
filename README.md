# Snake and Ladder Game

## Overview
This is a simple **Snake and Ladder** game implemented in Python for two players. The game continues until one of the players reaches the **winning position (100)**.

## Features
- Two players take turns rolling a **six-sided die (1-6)**.
- Players may encounter **No Play, Ladder, or Snake** events:
  - **No Play**: The player stays at the same position.
  - **Ladder**: The player moves forward by the rolled dice value.
  - **Snake**: The player moves backward by the rolled dice value.
- Players must land exactly on position **100** to win.
- If a player moves below position **0**, they restart from position **0**.
- The program keeps track of the **number of dice rolls** for each player.

## How to Play
1. Run the script in Python.
2. The game starts with **both players at position 0**.
3. Each player rolls the die and moves accordingly.
4. The game continues until one player **exactly reaches 100**.
5. The winner and the number of dice rolls taken are displayed at the end.

## Installation
No additional libraries are required. The game runs with Python's built-in `random` module.

### To run the game:
```sh
python snake_ladder.py
```

## Code Structure
- `SnakeLadderGame`: The main class that manages the game.
- `start_game()`: Initializes the game.
- `roll_dice()`: Rolls the dice and returns a random number between 1-6.
- `move_player(player)`: Moves the player based on dice roll and event type.
- `play_game()`: Runs the game loop until a player reaches 100.

## Example Output
```
Game initialized. Both players start at position 0.

Player 1 rolled a 4
Event: Ladder
Player 1 climbed a Ladder! Moving ahead by 4 steps.
Player 1 is now at position 4

Player 2 rolled a 2
Event: No Play
Player 2 stays at position 0.

... (Game continues) ...

Player 1 wins the game in 25 rolls!
```






