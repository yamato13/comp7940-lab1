#-----------------------------------------------------------------------EX1
# Find the all factors of x using a loop and the operator % 
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
# 能被整除且没有余数的就是因子



x = 52633
for i in range(x+1):
    if (x % (i+1) == 0):
        print(f"{i+1}是x的因子")
    
#-----------------------------------------------------------------------EX2
# Write a function that prints all factors of the given parameter x
def print_factor(x):
    for i in range(x+1):
        if (x % (i+1) == 0):
            print(f"{i+1}是x的因子")

#-----------------------------------------------------------------------EX3
# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
def find_factor(list):
    for i in range(len(list)):
        print("************************************************")
    
        print_factor(list[i])

        print(f"__________以上是第{i+1}个list元素{list[i]}的因子_________")

find_factor(l)

