class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # List of available digits
        numbers = list(range(1, n + 1))
        # Precompute factorials: factorial[i] = i!
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        # k is 1-indexed, so convert to 0-indexed
        k -= 1

        result = []

        for i in range(n, 0, -1):
            # Index of the digit to pick from the remaining numbers
            index = k // factorial[i - 1]
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= factorial[i - 1]

        return ''.join(result)