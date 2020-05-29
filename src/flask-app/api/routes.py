"""Defines the routes for the API"""
import calendar
from flask import Flask, request, abort
import math
import os
import sqlite3
import time

from .. import config as cfg
from ..giud import generate_guid
from ..db import sqlite

db_path = os.path.abspath(os.path.join(os.getcwd(), 'src', 'flask-app', 'db', 'shortguid.db'))
sqlite.create_database(db_path)

FLASK = Flask(__name__)

@FLASK.route("/")
def api_version():
    """API version 'tag-hash'"""
    return cfg.API_VERSION

@FLASK.route("/api/shortGuid")
def get_short_guid() -> str:
    """get new generated short guid, check db to ensure unique
    :return: string
    """
    conn = sqlite.create_database(db_path)
    while True:
        new_guid = generate_guid.get_short_guid()
        insert_query = '''INSERT INTO short_guids (xGuid) VALUES('{}');'''.format(new_guid)

        if sqlite.execute_statement(conn, insert_query):
            break

    conn.close()
    return new_guid