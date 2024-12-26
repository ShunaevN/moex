import datetime
import sqlalchemy
from src.database.db_session import SqlAlchemyBase


class History(SqlAlchemyBase):
    __tablename__ = 'history'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    secid = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("securities.secid"))
    tradedate = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    numtrades = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    open = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    close = sqlalchemy.Column(sqlalchemy.Float, nullable=True)

    securities = sqlalchemy.orm.relationship('Securities')