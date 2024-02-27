from collections import Counter

def filtrar_valores_repetidos(lista):
    # Conta a frequência de cada valor na lista
    contador = Counter(lista)
    
    # Filtra os valores que se repetem dentro da margem
    valores_repetidos = [valor for valor, frequencia in contador.items() if 200 <= valor <= 600 and frequencia > 1]
    
    return valores_repetidos

# Exemplo de uso com uma lista de valores
valores_exemplo = [300, 400, 500, 300, 600, 500, 700, 300]
valores_filtrados = filtrar_valores_repetidos(valores_exemplo)

print("Valores originais:", valores_exemplo)
print("Valores filtrados:", valores_filtrados)
