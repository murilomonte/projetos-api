from typing import Literal, Optional
from pydantic import BaseModel

## TODO: Buscar sobre o Field do pydantic
# https://fastapi.tiangolo.com/tutorial/query-param-models/#query-parameters-with-a-pydantic-model

class Message(BaseModel):
    message: str

class Project(BaseModel):
    title: str
    description: str
    priority: Literal[1, 2, 3]
    status: Literal["Planejado", "Em Andamento", "Concluído", "Cancelado"]

class ProjectDB(Project):
    id: int

class ProjectList(BaseModel):
    projects: list[ProjectDB]

class FilterParams(BaseModel):
    skip: Optional[int] = None # Número de registros a pular (para paginação).
    limit: Optional[int] = None # Número máximo de registros a retornar.
    status: Optional[Literal["Planejado", "Em Andamento", "Concluído", "Cancelado"]] = None # Filtrar por status do projeto.
    priority: Optional[Literal[1, 2, 3]] = None  # Filtrar por prioridade