import random
import tkinter as tk
from tkinter import ttk, StringVar
from functools import partial

class Crosses_zeroes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.set_name.trace_add("write", self.set_name_players)
        self.players = {"X": "",
                   "0": ""}
        self.move = 1
        self.symbol = "X"


        self.label = tk.Label(self, text="")
        self.label.grid(row=0, column=1, columnspan=3, pady=20)

        self.playing_field = {(0, 0): "-", (0, 1): "-", (0, 2): "-",
                              (1, 0): "-", (1, 1): "-", (1, 2): "-",
                              (2, 0): "-", (2, 1): "-", (2, 2): "-"}


        self.button_creation()

    def button_creation(self):
        for row in range(1, 4):
            for column in range(1, 4):
                if self.playing_field[(row - 1, column - 1)] != "-":
                    state = "disabled"
                else:
                    state = "normal"

                btn = ttk.Button(self, text=f"{self.playing_field[(row - 1, column - 1)]}", state=state,
                                 command=lambda i = row - 1, j = column - 1: self.set_symbol_playfield(row=i, column=j)
                                 )

                btn.grid(row=row, column=column, ipadx=20, ipady=20, padx=5, pady=5)

        reset_button = ttk.Button(self, text=f"Обновить поле",
                              command=lambda: self.playfield_reset())
        reset_button.grid(row=5, column=0, columnspan=4, ipadx=100, pady=20)

        button = ttk.Button(self, text=f"Игроки",
                              command=lambda: self.test())
        button.grid(row=6, column=0, columnspan=4, ipadx=100, pady=20)


    def set_symbol(self):
        if self.move % 2 == 0:
            self.symbol = "0"
        else:
            self.symbol = "X"

        self.set_text()


    def set_symbol_playfield(self, row, column):
        self.playing_field[(row, column)] = self.symbol
        self.move += 1
        self.button_creation()
        self.set_symbol()
        if self.check_win():
            print("Победа")
        print(self.playing_field)

    def set_name_players(self, *args):
        self.players = {"X": self.controller.shared_data["X"].get(),
                   "0": self.controller.shared_data["0"].get()}

        self.set_text()



    def set_text(self):
        self.label['text'] =  f"Сейчас делает ход: {self.symbol} - {self.players[f"{self.symbol}"]}"

    def playfield_reset(self) -> None:

        for i in range(3):
            for j in range(3):
                self.playing_field[(i, j)] = "-"

        self.move = 1
        self.set_symbol()
        self.button_creation()


    def check_win(self) -> bool:

        """Проверка выигрышных комбинаций

        в функции создается контрольный список "control_list" с проверяемыми символами
        и 4 списка:
         - "diagonal_1", "diagonal_2" - списки, для проверки выигрышных комбинаций по диагонали
         - line - список, для проверки выигрышных комбинаций по строке
         - column - список, для проверки выигрышных комбинаций по столбцу

        если хотя-бы один из 4-х списков совпадет с контрольным, фунция вернет: "True",
        иначе:  False"""

        control_list = [self.symbol] * 3  # создаем тестовый список из необходимых символов
        diagonal_1 = []  # списки для проверки комбинации по диагонали
        diagonal_2 = []
        for i in range(3):
            line = []  # список для проверки комбинации по строке
            column = []  # список для проверки комбинации по столбцу
            for j in range(3):
                line.append(self.playing_field[(i, j)])  # заполняем список строк
                column.append(self.playing_field[(j, i)])  # заполняем список столбцов
                if i == j:
                    diagonal_1.append(self.playing_field[(j, i)])  # заполняем списки диагоналей
                if i + j == 2:
                    diagonal_2.append(self.playing_field[(j, i)])

            if (line == control_list or column == control_list or
                    diagonal_1 == control_list or diagonal_2 == control_list):  # сравниваем списоки с тестовым
                return True
        return False



#Создаем игровое поле
playinig_field = {(0, 0): "-", (0, 1): "-", (0, 2): "-",
                  (1, 0): "-", (1, 1): "-", (1, 2): "-",
                  (2, 0): "-", (2, 1): "-", (2, 2): "-"}


