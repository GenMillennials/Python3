def rock_paper_scissors(pl_1, pl_2):
    if pl_1 == pl_2:
        return "drawn game"
    elif (pl_1 == "rock" and (pl_2 == "scissors" or pl_2 == "lizard")):
        return "Timur"
    elif (pl_1 == "scissors" and (pl_2 == "paper" or pl_2 == "lizard")):
        return "Timur"
    elif (pl_1 == "paper" and (pl_2 == "rock" or pl_2 == "Spock")):
        return "Timur"
    elif (pl_1 == "lizard" and (pl_2 == "paper" or pl_2 == "Spock")):
        return "Timur"
    elif (pl_1 == "Spock" and (pl_2 == "rock" or pl_2 == "scissors")):
        return "Timur"
    else:
        return "Ruslan"

Tim = input()
Rusl = input()
print(rock_paper_scissors(Tim, Rusl))