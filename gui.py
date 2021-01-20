import tkinter as tk
from tkinter import Frame
from fit_data import data_import

main_menu_frame = tk.Tk()
main_menu_frame.title("Analysis of Experimental Data")
main_menu_frame.geometry("{}x{}".format(500, 350))
main_menu_frame.maxsize(500, 350)
main_menu_frame.config(bg='lightgrey')
main_menu_frame.iconbitmap('zbt_logo.ico')

#implementation of subframes(top,bot) of menu_frame
top_menu_frame = Frame(main_menu_frame, bg='blue', width=500, height=350)
top_menu_frame.grid_propagate(0)

bot_menu_frame = Frame(main_menu_frame, bg='green', width=500, height=50)
bot_menu_frame.grid_propagate(0)

top_menu_frame.grid(row=0)
bot_menu_frame.grid(row=1)

#implementation Buttons
#button - import
main_menu_frame_button1 = tk.Button(top_menu_frame, text='Data Import',
                               width=40, command=lambda: data_import(main_menu_frame))

main_menu_frame_button2 = tk.Button(top_menu_frame, text='Data Analysis',
                               width=40, command=lambda: get_qms_file(menu_frame))

main_menu_frame_button1.grid(padx=(100, 100), pady=10, row=0, column=0, sticky='nesw')
main_menu_frame_button2.grid(padx=(100, 100), pady=10, row=1, column=0, sticky='nesw')

main_menu_frame.mainloop()