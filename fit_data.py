import tkinter as tk
from tkinter import Frame
from data_import import import_eis_data
import tkinter.filedialog

#functions

#func --> file import
def get_file(frame):
    eis_filename = \
        tk.filedialog.askopenfilename(initialdir="W:\Projekte\Graphenblocker_61905\04_Bearbeitung\Elektrochemische Analyse\Daten",
                                      title="Select file",
                                      filetypes=(("Text files", "*.txt"),
                                                 ("all files", "*.*")))

    import_eis_data(frame, eis_filename)

#GUI

#implementation menu_frame
menu_frame = tk.Tk()
menu_frame.title("EIS-Analyse")
menu_frame.geometry("{}x{}".format(500, 350))
menu_frame.maxsize(500, 350)
menu_frame.config(bg='lightgrey')
menu_frame.iconbitmap('zbt_logo.ico')

menu_frame.grid_rowconfigure(0, weight=1)
menu_frame.grid_rowconfigure(1, weight=1)

#implementation of subframes(top,bot) of menu_frame
top_menu_frame = Frame(menu_frame, bg='lightgrey', width=500, height=350)
top_menu_frame.grid_propagate(0)

bot_menu_frame = Frame(menu_frame, bg='grey', width=500, height=50)
bot_menu_frame.grid_propagate(0)

top_menu_frame.grid(row=0)
bot_menu_frame.grid(row=1)


#implementation Buttons
#button - import
menu_frame_button1 = tk.Button(top_menu_frame, text='Import EIS Measurement',
                               width=40, command=lambda: get_file(menu_frame))

menu_frame_button1.grid(padx=(20, 0), pady=10, row=0, column=0, sticky='w')

menu_frame.mainloop()