# -*- coding: utf-8 -*-
#  №5 Угадайка слов (Виселица - игра)
import random


def word_list(a, guessed_words):
    # сосзаем список слов, которые будет отгадывать юзер
    # 0, 3, 6, 9, 12, 15, 18 - категория программирование
    # 1, 4, 7, 10, 13, 16, 19 - категория физика
    # 2, 5, 8, 11, 14, 17, 20 - категория биология
    word_list = ["компилятор", "адгезия", "биосфера", "идентификатор", "аннигиляция", "иммунитет", "верификация",
                 "гидравлика", "клетка", "функция", "гистерезис", "популяция", "алгоритм", "гравитация",
                 "оплодотворение", "фреймворк", "деформация", "селекция", "рекурсия", "индуктивность", "антропогенез"]
    return word_list[a]


def help_term(a):
    help_term = ["программа, которая переводит текст, написанный на языке программирования, в набор машинных кодов",
                 "сцепление поверхностей разнородных твёрдых и/или жидких тел",
                 "оболочка Земли, заселённая живыми организмами, находящаяся под их воздействием и занятая продуктами их жизнедеятельности, а также совокупность её свойств как планеты",
                 "уникальный признак объекта, позволяющий отличать его от других объектов",
                 "реакция превращения частицы и античастицы при их столкновении в какие-либо иные частицы, отличные от исходных",
                 "способность организма поддерживать свою и биологическую индивидуальность путём распознавания и удаления чужеродных веществ и клеток",
                 "проверка соответствия программного обеспечения технической документации, представленной техзаданием, архитектурой или моделью предметной области",
                 "прикладная наука о законах движения, равновесии жидкостей и способах приложения этих законов к решению задач инженерной практики",
                 "структурно-функциональная элементарная единица строения и жизнедеятельности всех организмов",
                 "подпрограмма, которую можно вызвать из основной программы, причем неоднократно",
                 "свойство систем (физических, биологических и т. д.), мгновенный отклик которых на приложенные к ним воздействия зависит в том числе и от их текущего состояния",
                 "совокупность организмов одного вида, длительное время обитающих на одной территории (занимающих определённый ареал) и частично или полностью изолированных от особей других таких же групп",
                 "конечная совокупность точно заданных правил решения некоторого класса задач или набор инструкций, описывающих порядок действий исполнителя для решения определённой задачи",
                 "универсальное фундаментальное взаимодействие между материальными телами, обладающими массой",
                 "процесс соединения двух гамет, в результате чего образуется оплодотворенное яйцо зигота",
                 "программное обеспечение, облегчающее разработку и объединение разных компонентов большого программного проекта",
                 "изменение взаимного положения частиц тела, связанное с их перемещением друг относительно друга за счет приложения усилия, при котором тело искажает свои формы",
                 "наука о методах создания новых и улучшения существующих пород животных, сортов растений и штаммов микроорганизмов",
                 "вызов функции (процедуры) из неё же самой",
                 "коэффициент пропорциональности между электрическим током, текущим в каком-либо замкнутом контуре, и полным магнитным потоком, называемым также потокосцеплением, создаваемым этим током через поверхность, краем которой является этот контур",
                 "часть биологической эволюции, которая привела к появлению человека разумного, отделившегося от прочих гоминид, человекообразных обезьян и плацентарных млекопитающих"]

    return help_term[a]


def help_list(num):
    help_l = list()
    if num in [0, 3, 6, 9, 12, 15, 18]:
        help_l.append("термин из категории программирование")
    elif num in [1, 4, 7, 10, 13, 16, 19]:
        help_l.append("термин из категории физика")
    elif num in [2, 5, 8, 11, 14, 17, 20]:
        help_l.append("термин из категории биология")
    help_l.append(help_term(num))
    return help_l


def help_3(word, word_completion, guessed_letters, HLP3):
    if word_completion[0] == "_":
        word_completion.pop(0)
        word_completion.insert(0, word[0])
        guessed_letters.append(word[0])
        HLP3.append(word[0])
    if word_completion[-1] == "_":
        word_completion.pop(-1)
        word_completion.append(word[-1])
        guessed_letters.append(word[-1])
        HLP3.append(word[-1])
    return word_completion, guessed_letters, HLP3


