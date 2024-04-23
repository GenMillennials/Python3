def pick_source():
    print("Выберите вид источника публикации")
    while True:
        pick_type_src = input("Если журнал - ж, диссертация - д,\nавтореферат - a, конференция - к, НПА - нпа\n")
        if pick_type_src in ("ж", "д", "а", "к", "нпа"):
            break
        else:
            print("Введите корректное значение")
    return pick_type_src

def get_name_src():
    name_src = input("Введите название источника: ")
    return name_src

def get_authors():
    authors = input("Введите всех авторов через запятую.\nЕсли авторов нет, поставьте \"н\": ")
    if authors in ("н", "нет", "не", "n", "no"):
        authors = ""
    return authors

def get_material():
    src_material = input("Введите название материала: ")
    return src_material

def get_year():
    print("Введите год публикации:")
    src_year = input()
    return src_year

def get_volume():
    print("Введите том книги или журнала:")
    src_volume = input()
    return src_volume

def src_number():
    print("Введите номер периодического издания:")
    src_num = input()
    return src_num

def src_strings():
    print("Введите страницу или страницы:")
    src_strings = input()
    return src_strings

# def get_law():

# def get_websource(annot):

# def get_monography(annot):

# def get_article(annot):

# def get_confer(annot):

# def get_textbook(annot):
print("Давайте начнем описание источника")
print(pick_source())



