import os
import sqlite3
from sqlite3 import Error

def create_database(db_path) -> object:
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS short_guids (
                                        xGuid varchar UNIQUE
                                    ); """

    conn = None
    try:
        exists = os.path.exists(db_path)
        conn = sqlite3.connect(db_path)
        if not exists:
            execute_statement(conn, sql_create_projects_table)
        return conn
    except Error as e:
        print(e)

    return conn

def execute_statement(conn, sql_statement) -> bool:
    """ execute give sql statement
    :param conn: Connection object
    :param sql_statement: an sql statement
    :return: bool
    """
    try:
        c = conn.cursor()
        with conn:
            c.execute(sql_statement)
        return True
    except Error as e:
        print(e)
        return False