from app.schemas.task_schema import EntradaOrganizacao, RespostaOrganizacao

def organizar_tarefas(entrada: EntradaOrganizacao) -> RespostaOrganizacao:
    tarefas_ordenadas = sorted(
        entrada.tarefas,
        key=lambda t: t.prioridade,
        reverse=True
    )

    tempo_usado = 0
    cronograma = []

    for tarefa in tarefas_ordenadas:
        if tempo_usado + tarefa.duracao <= entrada.tempo_disponivel:
            tempo_usado += tarefa.duracao
            cronograma.append(f"{len(cronograma)+1}. {tarefa.descricao} ({tarefa.duracao} min)")

    tempo_restante = entrada.tempo_disponivel - tempo_usado

    return RespostaOrganizacao(
        cronograma=cronograma,
        tempo_total_usado=tempo_usado,
        tempo_restante=tempo_restante
    )