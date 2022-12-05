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
    # Escreva seu código aqui
def isValid(s):
    a=Counter(s)
    val=list(a.values())
    res=Counter(val)
    v=list(res.keys())
    if len(s)==1 or (max(v)-min(v))==0:
        return'YES'
    elif len(v)<3 and ((max(v)-min(v)==1 and res.get(max(v))==1) or (min(v)==1 and res.get(min(v))==1)):
        return 'YES'
    else:
        return'NO' 

if __name__ == '__main__':
    print(q5('abcc'))
