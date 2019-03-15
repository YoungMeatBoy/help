from random import uniform, randint
import os

class HelperException(Exception):

    def __init__(self, text=""):
        self.txt = text


def getValids(adds:str = "") -> str:
    """
    returns a string of valid letters
    """
    import string
    Accept = adds + string.ascii_lowercase + \
            string.ascii_uppercase + "".join([str(x) for x in range(10)])
    return Accept

def connectionCheck() -> bool:
    """ 
            Checks if you your devise is connected to the Internet
    """
    import socket
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def choosingFile(UI:bool, dir:str = "", extencions:list = []) -> "path to file":
    """  
            helps user to choose file from a directory
    """
    if UI:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        return askopenfilename()
    else:

        from os.path import isdir
        import os

        # checks directory
        if not isdir(dir):
            raise HelperException("No such directory!")

        from glob2 import glob as find
        slash = os.sep  # slash according to a system
        dir = dir.rstrip("/").rstrip("\\") + slash
        print("\nThe directory of searching: ", dir)
        dir = dir.rstrip("/").rstrip("\\") + slash + "*"  # here we create a glob pattern
        print(dir)
        # take a list of files
        if not extencions:
            files = [file for file in find(dir) if not isdir(file)]
            print(files)
        else:
            files = sum([find(dir + "." + end)
                         for end in extencions], [])  # still list here

        if not files:
            print("No matching files were found")
            return ""
        else:
            f = dict()
            dir = dir.rstrip("*")

            # printing all files if the list
            # here a dict of files is creates
            #
            # { 1: filename1
            #   2: filename2
            #   3: filename3
            #   4: filename4
            # }

            for i, file in enumerate(files):
                f[i + 1] = file
                print(f"{i+1}:", file.replace(dir, ""))

            def check(x, found=len(f) + 1):
                return x in range(1, found)

            answer = EInput(
                Types=[int],  # we need integer as a key
                Funcs=[check],  # which is in range
                ETexts=["Such number is unvalid!"],
                ITexts=["Enter number of the file: "]
            )
            return f[answer]


def EInput(Types:list=[], Amount:int=1, Funcs:list=[], Arguments=[], EndFunc=None, EArguments:list=[], ITexts:list=[], ETexts:list=[], EEText:str="", Adding:bool=True, STRIP:bool=False):
    """ 
    =========================================================
    That function helps you to make an easy input for a User.
    =========================================================
    Parametres:
        Types:
            In Types parametr set a list of functions (types of elements) , you want User to input.
            Note that you will have to make list in such way: [int]*5,
            Than there will be 5 elements of integer
        Amount:
            In Amount set the amoun of elements you want User to input
        Funcs:
            In Funcs you have to set rhe list of functions for each element.
            Note that you will have to put *args into your function.
            It should return True or False or string "OUT" (Read Adding for an information)
        Arguments:
            The list of arguments which will be given to your "check" function
        EncFunc:
            One Function that will check the list of User's inputs
            Note that yu will have to add *args   
        EArguments:
            The list of arguments which will be given to your " End function
        IText:
            The list of texts which will be shown to a Users
        EText:
            The list of texts which will be shown to a user if your check fucnction returns False
        EEText:
            The string which will be shown if your End function returns False
        Adding:
            If your Check function returns "OUT":
                if Adding:
                    The current input will be added to the list of answers
        """
    Answer = []
    while True:
        for _ in range(Amount):
            while True:
                if STRIP:
                    IT = input(ITexts[_]).strip()
                else:
                    IT = input(ITexts[_])
                try:
                    IT = Types[_](IT)
                except ValueError:
                    print(ETexts[_])
                else:
                    if Funcs:
                        if Arguments:
                            FuncRet = Funcs[_](IT, Arguments)
                        else:
                            FuncRet = Funcs[_](IT)
                        if FuncRet == "OUT":
                            if Adding:
                                Answer.apend(IT)
                            break
                        elif FuncRet:
                            Answer.append(IT)
                            break
                        else:
                            print(ETexts[_])
                    else:
                        Answer.append(IT)
        if EndFunc:
            if not EndFunc(Answer, EArguments):
                print(EEText)
            else:
                if Amount == 1:
                    return Answer[0]
                else:
                    return tuple(Answer)
        else:
            if Amount == 1:
                return Answer[0]
            else:
                return tuple(Answer)


