movies = {
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
}


def movies_5_5(movies):
    return movies['imdb']>5.5

res=movies_5_5(movies)
print (res)
