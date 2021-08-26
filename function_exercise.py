import random
# todo Exercise 1: Create a function that can accept two arguments name and age and print its value

def two_args(name,age):
    print(f"My name is {name} and I am {age} year old.")


two_args(name="Sophia", age=25)

#todo Exercise 2: Write a function func1() such that it can accept a variable length of
# argument and print all arguments value

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)


#todo Exercise 3: Write a function calculation() such that it can accept two variables andcalculate the addition
# and subtraction of them. And also it must return both addition and subtraction in a single return call


def calculation(a, b):
    return a + b, a-b
#In Python, we can return multiple values from a function. You can do this by separating return values with a comma


res = calculation(40, 10)
print(res)

#todo Exercise 4: Create a function showEmployee() in such a way that it should accept employee name, and its salary
# and display both. If the salary is missing in the function call assign default value 9000 to salary

def showEmployee(name, salary = 9000):
    print(f"Employee {name} salary is: {salary}")
#In Python, we can specify default values for arguments when defining a function.

showEmployee("Ben", 9000)
showEmployee("Ben")



def display(**kwargs): # ** when you do not know how many arguments to assign
    for i in kwargs:
        print(i)
display(emp="Kelly", salary=9000) # work with dictionary

#todo Exercise 5: Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#At last, an outer function will add 5 into addition and return it

def out_function(a,b):
    def inner_function(a,b):
        out_function(5)
    return a + b

result = out_function(5,10)
print(result)


def outerFun(a, b):
    square = a**2
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5

result = outerFun(5, 10)
print(result)


#todo Exercise 7: Assign a different name to function and call it through the new name Below is the function
# displayStudent(name, age). Assign a new name showStudent(name, age) to it and call through the new name


def displayStudent(name, age):
    print(name, age)

displayStudent("Emma", 26)
showStudent = displayStudent
showStudent("Emma", 26)

#todo Exercise 8: Generate a Python list of all the even numbers between 4 to 30

def even_num():
    list1 = []
    for i in range(4,30):
        if i % 2 == 0:
            list1.append(i)
    print(list1)
even_num()

# the easy way:
print(list( range(4, 30, 2)))

aList = [4, 6, 8, 24, 12, 2]
print(max(aList))





def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)