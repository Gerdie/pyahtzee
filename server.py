from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)
from jinja2 import StrictUndefined

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

if __name__ == "__main__":
    # Change app.debug to False before launch
    app.debug = True

    app.run()  # host="0.0.0.0"
