class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        small_queries,small_words = [],[]
        for word in queries:
            res = min(word)

            small_queries.append(res)
        
        for word in words:
            res = min(word)

            small_words.append(res)

        rep_q,rep_w = [],[]
        for i,word in enumerate(queries):
            count = word.count(small_queries[i])
            rep_q.append(count)

        for i,word in enumerate(words):
            count = word.count(small_words[i])
            rep_w.append(count)

        ans = []

        for val in rep_q:
            c = 0
            for num in rep_w:
                if val<num:
                    c+=1
            ans.append(c)

        return ans




        