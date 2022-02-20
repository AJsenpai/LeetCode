class Solution:
    def duplicateZeros(self, a: List[int]) -> None:
        '''
        1. count number of zeroes
        2. new length without trimming upto array length = n + zeroCount
        3. pointer 1 = len(a) -1 
        4. pointer 2 = newlength -1 
        5. if new length < original length then
        6. start from back and copy values to new array from original 
           array (both are same just 2 pointers)
        7. if a[i] is zero copy again 
        '''
        
        n = len(a)
        
        zeroCount = a.count(0)        
        newLength = zeroCount + n
        i = n-1 
        j = newLength -1 
        
        while j>=0:
            if j < n:
                a[j] = a[i] # copy
            j -= 1
            if a[i] == 0:
                if j<n:
                    a[j] = a[i]
                j -= 1
            i -= 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            