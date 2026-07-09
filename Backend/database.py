import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not set. Add a .env file with DATABASE_URL=... "
        "or set the environment variable in your shell. Example:\n"
        "  DATABASE_URL=postgresql+asyncpg://USER:PASSWORD@HOST:PORT/DBNAME"
    )

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://") and "+asyncpg" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Supabase requires SSL but the asyncpg driver doesn't support the "?sslmode" URL text.
# We split the URL to remove the query parameters, and pass ssl="require" instead.
if "supabase.com" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.split("?")[0]
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
        connect_args={
            "ssl": "require",
            "prepared_statement_cache_size": 0,
            "statement_cache_size": 0
        }
    )
else:
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
        connect_args={
            "prepared_statement_cache_size": 0,
            "statement_cache_size": 0
        }
    )
# sanity check: ensure async driver is requested
if "asyncpg" not in DATABASE_URL and "aiosqlite" not in DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL does not request an async driver (asyncpg/aiosqlite).\n"
        "Use a URL like: postgresql+asyncpg://USER:PASSWORD@HOST:PORT/DBNAME\n"
        "and ensure `asyncpg` is installed in your environment (pip install asyncpg)."
    )
SessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
# generator - uses yield and after it uses it can be used in try block 
# after the use it is closed
# prevents the memory leek , connection to db is closed properly
# it creates session for each request and closes it after the request
# ensures that each request has its own session