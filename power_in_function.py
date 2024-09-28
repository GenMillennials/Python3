import math

def power(p):
    def n_power(n):
        return n ** p
    return n_power

commands = {"квадрат": power(2), "куб": power(3), "корень": power(0.5), "модуль": abs, "синус": math.sin}
n = int(input())
command = input()

print(commands[command](n))