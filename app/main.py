from fastapi import FastAPI
from app.router.projects import project_router

app: FastAPI = FastAPI()
## Adiciona a rota
app.include_router(project_router)
