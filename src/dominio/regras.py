from datetime import timedelta, datetime


# Prazo padrão de devolução
def prazo_padrao():
    return timedelta(days=7)


# Cálculo simples de multa
def calcular_multa(data_prevista, data_devolucao, valor_dia=2.5):
    if data_prevista is None or data_devolucao is None:
        return 0.0

    atraso = (data_devolucao - data_prevista).days

    if atraso <= 0:
        return 0.0

    return atraso * valor_dia
