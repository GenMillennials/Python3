def get_factors(num):
    dividers = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            dividers.append(i)

    dividers.append(num)
    return dividers


def number_of_factors(num):
    return len(get_factors(num))

n = int(input())

print(number_of_factors(n))