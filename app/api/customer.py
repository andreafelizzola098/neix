import httpx

API_URL = "https://api.ejemplo.com/clientes"  # Cambia esto por la URL de tu API

async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL)
        response.raise_for_status()  # Lanza un error si la respuesta no es 200
        return response.json()  # Devuelve los datos en formato JSON
