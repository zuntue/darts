# We're trying to create a summary table of each player's average check out shot count from a score of 501 or below.
# The table will have each player as a row and one column with the average check out shot count from  501 or below.
import pandas as pd
import statistics as stat

df = pd.read_csv('data.csv')
players = {key: [] for key in df['Player'].unique()}
df.loc[:, 'Seen'] = False

# Loop through rows
for index, row in df.iterrows():
    if int(row['Total Score']) <= 501 and (not df.loc[index, 'Seen']) and int(row['Total Score']) != 0:
        player = row['Player']
        leg = row['Legs']
        shots = 0
        for loop_index, loop_row in df.iloc[index:].iterrows():
            if loop_row['Legs'] is leg and loop_row['Player'] is player:
                df.loc[loop_index, 'Seen'] = True
                shots += 1
                if loop_row['Total Score'] == 0:  # the player checked out
                    players[player].append(shots)
                    break
            if loop_row['Legs'] is not leg:
                break


# Function to calculate the average checkout shot count for each player
def calculate_average_shots_to_checkout(player):
    return stat.mean(players[player])


[print(i, ": ", players[i], "\n") for i in players]

# Create the summary table
summary_table = {}
for p in players.keys():
    average_checkout = calculate_average_shots_to_checkout(p)
    summary_table[p] = average_checkout

# Print the summary table
print('{:<20}\t\t\t{:<20}'.format('Player', 'Average Check Out Shot Count From a Score of 501 or Below'))
for player, average_checkouts in summary_table.items():
    print('{:<20}\t{:^20}'.format(player, str(round(average_checkouts, 2))))
