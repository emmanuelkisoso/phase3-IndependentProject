# lib/cli.py

from models.genre import Genre, session
from models.movie import Movie

MAIN_MENU_OPTIONS = ("Manage Movies", "Manage Genres", "Exit")
MOVIE_MENU_OPTIONS = ("Add a new movie", "Delete a movie", "List all movies", "Find a movie by a ID", "Find movies by title", "Find movie by genre", "Mark a movie as watched/unwatched", "Go back to main menu")
GENRE_MENU_OPTIONS = ("Add a new genres", "Find movies by genre", "Go back to main menu")

def main_menu():
    while True:
        print("Welcome to the Movie Management System!")
        print("Please select an option:")
        for i,option in enumerate(MAIN_MENU_OPTIONS, start=1):
            print(f"{i}. {option}:")

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            movie_menu()
        elif choice == "2":
            genre_menu()
        elif choice == "3":
            print("Exiting the application.Bye!")
            break
        else:
            print("Invalid choice.Please try again.")

def movie_menu():
    while True:
        print("\nMovie Management Menu:")
        for i,option in enumerate(MOVIE_MENU_OPTIONS, start=1):
            print(f"{i}. {option}")

        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            create_movie()
        elif choice == "2":
            delete_movie()
        elif choice == "3":
            list_movies()
        elif choice == "4":
            find_movie_by_id
        elif choice == "5":
            find_movies_by_title()
        elif choice == "6":
            find_movies_by_genre()
        elif choice == "7":
            update_movie_watched_status()
        elif choice == "8":
            return
        else:
            print("Invalid choice.Please try again.")

def genre_menu():
    while True:
        print("\nGenre Management System")
        for i, option in enumerate(GENRE_MENU_OPTIONS, start=1):
            print(f"{i}. {option}")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            create_genre()
        elif choice == "2":
            delete_genre()
        elif choice == "3":
            list_genres()
        elif choice == "4":
            find_movies_by_genre()
        elif choice == "5":
            return
        else:
            print("Invalid choice. Please try again.")

def create_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the director: ")
    release_year = int(input("Enter the release year: "))
    runtime = int(input("Enter the runtime (in minutes): "))

    genres = session.query(Genre).all()
    genre_options = [(genre.id, genre.name) for genre in genres]

    print("Available genres:")
    for genre_id, genre_name in genre_options:
        print(f"{genre_id}. {genre_name}")

    genre_id = int(input("Enter the genre ID: "))

    movie = Movie.create(title, director, release_year, runtime, genre_id)
    print(f"Movie '{movie.title}' created successfully.")

def delete_movie():
    movie_id = int(input("Enter the movie ID to delete: "))
    Movie.delete(movie_id)
    print("Movie deleted successfully.")

def list_movies():
    movies = Movie.get_all()
    movie_data = []
    for movie in movies:
        movie_data.append({
            "id" : movie.id,
            "title" : movie.title,
            "director" : movie.director,
            "release_year" : movie.release_year,
            "runtime" : movie.runtime,
            "watched" : "Yes" if movie.watched else "No",
            "genre" : movie.genre.name
        })

    if movie_data:
        print("Movies:")
        for movie in movie_data:
            print(f"ID: {movie['id']}, Title: {movie['title']}, Director:{movie['director']}, " f"Release Year: {movie['release_year']}, Runtime:{movie['runtime']} minutes, " f"Watched: {movie['watched']}, Genre: {movie['genre']}")
        else:
            print("No movies found.")

def find_movie_by_id():
    movie_id = input("Enter the movie ID: ")
    movie = Movie.find_by_id(movie_id)
    if movie:
        movie_info = {
            "Title": movie.title,
            "Genre": movie.genre.name,
            "Watched": "Yes" if movie.watched else "No"
        }
        for key, value in movie_info.items():
            print(f"{key}: {value}")
    else:
        print("No movie found with the given ID.")

def find_movies_by_title():
    title = input("Enter the movie title (or part of it): ")
    movies = Movie.find_movies_by_title(title)
    if movies:
        print_movie_list(movies)
    else:
        print("No movies found matching the given title.")

def find_movies_by_genre():
    genres = Genre.get_all()
    genre_list = [(genre.id, genre.name) for genre in genres]

    print("Select a genre:")
    for i, (genre_id, genre_name) in enumerate(genre_list, start=1):
        print(f"{i}. {genre_name}")

    choice = input("Enter the genre number: ")
    try:
        genre_id, genre_name = genre_list[int(choice) - 1]
        movies = Movie.find_movies_by_genre(genre_id)
        if movies:
            print_movie_list(movies)
        else:
            print(f"No movies found in the '{genre_name}' genre.")
    except (IndexError, ValueError):
        print("Invalid genre choice.")

def update_movie_watched_status():
    movie_id = input("Enter the movie ID: ")
    movie = Movie.find_by_id(movie_id)
    if movie:
        movie_info = {
            "Title": movie.title,
            "Genre": movie.genre.name,
            "Watched": "Yes" if movie.watched else "No"
        }
        for key, value in movie_info.items():
            print(f"{key}: {value}")

        new_status = input(f"Current status: {movie_info['Watched']}. Enter new status (W/U): ")
        if new_status.upper() == 'W':
            Movie.update_watched_status(movie_id, True)
            print("Movie marked as watched.")
        elif new_status.upper() == 'U':
            Movie.update_watched_status(movie_id, False)
            print("Movie marked as unwatched.")
        else:
            print("Invalid input. Status unchanged.")
    else:
        print("No movie found with the given ID.")

def print_movie_list(movies):
    for movie in movies:
        movie_info = {
            "ID": movie.id,
            "Title": movie.title,
            "Genre": movie.genre.name,
            "Watched": "Yes" if movie.watched else "No"
        }
        print(", ".join(f"{key}: {value}" for key, value in movie_info.items()))

def create_genre():
    genre_name = input("Enter the new genre name: ")
    genre = Genre.create(genre_name)
    print(f"New genre '{genre.name}' created.")

def delete_genre():
    genres = Genre.get_all()
    genre_list = [(genre.id, genre.name) for genre in genres]

    print("Select a genre to delete:")
    for i, (genre_id, genre_name) in enumerate(genre_list, start=1):
        print(f"{i}. {genre_name}")

    choice = input("Enter the genre number: ")
    try:
        genre_id, genre_name = genre_list[int(choice) - 1]
        Genre.delete(genre_id)
        print(f"Genre '{genre_name}' deleted.")
    except (IndexError, ValueError):
        print("Invalid genre choice.")

def list_genres():
    genres = Genre.get_all()
    if genres:
        print("Genres:")
        for genre in genres:
            print(f"- {genre.name}")
    else:
        print("No genres found.")

def print_movie_list(movies):
    for movie in movies:
        movie_info = {
            "ID": movie.id,
            "Title": movie.title,
            "Genre": movie.genre.name,
            "Watched": "Yes" if movie.watched else "No"
        }
        print(", ".join(f"{key}: {value}" for key, value in movie_info.items()))