def verificar_intervalo(valor, inicio_intervalo, fim_intervalo):
    """
    Verifica se um valor está dentro do intervalo especificado.

    Args:
        valor (float): Valor a ser verificado.
        inicio_intervalo (float): Limite inferior do intervalo.
        fim_intervalo (float): Limite superior do intervalo.

    Returns:
        bool: True se o valor estiver dentro do intervalo, False caso contrário.
    """
    return inicio_intervalo <= valor <= fim_intervalo

valores = [339, 337, 345, 320, 335]
inicio_intervalo_exemplo = 330
fim_intervalo_exemplo = 340

for valor in valores:
    if verificar_intervalo(valor, inicio_intervalo_exemplo, fim_intervalo_exemplo):
        print(f"O valor {valor} está dentro do intervalo.")
    else:
        print(f"O valor {valor} está fora do intervalo.")
