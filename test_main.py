import pytest
from unittest.mock import AsyncMock
from app.services.book_service import get_book_by_id

@pytest.mark.asyncio
async def test_get_book_by_id():
    mock_collection = AsyncMock()
    mock_collection.find_one.return_value = {"_id": "123", "title": "Test Book"}

    book = await get_book_by_id(mock_collection, "123")
    
    assert book["_id"] == "123"
    assert book["title"] == "Test Book"
