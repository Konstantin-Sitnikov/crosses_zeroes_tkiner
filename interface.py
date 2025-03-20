import tkinter as tk
from tkinter import ttk
from crosses_zeroes import Crosses_zeroes


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
                            "0": tk.StringVar(container)}

        self.set_name = tk.BooleanVar(container)



        self.frames = {}
        for F in (StartPage, Crosses_zeroes, CompletionScreen):
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
        self.label = tk.Label(self, text="Добро пожаловать в игру крестики-нолики,\n чтобы продолжить введите имена игроков")
        self.label.grid(row=1, column=0, columnspan=2, sticky="n")
        self.label_first_player = tk.Label(self, text="Введите имя первого игрока")
        self.label_first_player.grid(row=2, column=0)
        self.entry_first_player = tk.Entry(self)
        self.entry_first_player.grid(row=3, column=0)

        self.label_third_player = tk.Label(self, text="Введите имя второго игрока")
        self.label_third_player.grid(row=2, column=1)
        self.entry_third_player = tk.Entry(self)
        self.entry_third_player.grid(row=3, column=1)


        switch_window_button = tk.Button(
            self,
            text="Играть",
            command=lambda: self.set_player(),
        )
        switch_window_button.grid(row=5, column=0, columnspan=2, sticky="s")


    def set_player(self):
        self.controller.shared_data["X"].set(self.entry_first_player.get())
        self.controller.shared_data["0"].set(self.entry_third_player.get())
        self.controller.set_name.set(True)

        self.controller.show_frame(Crosses_zeroes)



class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(StartPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)




if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()