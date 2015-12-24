import sqlite3


import pytest


import data_py.sqlite.repository as sut


def test_can_create_an_in_memory_db():
    repo = sut.Repository()
    assert ":memory:" == repo.location

def test_can_access_db_with_context_manager():
    repo = sut.Repository()
    with repo.connect() as db:
        assert None != db.connection
        assert db.connected

    assert not db.connected
    assert None == db.connection

def test_can_execute_sql():
    repo = sut.Repository()
    with repo.connect() as db:
        db.execute("Create table test (foo text)")
        db.execute("insert into test(foo) values ('bar')")
        db.execute("select foo from test")
        assert "bar" == db.fetchone()[0]
