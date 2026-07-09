
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

#### every llm has a default model --> Transformers

RAG - Retrival Augmented Generation
It is used to increase the accuracy of llm by providing relevant information to the llm -> it is used to increase the accuracy of llm by providing relevant information to the llm


How will it make chunks in vector db?
let's say we have 3 documents --> each one has 100 words so it will make 3 chunks -- each chunk will overlap with previous chunk by 100 chars -> so each chunk will have 500 chars
like 0-499 --> 400-899 ---> 800-1399

this chunk will be converted into vectors
eg: I am a developer, I have 3 years of expirience in python developement. I have good knowledge of python developement and I am  good python developer. I have good knowledge of fastapi 
--> will convert all the 3 chunks into vectors

#### godlocks principle ---> just right amount of information
semantic search -> It is used to find the most relevant information to the query -> It is used to find the most relevant information to query.

semantic similarity
It is used to find the most similar vectors
if two vectors are close to each other and similar

cosine similarity -> used iin nlp to find the similarity between two vectors

quadrantdb -is a vector database
it is used to store the vectors and do the semantic search
embeddings model -> it is used to convert the text into vectors

initially without rag
user query -> send to llm -> here transformers model will answer based on its training data -> response

with rag
user query -> embed done by embeddings model -> vector -> semantic search done by quadrantdb(vectordb) -> retrieve relevant chunks -> construct prompt -> combined text+query -> llm -> response

## Before Deployement checklist
.env configured
on startup create all tables in db
async await in every api and function and sessions handling for all apis
exception handeling for all apis ->
eg.
1. resourse not found
2. internal server error
3. bad request
4. unauthorized 
5. forbidden
6. validation error
7. email already exists
8. password incorrect
9. company not found

