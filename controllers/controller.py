from random import choices
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
    return render_template('result.html', title="Results are in!", result=result, player1=player1, player2=player2)

@app.route('/2players')
def two_player_input():
    return render_template('index.html', title="2 Player Game", choices_list=choices_list)

@app.route('/play', methods=["POST"])
def two_player_play_game():
    player1_name = request.form["player1_name"]
    player1_choice = request.form["player1_choice"]
    player2_name = request.form["player2_name"]
    player2_choice = request.form["player2_choice"]
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    result = play_game(player1, player2)

    return render_template('result.html', title="2 Player Game - Results are in!", choices_list=choices_list, player1=player1, player2=player2, result=result)

