class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def operation(num):
            count = 0
            while num != 1:
                count += 1
                if num % 2 == 1:
                    num = 3 * num + 1
                else:
                    num //= 2
            return count

        # Create a list of tuples (power, number)
        arr = [(operation(i), i) for i in range(lo, hi + 1)]

        # Sort by power first, and by the number itself in case of ties
        arr.sort(key=lambda x: (x[0], x[1]))

        # Return the k-th smallest number
        return arr[k - 1][1]
