from fastapi.testclient import TestClient
from main import app

# Initialize TestClient using context manager for proper resource cleanup
def test_read_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World and welcome to my test environment"}

def test_read_item():
    with TestClient(app) as client:
        response = client.get("/items/42?q=test")
        assert response.status_code == 200
        assert response.json() == {"item_id": 42, "q": "test"}

# Optional: Add async test example if using async endpoints
# pytest.mark.anyio
# async def test_async_endpoint():
#     async with AsyncTestClient(app) as client:
#         response = await client.get("/async-route")
#         assert response.status_code == 200