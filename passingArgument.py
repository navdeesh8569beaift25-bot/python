# Passing Arguments
# def greet(name,age):
#     print(f"hello {name},you are {age} years old")
# greet("navdeesh",18)

# def greet(name="Guest"):
#     print(f"hello {name}")
# greet("navdeesh")
# greet("parth")


def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print("fact of 5",factorial(5)) 