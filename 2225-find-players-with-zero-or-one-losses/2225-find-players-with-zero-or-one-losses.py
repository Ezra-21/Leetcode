class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_hashh = Counter()
        loser_hashh = Counter()

        winner = []
        loser = []

        for w,l in matches:
            winner_hashh[w]+=1
            loser_hashh[l]+=1

        for player in winner_hashh:
            if player not in loser_hashh:
                winner.append(player)
        for player in loser_hashh:
            if loser_hashh[player] == 1:
                loser.append(player)

        winner.sort()
        loser.sort()

        return winner , loser
        