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
    x = 0
    for i in range(1, len(s)):
        if s[i] == s[i].upper():
            x +=1
    if len(s) > 0:
        x += 1
    return x
    
if __name__ == '__main__':
    print(len(q4('hexaVemEsseAno')))
