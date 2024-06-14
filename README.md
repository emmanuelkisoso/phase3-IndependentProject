# Movie Management System

## Summary

A Python CLI application to manage movies and genres using an ORM-backend database.

## Features

- Create, delete, and list movies
- Mark movies as watched/unwatched
- Add, delete, and list genres
- Search movies by title, genre, or ID

## Directory Structure

- `lib/cli.py`: Main application
- `lib/database/movies.db`:Database
- `lib/models/`: Model classes and ORM methods
- `lib/helpers.py`: Helper functions
- `requirements.txt`: Requirements

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the CLI: `python cli.py`
2. Use the menu options to manage movies and genres

## Data Model

- Movie: title, director, release year, runtime, genre
- Genre: name

## ORM Methods

- `create`, `delete`, `get_all`, `find_by_id`

## Dependencies

- SQLAlchemy
- Click

## Author

Kisoso,Emmanuel.