def generateMatrix(Auto:bool=True, Size:tuple=(10, 10), Typ:str="int", Zeros:bool=False, Span:tuple=(-100, 100)) -> list:
    """
    Automatically or manualy generates matrix of given size and span and type
    """

    if Auto:
        if Zeros:
            return [[0 for i in range(Size[0])] for i in range(Size[1])]
        else:
            if Typ == "int":
                return [[randint(Span[0], Span[1]) for i in range(Size[0])] for i in range(Size[1])]
            elif Typ == "float":
                return [[uniform(Span[0], Span[1]) for i in range(Size[0])] for i in range(Size[1])]
            else:
                pass
    else:
        if Typ == "int":
            return [[int(input("Enter value: ")) for i in range(Size[0])] for i in range(Size[1])]
        elif Typ == "float":
            return [[float(input("Enter value: ")) for i in range(Size[0])] for i in range(Size[1])]
        else:
            raise HelperException("No type was given!")


def goodOut(object) -> None:
    """
    An easy output of a matrix or a dict
    """
    if type(object) is dict:
        flag = False
        for key in (object):
            if str(key) in "1234567890":
                flag = True
        if flag:
            for key in object:
                print(key, ":", object[key])
        else:
            for ind, key in enumerate(object):
                print(f"{str(ind + 1)} | {str(key)} : ", object[key])
    elif type(object) is list:
        print()
        for item in object:
            for chislo in item:
                print(("{:>5}").format(chislo), end=" ")
            print()
    return


def ask(text:str="yes/no?: ") -> bool:
    """
    Yes or no?
    """
    answer = input(text) 
    if not answer:
        return True # if enter was pressed
    else:
        return "y" in answer.lower()


def askPath(Dir:str=os.getcwd(), extencion:str=".txt") -> str:
    """
    Ask for a new name of the file
    """
    import os
    slash = os.sep

    def Check(x, *args):
        Valids = getValids() + "_"
        if not x:
            return False
        for item in x:
            if item not in Valids:
                return False
        return True
    
    while True:
        Name = EInput(Types=[str],
                      Funcs=[Check],
                      ITexts=["\nEnter file name: "],
                      ETexts=["\nIncorrect name!"])
        if not os.path.isfile(Dir + slash + Name + "." + extencion):
            return Dir + slash + Name + "." + extencion
        else:
            print("\nThis file already excists!")


