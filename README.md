
## To run the application
### Initialise virtual environment 
- python -m venv env ----> - .\env\Scripts\activate e<tab>S<tab>a<tab>
### Install requirements 
- pip install -r re<tab>
### Run the application
#### Run Backend
 - uvicorn app.main:app --reload
#### Run frontend 
- npm run dev


## Architecture
backend/
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


LLM - Large Language Models
Tokenization - sentence into words in list -> like this ["","",""]

Embeddingd- sentence into vector numbers -> like this [1,2,3,4,5]

Transformer -> "self attention mechanism" -> it is used to give the weights to the words in the sentence

SSE - Server sent events -> it is used to send the response from server to client in form of chunks of text so that we can show the response in form of chunks of text like chatbot ui

RAG -Retrival Augmented Generation - it is used to increase the accuracy of llm by providing relevant information to llm

context-window - it is the maximum number of words that the llm can process at a time

langchain -> its a framework to build llm's, its useful to connect llm to external sources of information -> like database, files, websites -> it is used to create complex workflows of llm -> like chatbot that can answer questions about specific documents



-Vercel ---> 
"user"://"password"

https://meet.google.com/ens-mkxd-wgb