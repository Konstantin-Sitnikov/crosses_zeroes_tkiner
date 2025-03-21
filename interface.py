import tkinter as tk
from tkinter import ttk
import random


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Игра крестики-нолики")
        self.geometry("400x400")

        container = tk.Frame(self, height=500, width=500)
        container.pack(expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.shared_data = {"X": tk.StringVar(container),
                            "0": tk.StringVar(container),
                            "set_name": tk.BooleanVar(container),
                            "win": tk.StringVar(container),
                            "restart_game": tk.BooleanVar(container)}

        self.frames = {}
        for F in (StartPage, CrossesZeroes, CompletionScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Добро пожаловать в игру крестики-нолики,\n чтобы продолжить введите имена игроков")
        label.grid(row=1, column=0, columnspan=2, sticky="n")
        label_first_player = tk.Label(self, text="Введите имя первого игрока")
        label_first_player.grid(row=2, column=0)
        self.entry_first_player = tk.Entry(self)
        self.entry_first_player.grid(row=3, column=0)

        label_third_player = tk.Label(self, text="Введите имя второго игрока")
        label_third_player.grid(row=2, column=1)
        self.entry_third_player = tk.Entry(self)
        self.entry_third_player.grid(row=3, column=1)


        switch_window_button = tk.Button(self, text="Играть", command=lambda: self.set_player())
        switch_window_button.grid(row=5, column=0, columnspan=2, sticky="s")


    def set_player(self):
        list_players = [self.entry_first_player.get(), self.entry_third_player.get()]
        x_player = random.choice(list_players)
        list_players.remove(x_player)
        o_player = list_players[0]
        self.controller.shared_data["X"].set(x_player)
        self.controller.shared_data["0"].set(o_player)
        self.controller.shared_data["set_name"].set(True)

        self.controller.show_frame(CrossesZeroes)


class CrossesZeroes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.shared_data["set_name"].trace_add("write", self.set_name_players)
        self.controller.shared_data["restart_game"].trace_add("write", self.playfield_reset)
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


    def set_symbol(self):
        if self.move % 2 == 0:
            self.symbol = "0"
        else:
            self.symbol = "X"

        self.set_text()


    def set_symbol_playfield(self, row, column):
        self.playing_field[(row, column)] = self.symbol
        if self.check_win():
            self.controller.show_frame(CompletionScreen)
        self.move += 1
        self.button_creation()
        self.set_symbol()



    def set_name_players(self, *args):
        self.players = {"X": self.controller.shared_data["X"].get(),
                   "0": self.controller.shared_data["0"].get()}

        self.set_text()


    def set_text(self):
        self.label['text'] =  f"Сейчас делает ход: {self.symbol} - {self.players[f"{self.symbol}"]}"

    def playfield_reset(self, *args) -> None:

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
                self.controller.shared_data["win"].set(self.symbol)
                return True
        return False

class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.shared_data["win"].trace_add("write", self.set_win_player)
        self.label_win = tk.Label(self, text="")
        self.label_win.grid(row=0, column=0, columnspan=3, pady=20)

        switch_window_button = tk.Button(
            self,
            text="Играть",
            command=lambda: self.restart_game(),
        )
        switch_window_button.grid(row=5, column=0, columnspan=2, sticky="s")


    def set_win_player(self, *args):
        self.label_win["text"] = f"Победил: {self.controller.shared_data[self.controller.shared_data["win"].get()].get()}"

    def restart_game(self):
        self.controller.show_frame(CrossesZeroes)
        self.controller.shared_data["restart_game"].set(True)


if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()