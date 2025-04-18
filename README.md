# TimeSaver API

Uma API desenvolvida com FastAPI para ajudar as pessoas a organizarem suas tarefas com base no tempo disponível.

## Como usar

### 1. Clone o projeto
```bash
git clone https://github.com/seuusuario/timesaver-api.git
cd timesaver-api
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Rode a aplicação
```bash
python run.py
```

### 4. Acesse a documentação automática (Swagger)
[http://localhost:8000/docs](http://localhost:8000/docs)

## Exemplo de Requisição
POST `/organizar`
```json
{
  "tempo_disponivel": 240,
  "tarefas": [
    {"descricao": "Estudar", "duracao": 60, "prioridade": 5},
    {"descricao": "Exercício", "duracao": 90, "prioridade": 4},
    {"descricao": "Almoço", "duracao": 60, "prioridade": 1},
    {"descricao": "E-mails", "duracao": 30, "prioridade": 3}
  ]
}
```

## Resposta
```json
{
  "cronograma": [
    "1. Estudar (60 min)",
    "2. Exercício (90 min)",
    "3. E-mails (30 min)",
    "4. Almoço (60 min)"
  ],
  "tempo_total_usado": 240,
  "tempo_restante": 0
}
```