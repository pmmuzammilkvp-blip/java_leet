class Solution:
    def getPermutation(self, n, k):
        import math

        numbers = list(range(1, n + 1))
        k -= 1  # convert to 0-based index
        permutation = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            permutation.append(str(numbers.pop(index)))
            k %= fact

        return ''.join(permutation)
