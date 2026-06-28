from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from database import get_db,SessionLocal,engine
from models.job import Job
from schemas.job import JobCreate,JobUpdate,JobResponse

router=APIRouter(prefix="/job",tags=["job"])

@router.post("/",status_code=201,response_model=JobCreate)
def create_job(job: JobCreate,db: Session = Depends(get_db)):
    db_job = Job(**job.dict())
    db.add(db_job) 
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/",status_code=200,response_model=list[JobCreate])
def get_all_job(db: Session = Depends(get_db)):
    return db.query(Job).all()

@router.get("/:{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == job_id).first()

@router.put("/{job_id}")
def update_job(job_id:int, job:JobUpdate, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    for key, value in job.dict().items():
        setattr(db_job, key, value)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.delete("/{job_id}")
def delete_job(job_id:int, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit() 
    return db_job

# @router.get("/")
# def read_job():
#     return{"Job": "Job root"}

# @router.get("/{job_id}")
# def read_Job(job: int):
#     return {"Job_id": "job_id"}

