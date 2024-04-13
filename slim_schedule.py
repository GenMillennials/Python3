day = int(input())
weight = float(input())
planned = 100 - (0.2 * day)
if weight > planned:
    res = False
else:
    res = True
print("Все идет по плану" if res else "Что-то пошло не так")
print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {planned} кг")