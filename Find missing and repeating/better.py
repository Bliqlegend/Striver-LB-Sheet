class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        nums = [0,0]
        miss = 0
        repeat = 0
        for i in range(n):
                if arr[abs(arr[i])-1] > 0:
                    arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
                else: 
                    repeat = abs(arr[i])
                    nums[0] = repeat
                    
        
        for i in range(n):
                if arr[i]>0:
                    miss = i+1
                    nums[1] = miss
                    
        return nums