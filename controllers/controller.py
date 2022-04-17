from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/')
def home():
    return render_template('home.html', title="Rock Paper Scissors!")

@app.route('/<player1choice>/<player2choice>')
def play_the_game(player1choice, player2choice):
    player1 = Player("Player 1", player1choice)
    player2 = Player("Player 2", player2choice)
    result = play_game(player1, player2)
    return render_template('index.html', title="Results", result=result, player1=player1, player2=player2)

