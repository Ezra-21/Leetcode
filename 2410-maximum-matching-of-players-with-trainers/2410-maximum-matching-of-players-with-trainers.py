class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n,m = len(players) , len(trainers)
        left_1,left_2 = 0,0
        players.sort()
        trainers.sort()
        ans = 0
        while left_1 < n and left_2 < m:
            if players[left_1] <= trainers[left_2]:
                ans+=1
                left_1 += 1
            left_2 += 1
        return ans

        
        