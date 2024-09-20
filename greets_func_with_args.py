def greet(name, *args):
    s = " and ".join((name,) + args)
    return f"Hello, {s}!"

print(greet("Sam", "Paul", "Joe"))