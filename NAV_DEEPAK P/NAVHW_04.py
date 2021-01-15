#NAVHW_004: Draw a flow chart for swapping two numbers without using 3rd/temp variable. (Without using a,b = b,a)

a=int(input("first number"))
b=int(input("second number"))
a=a-b
b=b+a
a=b-a
print("swapping first number",a,"swapping second number",b)
