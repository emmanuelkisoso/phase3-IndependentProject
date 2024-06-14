# lib/helpers.py

def print_movie_list(movies):
    if movies:
        print("Movies:")
        for movie in movies:
            print(f"ID: {movie['id']}, Title: {movie['title']}, Director:{movie['director']}, "
                  f"Release Year: {movie['release_year']}, Runtime:{movie['runtime']} minutes, "
                  f"Watched: {movie['watched']}, Genre: {movie['genre']}")
    else:
        print("No movies found.")

def validate_movie_input():
    title = input("Enter the movie title: ")
    director = input("Enter the director: ")
    release_year = int(input("Enter the release year: "))
    runtime = int(input("Enter the runtime (in minutes): "))
    return title, director, release_year, runtime

def format_movie_info(movie):
    return {
        "id": movie.id,
        "title": movie.title,
        "director": movie.director,
        "release_year": movie.release_year,
        "runtime": movie.runtime,
        "watched": "Yes" if movie.watched else "No",
        "genre": movie.genre.name
    }

def print_genre_options(genre_options):
    print("Available genres:")
    for genre_id, genre_name in genre_options:
        print(f"{genre_id}. {genre_name}")

