from fastapi import FastAPI
from app.api.customer import get_data
from app.services.data_manipulation import manipulate_data

app = FastAPI()

@app.get("/data")
async def fetch_and_process_data():
    data = await get_data()  # Llama a la API
    processed_data = manipulate_data(data)  # Manipula los datos con pandas
    return processed_data

@app.get("/hola")
async def read_root():
    return {"message": "¡Hola, Juan!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

