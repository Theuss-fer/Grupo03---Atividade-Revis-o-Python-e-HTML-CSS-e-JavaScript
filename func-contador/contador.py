import string

def contator(texto):
    texto = texto.lower()
    
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    
    palavras = texto.split()
    
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
            
    return contagem


entrada = input("Digite uma frase: ")
resultado = contator(entrada)
print("Contagem de palavras:")
print(resultado)