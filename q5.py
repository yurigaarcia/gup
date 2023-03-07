# Solicitar que o usuário insira uma palavra ou frase
palavra = input("Digite uma palavra ou frase: ")

# Converter a palavra em uma lista de caracteres
lista_caracteres = list(palavra)

# Definir um índice inicial e um final
indice_inicial = 0
indice_final = len(lista_caracteres) - 1

# Enquanto o índice inicial for menor que o índice final
while indice_inicial < indice_final:
    # Trocar os caracteres nos índices
    lista_caracteres[indice_inicial], lista_caracteres[indice_final] = lista_caracteres[indice_final], lista_caracteres[indice_inicial]
    
    # Incrementar o índice inicial e decrementar o índice final
    indice_inicial += 1
    indice_final -= 1

# Converter a lista de caracteres de volta para uma string
palavra_invertida = ''.join(lista_caracteres)

# Imprimir a palavra invertida
print("A palavra ou frase invertida é:", palavra_invertida)

