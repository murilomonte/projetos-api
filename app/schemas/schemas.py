from typing import Any, Literal, Optional
from fastapi import Query
from pydantic import BaseModel, field_validator
from datetime import datetime
import uuid

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
    id: uuid.UUID
    created_at: datetime


class ProjectList(BaseModel):
    projects: list[ProjectDB]


class FilterParams(BaseModel):
    skip: int = Query(0, ge=0)  # Número de registros a pular (para paginação).
    limit: int = Query(10, gt=0, le=100)  # Número máximo de registros a retornar.
    status: Optional[Literal["Planejado", "Em Andamento", "Concluído", "Cancelado"]] = None # Filtrar por status do projeto.)
    priority: Optional[Literal[1, 2, 3]] = None  # Filtrar por prioridade

    @field_validator('priority', mode='before')
    def priority_to_int(cls, value: Any) -> Any:
        if isinstance(value, str) and value.isdigit():
            return int(value)
        return value
