def get_law(annot):
    res = ""
    url = ""
    comp = annot.split()
    for i in comp:
        if i == "https://www.consultant":
            res = i + " " + "// СПС \"Консультант Плюс\" - URL:" + url
        elif i == "https://www.garant":
            res =

# def get_websource(annot):

# def get_monography(annot):

# def get_article(annot):

# def get_confer(annot):

# def get_textbook(annot):


# print("Введите текст источника:")
# source = input()
print(get_law("Абвг, дежз иклмн."))