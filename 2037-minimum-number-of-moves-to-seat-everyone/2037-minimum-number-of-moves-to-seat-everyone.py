class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        move = 0
        for pos_seat,pos_stds in zip(seats,students):
            move += abs(pos_seat-pos_stds)

        return move

