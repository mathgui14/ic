def calcular_variacao_total(lista_valores):
    # Inicializa a variável para armazenar a variação total
    variacao_total = 0
    
    # Itera sobre a lista de valores
    for i in range(len(lista_valores) - 1):
        # Calcula a diferença entre o valor atual e o próximo valor
        variacao = abs(lista_valores[i + 1] - lista_valores[i])
        
        # Adiciona a variação ao total
        variacao_total += variacao
    
    return variacao_total

# Exemplo de uso com a lista (10, 20, 30, 40, 50, 60)
valores_exemplo = [400, 400, 400, 600, 500, 400]
resultadov = calcular_variacao_total(valores_exemplo)

print(f"A variação total é: {resultadov}")


def calcular_media_dos_filtros(valores_filtros):
    # Calcula a soma dos valores dos filtros
    soma_filtros = sum(valores_filtros)/6
    
    # Divide a soma pelo valor 3.4
    media = soma_filtros / 3.390239132432
    #W=3.390239132432

    return media

# Exemplo de uso com uma lista de valores de filtros
valores_filtros_exemplo = [200,200,200,300,250,200]
resultadoe = calcular_media_dos_filtros(valores_filtros_exemplo)

print(f"A média dos filtros dividida por W é: {resultadoe:.2f}")

#valor puro
P = 400
#E é a média dos ultimos 6 valores filtrados dividido por 3.39...
E = resultadoe
D = resultadov/294
F = ((E*P)*(D))/10
print (f"o valor filtrado é: {F}")

#calculo para L
L = D*(F/100)

if L < 5:
        print(f"Resultado filtrado (L): {L:.2f} - futil")
elif L > 10:
        print(f"Resultado filtrado (L): {L:.2f} - util")
   

#print (f"o valor de L é: {L}") se quiser tirar a classificação