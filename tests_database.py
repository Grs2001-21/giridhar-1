from unittest.mock import patch
from app.database import get_database

@patch("app.database.MongoClient")
def test_get_database(mock_mongo_client):
    db = get_database()
    assert db is not None
