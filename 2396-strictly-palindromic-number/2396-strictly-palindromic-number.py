class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert_n(n, base):
            if n < 1:
                return ''
            n, mod = divmod(n, base)
            return convert_n(n, base) + str(mod)
        for base in range(2, n - 1):
            converted_n = convert_n(n, base)
            if converted_n != converted_n[::-1]: 
                return False
        return True

        