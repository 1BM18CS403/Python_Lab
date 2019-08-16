li=[]
n=int(input("Enter no of elements : "))
for i in range(0,n):
    ele=int(input())
    li.append(ele)

print(li)
for i in li:
    li2=[]
    if (i%2==0):
        li2.append(i)
        print(li2)
