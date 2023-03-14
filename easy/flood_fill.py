class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = image[sr][sc]

        def flood_fill(x, y):
            # check if we are within image's boundaries
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return

            # check if the colour needs to change
            if image[x][y] == color or image[x][y] != start_color:
                return

            # change colour
            image[x][y] = color

            # recursive calls to next pixels
            flood_fill(x - 1, y)
            flood_fill(x + 1, y)
            flood_fill(x, y + 1)
            flood_fill(x, y - 1)

        flood_fill(sr, sc)
        return image
