class Solution {
public:
    bool flag(int row,int col,vector<vector<char>>& ans){
        for(int i=row; i>=0; i--){
            if(ans[i][col]=='Q') return false;
        }
        for(int i=row,j=col; i>=0 && j>=0; i--,j--){
            if(ans[i][j]=='Q') return false;
        }
        for(int i=row,j=col; i>=0 && j<ans.size(); i--,j++){
            if(ans[i][j]=='Q') return false;
        }
        return true;
    }
    void find(int n,int i,vector<vector<char>>& q,int& cnt){
        if(i==n){
            cnt++;
            return;
        }
        for(int j=0; j<n; j++){
            if(flag(i,j,q)){
                q[i][j]='Q';
                find(n,i+1,q,cnt);
                q[i][j]='.';
            }
        }
    }
    int totalNQueens(int n) {
        vector<vector<char>>q(n,vector<char>(n,'.'));
        int cnt=0;
        find(n,0,q,cnt);
        return cnt;
    }
};