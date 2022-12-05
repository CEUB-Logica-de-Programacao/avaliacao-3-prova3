# ## Questão 4
#
# Você receberá uma string em [CamelCase](https://en.wikipedia.org/wiki/CamelCase). Ela possuí as seguintes propriedades:
#
# * É a concatenação de uma ou mais palavras, onde a primeira letra de cada palavra é maiúscula, e as demais são
#   minúsculas.
# * Não contém espaços, números ou caracteres especiais.
#
# Você deverá retornar o número de palavras na string.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# hexaVemEsseAno
# ```
#
# A saída deve ser:
#
# ```
# 4
# ```
#
# Isso porque a string possui 4 palavras: ``hexa``, ``Vem``, ``Esse`` e ``Ano``.
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q4(s):
    def camel_case_split(str): 
    words = [[str[0]]] 
  
    for c in str[1:]: 
        if words[-1][-1].islower() and c.isupper(): 
            words.append(list(c)) 
        else: 
            words[-1].append(c) 
  
    return [''.join(word) for word in words] 
    
s= str(input("Digite sua string"))
print(len(camel_case_split(s)))


if __name__ == '__main__':
    print(q4('hexaVemEsseAno'))
