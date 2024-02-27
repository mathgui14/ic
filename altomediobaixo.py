def filtragem_semg(F, E, P, V):
    constante_E = 3.398338

    E_media = sum(E) / len(E)
    delta = V / (6 * 49)
    L = delta * (F / 100)

    if L < 5:
        print(f"Resultado filtrado (L): {L:.2f} - futil")
    elif L > 10:
        print(f"Resultado filtrado (L): {L:.2f} - util")
   

# Exemplo de uso
F_atual = 2566 # Valor filtrado atual
E_ultimos_6 = [300, 350, 400, 450, 400, 300]  # Últimos 6 valores filtrados
P_puro = 400  # Valor puro
V_variacao = 2  # Variação (exemplo: 400 - 400 = 0)

filtragem_semg(F_atual, E_ultimos_6, P_puro, V_variacao)    