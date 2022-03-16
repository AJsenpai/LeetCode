class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol=[]
        
        def backtrack(remain,comb,nex):
			# solution found
            if remain==0:
                sol.append(comb.copy())
            else:
				# iterate through all possible candidates
                for i in range(nex,n+1):
					# add candidate
                    comb.append(i)
					#backtrack
                    backtrack(remain-1,comb,i+1)
					# remove candidate
                    comb.pop()
            
        backtrack(k,[],1)
        return sol
#         if not n or k<=0:
#             return []
        
#         buffer = [None] * k
#         result = []
#         a = [i for i in range(1,n+1)]
        
#         self.solve(a,buffer,0,0,result)
#         return result
    
#     def solve(self,a,buffer,bufferIdx,startIdx,result):                
#         if bufferIdx == len(buffer):            
#             print(buffer)
#             # result.append(buffer)
#             return 
        
        
#         if startIdx==len(a):
#             return 
        
#         for i in range(startIdx,len(a)):            
#             buffer[bufferIdx] = a[i]
#             self.solve(a,buffer,bufferIdx+1,i+1,result)
        
        
        
        