import sqlite3
from flask import (
    Flask,
    render_template,
    session,
)
from flask_session import Session
from poster_downloader import get_movie_obj

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
CLASSIC = 1
LAUGHABLE = 2
EMOTIONAL = 3
FAMILY = 4
FUN = 5
HOPEFUL = 6
FRESH = 7
SCARY = 8
SOCIAL = 9
UNKNOWN = 10

def init_chosen():
    if 'chosen' not in session:
        session['chosen'] = []

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    init_chosen()
    return render_template("index.html")


def get_movie_id(mood):
    con = sqlite3.connect('movies.db')
    cur = con.cursor()
    cur.execute("SELECT movie_id FROM recommendations WHERE mood_id = ? ORDER BY random() LIMIT 1;", (mood,))
    query = cur.fetchone()
    if query:
        movie_id = query[0]  # Accede al primer valor en la tupla
    else:
        movie_id = None  # O maneja de acuerdo a tus necesidades si no se encontraron resultados
    con.close()
    return movie_id

def get_spanish_name(movie_id):
    con = sqlite3.connect('movies.db')
    cur = con.cursor()
    cur.execute("SELECT name_spanish FROM movies WHERE id = ?", (movie_id,))
    movies = cur.fetchall()
    con.close()

    if movies:
        spanish_name = movies[0][0]  # Accede al primer valor en la tupla
        return spanish_name
    else:
        return None

def get_movie(movie_id):
    con = sqlite3.connect('movies.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
    movies = cur.fetchall()
    con.close()

    if movies:
        db_movie = movies[0]
        movie = get_movie_obj(db_movie[1], db_movie[2])  # Accede a los valores por índice
        return movie
    else:
        return None

def get_reco(movie_id):
    con = sqlite3.connect('movies.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM recommendations WHERE movie_id = ?", (movie_id,))
    movies = cur.fetchall()
    con.close()
    if movies:
        movie = movies[0]
        return movie[3]  # Accede a los valores por índice
    else:
        return None

def get_reco_esp(movie_id):
    con = sqlite3.connect('movies.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM recommendations WHERE movie_id = ?", (movie_id,))
    movies = cur.fetchall()
    con.close()
    if movies:
        movie = movies[0]
        return movie[2]  # Accede a los valores por índice
    else:
        return None

@app.route("/esp_home", methods=["GET", "POST"])
def esp_home():
    init_chosen()
    return render_template("esp_home.html")

@app.route("/classic", methods=["GET", "POST"])
def classic():
    init_chosen()
    movie_id = get_movie_id(CLASSIC)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("classic_general.html", reco = reco, movie = movie)

@app.route("/classic_esp", methods=["GET", "POST"])
def classic_esp():
    init_chosen()
    movie_id = get_movie_id(CLASSIC)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("classic_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/emotional", methods=["GET", "POST"])
def emotional():
    init_chosen()
    movie_id = get_movie_id(EMOTIONAL)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("emotional_general.html", reco = reco, movie = movie)

@app.route("/emotional_esp", methods=["GET", "POST"])
def emotional_esp():
    init_chosen()
    movie_id = get_movie_id(EMOTIONAL)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("emotional_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/familiar", methods=["GET", "POST"])
def familiar():
    init_chosen()
    movie_id = get_movie_id(FAMILY)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("familiar_general.html", reco = reco, movie = movie)

@app.route("/familiar_esp", methods=["GET", "POST"])
def familiar_esp():
    init_chosen()
    movie_id = get_movie_id(FAMILY)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("familiar_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/laughable", methods=["GET", "POST"])
def laughable():
    init_chosen()
    movie_id = get_movie_id(LAUGHABLE)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("laughable_general.html", reco = reco, movie = movie)

@app.route("/laughable_esp", methods=["GET", "POST"])
def laughable_esp():
    init_chosen()
    movie_id = get_movie_id(LAUGHABLE)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("laughable_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/scary", methods=["GET", "POST"])
def scary():
    init_chosen()
    movie_id = get_movie_id(SCARY)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("scary_general.html", reco = reco, movie = movie)

@app.route("/scary_esp", methods=["GET", "POST"])
def scary_esp():
    init_chosen()
    movie_id = get_movie_id(SCARY)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("scary_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/fresh", methods=["GET", "POST"])
def fresh():
    init_chosen()
    movie_id = get_movie_id(FRESH)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("fresh_general.html", reco = reco, movie = movie)

@app.route("/fresh_esp", methods=["GET", "POST"])
def fresh_esp():
    init_chosen()
    movie_id = get_movie_id(FRESH)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("fresh_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/social", methods=["GET", "POST"])
def social():
    init_chosen()
    movie_id = get_movie_id(SOCIAL)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("social_general.html", reco = reco, movie = movie)

@app.route("/social_esp", methods=["GET", "POST"])
def social_esp():
    init_chosen()
    movie_id = get_movie_id(SOCIAL)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("social_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/fun", methods=["GET", "POST"])
def fun():
    movie_id = get_movie_id(FUN)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("fun_general.html", reco = reco, movie = movie)

@app.route("/fun_esp", methods=["GET", "POST"])
def fun_esp():
    init_chosen()
    movie_id = get_movie_id(FUN)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("fun_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)

@app.route("/unknown", methods=["GET", "POST"])
def unknown():
    init_chosen()
    movie_id = get_movie_id(UNKNOWN)
    movie = get_movie(movie_id)
    reco = get_reco(movie_id)
    return render_template("unknown_general.html", reco = reco, movie = movie)

@app.route("/unknown_esp", methods=["GET", "POST"])
def unknown_esp():
    init_chosen()
    movie_id = get_movie_id(UNKNOWN)
    movie = get_movie(movie_id)
    reco = get_reco_esp(movie_id)
    spanish_name = get_spanish_name(movie_id)
    return render_template("unknown_esp.html", reco = reco, movie = movie, spanish_name = spanish_name)