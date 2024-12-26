import datetime
import sqlalchemy
from src.database.db_session import SqlAlchemyBase


class Securities(SqlAlchemyBase):
    __tablename__ = 'securities'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    secid = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    regnumber = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    emitent_title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    history = sqlalchemy.orm.relationship("History", back_populates='securities')



