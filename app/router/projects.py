from http import HTTPStatus
# from typing import Any, Union
from fastapi import APIRouter
project_router:APIRouter = APIRouter(prefix='/projects')

# Obtém todos os projetos
@project_router.get("/", status_code=HTTPStatus.OK)
def read_all_projects():
    return {"Hello": "World"}

# Obtém somente um projeto
@project_router.get("/{project_id}", status_code=HTTPStatus.OK)
def read_project():
    ...

# Cria um projeto
@project_router.post("/", status_code=HTTPStatus.CREATED)
def create_project():
    ...

# Atualiza um projeto
@project_router.put("/{project_id}", status_code=HTTPStatus.OK)
def update_project():
    ...

# Deleta um projeto
@project_router.delete("/{project_id}", status_code=HTTPStatus.OK)
def delete_project():
    ...