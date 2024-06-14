from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///database/movies.db')
Session = sessionmaker(bind=engine)
session = Session()

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @classmethod
    def create(cls, name):
        genre = cls(name=name)
        session.add(genre)
        session.commit()
        return genre

    @classmethod
    def delete(cls, genre_id):
        genre = session.query(cls).get(genre_id)
        if genre:
            session.delete(genre)
            session.commit()

    @classmethod
    def get_all(cls):
        return session.query(cls).all()
