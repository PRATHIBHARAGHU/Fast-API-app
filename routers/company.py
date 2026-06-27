from fastapi import APIRouter,HTTPException,Depends,status
#API router for endpoints  # HTTPException is used to raise exceptions itself #Depends is used to get the database session from the dependency injection system of FastAPI  #status is used to return the status code of the response
from schemas.company import CompanyCreate,CompanyUpdate,CompanyResponse
from models import Company
from models.company import CompanyBase
from sqlalchemy.orm import  Session
from database import get_db

router = APIRouter(prefix="/company",tags=["company"])
companies=[]

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = company.CompanyBase(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


@router.get("/",status_code=status.HTTP_200_OK,response_model=list[CompanyResponse])
def get_all_company():
    pass

@router.get("/:{company_id}",status_code=status.HTTP_200_OK,response_model=CompanyResponse)
def get_company(company_id: int):
    return companies[company_id]

@router.put("/{company_id}",status_code=status.HTTP_200_OK,response_model=CompanyResponse)
def update_company(company_id:int, company:CompanyUpdate):
    companies[company_id]=company
    return companies

@router.delete("/{company_id}",status_code=status.HTTP_200_OK)
def delete_company(company_id:int):
    companies.pop(company_id)
    return companies


# @router.get("/")
# def read_company():
#     return{"Company": "Company root"}

# @router.get("/{company_id}")
# def read_company(company_id: int):
#     return {"company_id": company_id}

