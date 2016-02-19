

import sqlite3

from bts import BTS

class BadimsicoreBtsConfig:
    config = []

    def __init__(self, config_db):
        """
        :param config_db, a string containing the path to the OpenBTS.db file
        """
        self.db = config_db
        self.conn = sqlite3.connect(self.db)
        self.data = {}

    def read_badimsicore_bts_config(self):
        """
        Read from the OpenBTS db config file into the BadimsicoreBtsConfig object
        """
        c = self.conn.cursor()
        c.execute("SELECT * FROM CONFIG;")
        results = c.fetchall()

        for conf in results:
            self.data[conf[0]] = conf[1:]

        return results

    def get_config(self, key):
        """
        Get a config parameter
        :param key, the key designing the data
        """
        return self.data.get(key)

    def set_config(self, key, data):
        """
        Set a config parameter
        :param key, the key designing the data
        :param data, the tuple data representing a OpenBTS config parameter
        """
        self.data[key] = data

    def write_badimsicore_bts_config(self):
        """
        Write the config to the database
        """
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

    def update_badimsicore_bts_config(self, bts):
        """
        Update the database with the bts config
        :param bts: An object bts
        """
        self.update_database("GSM.Identity.ShortName", bts.shortname)
        self.update_database("GSM.Identity.MCC", bts.MCC)
        self.update_database("GSM.Identity.MNC", bts.MNC)
        self.update_database("GSM.Identity.LAC", bts.LAC)
        self.update_database("GSM.Identity.CI", bts.CI)

        self.close()

    def update_database(self, keystring, valuestring):
        """
        :param keystring: the column name
        :param valuestring: the value associated to the column name
        :return:
        """
        try:
            c = self.conn.cursor()
            query = "UPDATE CONFIG SET VALUESTRING = \""+valuestring+"\" WHERE KEYSTRING = \""+keystring+"\""
            c.execute(query)
            self.conn.commit()

        except sqlite3.Error as e:
            self.conn.rollback()
            raise e

    def close(self):
        """
        Cole the config
        """
        self.conn.close()