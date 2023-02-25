class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(n, base):
            if n < 1:
                return ''
            n, mod = divmod(n, base)
            return convert(n, base) + str(mod)
        for base in range(2, n - 1):
            converted_n = convert(n, base)
            if converted_n != converted_n[::-1]:
                return False  
        return True

        