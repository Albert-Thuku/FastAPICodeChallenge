from sqlalchemy import String, Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    book_no = Column(Integer, primary_key = True)
    book_name = Column(String(), nullable = False)
    book_price = Column(Integer, nullable =False)
    book_color = Column(String(), nullable = False)


engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()