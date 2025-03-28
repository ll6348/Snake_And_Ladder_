import random

class SnakeLadderGame:
    def __init__(self):
        self.board_size = 100
        self.player_position = 0  # Single player starts at position 0

    def start_game(self):
        print("Game initialized. Player starts at position 0.")

    def roll_dice(self): 
        dice_value = random.randint(1, 6)  # Generate a number between 1 and 6
        print(f"Player rolled a {dice_value}")
        return dice_value

# Start the game
game = SnakeLadderGame()
game.start_game()
game.roll_dice()  # Player rolls the dice when prompted