def unitest(func,right=None, wrong=None, dic=None):
    """
    Универсальная проверка пользовательских функций.
    Использование:
            (!) Если ваша функция возвращает значения True или False:
                            1) В файле создайте список со значениями, при которых ваша функция возвращает True.
                            2) Если нужно, можно создать второй список со значениями при которых ваша функция возвращает False.
                            3) Определите свою функцию с помощью def или импортируйте из своего файла.
                            Запуск происходит со следующим синтаксисом:
                            -------------------------------------------
                                    from mlib import unitest
                                    from myfile import myfunction
                                    true = []
                                    false = []
                                    unitest(myfunction,
                                                    right=true,
                                                    wrong=false)
                            --------------------------------------------
                            По умолчанию параметр wrong равен None, поэтому его не обязательно передавать.
            (!) Если ваша функция возвращает определенное значение:
                            1) Создайте словарь, в котором значения ключей - это значения, передаваемые в вашу функцию,
                            а значения являются заведомо известными результатами работы функций.
                            2) Определите свою функцию с помощью def или импортируйте из своего файла.
                            Запуск происходит со следующим синтаксисом:
                            --------------------------------------------
                                    from mlib import unitest
                                    def foo(x):
                                            return x**2
                                    dictionary = {2:4, 3:9, 4:16}
                                    unitest(foo, dic=dictionary)
                            --------------------------------------------
                            Обязателен запуск с определением параметра!
    (!) Если функция возвращает неверные значения вы будете сразу же уведомлены об этом.
    При возникновении каких либо ошибок, связанных с логикой работы вашей функции:
    они будут сохранены и выведены в самом конце с описанием ошибки.
    """

    errors_on_right = {}  # Хранит в себе сообщения об ошибках при верных значениях
    errors_on_dict = {}   # Хранит в себе информацию об ошибках при проверке через словарь
    errors_on_wrong = {}  # Хранит в себе сообщения об ошибках при проверке неверных значениях

    if (str(type(func)) == "<class 'function'>") and\
       (right == None or type(right) is list) and\
       (wrong == None or type(wrong) is list) and\
       (dic == None or type(dic) is dict):
        #if right is None or isinstance(right, list)?

        if right:
            s = 0                # Ключ к словарю
            print("Происходит проверка правильных значений... \n")
            # Начинается проверка каждого значения с обработкой исключений
            for _, item in enumerate(right):
                try:
                    if func(item):
                        continue
                    else:
                        print("Функция вернула False, а не True")
                        print("Значение: {}; Индекс: {}/n".format(item, _))
                except Exception as e:
                    s += 1
                    # Запись ошибки и информации о ней
                    errors_on_right[s] = (_, e)
                else:
                    continue
            print("Проверка правильных значений завершена\n\n")

        if wrong:
            # Начало проверки неверных значений
            s = 0                # Обновляем ключ к словарю
            print("Происходит проверка неверных значений...")
            for _, item in enumerate(wrong):
                try:
                    if not func(item):
                        continue
                    else:
                        print("Функция True, а не False")
                        print("Значение: {}; Индекс: {}\n".format(item, _))
                except Exception as e:
                    s += 1
                    # Запись ошибки и информации о ней
                    errors_on_wrong[s] = (_, e)
                else:
                    continue
        if dic:
            print("Начало проверки при помощи словаря... \n")
            s = 0               # Обновляем ключ к словарю
            for item in dic:
                try:
                    if func(item) == dic[item]:
                        print("(", item, ":", dic[item], ")  : Успешно")
                        continue
                    else:
                        d = func(item)
                        print(
                            "(", item, ":", dic[item], ")  : Ошибка, функция вернула: ", d)
                except Exception as e:
                    s += 1
                    # Запись ошибки и информации о ней
                    errors_on_dict[s] = (item, dic[item], e)
                else:
                    continue

        # Вывод ошибок при проверке правильных:
        if errors_on_right:
            print()
            print("Сообщения об ошибках при проверке правильных значений: \n")
            for item in errors_on_right:
                print("Элемент: {}\nИндекс: {}\n".format(
                    right[errors_on_right[item][0]], errors_on_right[item][0]))
                print("Ошибка: \n", errors_on_right[item][1])
                print("________________________________________________________")

        # Вывод ошибок при проверке неправильных:
        if errors_on_wrong:
            print()
            print("Сообщения об ошибках при проверке ложных значений: \n")
            for item in errors_on_right:
                print("Элемент: {}\nИндекс: {}".format(
                    right[errors_on_wrong[item][0]], errors_on_wrong[item][0]))
                print("Ошибка: \n", errors_on_wrong[item][1])
                print("________________________________________________________")

        # Вывод ошибок при проверке с помощью словаря
        if errors_on_dict:
            print()
            print("Ссобщения об ошибках при проверке значений через словарь: \n")
            for _ in errors_on_dict:
                print("При передаче значения {} возникла ошибка {}\n".format(
                    errors_on_dict[_][0], errors_on_dict[_][1]))
                print("________________________________________________________")
    else:
        print("Переданы неверные аргументы")
