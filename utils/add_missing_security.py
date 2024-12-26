from src.models.securities import Securities
from src.database import db_session
import requests
import asyncio


def add_missing_security_to_db(target: str) -> None:
    try:
        db_sess = db_session.create_session()
        data = requests.get(f'https://iss.moex.com/iss/securities.json?q={target}').json()['securities']['data'][0]
        if data:
            security = Securities(
                id=data[0],
                secid=data[1],
                regnumber=data[3],
                name=data[4],
                emitent_title=data[8]
            )
            db_sess.add(security)
            db_sess.commit()
        db_sess.close()
    except Exception:
        ...