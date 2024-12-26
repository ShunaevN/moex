import time

from src.models.history import History
from src.models.securities import Securities
from src.database import db_session
from utils.history_json_preprocessing import history_preprocessing
from utils.add_missing_security import add_missing_security_to_db


def load_history_to_db(url: str) -> None:
    db_sess = db_session.create_session()
    data = history_preprocessing(url)
    history_with_secid = [i.secid for i in db_sess.query(History).all()]
    for note in data:
        is_security = db_sess.query(Securities).where(Securities.secid == str(note['secid'])).first()
        if not is_security:
            print(f"Добавляю бумагу {note['secid']}")
            add_missing_security_to_db(note['secid'])
        else:
            if note['secid'] not in history_with_secid:
                history = History(
                    id=note['id'],
                    secid=note['secid'],
                    tradedate=note['tradedate'],
                    numtrades=note['numtrades'],
                    open=note['open'],
                    close=note['close']
                )
                db_sess.add(history)
                db_sess.commit()
    db_sess.close()