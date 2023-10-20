# RECOMOOD

### Description:

How many time do you want to watch a movie but you are unsure which one? With RECOMOOD, you will get easy and curated recommendations.
The website uses the TMDB API, an online huge database from movies and TV Shows and also uses a wrapper to handle that API called "tmdbsimple".
Mixing that database with a curated personal database in SQLite, the user will get easy and fast recommendations, selecting a mood and available both in english and spanish.
To use this API, it needs an API key, that it's alreaady generated for free in themoviedb.org.
The use of the wrapper tmdbsimple is also a free available source for everyone.

The curated database has 3 tables, one being the name of the moods and its mood_id. Another table is "movies", when there's a full list of curated movies, with the released year date and the name both in spanish and english. The final table, recommendations, is the table when we mix the moods and movies, making curated and personal recommendations for each movie and mood. To do that, the table has a movie_id, a mood_id, and the text recommendation written in both english and spanish.

The website uses Bootstrap in the index, for the cards layout. To the date of release, the site has 9 moods available, being "Classic", "Laughable", "Emotional", "Family", "Fun", "New", "Scary", "Social", and "Unknown".

In app.py, the program uses SQLite queries to get and interact with the database, getting a random movie for each mood. 

Every single recomendation was personally written and curated, so you'll get not only great recommendations and movies to watch, but also a sense of taste by the creator of the site, having a more human and personal approach. It really is a curated list!

For the translation of the site, the Index page is presented in english, but you have a button that will deliver you to the spanish version of the site. If you are in the spanish version, every mood that you select will deliver you to a spanish version of the View page, having everything translated and with huge care.

Thanks for reading!
