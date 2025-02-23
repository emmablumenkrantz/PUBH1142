#Question 1 basic math
print("Question 1")
print("3 x 8 = ", 3*8)
print("33+7 / 5 = ", (33+7)/5)
print(" ")
print(" ")
#Question 2 find data type
print("Question 2")
print("1+2. is a ", type(1+2.), ". This is because adding an integer and a float results in a float.")
print("1+2 is a ", type(1+2), ". This is because adding two integers results in an integer.")
print(" ")
print(" ")
#Question 3 making a loop
print("Question 3")
print("The following sequence prints n\u00b2 for each of the numbers n={1,2,3,4,5}.")
for i in range (5):
    n = i+1
    print(n*n)
print(" ")
print(" ")
#Question 4 
print("Question 4")
q = 1
while q*q <1000:
    print("i\u00b2 = ", q*q)
    q = q+1
print("The final value of i is ", q, ". This is the final value because 32 times 32 results in 1024 which is greater than 1000.")