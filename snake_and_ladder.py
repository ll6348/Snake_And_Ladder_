import random

class SnakeLadderGame:
    def __init__(self):
        self.board_size = 100
        self.player_position = 0  # Single player starts at position 0

    def start_game(self):
        print("Game initialized. Player starts at position 0.")

# Start the game
game = SnakeLadderGame()
game.start_game()