def display_hangman(tries):
    stages = [  # 0 финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # 1 голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # 2 голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # 3 голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # 4 голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # 5 голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # 6 начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def valid(a):
    while (a not in "абвгдеёжзийклмнопрстуфхцчшыщъьэюя" or len(a) > 1):
        print("Введите одну букуву из русского алфавита")
        a = (input().lower())
    return a


def valid2(otvet):
    while (otvet.lower() not in ["д", "н", "да", "нет", ""]):
        print('Введите "д"/"н" (или enter если нет)')
        otvet = input().lower()
    if otvet in ["д", "да"]:
        return True
    elif otvet in ["н", "нет", ""]:
        return False


def HELPme(help, help_total, word, word_completion, guessed_letters, HLP3):
    if help_total < 2:
        print("Подсказка №", help_total + 1, sep="")
        print(help[help_total])
        help_total += 1
        return help_total, HLP3
    elif help_total == 2:
        word_completion, guessed_letters, HLP3 = help_3(word, word_completion, guessed_letters, HLP3)
        print("Подсказка №", help_total + 1, sep="")
        print(*word_completion, sep="", end="  ")
        print(len(guessed_letters), "/", len(word), sep="")
        help_total += 1
        return help_total, HLP3
    elif help_total >= 3:
        print("Подсказки закончились")


def play(guessed_words, ranNum):
    num = random.randint(0, 20)
    HLP3 = []  # сюда записываем первую и последнюю букву для хелп3
    # num = 14
    while num in ranNum:
        num = random.randint(0, 20)
    word = word_list(num, guessed_words)
    help = help_list(num)
    guessed_letters = []  # список уже названных букв
    tries = 6  # количество попыток
    help_total = 0  # номер подсказки
    word_completion = list()
    word_completion.extend("_" * len(word))
    print(*word_completion, sep="", end="  ")
    print(len(guessed_letters), "/", len(word), sep="")
    while (len(guessed_letters) != len(word) and tries >= 0):  # основной цикл программы
        print("Введите одну букуву из русского алфавита")
        a = valid(input().lower())
        if a in word and a not in guessed_letters:
            for i in range(len(word)):
                if word[i] == a:
                    word_completion.pop(i)
                    word_completion.insert(i, a)
                    guessed_letters.append(a)
                    print(*word_completion, sep="", end="  ")
                    print(len(guessed_letters), "/", len(word), sep="")
                    print(display_hangman(tries))
                    print("У Вас осталось: жизни -", tries, "подсказки -", 3 - help_total)
        elif a in word and a in HLP3:
            for i in range(1, len(word) - 1):
                if word[i] == a:
                    word_completion.pop(i)
                    word_completion.insert(i, a)
                    guessed_letters.append(a)
                    print(*word_completion, sep="", end="  ")
                    print(len(guessed_letters), "/", len(word), sep="")
                    print(display_hangman(tries))
                    print("У Вас осталось: жизни -", tries, "подсказки -", 3 - help_total)
        elif a in word and a in guessed_letters:
            print("Такая буква в слове уже есть")
        elif a not in word:
            tries -= 1
            print("Такой буквы в слове нет")
            print(*word_completion, sep="", end="  ")
            print(len(guessed_letters), "/", len(word), sep="")
            print(display_hangman(tries))
            print("У Вас осталось: жизни -", tries, "подсказки -", 3 - help_total)
            if tries == 0:
                break
            print('Нужна ли Вам подсказка? "д"/"н"(или enter если нет)')
            if valid2(input().lower()) == True:
                help_total, HLP3 = HELPme(help, help_total, word, word_completion, guessed_letters, HLP3)
    if len(guessed_letters) == len(word):
        guessed_words.append(word)
        ranNum.append(num)
        print("Поздравляем, Вы отгодали слово!     Вы отгодали", len(guessed_words), "из 21 слов")
    #if len(guessed_letters) != len(word) and help_total == 0:
    if len(guessed_letters) != len(word) and tries == 0:
        print("Вы проиграли, у Вас за    кончились жизни")
        word = ""
    if len(guessed_words) < 21:
        print('Желаете отгадать следующее слово? "д"/"н"(или enter если нет)')
        if valid2(input().lower()) == True:
            return True, guessed_words, ranNum
        else:
            return False, guessed_words, ranNum
    if len(guessed_words) == 21:
        print("*******Поздравляем Вы отгадали все слова!!!*******")
        #break


def hello():
    print("Добро пожаловать в Угадайку слов или игру - Виселица!")
    print("В данной игре компьютер загадывает 1 из 20 произвольное слово, Ваша задача его отгадать!")
    print("Колличество жизней - 6, подсказок - 3")
    guessed_words = []  # список уже названыых слов
    ranNum = []  # список рандомных номеров
    guessed = False  # сигнальная метка
    PLAY, guessed_words, ranNum = play(guessed_words, ranNum)
    while (PLAY == True):
        PLAY, guessed_words, ranNum = play(guessed_words, ranNum)


hello()