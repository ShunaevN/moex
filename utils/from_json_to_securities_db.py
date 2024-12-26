from src.models.securities import Securities
from src.database import db_session
from utils.securities_json_preprocessing import securities_preprocessing


def load_securities_to_db(url: str) -> None:
    db_sess = db_session.create_session()
    data = securities_preprocessing(url)
    securities_with_secid = [i.secid for i in db_sess.query(Securities).all()]
    for note in data:
        if note['secid'] not in securities_with_secid:
            security = Securities(
                id=note['id'],
                secid=note['secid'],
                regnumber=note['regnumber'],
                name=note['name'],
                emitent_title=note['emitent_title']
            )
            db_sess.add(security)
            db_sess.commit()
    db_sess.close()