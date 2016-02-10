

import sqlite3


class BadimsicoreBtsConfig:
    config = []

    def __init__(self, config_db):
        self.db = config_db
        self.conn = sqlite3.connect(self.db)
        self.data = {}

    def read_badimsicore_bts_config(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM CONFIG;")
        results = c.fetchall()

        for conf in results:
            self.data[conf[0]] = conf[1:]

        return results

    def get_config(self, key):
        return self.data.get(key)

    def set_config(self, key, data):
        self.data[key] = data

    def write_badimsicore_bts_config(self):
        newdat = []
        for k, v in self.data.items():
            newdat.append(tuple([k]) + v)

        try:
            c = self.conn.cursor()
            c.execute("DELETE FROM CONFIG")
            c.executemany("INSERT INTO CONFIG VALUES (?, ?, ?, ?, ?);", newdat)
            self.conn.commit()
        except sqlite3.Error as e:
            self.conn.rollback()
            raise e

    def close(self):
        self.conn.close()
