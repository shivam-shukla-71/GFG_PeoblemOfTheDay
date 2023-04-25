def MissingNumber(array,n):
        # code here
        sum = n*(n+1)/2
        arrSum=0
        for i in range(0,len(array)):
            arrSum+=array[i]
        
        return int(sum-arrSum)
        
n=7
array=[1,5,2,4,6,7]
print(MissingNumber(array,n))