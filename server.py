from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)
from jinja2 import StrictUndefined

from run_pyahtzee.py import *

app = Flask(__name__)

#Required to use Flask sessions
app.secret_key = "Yahtzeeeeeeeeee!"

#For debugging - see Jinja fails
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def show_home():
    """Display homepage"""

    return render_template("index.html")


@app.route('/players', methods=['POST'])
def get_players():
    """Get number of players"""

    players = request.form.get('players')
    players = int(players)
    session['players'] = players
    scoreboard = populate_scoreboards(players)
    session['scoreboard'] = scoreboard

    return redirect('/')


if __name__ == "__main__":
    # Change app.debug to False before launch
    app.debug = True

    app.run()  # host="0.0.0.0"
