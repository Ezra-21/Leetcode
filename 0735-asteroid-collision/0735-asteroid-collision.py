class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            found = True
            while stack and stack[-1]>0 and val<0:
                if abs(val) > stack[-1]:
                    stack.pop()
                elif abs(val) == stack[-1]:
                    stack.pop()
                    found = False
                    break
                else:
                    found = False
                    break
            if found:
                stack.append(val)

        return stack

            

            