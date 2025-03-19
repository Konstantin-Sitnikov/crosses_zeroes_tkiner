# from functools import partial
# from tkinter import ttk
# from tkinter import *
#
#
#
# def set_symbol(game, frame, row, column):
#     game.set_symbol(row=row, column=column)
#     buttons_game(game, frame)
#     # if game.check_win():
#
#
#
# def buttons_game(game, frame):
#     for row in range(3):
#         for column in range(3):
#             if game.playinig_field[(row, column)] != "-":
#                 state = "disabled"
#             else:
#                 state = "normal"
#
#             btn = ttk.Button(frame, text=f"{game.playinig_field[(row, column)]}", state=state,
#                              command=partial(set_symbol,game=game, row=row, column=column, frame=frame))
#
#             btn.grid(row=row, column=column)
#
#
# def start_game(game, first_name, third_name, frame_close, frame_open):
#     game.set_name(first_name.get(), third_name.get())
#     frame_close.pack_forget()
#     buttons_game(game, frame=frame_open)
#     frame_open.pack(expand=True, anchor=CENTER)
#
#     print(game.first_player, game.third_name)
#
# def update_game(game,frame):
#     game.playfield_reset()
#     buttons_game(game, frame=frame)
#