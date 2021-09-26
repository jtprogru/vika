"""
Template for testing
"""

__test_data = {
    "username": "admin",
    "email": "admin@mail.local",
    "extends": {
        "is_superuser": True,
        "is_staff": True,
    },
}


def test_username(data=__test_data):
    assert data["username"] == "admin"
    assert isinstance(data["username"], str)


def test_email(data=__test_data):
    assert data["email"] == "admin@mail.local"
    assert isinstance(data["email"], str)


def test_extends_superuser(data=__test_data):
    assert data["extends"]["is_superuser"] is True
    assert isinstance(data["extends"]["is_superuser"], bool)


def test_extends_staff(data=__test_data):
    assert data["extends"]["is_staff"] is True
    assert isinstance(data["extends"]["is_staff"], bool)


def test_object(data=__test_data):
    assert isinstance(data, dict)
