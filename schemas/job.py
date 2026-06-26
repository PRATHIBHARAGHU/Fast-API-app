from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    Title:str
    Salary:int

class JobUpdate(BaseModel):
    title: Optional[str] = None
    Salary: Optional[int] = None
