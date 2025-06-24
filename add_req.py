import requests
from typing import Any, List

# URL base da API (substitua pela URL real da sua API)
API_URL = "http://localhost:8000/projects"

# Dados de exemplo para enviar
projects_data: List[dict[str, Any]] = [
    {
        "title": "Projeto A",
        "description": "Descrição do Projeto A",
        "priority": 1,
        "status": "Planejado"
    },
    {
        "title": "Projeto B",
        "description": "Descrição do Projeto B",
        "priority": 2,
        "status": "Em Andamento"
    },
    {
        "title": "Projeto C",
        "description": "Descrição do Projeto C",
        "priority": 3,
        "status": "Concluído"
    },
    {
        "title": "Projeto D",
        "description": "Descrição do Projeto D",
        "priority": 1,
        "status": "Cancelado"
    }
]

def adicionar_projetos(api_url: str, projetos: List[dict[str, Any]]) -> None:
    for projeto in projetos:
        response = requests.post(api_url, json=projeto)
        if response.status_code == 200 or response.status_code == 201:
            print(f"Projeto '{projeto['title']}' adicionado com sucesso!")
        else:
            print(f"Erro ao adicionar projeto '{projeto['title']}': {response.status_code} - {response.text}")

if __name__ == "__main__":
    adicionar_projetos(API_URL, projects_data)
