class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))

        product = 1
        total = 0

        for digit in digits:
            product *= digit
            total += digit

        return product - total
