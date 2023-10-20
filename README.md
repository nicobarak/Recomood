# RECOMOOD

### Description:

How often have you wanted to watch a movie but weren't sure which one to pick? With RECOMOOD, you can easily discover curated recommendations. Our website harnesses the power of the TMDB API, an extensive online database of movies and TV shows, and it also utilizes a wrapper called "tmdbsimple" to streamline API interactions. By combining this database with our own curated personal database in SQLite, users can quickly access recommendations by selecting a mood, available in both English and Spanish. To utilize this API, you'll need an API key, which can be obtained for free at themoviedb.org. The use of the tmdbsimple wrapper is also freely accessible to everyone.

The database consists of three tables. The first table contains mood names and their corresponding mood_id. The second table, "movies," contains a list of the selected movies, complete with release year and names in both Spanish and English. The third table, "recommendations," combines moods and movies to generate personalized recommendations for each mood. This table includes a movie_id, mood_id, and recommendation text written in both English and Spanish.

The website employs Bootstrap for the card layout on the index page. As of now, the site offers nine different moods, including "Classic," "Laughable," "Emotional," "Family," "Fun," "New," "Scary," "Social," and "Unknown."

In app.py, the program utilizes SQLite queries to access and interact with the database, retrieving a random movie recommendation for each mood.

Every single recommendation is personally crafted and curated, ensuring that you not only receive great movie suggestions but also experience the creator's unique taste, providing a more human and personal touch. It truly is a carefully curated list!

For site translation, the index page is presented in English, but you'll find a button that will take you to the Spanish version of the site. If you're on the Spanish version, selecting a mood will redirect you to a Spanish version of the View page, with all content thoughtfully translated and cared for.

Thanks for reading!
