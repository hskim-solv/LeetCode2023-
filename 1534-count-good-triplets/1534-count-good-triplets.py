class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans, lenth = 0, len(arr)

        for i in range( 0, lenth - 2 ):
            for j in range(i + 1, lenth - 1):
                for k in range(j + 1, lenth ):
                    if abs(arr[i] - arr[k]) <= c:
                        if abs(arr[j] - arr[k]) <= b:
                            if abs(arr[i] - arr[j]) <= a:
                                ans += 1
        return ans

        