class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        result = deque([deck.pop(0)])
        for elem in deck:
            result.appendleft(result.pop())
            result.appendleft(elem) 
        return result