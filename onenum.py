n=int(input())
for i in range(n):
    x=input().split()
    for j in range(n):
        count=0
        for k in range(n):
            if x[j]==x[k]:
                count=count+1
        if count==1:
            x[j]=int(x[j])
            print(x[j])

