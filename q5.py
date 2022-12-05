# ## Questão 5
#
# Sherlock considera uma string válida se todos os caracteres dela aparecerem o mesmo número de vezes.
# Também é válida se ele puder remover apenas um caractere, e os caracteres restantes aparecerem o
# mesmo número de vezes. Dada uma cadeia de caracteres, determine se ela é válida. Se for o caso, retorne `True`, caso
# contrário retorne `False`.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# aabbcd
# ```
#
# A saída deve ser:
#
# ```
# False
# ```
#
# Isso porque não é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abcc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q5(s):
    caracteres = {}
    for i in s:
        if i in caracteres:
            caracteres[i] += 1
        else:
            caracteres[i] = 1
    min = caracteres[i]
    max = caracteres[i]
    qdict = {}
    for i, qnt in caracteres.items():
        if qnt in qdict:
            qdict[qnt] += 1
        else:
            qdict[qnt] = 1
        if qnt < min:
            min = qnt
        if qnt > max:
            max = qnt
    if len(qdict) == 1:
        return True
    elif len(qdict) == 2:
        if qdict[max] == 1 and max - min == 1:
            return True
        elif qdict[min] == 1 and min == 1:
            return True
    return False
if __name__ == '__main__':
    print(q5('abcc'))
