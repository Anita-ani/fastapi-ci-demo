from fastapi.testclient import TestClient
from httpx import WSGITransport
from main import app

# Modern TestClient initialization with transport
def test_read_root():
    with TestClient(app, transport=WSGITransport(app=app)) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

def test_read_item():
    with TestClient(app, transport=WSGITransport(app=app)) as client:
        response = client.get("/items/42?q=test")
        assert response.status_code == 200
        data = response.json()
        assert data["item_id"] == 42
        assert data["q"] == "test"

# For async endpoints (uncomment when needed)
# @pytest.mark.anyio
# async def test_async_endpoint():
#     from httpx import AsyncClient
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         response = await client.get("/async-route")
#         assert response.status_code == 200