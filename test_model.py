import pytest
from app.models import User  # Adjust the import based on your project structure

def test_user_creation():
    user = User(username="testuser", email="testuser@example.com", password="password123")
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.password == "password123"
