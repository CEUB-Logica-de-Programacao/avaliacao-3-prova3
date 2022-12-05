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
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans []


if __name__ == '__main__':
    print(bonus(10))
