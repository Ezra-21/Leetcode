class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        std::vector<int> res = {0, 0};
        int row = mat.size();
        for (int i = 0; i < row; i++){
            int count = std::accumulate(mat[i].begin(), mat[i].end(), 0);
            if (count > res[1]){
                res[0] = i;
                res[1] = count;
            }
        }
        return res;
    }
};