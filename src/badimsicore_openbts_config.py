#!/usr/bin/env python3.4

"""
    This module configures the openBTS database. This one
    is an sqlite3 type. After opening the connection, we
    can either configure the BTS according to deploy a fake BTS,
    using the function update_badimsicore_bts_config(), or any other entries by
    calling update_database().
"""

import sqlite3
from bts import BTS

__authors__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__maintener__ = "Arthur Besnard, Philippe Chang, Zakaria Djebloune, Nicolas Dos Santos, Thibaut Garcia and John Wan Kut Kai"
__licence__ = "GPL v3"
__copyright__ = "Copyright 2016, MIMSI team" 

class BadimsicoreBtsConfig:

    def __init__(self, config_db):
        """
        :param config_db, a string containing the path to the OpenBTS.db file
        """
        self.db = config_db
        self.conn = sqlite3.connect(self.db)


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

        #self.close()

    def update_database(self, keystring, valuestring):
        """
        Update the database with pair (keystring, valuestring)
        :param keystring: the column name
        :param valuestring: the value associated to the column name
        :return: None
        """
        try:
            c = self.conn.cursor()
            query = "UPDATE CONFIG SET VALUESTRING = \""+valuestring+"\" WHERE KEYSTRING = \""+keystring+"\""
            c.execute(query)
            self.conn.commit()

        except sqlite3.Error as e:
            self.conn.rollback()
            raise e
        finally:
            if c:
                c.close()

    def close(self):
        """
        Close the connection
        """
        if self.conn:
            self.conn.close()
