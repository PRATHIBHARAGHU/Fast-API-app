from sqlalchemy import create_engine  # used to connect fastapi with postgres database
from sqlalchemy.orm import sessionmaker # used to create session with database 
from sqlalchemy.orm import declarative_base # used to create the base class for the models

SQLALCHEMY_DATABE_URL = "postgresql://postgres:postgres@localhost:5432/student-DB" # postgresql://"user":"password""@"hostname":"port name"/"DB name"
# Capitalize the term to make it a constant variable, so that it can be used anywhere in the code.(SQLALCHEMY_DATABE_URL is a constant variable .)
engine=create_engine(SQLALCHEMY_DATABE_URL)
SessionLocal = sessionmaker(autocommit=False,autoFlush=False,bind=engine)
Base=declarative_base 
def get_db():
    db=SessionLocal()
    
    try:
        yield db # fetch the data one by one from the database and return it to the user
    finally:
        db.close() 
