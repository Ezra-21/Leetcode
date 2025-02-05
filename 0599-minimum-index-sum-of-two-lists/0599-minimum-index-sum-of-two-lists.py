class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_list1 = {}
        for i,strr in enumerate(list1):
            if strr not in hash_list1:
                hash_list1[strr] = i
        
        min_len = float('inf')

        collect = defaultdict(list)

        for i,strr in enumerate(list2):
            if strr in hash_list1:
                idx_sum = hash_list1[strr]+i
                collect[idx_sum].append(strr)
                if idx_sum < min_len:
                    min_len = idx_sum
        return collect[min_len]

        