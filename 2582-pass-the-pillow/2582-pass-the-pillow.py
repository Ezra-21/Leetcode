class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position = 1
        change_direction = False
        for i in range(time):
            if not change_direction:
                position += 1
                if position == n:
                    change_direction = True
            else:
                position -= 1
                if position == 1:
                    change_direction = False

        return position


