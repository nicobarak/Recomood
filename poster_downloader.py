import tmdbsimple as tmdb
import re
from dotenv import load_dotenv
import os


def get_movie_obj(movie_name, year):
    try:
        tmdb.API_KEY = os.getenv("TMDB_API_KEY")
        if tmdb.API_KEY is None:
            tmdb.API_KEY = TMDB_API_KEY
        search = tmdb.Search()
        search.movie(query=movie_name, year=year)
        if search.total_results <= 0:
            raise ValueError
        for movie in search.results:
            if (
                movie["title"].lower() == movie_name.lower()
                and re.search(str(year), movie["release_date"]) != None
            ):
                return movie


        raise ValueError
    except ValueError:
        return 1
