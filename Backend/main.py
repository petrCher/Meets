from fastapi import FastAPI
import uvicorn
from routes.profile import profile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Приложение для знакомств", description="Познакомьтесь с интересными людьми")

app.include_router(profile)

# --------------------------
# enable cors, or cross origin request something
# allows frontend to talk to backend
#
# app = FastAPI()

# address of your live-server in quotes
origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------

# i specified 0.0.0.0 because apparently 127.0.0.1 cannot be reached outside of the docker container
if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')
