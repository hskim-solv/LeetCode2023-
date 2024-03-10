class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        result = deque()
        result.appendleft(deck.pop(0))
        for i, elem in enumerate(deck):
            result.appendleft(result.pop())
            result.appendleft(elem) 
        return result