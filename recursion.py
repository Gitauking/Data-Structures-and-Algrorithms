#a function that calls itself. Im using a simple example demonstrating a countdown procedure

def countdown(n):
    if n == 0: #base case
        print("Blast off!")
    else: #the recursive case
        print(n)
        countdown(n-1)

countdown(5)


#lets use another example using factorials

def factorial(n):
    if n == 1:
        return 1 #base case
    else:
        return n * factorial(n-1)# recursive case
    

print("The factorial is : ", factorial(7)) 

