from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    title:str
    description:str
    Salary:int
    company_id:int

class JobCreate(BaseModel):
    pass
    
class JobUpdate(BaseModel):
    title: Optional[str] = None
    Salary: Optional[int] = None
    Description: Optional[str] = None
    company_id: Optional[int] = None
    
class JobResponse(JobBase):
    id:int
    company_id:int

    class Config:
        from_attributes=True         # Read data from SQLAlchemy models and convert it to Pydantic models
