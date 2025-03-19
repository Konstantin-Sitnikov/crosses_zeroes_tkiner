import tkinter as tk
from tkinter import ttk
from crosses_zeroes import Crosses_zeroes

# from crosses_zeroes import Crosses_zeroes
# from game_window import game_window
# from player_creation import frame_name


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Тестовое приложение")
        self.geometry("400x400")

        container = tk.Frame(self, height=300, width=300)
        container.pack(expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.shared_data = tk.StringVar(container, value="Имя", name="name")

        self.frames = {}
        for F in (MainPage, Crosses_zeroes, CompletionScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Моя страница")
        label.pack(padx=10, pady=1)
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(Crosses_zeroes),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

        test_button = tk.Button(
            self,
            text="Тест",
            command=lambda: self.test(),
        )
        test_button.pack(side="bottom", fill=tk.X)

        test_button = tk.Button(
            self,
            text="Тест Set",
            command=lambda: self.set_test(),
        )
        test_button.pack(side="bottom", fill=tk.X)


    def test(self):
        print(self.controller.shared_data.get())

    def set_test(self):
        self.controller.shared_data.set("Не имя")


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)




if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()