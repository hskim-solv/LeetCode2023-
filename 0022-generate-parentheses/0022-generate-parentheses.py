class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p: str, left: int, right: int) -> str:
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))

  