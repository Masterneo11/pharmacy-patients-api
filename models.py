from pydantic import BaseModel
import uuid

class Patient(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    address: str 
    age: int 

