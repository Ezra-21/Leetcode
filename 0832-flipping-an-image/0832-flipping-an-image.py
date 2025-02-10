class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            for col in range(len(image[0])):
                image[row][col] = abs(image[row][col] - 1)
            image[row].reverse()

        return image
        
        