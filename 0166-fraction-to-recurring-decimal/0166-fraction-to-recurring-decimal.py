class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        if denominator == 1:
            return str(numerator)
        check = denominator
        while check % 5 == 0:
            check //= 5
        while check % 2 == 0:
            check //= 2
        if str(numerator/check)[-1]=="0":
            return str(numerator/denominator)
        res = str(format(numerator/denominator,'.32'))
        first = 2
  
        while res[first] not in res[first+1:]:

            first += 1
        idx = res[first+1:].index(res[first])
        while first < len(res)-1 and not(res[first:first+idx+1] == res[first+idx+1:first+(idx+1)*2] == res[first+(idx+1)*2:first+(idx+1)*3]):
            print(res[first:first+idx+1], res[first+idx+1:first+(idx+1)*2], res[first+(idx+1)*2:first+(idx+1)*3])
            first += 1
            if res[first] not in res[first+1:]:
                continue
            idx = res[first+1:].index(res[first])
            print(res[first:first+idx+1], res[first+idx+1:first+(idx+1)*2], res[first+(idx+1)*2:first+(idx+1)*3])
        
        res = res[:first+1+idx]
        res += ")"
        return res[:first] + "(" +res[first:]
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        remainders = {}

        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(result)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        if remainder in remainders:
            idx = remainders[remainder]
            result.insert(idx, '(')
            result.append(')')

        return ''.join(result).rstrip(".")