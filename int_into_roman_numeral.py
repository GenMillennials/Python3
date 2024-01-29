def int_into_roman(num):
    arabian_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    dict_pairs = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    roman_numeral = ""
    for i in dict_pairs:
        while num >= i:
            roman_numeral = roman_numeral + dict_pairs[i]
            num = num - i
    return roman_numeral

print(int_into_roman(64))
print(int_into_roman(99))
print(int_into_roman(490))
print(int_into_roman(922))
print(int_into_roman(4458))