from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)
from jinja2 import StrictUndefined

from run_pyahtzee import *

app = Flask(__name__)

#Required to use Flask sessions
app.secret_key = "Yahtzeeeeeeeeee!"

#For debugging - see Jinja fails
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def show_home():
    """Display homepage"""

    # if players in session and players > 0:
    #         while session['null_count'] > 0:
    #             for x in range(players):
    #                 print "Your turn, Player", x + 1
    #                 turn(x)
    #                 session['null_count'] -= 1
    #         for y in range(players):
    #             print "Player %r, your score is:" % (y + 1), final_score(y)

    return render_template("index.html")


@app.route('/players', methods=['POST'])
def get_players():
    """Get number of players"""

    players = request.form.get('players')
    players = int(players)
    session['players'] = players
    scoreboard = populate_scoreboards(players)
    session['scoreboard'] = scoreboard
    null_count = len(SCORE_DISPLAY) * players
    session['null_count'] = null_count

    return redirect('/')


if __name__ == "__main__":
    # Change app.debug to False before launch
    app.debug = True

    app.run()  # host="0.0.0.0"
