import random

class SnakeLadderGame:
    def __init__(self):
        self.board_size = 100
        self.player_position = 0  # Single player starts at position 0
        self.options = ["No Play", "Ladder", "Snake"]  # Possible events

    def start_game(self):
        print("Game initialized. Player starts at position 0.")

    def roll_dice(self):  
        dice_value = random.randint(1, 6)  # Generate a number between 1 and 6
        print(f"Player rolled a {dice_value}")
        return dice_value

    def move_player(self):
        dice_value = self.roll_dice()
        event = random.choice(self.options)  # Randomly select an event
        print(f"Event: {event}")

        if event == "No Play":
            print("No Play! Player stays at the same position.")
        elif event == "Ladder":
            self.player_position += dice_value
            print(f"Ladder! Moving ahead by {dice_value} steps.")
        elif event == "Snake":
            self.player_position = max(0, self.player_position - dice_value)  # Prevent negative position
            print(f"Snake! Moving back by {dice_value} steps.")

        print(f"Player is now at position {self.player_position}")

# Start the game
game = SnakeLadderGame()
game.start_game()

# Simulate one turn where the player rolls the dice and moves
game.move_player()
