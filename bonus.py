# ## Desafio
#
# Dados ``n`` pares de parênteses, escreva uma função para gerar todas as combinações de parênteses bem formados.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# n = 3
# ```
#
# A saída deve ser:
#
# ```
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# ```
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def bonus(n):
    # Escreva seu código aqui
    def generate(result: List[str], s: str, _open: int, close: int, n: int):
    
    if _open == n and close == n:
        result.append(s)
        return
    
    if _open < n:
        generate(result, s + "(", _open + 1, close, n)
    # If we need more close parentheses to balance
    if close < _open:
        generate(result, s + ")", _open, close + 1, n)


def generateParenthesis(n: int) -> List[str]:
    
    result = []
    
    generate(result, "", 0, 0, n)
    return result

    return []


if __name__ == '__main__':
    print(bonus(10))
