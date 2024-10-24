# from fastapi import APIRouter
# from app.schemas.customer import CustomerCreate, CustomerResponse
# from app.services.customer_service import create_customer
# from models import customer

# router = APIRouter()

# @router.post("/customers/", response_model=CustomerResponse)
# async def create_user_route(user: CustomerCreate):
#     return await create_customer(customer)
