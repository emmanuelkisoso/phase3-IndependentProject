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