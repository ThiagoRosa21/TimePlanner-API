from fastapi import APIRouter
from App.schemas.task_schemas import EntradaOrganizacao, RespostaOrganizacao
from App.services.scheduler import organizar_tarefas

router = APIRouter()

@router.post("/organizar", response_model=RespostaOrganizacao)
def organizar(entrada: EntradaOrganizacao):
    return organizar_tarefas(entrada)