def dislayning_the_playinig_field(a: dict) -> str:

    """Отображение текущего состояния игрового поля


        функция формирует и возвращает игровое проле в виде строки
    """

    field = (f"{" " * 15} X\n"             #Подпись оси Х
             f"{" " * 9} 0     1     2\n"    #Значения координат по оси Х
             f"{" " * 7}{"-" * 19}\n")       #Оформление горизонтальной линии
    for i in range(3):
        new_string = f" Y  {i}" if i == 1 else f"    {i}" # Создаем новую строку с подписью значений координат по оси Y
        for j in range(3):
            new_string += f"  |  {a[(i, j)]  }"        #Добавляем в новую строку значения столбцов
        new_string += (f"  |\n"
                       f"{" " * 7}{"-" * 19}\n")        #Делаем переход на новую строку с оформлением горизонтальной линии
        field += new_string         #Добавляем новую строку к игровому полю
    return field        #Возвращаем значение текущего игрового поля



def check_win(a: dict, symbol) -> bool:

    """Проверка выигрышных комбинаций

    в функции создается контрольный список "control_list" с проверяемыми символами
    и 4 списка:
     - "diagonal_1", "diagonal_2" - списки, для проверки выигрышных комбинаций по диагонали
     - line - список, для проверки выигрышных комбинаций по строке
     - column - список, для проверки выигрышных комбинаций по столбцу

    если хотя-бы один из 4-х списков совпадет с контрольным, фунция вернет: "True",
    иначе:  False"""


    control_list = [symbol] * 3 #создаем тестовый список из необходимых символов
    diagonal_1 = []         #списки для проверки комбинации по диагонали
    diagonal_2 = []
    for i in range(3):
        line = []           #список для проверки комбинации по строке
        column = []         #список для проверки комбинации по столбцу
        for j in range(3):
            line.append(a[(i, j)])             #заполняем список строк
            column.append(a[(j, i)])           #заполняем список столбцов
            if i == j:
                diagonal_1.append(a[(j, i)])   #заполняем списки диагоналей
            if i + j == 2:
                diagonal_2.append(a[(j, i)])

        if (line == control_list or column == control_list or
                diagonal_1 == control_list or diagonal_2 == control_list):      #сравниваем списоки с тестовым
            return True
    return False



def coordinate_check(x:str, y:str) -> bool:

    """ Проверка введенных кординат

    Функция принимает на вход значения координат и проверяет:
    - количество введенных символов;
    - что введены именно числа,
    - введеные числа лежат в нужном диапазоне

    Функция возвращает "True" если пользовать верно ввел координаты

    """

    if len(x) == 1 and len(y) == 1:                     #Проверяем длинну введенных чисел
        if x.isdigit() and y.isdigit():                 #Проверяем что введены числа
            if 0 <= int(x) <= 2 and 0 <= int(y) <= 2:   #Проверяем что числа лежат в нужном диапазоне
                return True
    return False


def check_add_symbol(a: dict, symbol:str) -> any:

    """Добавление символа на игровое поле

    Функция запрашивает у пользователя координаты, проверяет,
    что указанные координаты свободны, и записывает символ на игровое поле
    если пользователь ввел неверные координаты или позиция уже занята, выводид
    соответствующее сообщение.

    """


    while True:
        print(f"Ход '{symbol}'")
        x = input("Введите x (от 0 до 2): ")
        y = input("Введите y (от 0 до 2): ")        #Пользователь вводит координаты
        if coordinate_check(x, y):      #Проверяем что координаты введены верно
            if a[(int(y), int(x))] == "-": #Проверяем что в указанных координатах поле пустое
                a[(int(y), int(x))] = symbol   #если поле пустое добавляем нужный символ
                break
            else:
                print("Позиция занята, введите другие координаты")
                continue
        else:
            print("Вы ввели не верные координаты, попробуйте снова")
            continue



def playing_field_full(a: dict) -> bool:

    """Проверка заполнености игрового поля

    Функция проверяет что на игровои поле не осталось пустых ячеек,
    и возвращает 'True' если игровое поле заполнено, иначе возвращает 'False'

    """

    x = True
    for value in a.values():
        if value == "-":
            x = False
    return x


def playfield_reset(my_dict: dict) -> None:

    """ Обнуление игрового поля

    Функция записывает во все ячейки игрового поля символ '-'

    """

    for i in range(3):
        for j in range(3):
            my_dict[(i , j)] = "-"




