import uuid
import sqlalchemy
from src.database import db_session
from src.models.history import History
import datetime


class HistoryApi:
    def create(self, secid: str, tradedate: str, numtrades: float, _open: float, close: float):
        db_sess = db_session.create_session()
        try:
            new_obj = History(
                id=str(uuid.uuid4()),
                secid=secid,
                tradedate=datetime.datetime.strptime(tradedate, "%Y-%m-%d"),
                numtrades=numtrades,
                open=_open,
                close=close
            )
            db_sess.add(new_obj)
        except Exception as e:
            print(e)
        finally:
            db_sess.close()

    def read(self):
        db_sess = db_session.create_session()
        try:
            return db_sess.query(History).all()
        except Exception as e:
            print(e)
        finally:
            db_sess.close()

    def update(self, _id, secid: str, tradedate: str, numtrades: float, _open: float, close: float):
        db_sess = db_session.create_session()
        try:
            obj: History | None = db_sess.query(History).where(Securities.id == str(_id)).first()
            obj.secid = secid
            obj.tradedate = datetime.datetime.strptime(tradedate, "%Y-%m-%d")
            obj.numtrades = numtrades
            obj.open = _open
            obj.close = close
            db_sess.commit()
        except Exception as e:
            print(e)
        finally:
            db_sess.close()

    def delete(self, _id):
        db_sess = db_session.create_session()
        try:
            db_sess.query(History).filter(History.id == str(_id)).delete()
            db_sess.commit()
        except Exception as e:
            print(e)
        finally:
            db_sess.close()