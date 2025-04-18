def formatar_tempo(minutos: int) -> str:
    horas = minutos // 60
    mins = minutos % 60
    return f"{horas}h {mins}min" if horas else f"{mins}min"