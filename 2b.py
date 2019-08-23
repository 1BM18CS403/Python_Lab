def rev(str1):
    li=str1.split(" ")
    li.reverse()
    print(str1)
    return str1[::-1]
str1=input(" Enter the string: ")
print(rev(str1))
