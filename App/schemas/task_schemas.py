from pydantic import BaseModel
from typing import List

class Tarefa(BaseModel):
    descricao: str
    duracao: int
    prioridade: int

class EntradaOrganizacao(BaseModel):
    tempo_disponivel: int
    tarefas: List[Tarefa]

class RespostaOrganizacao(BaseModel):
    cronograma: List[str]
    tempo_total_usado: int
    tempo_restante: int
