# from tkinter import ttk, SOLID
#
# from crosses_zeroes import Crosses_zeroes
# from game_window import game_window
# from functions import start_game, update_game
# from functools import partial
#
# new_game=Crosses_zeroes()
#
# frame_name = ttk.Frame(game_window, borderwidth=1, relief=SOLID, width=500, height=500)
#
# frame_game = ttk.Frame(game_window, borderwidth=1, relief=SOLID, width=500, height=500)
#
# frame_win = ttk.Frame(game_window, borderwidth=1, relief=SOLID, width=500, height=500)
# label_win = ttk.Label(frame_win, text="Игрок победил")
# label_win.grid(row=0, column=0)
#
# #Фреймы для ввода имен
#
#
# label_first_name = ttk.Label(frame_name, text="Введите имя первого игрока")
# label_first_name.grid(row=0, column=0)
# entry_first_name = ttk.Entry(frame_name)
# entry_first_name.grid(row=1, column=0)
#
#
# label_third_name = ttk.Label(frame_name, text="Введите имя первого игрока")
# label_third_name.grid(row=0, column=1)
# entry_third_name = ttk.Entry(frame_name)
# entry_third_name.grid(row=1, column=1)
#
#
# button_start_game = ttk.Button(frame_name, text=f"Начать играть",
#                                command=partial(start_game,
#                                                game=new_game,
#                                                first_name=entry_first_name,
#                                                third_name=entry_third_name,
#                                                frame_close=frame_name,
#                                                frame_open=frame_game))
# button_start_game.grid(row=2, column=0)
#
#
#
#
#
# button_update_game = ttk.Button(frame_game, text=f"Обновить поле",
#                                 command=partial(update_game,
#                                                 game=new_game,
#                                                 frame=frame_game))
# button_update_game.grid(row=4, column=0, columnspan=3)
