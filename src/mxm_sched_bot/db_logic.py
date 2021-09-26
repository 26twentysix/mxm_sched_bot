from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite://data/bot_db.db?check_same_thread=false', echo=True)
base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Schedule(base):
    __tablename__ = 'schedule'
    group_id = Column(Integer, primary_key=True)
    upd_date = Column(String)
    mon = Column(String)
    tue = Column(String)
    wed = Column(String)
    thu = Column(String)
    fri = Column(String)
    sat = Column(String)
    sun = Column(String)
    n_mon = Column(String)
    n_tue = Column(String)
    n_wed = Column(String)
    n_thu = Column(String)
    n_fri = Column(String)
    n_sat = Column(String)
    n_sun = Column(String)


class User(base):
    __tablename__ = 'students_list'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    group_name = Column(String)
    group_id = Column(Integer)
    state = Column(String)


base.metadata.create_all(engine)
