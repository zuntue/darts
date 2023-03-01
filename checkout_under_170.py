# We're trying to create a summary table of each player's average check out shot count from a score of 170 oar below.
# The table will have each player as a row and one column with the average check out shot count from  170 or below.
import pandas as pd
import statistics as stat


df = pd.read_csv('data.csv')
players = {key: [] for key in df['Player'].unique()}
df.loc[:, 'Seen'] = False

# Loop through rows
for index, row in df.iterrows():
    if int(row['Total Score']) <= 170 and row['Seen'] is False:
        player = row['Player']
        leg = row['Legs']
        shots = 0
        for loop_index, loop_row in df.iloc[index:].iterrows():
            if loop_row['Legs'] is leg and loop_row['Player'] is player:
                row['Seen'] = True
                shots += 1
                if loop_row['Total Score'] == 0:  # the player checked out
                    players[player].append(shots)
            if loop_row['Legs'] is not leg:
                break


# Function to calculate the average checkout shot count for each player
def calculate_average_shots_to_checkout(player):
    return stat.mean(players[player])


# Create the summary table
summary_table = {}
for p in players.keys():
    average_checkouts = calculate_average_shots_to_checkout(p)
    summary_table[p] = average_checkouts

# Print the summary table
print("Player\tAverage Check Out Shot Count")
for player, average_checkouts in summary_table.items():
    print(player + "\t" + str(round(average_checkouts, 2)))
