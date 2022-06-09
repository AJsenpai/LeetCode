class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        def solve(r,c):
            # OOB
            if r<0 or c<0 or r>len(image)-1 or c>len(image[0])-1:
                return 
            
            # if already filled with new color or dpesn't match with adjacent colors
            if image[r][c]==newColor or image[r][c]!=color:
                return 
            
            image[r][c] = newColor
            solve(r+1,c)
            solve(r-1,c)
            solve(r,c+1)
            solve(r,c-1)
            return

            
        
        color = image[sr][sc]
        solve(sr,sc)
        return image