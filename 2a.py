def li(list1,a):
    if a in list1:
        return  True
    else:
        return False
list1=[2,3,4,5,6,7,8]
#list1=input("Enter the list: ")
a=int(input("Enter the no: "))
print(li(list1,a))
