# write a python program to swap two variables

a = eval(input("Enter the value of the first variable :"))
b = eval(input("Enter the value of the second variable :"))
print("The original values are :","a =", a ,"b =", b)
temp = a
a=b
b=temp
print("The swapped values are :","a=",a,"b=",b)