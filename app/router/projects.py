from http import HTTPStatus
from datetime import datetime
from typing import Annotated
import uuid

from fastapi import APIRouter, HTTPException, Query
from app.schemas.schemas import Message, Project, ProjectDB, ProjectList, FilterParams  # type: ignore

project_router: APIRouter = APIRouter(prefix="/projects")

database: list[ProjectDB] = []


# Obtém todos os projetos - falta o filtro
@project_router.get("/", status_code=HTTPStatus.OK, response_model=ProjectList)
def read_all_projects(filter_query: Annotated[FilterParams, Query()]):
    projects: list[ProjectDB] = []

    ## Configura o skip
    if filter_query.skip:
        projects = database[filter_query.skip:]
    else:
        projects = database
    
    ## Filtra pelo status
    if filter_query.status:
        projects = [p for p in projects if p.status == filter_query.status]

    ## Filtra pela prioridade
    if filter_query.priority:
        projects = [p for p in projects if p.priority == filter_query.priority]

    ## Define um limite para retorno
    if filter_query.limit:
        projects = projects[:filter_query.limit]

    return {"projects": projects}


# Obtém somente um projeto - ok
@project_router.get("/{project_id}", status_code=HTTPStatus.OK, response_model=ProjectDB)
def read_project(project_id: uuid.UUID):
    ## TODO: tentar fazer isso da melhor forma
    for project in database:
        if project.id == project_id:
            return project
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail='Project not found'
    )


# Cria um projeto - ok
@project_router.post("/", status_code=HTTPStatus.CREATED, response_model=ProjectDB)
def create_project(project: Project):
    new_project = ProjectDB(
        id=uuid.uuid4(),
        title=project.title,
        description=project.description,
        priority=project.priority,
        status=project.status,
        created_at=datetime.now()
    )

    database.append(new_project)
    ## https://stackoverflow.com/questions/19199872/best-practice-for-restful-post-response
    return new_project


# Atualiza um projeto - ok
@project_router.put("/{project_id}", status_code=HTTPStatus.OK, response_model=ProjectDB)
def update_project(project_id: uuid.UUID):
    ## TODO: tentar fazer isso da melhor forma
    for project in database:
        if project.id == project_id:
            return project

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail='Project not found'
    )


# Deleta um projeto - ok
@project_router.delete("/{project_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_project(project_id: uuid.UUID):
    ## TODO: tentar fazer isso da melhor forma
    # https://stackoverflow.com/questions/25970523/restful-what-should-a-delete-response-body-contain
    found: bool = False
    for index, project in enumerate(database):
        if project.id == project_id:
            database.pop(index)
            found = True
            break

    if not found:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Project not found'
        )
        
