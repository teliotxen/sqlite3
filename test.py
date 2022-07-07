from sqlalchemy import create_engine


engine = create_engine('sqlite:///new_file.db"', echo=True)


Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    date = Column(Integer)
    rank = Column(Integer)
    movieNm = Column(String(30))
    movieCd = Column(Integer)
    salesAmt = Column(Integer)
    audiCnt = Column(Integer)

Movie.__table__.create(bind=engine, checkfirst=True)