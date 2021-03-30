arr=list(map(int,input("수를 입력하세요(예:1,2,3):").split(',')))

for i in range(0,len(arr)):
    for j in range(len(arr)-1,i,-1):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
        print(arr)
