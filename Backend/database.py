from sqlalchemy import create_engine  # used to connect fastapi with postgres database
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncSession # used to create session with database 
from sqlalchemy.orm import declarative_base # used to create the base class for the models
from dotenv import load_dotenv
import os
load_dotenv

DATABASE_URL = os.getenv("DATABASE_URL") # postgresql://"user":"password""@"hostname":"port name"/"DB name"
# Capitalize the term to make it a constant variable, so that it can be used anywhere in the code.(SQLALCHEMY_DATABASE_URL is a constant variable .)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL=DATABASE_URL.replace("postgres://","postgresql+asyncpg://",1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL=DATABASE_URL.replace("postgresql://","postgresql+asyncpg://",1)

# Supabase requires SSL but the asyncpg driver doesn't support "?sslmode" URL text.
# we split URL to remove query parameter, and pass ssl="require" instead
if "supabase.com" in DATABASE_URL:
    DATABASE_URL=DATABASE_URL.split("?")[0]
    engine=create_async_engine(DATABASE_URL,echo=False,connect_args={"ssl":"require"})
else:
    engine=create_async_engine(DATABASE_URL,echo=False)
SessionLocal = async_sessionmaker(autocommit=False,autoflush=False,bind=engine,class_=AsyncSession)
Base=declarative_base()

async def get_db():
    async with SessionLocal() as db:
        try:
            yield db # fetch the data one by one from the database and return it to the user
        finally:
            await db.close()
## yield keyword
# generator - uses yield and after it uses it can be used in try block
# after the use it is closed
# prevents memory leak, connection to db is closed properly
# it creates session for each request and closes it after the request
# ensures that each request has its own session
