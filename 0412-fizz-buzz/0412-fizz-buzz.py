class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            name = ""
            if i % 3 == 0:
                name += "Fizz"
            if i % 5 == 0:
                name += "Buzz"
            if not name:
                name += str(i)
            result.append(name)
        return result
            
        