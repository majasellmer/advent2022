"""
Advent of Code 2022, Day 2
solution by Maja Sellmer
part 2 only
"""

with open('advent2.txt') as strategy:
    strategy_list = strategy.readlines()
    total_score = 0
    for rps_round in strategy_list:
        round_score = 0
        opponents_move = rps_round[0]
        desired_outcome = rps_round[2]
        if desired_outcome == "X":
            # loss = + 0 points
            if opponents_move == "A":
                round_score += 3
            elif opponents_move == "B":
                round_score += 1
            elif opponents_move == "C":
                round_score += 2
        elif desired_outcome == "Y":
            # draw = + 3 points
            round_score += 3
            if opponents_move == "A":
                round_score += 1
            elif opponents_move == "B":
                round_score += 2
            elif opponents_move == "C":
                round_score += 3
        elif desired_outcome == "Z":
            # win = + 6 points
            round_score += 6
            if opponents_move == "A":
                round_score += 2
            elif opponents_move == "B":
                round_score += 3
            elif opponents_move == "C":
                round_score += 1
        total_score += round_score
    print(total_score)
      