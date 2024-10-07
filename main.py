#!/usr/bin/env python3

from fastapi import FastAPI
from models.base import Base
from pydantic_schemas.user_create import UserCreate
from routes import auth, song
from database import engin
import uvicorn
import os

app = FastAPI()
app.include_router(auth.router, prefix='/auth')
app.include_router(song.router, prefix='/song')

# postgresql://render_example_q167_user:1YoSQ50RhpjigXrhXClvfrkGpc6ccBOT@dpg-cs1oh45ds78s73b7umb0-a.singapore-postgres.render.com/render_example_q167

Base.metadata.create_all(engin)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use PORT from environment, default to 8000 for local testing
    uvicorn.run(app, host="0.0.0.0", port=port)



# from fastapi import FastAPI
# from models.base import Base
# from pydantic_schemas.user_create import UserCreate
# from routes import auth,song
# from database import engin
# import uvicorn


# app=FastAPI()
# app.include_router(auth.router,prefix='/auth')
# app.include_router(song.router,prefix='/song')

# Base.metadata.create_all(engin)


# uvicorn.run(app, host="192.168.225.63", port=8000)
   


# from fastapi import FastAPI
# from models.base import Base
# from pydantic_schemas.user_create import UserCreate
# from routes import auth, song
# from database import engin
# import uvicorn


# app = FastAPI()
# app.include_router(auth.router, prefix='/auth')
# app.include_router(song.router, prefix='/song')

# Base.metadata.create_all(engin)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
