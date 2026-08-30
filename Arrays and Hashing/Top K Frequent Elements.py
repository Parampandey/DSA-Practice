class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # there are two method to slove first is hashap and sort the map by value is time complexitity is nlogn bt we also use heap or buckt sort to reduce it
        #method one
        dict={} 
        for num in nums:
            if num not in dict   :
                dict[num]=1
            dict[num]+=1
            #dict[num] = dict.get(num, 0) + 1 you can diectly use this also to avoid above if
        # sorted(dict,key=dict.get, reverse=True) means #sorted give sort item in list key is tumhe kiss pr sorting krni h muje value pr krni h to me key=dict.get kia hu dict.get krne s value aa jaegi aur vo key ho jargi usi p sorting hogi reverse=true menas sort in decesending order
        # last me [:k]meaning sort krne k baad jo list aaegi decending m to muje most frequent k element chai to uss list m s starting 0 s k-1 tk k element means only k element hi reutrun kro 
        topk=sorted(dict,key=dict.get, reverse=True)[:k]  # sort krrke y key return karega
        return topk

        #2nd method min heap 
        #insted of sorting all elemet do only
       # Count frequencies.
        #Keep only the k most frequent elements in a min heap. T(C)=O(n+mlogk) k=heap size count=o(n) heap =mlogk

        #method 3 best  T(C)=O(N) Bucket sort  create bucket no sorting needed tc=o(n)
        #Observation: A number can appear at most n times. means size of array
        #isme hota y h ki ex[1 1 1 2 2 3] hm 6 length ki bucket bna denge ab y check karenge ki 1 kitni baar aaya h ,1 3 baar aaya h to one place pr y 1 ki bucket me 3 daal denge means 1 to map kr denge 3 se 1:3, same 2:2 ,3:1 ek element maximum utni baar hi aa skta h jitna array ki len h islea hum array ki length jitna bucket banae
        # traverse bucket from higher freq to lower so start from high bucket most freq vla the go down till k elemtn which want so no sorting needed we get ans 

