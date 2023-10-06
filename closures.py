"""Python Closures
Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

Before we learn about closure, let's first revise the concept of nested functions in Python."""

# Nested function in Python

def greet(name):
    # inner function
    def display_name():
        print("Hello",name)
    #call inner function
    display_name()

#call outer function
greet("John")

#Python Closures
def greet():
    #variable defined outside the inner function
    name = "TenzinNyima"

    #return a nested anonymous function
    return lambda: "Hi " + name

# call the outer function
message = greet()

#call the inner function
print(message())

""" In the above example, we have created a function named greet() that returns a nested anonymous function.

Here, when we call the outer function,

message = greet()
The returned function is now assigned to the message variable.

At this point, the execution of the outer function is completed, so the name variable should be destroyed. However, when we call the anonymous function using

print(message())
we are able to access the name variable of the outer function.

It's possible because the nested function now acts as a closure that closes the outer scope variable within its scope even after the outer function is executed.

Let's see one more example to make this concept clear."""

#Example: Print Odd Numbers using Python Closure
def calculate():
    num =  1 
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func
#call the outer function
odd = calculate()

#call the inner function
print(odd())
print(odd())
print(odd())

#call the outer function again
odd2 = calculate()
#call the inner function again
print(odd2())

"""When to use closures?
So what are closures good for?

Closures can be used to avoid global values and provide data hiding, and can be an elegant solution for simple cases with one or few methods.

However, for larger cases with multiple attributes and methods, a class implementation may be more appropriate."""

def make_multiplier_of(n):
    def multiplier(x):
        return x * n 
    return multiplier

times3 = make_multiplier_of(3)

times5 = make_multiplier_of(5)

print(times3(9))
print(times3(2))
print(times5(3))
print(times5(times3(2)))
      
"""The code you've provided defines a function make_multiplier_of(n) that returns another function multiplier(x) when called. The returned multiplier function multiplies its argument x by the value n passed to make_multiplier_of.

In your code:

times3 = make_multiplier_of(3) creates a times3 function that multiplies its argument by 3.
times5 = make_multiplier_of(5) creates a times5 function that multiplies its argument by 5.
times3(2) is equivalent to 2 * 3, which is 6.
times5(times3(2)) is equivalent to times5(6), which is 6 * 5, resulting in 30.
So, the code will print 30 as the output."""




