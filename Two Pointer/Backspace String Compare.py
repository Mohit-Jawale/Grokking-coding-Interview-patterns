class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        ptr1 = len(s)
        ptr2 = len(t)
        s1= []
        s2 = []

        for i in range(0,ptr1):
            if s[i]=='#' and s1:
                s1.pop()
            elif s[i]=='#'and not s1:
                continue      
            else:
                s1.append(s[i])

        for i in range(0,ptr2):
            if t[i]=='#' and s2:
                s2.pop()
            elif t[i]=='#'and not s2:
                continue    
            else:
                s2.append(t[i])
        s1 = "".join(s1)
        s2 = "".join(s2)
        print(s1,s2)
        if s1==s2:
            return True
        return False            

