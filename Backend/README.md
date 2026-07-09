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

# mysql example
CREATE TABLE Students(
  Student_ID int PRIMARY KEY, 
  LastName varchar(255) NOT NULL,
  FirstName varchar(255)
);

# Modules
- SQLAlchemy -- orm (object Relational mappinng)
- fastapi -- web framework
- uvicorn -- server for running fastapi application ---> 'uvicorn app.main:app --reload'
- psycopg2 -- postgresql driver
- Swagger AI -- validation of API
- Pydantic -- Data validation
- typing-extensions -- type hints
- alembic -- database migration tool

# Concepts:
- ORM 
    - Object Mapping -->to convert pythonm code to sql commands without writing SQL commands
- Depends
    - Dependancy injection -->To install dependencies into router handlers
- Session maker 
    - To create a session with Database
- SessionLocal 
    - To create session with the database for a single request
- declarative_base 
    - To create a base class for all the models

# Alembic - to modify tables or constraints of a particular table in models of postgres
- pip install alembic
- alembic init alembic -- creates new file alembic

- alembic -> env.py ->  from imported models -> metadata data
- alembic.ini -->  SQLALCHEMY url to postgres database ---> postgresql://user:password@host:port/database_name

- alembic revision --autogenerate -m "Initial migration"
You will have a new version update with def upgrade() in that for eg:713e98317319.py before doing upgrade check that.
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



# for user authentication in JWT
- pip install passlib --- used to encrypt passwords
# hashing algorithm
argon2
bcrypt

- pip install python-jose[cryptography]

- Jose --> used to create jwt tokens --> used to authenticate and authorize users its in the format xxxx.yyyy.zzzz basically 3 parts 
1. header -> algo + token type: {alg:HS256, typ:JWT}
2. payload -> data, for eg: {user_id:1, role:admin}
3. signature -> used to clarify the token: {hash(header + payload + secretkey)}
- access token -> used to acces protected resources
- refresh tokens -> used to refresh access tokens


pip install python-multipart

## Utils 

## RBAC
- Role Based Access Control
-> used to give different permissionsto different roles
-> eg: admin can do anything, user can do only specific things
-> use oauth2 module to implement RBAC
-> get_current_user() - for authenticated user
-> role_required() - fro role based access control
-> create_access_token() - for creating access token with(secret_key, algorithm, payload) - token created then 
->verify_access_token() - for decoding acess token with (Secret  key, algorith.token) - token decoded then

## Flow of application 
1. login --> create access token 
2. access token --> get current user
3. current user --> get role --> role_required --> access protected resources

# LLM
- pip install langchain
- pip install langchain-community
- pip install langchain-google-genai
- pip install python-dotenv
- pip install langchain-ollama -if ollama using locally