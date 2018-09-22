#Sydnee Ramirez
#lab4

n = int(input ( "Enter number for fibionacci sequence: "))
#defined variables
a = 0
b = 1
for i in range(n) :
    print(a)
    temp = a
    a = b
    b = temp + b
