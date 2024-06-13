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
