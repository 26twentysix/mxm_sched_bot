from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///data/bot_db.db?check_same_thread=false', echo=True)
base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
states = ['none', 'err', 'setting group', 'ready']


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


def add_user(user_id, username):
    current_user = session.query(User).filter_by(user_id=user_id).one_or_none()
    if current_user:
        return False
    else:
        user = User(user_id=user_id, username=username, state=None)
        session.add(user)
        session.commit()
        return True


