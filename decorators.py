def deco(t):
    def deconew(f):
        def say(s):
            print(t)
            f(s)
            print("!")
        return say
    return deconew


@deco("Hello!")
def dear(s):
    print("Dear", s)


@deco("Goodbye!")
def muchesteemed(s):
    print("Muchesteemed", s)


name = input("What's your name? ")
dear(name)
print("I'm Python!")
muchesteemed(name)