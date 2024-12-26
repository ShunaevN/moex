import json
import os
import uuid
from datetime import datetime
from flask import Flask, request, send_file, redirect, render_template, jsonify, Response
from config import KEY, MODE, BASE_SECURITIES_URL, BASE_HISTORY_URL
from src.database import db_session
from sqlalchemy import inspect
from utils.from_json_to_history_db import load_history_to_db
from utils.from_json_to_securities_db import load_securities_to_db
from src.models.history import History
from src.models.securities import Securities


app = Flask(__name__)
app.config['SECRET_KEY'] = KEY


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/securities', methods=['GET', 'POST'])
def securities_page():
    return render_template("security.html")


@app.route('/cross', methods=['GET', 'POST'])
def cross_page():
    return render_template("cross.html")


@app.route('/api/securities', methods=['GET', 'POST'])
def get_securities():
    db_sess = db_session.create_session()
    securities = db_sess.query(Securities).all()
    securities_to_json = dict()
    for i in range(len(securities)):
        securities_to_json[i] = {
            'id': securities[i].id,
            'secid': securities[i].secid,
            'regnumber': securities[i].regnumber,
            'name': securities[i].name,
            'emitent_title': securities[i].emitent_title,
        }
    db_sess.close()
    return jsonify(securities_to_json)


@app.route('/api/cross', methods=['GET', 'POST'])
def get_cross():
    db_sess = db_session.create_session()
    securities = db_sess.query(Securities).all()
    cross_to_json = dict()
    for i in range(len(securities)):
        history = db_sess.query(History).where(History.secid == str(securities[i].secid)).first()
        cross_to_json[i] = {
            'secid': securities[i].secid,
            'regnumber': securities[i].regnumber,
            'name': securities[i].name,
            'emitent_title': securities[i].emitent_title,
            'tradedate': history.tradedate if history else None,
            'numtrade': history.numtrades if history else None,
            'open': history.open if history else None,
            'close': history.close if history else None,
        }
    db_sess.close()
    return jsonify(cross_to_json)


def main():
    db_session.global_init()
    load_securities_to_db(BASE_SECURITIES_URL)
    load_history_to_db(BASE_HISTORY_URL)
    app.run()


if __name__ == '__main__':
    main()
