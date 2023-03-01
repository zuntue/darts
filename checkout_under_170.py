# We're trying to create a summary table of each player's average check out shot count from a score of 170 oar below.
# The table will have each player as a row and one column with the average check out shot count from  170 or below.

# Sample data of players and their scores
players = {
    "Player 1": [170, 100, 80, 60, 40, 20],
    "Player 2": [170, 150, 120, 50, 30],
    "Player 3": [170, 140, 90, 80, 40, 30],
    "Player 4": [170, 130, 70, 60, 20],
    "Player 5": [170, 160, 130, 120, 70, 20],
}

# Function to calculate the average checkout shot count for each player
def calculate_average_shots_to_checkout(player):
    checkout_count = 0
    total_score = None
    if total_score <= 170:
        checkout_count += 1

        # TODO: add looping to find remaining shots by the player before either they checkout or they lose.

    return checkout_count if checkout_count > 0 else 0

# Create the summary table
summary_table = {}
for player, scores in players.items():
    average_checkouts = calculate_average_shots_to_checkout(scores)
    summary_table[player] = average_checkouts

# Print the summary table
print("Player\tAverage Check Out Shot Count")
for player, average_checkouts in summary_table.items():
    print(player + "\t" + str(round(average_checkouts, 2)))
