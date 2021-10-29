from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template("base.html", title="Home")

@app.route("/<player1_choice>/<player2_choice>")   
def find_winner(player1_choice,player2_choice):
    player_1 = Player("player_1", player1_choice )
    player_2 = Player("player_2", player2_choice)
    game_1 = Game(player_1,player_2)
    winner = game_1.determin_winner((player_1),(player_2))
    return render_template("index.html", title="Home", winner=winner, player_1_name = player_1.name, player_1_played = player_1.choice,player_2_name = player_2.name,player_2_played=player_2.choice)

   
    # return print(result)

    # return render_template("base.html", title="Home", result = result)
    