def pick_source():
    print("Выберите вид источника публикации")
    while True:
        pick_type_src = input("Если журнал - ж, диссертация - д,\nавтореферат - a, конференция - к, НПА - нпа\n")
        if pick_type_src in ("ж", "д", "а", "к", "нпа"):
            break
        else:
            print("Введите корректное значение из предложенных")
    return pick_type_src

def get_name_src():
    name_src = input("Введите название источника:\n")
    return name_src

def get_authors():
    while True:
        authors = input("Введите всех авторов через запятую.\nЕсли авторов нет, поставьте \"н\":\n")
        if authors not in ("н", "нет", "не", "n", "no"):
            break
        else:
            print("Введите корректное значение")
    return authors

def get_material():
    src_material = input("Введите название материала:\n")
    return src_material

def get_year():
    while True:
        src_year = input("Введите год публикации:\n")
        if src_year.isdigit() and len(src_year) == 4 and src_year[0:2] in ("17", "18", "19", "20"):
            break
        else:
            print("Год публикации некорректен")  
    return src_year

def get_volume():
    while True:
        src_volume = input("Введите том книги или журнала:\n")
        if src_volume.isdigit() and len(src_volume) <= 2 and src_volume[0] != "0":
            break
        else:
            print("Номер тома издания некорректен")
    return src_volume

def src_number():
    while True:
        src_num = input("Введите номер периодического издания:\n")
        if src_num.isdigit() and len(src_num) <= 3:
            break
        else:
            print("Введенный номер издания некорректен")
    return src_num

def src_strings():
    while True:
        src_strings = input("Введите страницу или страницы:\n")
        if src_strings.isdigit() and len(src_strings) <= 3:
            break
        else:
            print("Номера страниц указаны некорректно")
    return src_strings

# def get_law():

# def get_websource(annot):

# def get_monography(annot):

# def get_article(annot):

# def get_confer(annot):

# def get_textbook(annot):
print("Давайте начнем описание источника")
# pick_source()
print(src_strings())



