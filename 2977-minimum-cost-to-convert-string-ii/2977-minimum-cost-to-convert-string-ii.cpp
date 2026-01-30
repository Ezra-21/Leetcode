class Solution {
public:
    long long minimumCost(
        string source, 
        string target,
        vector<string>& original,
        vector<string>& changed,
        vector<int>& cost
    ) {
        int n = source.size();

        // Build Index {substring -> id}
        unordered_map<string, int> index;
        index.reserve(original.size() * 2 + changed.size() * 2);
        for (auto &s : original)
            if (!index.count(s)) 
                index[s] = index.size();
        for (auto &s : changed)
            if (!index.count(s)) 
                index[s] = index.size();

        int K = index.size();
        const long long INF = 1e18;

        // Create Distances
        vector<vector<long long>> dist(K, vector<long long>(K, INF));
        for (int i = 0; i < cost.size(); ++i) {
            int u = index[original[i]], v = index[changed[i]];
            if (cost[i] < dist[u][v])
                dist[u][v] = cost[i];
        }

        // Floyd-Warshall for shortest paths
        for (int k = 0; k < K; ++k)
            for (int u = 0; u < K; ++u) 
                if (dist[u][k] != INF)
                    for (int v = 0; v < K; ++v) 
                        if ((dist[k][v] != INF) && (dist[u][k] + dist[k][v] < dist[u][v]))
                            dist[u][v] = dist[u][k] + dist[k][v];
                
        unordered_set<int> lengths;
        lengths.reserve(original.size() * 2);
        for (auto &s : original) 
            lengths.insert(s.size());

        // DP
        vector<long long> dp(n + 1, INF);
        dp[0] = 0;

        for (int i = 0; i < n; ++i) {
            if (dp[i] == INF) continue;

            if (source[i] == target[i])
                dp[i + 1] = min(dp[i + 1], dp[i]);

            // For each position i we try to match all possible substring lengths
            for (int l : lengths) {
                if (i + l > n) continue;

                string subS = source.substr(i, l);
                string subT = target.substr(i, l);

                auto itU = index.find(subS);
                if (itU == index.end()) continue;
                auto itV = index.find(subT);
                if (itV == index.end()) continue;

                int u = itU->second;
                int v = itV->second;

                if (dist[u][v] != INF)
                    dp[i + l] = min(dp[i + l], dp[i] + dist[u][v]);
            }
        }

        return dp[n] == INF ? -1 : dp[n];
    }
};