def calcular_media_dos_filtros(valores_filtros):
    # Calcula a soma dos valores dos filtros
    soma_filtros = sum(valores_filtros)/6
    
    # Divide a soma pelo valor 3.4
    media = soma_filtros / 3.4
    
    return media

# Exemplo de uso com uma lista de valores de filtros
valores_filtros_exemplo = [150,175,200,225,200,150]
resultado = calcular_media_dos_filtros(valores_filtros_exemplo)

print(f"A média dos filtros dividida por 3.4 é: {resultado:.2f}")
