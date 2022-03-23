class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for sublist in image:
            # flip horizontally - swap
            sublist.reverse()
            # invert - compliment
            self.invert(sublist)            
        return image
    
    def invert(self,a):
        for i,num in enumerate(a):
            num ^= 1 #xor
            a[i] = num
    
        