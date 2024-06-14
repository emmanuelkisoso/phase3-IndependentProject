from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .genre import Genre, session

Base = declarative_base()

class  Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    director = Column(String)
    release_year = Column(Integer)
    runtime = Column(Integer)
    watched = Column(Boolean, default=False)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship('Genre', backref='movies')

    @classmethod
    def create(cls, title, director, release_year, runtime, genre_id):
        movie = cls(title=title, director=director, release_year=release_year, runtime=runtime, genre_id=genre_id)
        session.add(movie)
        session.commit()
        return movie

    @classmethod
    def delete(cls, movie_id):
        movie = session.query(cls).get(movie_id)
        if movie:
            session.delete(movie)
            session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, movie_id):
        return session.query(cls).get(movie_id)

    @classmethod
    def find_movies_by_title(cls, title):
        return session.query(cls).filter(cls.title.ilike(f'%{title}%')).all()

    @classmethod
    def find_movies_by_genre(cls, genre_id):
        return session.query(cls).filter_by(genre_id=genre_id).all()

    @classmethod
    def update_watched_status(cls, movie_id, watched):
        movie = session.query(cls).get(movie_id)
        if movie:
            movie.watched = watched
            session.commit()
        return movie