""" This module provides and abstraction for sqlite3 database connectivity """

from contextlib import contextmanager
import sqlite3

class Repository(object):
    """ The Repository class is a storage facility for data """
    def __init__(self, location=":memory:"):
        self.location = location
        self.connection = None
        self.connected = False

    @contextmanager
    def connect(self):
        """
        Used to connect to open and close a connection to a db.

        Usage:

        repo = Repository()
        with repo.connect() as db:
            db.execute("Select foo from bar")
        """
        self.connection = sqlite3.connect(self.location)
        self.connected = True
        yield self
        self.connection.close()
        self.connection = None
        self.connected = False

    def execute(self, sql):
        """ Executes sql.  Expects an existing connection """
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)

    def fetchone(self):
        """ Returns data from the db.  Expects an open cursor """
        return self.cursor.fetchone()
