class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # this is my solution but TLE come so we going to see video
         # if k <= 0 or k > len(nums):
          #  return []
        #left=0
        #right=k-1
        #finalresult=[]
        #while right<len(nums): #for window slide
          #  maxnum=[]
           # for i in range(left,right+1,1):
           #     maxnum.append(nums[i])
            #res=max(maxnum)
            #finalresult.append(res)
            #right+=1
            #left+=1
        #return finalresult
        #next solution by video seeing and then solve using deque this is main
        output=[]
        q=collections.deque()# index
        l=r=0
        while r<len(nums):
            #pop smaller values from q
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            #remove left val from window
            if l>q[0]:
                q.popleft()
            if(r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output

