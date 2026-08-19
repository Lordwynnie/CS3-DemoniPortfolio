# Code 1
def greet_students(name, nChar): 
    for i in range(nChar): 
        print(name[i])
    


name = input("Enter your name: ")
nChar = int(input("Enter any numeric number: "))
nChar = int(nChar)

if nChar > len(name):
    print("Error: The number of characters exceeds the length of the name.")
else: 
    greet_students(name, nChar)


# a.) The output of the code will be "J O S E P" where in each letter is printed on a new line. The code prints the given name letter by letter, line by line, up to the number of characters specified by the user input for nChar. 
# b.) Using nChar as 20 will result in an index error because it exceeded the amount of characters in the name, which makes the code unable to print the name.
# c.) To fix the error, we can add a condition that checks whether nChar is greater than the length of the name, resulting in an intentional Error message instead.

#Code 2

def greet_students(name, nChar):
    for i in range(nChar):
        print(name[0:nChar -1])

name = input("Enter a name: ")
greet_students(name, len(name) )

# a.) The syntax error in the code is that it printed the full name instead of slicing in letter by letter. You can fix it by subtracting 1 from nChar in the print statement so that each letter will one by one be subtracted resulting into an inverted triangle.

#Code 3

n=0
while n < 1 or n > 100:
    n = int(input( "Enter a number between 1 and 100: "))

#needed function
def sum_of_squared(n):
    sum = 0
    for i in range(1, n+1):
        sum += i ** 2
    return sum

print("Sum of all squared numbers is", sum_of_squared(n))

