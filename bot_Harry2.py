def choice(round_score, my_score, opponent_score):
    if opponent_score == 0 and my_score == 0:
        return round_score <= 20
    elif opponent_score < 43 and my_score < 43:
        return round_score <= (15 + (abs(opponent_score - my_score))/4)
    while my_score >= 70:
        return my_score + round_score < 100
