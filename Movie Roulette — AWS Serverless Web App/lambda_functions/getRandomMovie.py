import requests
import json
import random

def lambda_handler(event, context):
    # get a random movie
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5YTBmMjM1NjU1NmE3NDExN2VkY2I3ZGZkZjA4NjgyZSIsInN1YiI6IjY1YjU2ZTNlMWM2MzViMDE3YjEzOGNlZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0Z3DfcOUg4TqPp-5Jltl_kJeZ0H71f6piuf7b5q1wOs"
    }
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={random.randint(1, 100)}"
    random_movies = requests.get(url, headers=headers).text
    random_movie = json.loads(random_movies)["results"][random.randint(0, 20)]
    
    # get a list of genres
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    genres = requests.get(url, headers=headers).text
    genres = json.loads(genres)["genres"]
    
    # assemble necessary movie metadata
    movie = {}
    movie['id'] = random_movie['id']
    movie['title'] = random_movie['title']
    movie['year'] = random_movie['release_date'][0:4]
    movie['rating'] = str(random_movie['vote_average'])
    movie['genre'] = ''
    genres_num = len(random_movie['genre_ids'])
    for i in random_movie['genre_ids']:
        for j in genres:
            if int(j['id']) == int(i):
                if genres_num > 1:
                    movie['genre'] += (j['name'] + ' | ')
                    genres_num -= 1
                else:
                    movie['genre'] += j['name']

    movie['overview'] = random_movie['overview']
    movie['poster'] = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + random_movie['poster_path']
    
    # return the movie data to the user
    return {
        'statusCode': 200,
        'body': json.dumps(movie)
    }
