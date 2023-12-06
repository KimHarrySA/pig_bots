def choice(round_score, my_score, opponent_score):
    if round_score > 18 + 2.*opponent_score/100 + 5.*(my_score)/100 or my_score + round_score >= 100:
        return False
    else:
        return True
