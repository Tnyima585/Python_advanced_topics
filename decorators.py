#Prerequisites for learning decorators
#Nested Function

def outer(x):
    def inner(y):
        return x + y
    return inner

x = outer(5)
result = x(6)
print(result)

#Pass Function as Argument
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add,50, 25)
print(result)

"""In the above example, the calculate() function takes a function as its argument. While calling calculate(), we are passing the add() function as the argument.

In the calculate() function, arguments: func, x, y become add, 50, and 25 respectively.

And hence, func(x, y) becomes add(50, 25) which returns 75."""

#Return a Function as a Value
def greeting(name):
    def hello():
        return "Hello " + name + "!"
    return hello

greet = greeting("Jonny")
print(greet())

#In the above example, the return hello statement returns the inner hello() function. This function is now #assigned to the greet variable.

#That's why, when we call greet() as a function, we get the output.


#Python Decorators
#As mentioned earlier, A Python decorator is a function that takes in a function and returns it by adding some #functionality.Basically, a decorator takes in a function, adds some functionality and returns it.


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
        

def ordinary():
    print("I am ordinary")


ordinary()
decorated_func = make_pretty(ordinary)
decorated_func()

#@ Symbol With Decorator
#Instead of assigning the function call to a variable, Python provides a much more elegant way to achieve this #functionality using the @ symbol. For example,

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()


