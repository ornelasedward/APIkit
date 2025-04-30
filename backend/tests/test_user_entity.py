import pytest
from app.entities.user import User

def test_valid_user():
    user = User("Alice", "alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"

def test_missing_name():
    with pytest.raises(ValueError):
        User("", "email@example.com")

def test_invalid_email():
    with pytest.raises(ValueError):
        User("Alice", "bad-email")
