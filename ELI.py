def filtragem_semg(F, E, P, V):
    # Constante para cálculo de E
    constante_E = 3.398338

    # Média dos últimos 6 valores filtrados
    E_media = sum(E) / len(E)

    # Cálculo do termo delta
    delta = V / (6 * 49)

    # Cálculo do resultado final L
    L = ( delta) * (F / 100)

    # Retorna o valor filtrado
    return L

# Exemplo de uso
F_atual = 2566 # Valor filtrado atual
E_ultimos_6 = [300, 350, 400, 450, 400, 300]  # Últimos 6 valores filtrados
P_puro = 400  # Valor puro
V_variacao = 350  # Variação (exemplo: 400 - 400 = 0)

resultado_filtrado = filtragem_semg(F_atual, E_ultimos_6, P_puro, V_variacao)
print(f"Resultado filtrado (L): {resultado_filtrado:.2f}")
