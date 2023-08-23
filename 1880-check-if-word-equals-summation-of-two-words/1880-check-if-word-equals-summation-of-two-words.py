class Solution:
    def __init__(self):
        self.d = {
            'a':'0',
            'b':'1',
            'c':'2',
            'd':'3',
            'e':'4',
            'f':'5',
            'g':'6',
            'h':'7',
            'i':'8',
            'j':'9'
        }
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        up = 0
        firstWord,secondWord,targetWord = list(firstWord),list(secondWord),list(targetWord)
        while targetWord:
            res = 0
            if firstWord:
                res += int(self.d[firstWord.pop()])
            if secondWord:
                res += int(self.d[secondWord.pop()])
            up, sm = divmod(res+up, 10)
            if sm != int(self.d[targetWord.pop()]):
                return False
        if up:
            return False
        return True