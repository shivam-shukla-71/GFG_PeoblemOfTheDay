def sort012(arr,n):
        # code here
        count0=0
        count1=0
        count2=0
        for i in range(0,n):
            if(arr[i]==0):count0+=1
            elif(arr[i]==1):count1+=1
            elif(arr[i]==2):count2+=1
        # return count0,count1,count2
        for x in range (0,n):
              if(x<count0):arr[x]=0
        for x in range (0,n):
              if(x>=count0 and x<count1):arr[x]=1
        for x in range (0,n):
              if(x>=count1):arr[x]=2
        

n=7
arr=[1,0,1,1,2,0,2]
print(sort012(arr,n))