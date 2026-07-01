# Fast-API-app

## Creating fast api application

# CRUD operations
- Create
- Read
- Update
- Delete

# Rest API
- Get
- POST
- PUT 
- DELETE

# status codes
- 200 OK
- 201 Created
- 204 No Content
- 400 Bad Request
- 401 Unauthorised
- 403 Forbidden
- 404 Not Found
- 405 Method Not Allowed
- 409 Conflict
- 500 Internal Serval Error

# Architecture of fastapi application
- Model -- {Defines database tables}
- Router -- {routes requests to controller}
- Controller -- {Controls the logic, endpoints}
- Service -- {buisiness logic}
- Repository -- {data access layer}
- Middleware -- {request processing pipeline}
- Schema -- {Static models for validation}

# database
## relational databases
- mysql
- postgressql
- sqlite
- sql server

## non-relational databases
- mongoDB
- dynamodb
- redis
- cassandra


# constraints in database {imp}
- primary key --eg: student_id, staff_id
- foriegn key --eg: department_id in std table
- unique --eg: email
- not null --eg: name
- check --eg: salary>0
- default --eg: timestamp: func.now()

# Modules
- SQLAlchemy -- orm (object Relational mappinng)
- fastapi -- web framework
- uvicorn -- server for running fastapi application ---> "uvicorn app.main:app --reload"
- psycopg2 -- postgresql driver
- Swagger AI -- validation of API
- Pydantic -- Data validation
- typing-extensions -- type hints
- alembic -- database migration tool

# Concepts:
- ORM 
    - Object Mapping -->to convert pythonm code to sql commands without writing SQL commands
    - Dependancy injection -->To install dependencies into router handlers
    - Session maker - To create a session with Database
    - SessionLocal - To create session with the database for a single request
    - declarative_base - To create a base class for all the models

# Alembic - to modify tables or constraints of a particular table in models of postgres
- pip install alembic

- alembic -> env.py ->  from imported models -> metadata data
- alembic.ini -->  SQLALCHEMY url to postgres database 

- alembic init alembic -- creates new file alembic
- alembic revision --autogenerate -m "Initial migration"
- alembic upgrade head  -- to upgrade the file

## Frontend

- node -v
- npm install -g typescript
- tsc --version

- node "File_name.js"
### Typescript
- tsc "filename.ts" ----> create a new js file in the same name
- node "filename.js"

- npm init -y --- creates package.json

### Vite
-  npm install vite@latest
- npm create vite@latest-talentspark  ---> down arrow -->react --> typescript.

http://localhost:5173/