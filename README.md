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

# API
- Swagger AI -- validation of API