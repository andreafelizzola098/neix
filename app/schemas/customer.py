from pydantic import BaseModel
# Pydantic: used to define data validation schemas. These schemas are used for data input and output in your API.

class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
