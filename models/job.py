from sqlalchemy import Column,Integer,String,Enum,ForeignKey
from sqlalchemy.orm import relationship
from database import Base,engine,SessionLocal

class JobBase(Base):
    __tablename__="jobs"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    Salary=Column(Integer)
    company_id=Column(Integer,ForeignKey("companies.id"))
    company=relationship("CompanyBase",back_populates="jobs")
    
