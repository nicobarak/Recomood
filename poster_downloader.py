import requests
import sys
from PIL import Image
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
                poster_url = f"https://image.tmdb.org/t/p/w342{movie['poster_path']}"
                return movie
                original_poster = Image.open(requests.get(poster_url, stream=True).raw)


        raise ValueError
    except ValueError:
        return 1


def validate_name(name):
    if not name:
        return False

    return True


def validate_year(year):
    try:
        if year < 1900 or year > 2023:
            raise ValueError
        return year
    except ValueError:
        sys.exit("This is not a valid year (1900-2023)")


def main():
    name = input("Insert the name of the movie: ")
    while not validate_name(name):
        name = input("Please, insert a valid movie title: ")
    try:
        year = int(input("Insert the year of the movie: "))
    except ValueError:
        sys.exit("Not a valid number.")
    valid_year = validate_year(year)
    get_movie_obj(name, valid_year)


if __name__ == "__main__":
    main()