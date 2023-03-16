class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        '''        acc = pref[0]
        for i in range(len(pref)-1):
            pref[i+1] ^= acc
            acc ^= pref[i+1]
            print(pref)'''
        acc = 0
        for i in range(len(pref)):
            pref[i] ^= acc
            acc ^= pref[i]
        return pref