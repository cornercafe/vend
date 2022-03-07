from typing import Optional
from pydantic import BaseModel



class Status(BaseModel):
    water_level: int
    tea_powder: int
    coffee_power: int


class NewteaModel(BaseModel):
    count: int
    machine_number: str
    amount:int
    status: Optional[Status]

