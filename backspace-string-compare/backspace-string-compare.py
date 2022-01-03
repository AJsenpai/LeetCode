class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        index1 = len(s)-1
        index2 = len(t)-1
        while index1>=0 or index2>=0:
            p1 = self.next_valid_char(s, index1)
            p2 = self.next_valid_char(t, index2)
            if p1<0 and p2<0:
                return True
            if p1<0 or p2<0:
                return False
            if s[p1]!=t[p2]:
                return False
            index1 = p1-1
            index2 = p2-1
        return True
    
    def next_valid_char(self,s,i):
        backspace_count = 0
        while i>=0:
            if s[i] == '#':
                backspace_count += 1
            elif backspace_count>0:
                backspace_count -= 1
            else:
                break
            i -= 1
        return i