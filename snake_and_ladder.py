import random

class SnakeLadderGame:
    def __init__(self):
        self.board_size = 100
        self.players = {"Player 1": 0, "Player 2": 0}  # Both players start at position 0
        self.options = ["No Play", "Ladder", "Snake"]  # Possible events
        self.dice_roll_count = {"Player 1": 0, "Player 2": 0}  # Track dice rolls for each player

    def start_game(self):
        print("Game initialized. Both players start at position 0.\n")

    def roll_dice(self):
        dice_value = random.randint(1, 6)  # Generate a number between 1 and 6
        self.dice_roll_count[player] += 1  # Increment dice roll count for the player
        print(f"{player} rolled a {dice_value}")
        return dice_value

    def move_player(self, player):
        dice_value = self.roll_dice(player)
        event = random.choice(self.options)  # Randomly select an event
        print(f"Event: {event}")

        if event == "No Play":
            print(f"{player} stays at position {self.players[player]}.")
        elif event == "Ladder":
            new_position = self.players[player] + dice_value
            if new_position <= self.board_size:  # Move only if within bounds
                self.players[player] = new_position
                print(f"{player} climbed a Ladder! Moving ahead by {dice_value} steps.")
            else:
                print(f"{player}'s roll exceeds 100! Staying at {self.players[player]}.")
        elif event == "Snake":
            self.players[player] -= dice_value  # Move back
            if self.players[player] < 0:  # Restart from 0 if below 0
                self.players[player] = 0
                print(f"{player} fell below 0! Restarting from position 0.")
            else:
                print(f"{player} got bitten by a Snake! Moving back by {dice_value} steps.")

        print(f"{player} is now at position {self.players[player]}\n")

    def play_game(self):
        while True:  # Keep playing until one player reaches position 100
            for player in self.players:
                self.move_player(player)
                if self.players[player] == self.board_size:
                    print(f"{player} wins the game in {self.dice_roll_count[player]} rolls!")
                    return  # End game when a player reaches position 100

# Start the game
game = SnakeLadderGame()
game.start_game()
game.play_game()  # Keep playing until one player reaches 100
