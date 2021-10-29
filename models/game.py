class Game():
    def __init__(self,player_1,player_2):
       self.player_1 = player_1
       self.player_2 = player_2

    def determin_winner (self,player_1,player_2):
        if player_1.choice == "rock" and player_2.choice == "paper":
           return "player 2 wins"

        if player_1.choice == "rock" and player_2.choice == "scissors" :
           return "player 1 wins"

        if player_1.choice == "scissors" and player_2.choice == "rock" :
           return "player 2 wins"

        if player_1.choice == "scissors" and player_2.choice == "paper" :
           return "player 1 wins"

        if player_1.choice == "paper" and player_2.choice == "scissors" :
           return "player 2 wins"

        if player_1.choice == "paper" and player_2.choice == "rock" :
            return "player 1 wins"

        if player_1.choice ==  player_2.choice:
            return "it's a draw"
