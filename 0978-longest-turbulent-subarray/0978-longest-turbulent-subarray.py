class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def solve(arr, evod):
            max_length = 1  # Maximum turbulence length
            start = 0  # Start of the current turbulent subarray

            for end in range(len(arr) - 1):
                if end % 2 == evod:  # When even/odd index matches the condition
                    if arr[end] >= arr[end + 1]:  # Condition breaks
                        start = end + 1
                else:  # When index doesn't match evod
                    if arr[end] <= arr[end + 1]:  # Condition breaks
                        start = end + 1

                # Update the maximum turbulence length
                max_length = max(max_length, end - start + 2)

            return max_length

        # Return the maximum length for both patterns (0 for even, 1 for odd)
        return max(solve(arr, 0), solve(arr, 1))
