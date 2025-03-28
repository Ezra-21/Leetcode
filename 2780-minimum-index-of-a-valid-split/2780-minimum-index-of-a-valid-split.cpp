#include <vector>

class Solution
{
public:
    int minimumIndex(std::vector<int> &nums)
    {
        int n = nums.size();
        int maxFreq = 0;

        // **Step 1: Determine the potential dominant element using Boyer-Moore Voting Algorithm**
        int candidate = -1, count = 0;
        for (int &num : nums)
        {
            if (count == 0)
                candidate = num;
            count += (num == candidate) ? 1 : -1;
        }

        // **Step 2: Confirm if the candidate is the dominant element**
        for (int num : nums)
        {
            if (num == candidate)
                ++maxFreq;
        }

        // **Step 3: Check if the candidate is actually dominant (more than half the array)**
        if (maxFreq * 2 <= n)
            return -1; // No valid dominant element

        // **Step 4: Find the minimum index where we can split the array**
        int leftFreq = 0, rightFreq = maxFreq;
        for (int i = 0; i < n; ++i)
        {
            if (nums[i] == candidate)
            {
                ++leftFreq;
                --rightFreq;
            }

            // Ensure that the dominant element remains valid in both partitions
            if (leftFreq * 2 > (i + 1) && rightFreq * 2 > (n - i - 1))
                return i;
        }

        return -1; // No valid split found
    }
};
