# Here's a step-by-step explanation of the code:

# Initialize an empty dictionary called winners to keep track of each team's score.
#
# Iterate over the indices and results of the competitions using the enumerate function.
#
# Inside the loop, determine the winner of each competition based on the corresponding result. If the result is 1, it
# means the first team in the competition list (competitions[id][0]) won, otherwise, the second
# team (competitions[id][1]) won. Assign the winning team to the variable winner.
#
# Check if the winner is already present in the winners dictionary using the get method. If the winner is found,
# increment their score by 3 (since each win is worth 3 points in this tournament format). If the winner is not
# found, add them to the winners dictionary and initialize their score to 3.
#
# After the loop completes, use the max function with the key parameter set to winners.get to find the team with
# the highest score. The max function iterates over the dictionary and returns the key (team name) that has the
# highest corresponding value (score).
#
# Finally, return the team with the highest score, which represents the winner of the tournament.


# The space complexity of the code is O(n), where n is the number of competitions. This is because the space required
# to store the winners dictionary grows with the number of competitions.

# The time complexity of the code is O(n), where n is the number of competitions. This is because the code iterates
# through the competitions and performs a constant amount of operations for each competition. The max function with
# the key parameter has a time complexity of O(n) as well, where n is the number of unique winners.
def tournamentWinner(competitions, results):
    winners = {}
    for id, result in enumerate(results):
        wineer = competitions[id][0] if result == 1 else competitions[id][1]
        if winners.get(wineer):
            winners[wineer] += 3
        else:
            winners[wineer] = 3

    # using max function with the key parameter in aggregation with get function
    return max(winners, key=winners.get)


# improved solution
def tournamentWinner(competitions, results):
    winners = {}
    for id, result in enumerate(results):
        winner = competitions[id][0] if result == 1 else competitions[id][1]
        if winner not in winners:
            winners[winner] = 3
        winners[winner] += 3

    # using max function with the key parameter in aggregation with get function
    return max(winners, key=winners.get)

