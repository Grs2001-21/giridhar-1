# Testing Strategy

# Unit Tests  
- Test models, utility functions, and isolated logic using `pytest`.  
- Mock database connections to avoid dependency on MongoDB.  

# Integration Tests  
- Test API endpoints with `httpx` to validate CRUD operations.  
- Use `pytest-asyncio` to handle async FastAPI requests.

# Running Tests  
```sh
# Run unit tests with coverage
pytest --cov=app tests/unit --cov-report=term-missing

# Run integration tests
pytest tests/integration
