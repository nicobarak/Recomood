import tmdbsimple as tmdb
import re


def get_movie_obj(movie_name, year):
    try:
        tmdb.API_KEY = "7de1ad8d33f39ee11c34ba41813e0f25"
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
