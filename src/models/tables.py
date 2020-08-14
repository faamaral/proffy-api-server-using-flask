import datetime
from src.models.models import Base, db_session, initDB
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40),index=True,nullable=False)
    avatar = Column(String, nullable=False)
    whatsapp = Column(String, nullable=False)
    bio = Column(String, nullable=False)

    def __init__(self, name, avatar, whatsapp, bio):
        self.name = name
        self.avatar = avatar
        self.whatsapp = whatsapp
        self.bio = bio

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return '<User: {}>'.format(self.name)

class Classes(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    subject = Column(String(30), nullable=False)
    cost = Column(DECIMAL, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('users')

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return '<Subject: {}>'.format(self.subject)

class ClassSchedule(Base):
    __tablename__ = 'class_schedule'

    id = Column(Integer, primary_key=True)
    week_day = Column(Integer, nullable=False)
    initHour = Column(Integer, nullable=False)
    endHour = Column(Integer, nullable=False)

    class_id = Column(Integer, ForeignKey('classes.id'))
    classes = relationship('classes')

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self):
        return '<Week day: {}>'.format(self.week_day)

class Connections(Base):
    __tablename__ = 'connections'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user_con = relationship('users')
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)


if __name__ == '__main__':
    initDB()

