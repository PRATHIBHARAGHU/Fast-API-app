
## To run the application
### Initialise virtual environment 
- python -m venv env ----> - .\env\Scripts\activate e<tab>S<tab>a<tab>
In ubuntu . env/bin/activate
### Install requirements 
- pip install -r re<tab>
### Run the application
#### Run Backend
 - uvicorn app.main:app --reload
#### Run frontend 
- npm run dev


## Architecture
Backend/
    app/
        -- main.py   ------> Entry point creates fastapi app
        register all routers
        -- database.py  --------> Database connection (PostgreSQL + )
    SQLALCHEMY
    models/  -------> 
        -- users.py
        -- company.py
        -- job.py
    schemas/
        -- users.py
        -- company.py
        -- job.py
    routers/
        -- users.py
        -- company.py
        -- job.py
    utils.py/ 
        -- oauth2.py
        -- security.py
        -- token.py
        --
    alembic.ini
    alembic/env.py
    
## flow of the app
 react -> login -> oauthform -> accesstoken -> store in local -> send with every request -> logout

 react -> axios -> fastapi_url -> token -> header -> response -> store in local browser to remember the login-> then you can call or use apis you want-> then for all the api's like createjob.jsx use this axios function to call the api's-> fetchcompany() use axios.get(url)-> fastapi-> postgresql_db-> return response to axios-> store in local state and show in UI


