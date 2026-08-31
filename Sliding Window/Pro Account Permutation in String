class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #herer T(C)=O(nm) where n is length of the big/main string and m is       length  of the small/pattern string. you can also solve in T(C)=O(N)
        #self
        count1=[0]*26 # for s1
        count2=[0]*26 #
        if len(s1)>len(s2):
            return False        #if you don't write code will run it just for fast
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')]+=1
        left=0
        right=len(s1)
        
        while(right<=len(s2)):
            count2=[0]*26
            for i in range(left,right,1):
                count2[ord(s2[i])-ord('a')]+=1
            if count1==count2:
                return True
            left+=1
            right+=1
        return False
    
