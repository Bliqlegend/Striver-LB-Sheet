 def maxSubArraySum(self,a,size):
        ##Your code here
        CurrentS = a[0]
        OverallS = a[0]
        for i in range(1,size):
            CurrentS = max(a[i],CurrentS+a[i])
            OverallS = max(CurrentS,OverallS)
        return OverallS