def game(n:int) -> any:
    """Реализация игры

    1. Функция определяет очередность хода для игроков:
        - если число 'n' - четное переменной 'symbol' присваивается значение 'X'
            (ход выполняет игрок с символом 'X')
        - если число 'n' - не четное 'symbol' присваивается значение 'О'
            (ход выполняет игрок с символом 'О')

    2. Вызов функции 'check_add_symbol'.
        Игрок вводит координаты, и функция добавляет необходимий символ на игровое проле

    3. Вызов функции 'check_win'.
        Выполняется проверка выигрышних комбинаций,
        если комбинации есть выводится сообщение о победе игрока, и производится обнудение игрового поля

    4. Выполняется проверка на отсутствие выигрышних комбинаций и заполненость игрового поля,
        если комбинаций нет и поле полностью заполено выводится сообщение о ничьей,
        так же производится обнуление игрового поля.

    5. Если если небыло победы или ничьей ход выполняет следующий игрок

    """
    while True:
        print(dislayning_the_playinig_field(playinig_field)) #Вывод текущего состояния игрового поля

        if n % 2 != 0:                  # 1.
            symbol = "X"
            check_add_symbol(playinig_field, symbol)    # 2.
            n = 2                       #изменение значения переменной для перехода хода следуещему игроку
            if check_win(playinig_field, symbol): # 3.
                print("-" * 21)
                print(dislayning_the_playinig_field(playinig_field)) #Вывод текущего состояния игрового поля
                print("-" * 21)
                print("X победил")  #Вывод информации о победе игрока
                playfield_reset(playinig_field) #обнуление игрового поля
                break

            elif not(check_win(playinig_field, symbol)) and playing_field_full(playinig_field):   #4.
                # Проверка игорового поля на отсутствие выигрышних комбинаций
                print("-" * 21)
                print(dislayning_the_playinig_field(playinig_field))  #Вывод текущего состояния игрового поля
                print("-" * 21)
                print("Ничья")          #Вывод информации о ничьей
                print("-" * 21)
                playfield_reset(playinig_field)     #обнуление игрового поля
                break
            #5.
        else:
            symbol = "O"
            check_add_symbol(playinig_field, symbol)  # 2.
            n = 1 #изменение значения переменной для перехода хода следуещему игроку
            if check_win(playinig_field, symbol):
                print("-" * 21)
                print(dislayning_the_playinig_field(playinig_field)) #Вывод текущего состояния игрового поля
                print("-" * 21)
                print("O победил") #Вывод информации о победе игрока
                playfield_reset(playinig_field)
                break
            elif not (check_win(playinig_field, symbol)) and playing_field_full(playinig_field): #4.
                print("-" * 21)
                print(dislayning_the_playinig_field(playinig_field))  # Вывод текущего состояния игрового поля
                print("-" * 21)
                print("Ничья")
                print("-" * 21)
                playfield_reset(playinig_field) #обнуление игрового поля
                break


def game_rules():

    """Вывод на экран правил игры"""

    print("1. Игровое поле: сетка размером 3×3. \n"
          "2. Роли игроков: один играет за «X», другой за «O». \n"
          "3. Цель: выстроить три одинаковых символа подряд — вертикально, горизонтально или по диагонали. \n"
          "4. Ход игры: игроки размещают свои символы на свободные ячейки. Очередность определяется случайным образом. \n"
          "5. Последовательность ходов: участники игры ходят поочерёдно, пропуск хода кем-либо недопустим. \n"
          "6. Выигрыш: игрок побеждает, выстроив три своих символа подряд. \n"
          "7. Ничья: если все ячейки заняты, и никто не собрал линию из трёх символов, игра считается ничейной.")


def player_interaction():
    """Функция для взаимодействия с игроком

    Игроку предлагается выбрать одно из действий.
    Выплняется проверка корректности выбраного действия.
    В зависимости от выбора игрока:
    1. начинается новая игра
        игра случайным образом выбирает игрока кто первым выполняет ход,
        производится вызов функции 'game()'
    2. выводятся провила игры
    3. игра завершиется



    """
    while True:
        print("-" * 21)
        print("   Добро подаловать  \n"
              "       в игру \n"
              "  'Крестики-Нолики'")
        print("-" * 21)
        print("1. Начать новую игру!")
        print("2. Правила игры")
        print("3. Завершить игру")
        print("-" * 21)
        i = input("Выберете действие: ")
        if i.isdigit():
            if int(i) == 1 or int(i) == 2 or int(i) == 3:
                if int(i) == 1:
                    n = random.randint(1, 2)
                    game(n)
                elif int(i) == 2:
                    game_rules()
                elif int(i) == 3:
                    print("-" * 21)
                    print("Игра закончена!")
                    print("-" * 21)
                    break
            else:
                print("Введите коректное число")
        else:
            print("Вы ввели не число! попробуйте снова")




# player_interaction()