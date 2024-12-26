import sqlalchemy
from src.database import db_session
from src.models.securities import Securities


class SecurityApi:
    def create(self, _id, secid, regnumber, name, emitent_title):
        db_sess = db_session.create_session()
        try:
            new_obj = Securities(
                id=_id,
                secid=secid,
                regnumber=regnumber,
                name=name,
                emitent_title=emitent_title
            )
            db_sess.add(new_obj)
        except Exception as e:
            print(e)
        finally:
            db_sess.close()


    def read(self):
        db_sess = db_session.create_session()
        try:
            return db_sess.query(Securities).all()
        except Exception as e:
            print(e)
        finally:
            db_sess.close()

    def update(self, _id, secid, regnumber, name, emitent_title):
        db_sess = db_session.create_session()
        try:
            obj: Securities | None = db_sess.query(Securities).where(Securities.id == str(_id)).first()
            obj.secid = secid
            obj.regnumber = regnumber
            obj.name = name
            obj.emitent_title = emitent_title
            db_sess.commit()
        except Exception as e:
            print(e)
        finally:
            db_sess.close()

    def delete(self, _id):
        db_sess = db_session.create_session()
        try:
            db_sess.query(Securities).filter(Securities.id == str(_id)).delete()
            db_sess.commit()
        except Exception as e:
            print(e)
        finally:
            db_sess.close()