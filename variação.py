def calcular_variacao_total(lista_valores):
    # Inicializa a variável para armazenar a variação total
    variacao_total = 0
    
    # Itera sobre a lista de valores
    for i in range(len(lista_valores) - 1):
        # Calcula a diferença entre o valor atual e o próximo valor
        variacao = lista_valores[i + 1] - lista_valores[i]
        
        # Adiciona a variação ao total
        variacao_total += variacao
    
    return variacao_total

# Exemplo de uso com a lista (10, 20, 30, 40, 50, 60)
valores_exemplo = [100, 200, 300, 400, 500, 600]
resultado = calcular_variacao_total(valores_exemplo)

print(f"A variação total é: {resultado}")
