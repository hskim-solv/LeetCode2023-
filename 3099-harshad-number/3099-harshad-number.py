class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = sum([int(digit) for digit in str(x)])
        return sum_of_digits if 0 == x % sum_of_digits else -1