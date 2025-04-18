from pydantic import BaseModel

class TaskModel(BaseModel):
    descricao: str
    duracao: int
    prioridade: int