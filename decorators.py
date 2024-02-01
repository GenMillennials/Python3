def dear(s):
    print("Dear", s)


def muchesteemed(s):
    print("Muchesteemed", s)

def decohello(f):
    def say_hello(s):
        print("Hello!")
        f(s)
        print("!")
    return say_hello


hello = decohello(muchesteemed)
name = input("What's your name? ")
hello(name)