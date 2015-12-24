import pytest
import json
import os


from data_py import tweets as t


def test_user_has_id():
    user = t.User()
    assert None == user.id

def test_user_has_name():
    user = t.User()
    assert None == user.name

def test_user_has_screen_name():
    user = t.User()
    assert None == user.screen_name

@pytest.fixture
def test_user():
    cwd = os.getcwd()
    filename = os.path.join(cwd, "tests", "fixtures", "user.json")

    with open(filename) as data:
        user_data = json.load(data)

    return user_data["user"]

def test_user_can_populate_from_json(test_user):
    user = t.User()
    user.populate(test_user)

    assert 1234567890 == user.id
    assert "Test User" == user.name
    assert "Test_User" == user.screen_name

