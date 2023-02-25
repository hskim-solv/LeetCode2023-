class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(n, base):
            if n < 1:
                return ''
            n, mod = divmod(n, base)
            return convert(n, base) + str(mod)
        for base in range(2, n - 1):
            converted_n = convert(n, base)
            for i in range(len(converted_n)//2):
                if converted_n[i] != converted_n[-(i+1)]:
                    return False  
        return True

        