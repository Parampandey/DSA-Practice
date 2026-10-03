class Solution:
    def isPalindrome(self, s: str) -> bool :
        st=s.lower()
        st=st.replace(" ","")
        result=""
        for ch in st:
            if ch.isalnum():
                result+=ch

        i=0;
        j=len(result)-1
        while (i<=j):
            if result[i]!=result[j]:
                return False
            i=i+1
            j=j-1

        return True

            
