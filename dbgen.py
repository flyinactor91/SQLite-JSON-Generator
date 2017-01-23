#!/usr/bin/python3

import logging
import sqlite3
from json import load

def make_db(json_path: str, db_path: str):
    """Generate an SQLite database from a JSON config file"""

    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    dbdata = load(open(json_path))

    for key, settings in dbdata.items():
        cols = settings['columns']
        query = "CREATE TABLE {} (id,{})".format(key, ','.join(cols))
        logging.debug('Table query: %s', query)
        curs.execute(query)
        rows = [[i, *vals] for i, vals in enumerate(settings['rows'])]
        logging.debug('Prepended rows: %s', rows)
        query = "INSERT INTO {} VALUES ({})".format(key, ','.join(['?']*len(rows[0])))
        logging.debug('Insert query: %s', query)
        curs.executemany(query, rows)
        conn.commit()

    conn.close()

if __name__ == '__main__':
    from os.path import exists
    from sys import argv
    def error(msg: str, val: int):
        print(msg)
        exit(val)
    if len(argv) < 3:
        error('Missing arguments', 1)
    fjson, fdb = argv[1], argv[2]
    if not exists(fjson):
        error('Could not find JSON config file', 2)
    if exists(fdb):
        error('Target DB file already exists', 3)
    make_db(fjson, fdb)
    exit(0)
