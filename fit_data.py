import tkinter as tk
from tkinter import Frame
from data_import import import_eis_data, import_qms_data
from data_visualization import visualize_eis_data, visualize_qms_data
import tkinter.filedialog

#functions

#func --> file import
def get_eis_file(frame):
    eis_filename = \
        tk.filedialog.askopenfilename(initialdir="W:\Projekte\Graphenblocker_61905\04_Bearbeitung\Elektrochemische Analyse\Daten",
                                      title="Select file",
                                      filetypes=(("Text files", "*.txt"),
                                                 ("all files", "*.*")))

    import_eis_data(frame, eis_filename)

def get_qms_file(frame):
    qms_filename = \
        tk.filedialog.askopenfilename(initialdir="W:\Projekte\Graphenblocker_61905\04_Bearbeitung\Elektrochemische Analyse\Daten",
                                      title="Select file",
                                      filetypes=(("Text files", "*.dat"),
                                                 ("all files", "*.*")))

    import_qms_data(frame, qms_filename)

#GUI

#implementation menu_frame
menu_frame = tk.Tk()
menu_frame.title("DMFC in-situ Analyse")
menu_frame.geometry("{}x{}".format(500, 350))
menu_frame.maxsize(500, 350)
menu_frame.config(bg='lightgrey')
menu_frame.iconbitmap('zbt_logo.ico')

menu_frame.grid_rowconfigure(0, weight=1)
menu_frame.grid_rowconfigure(1, weight=1)

#implementation of subframes(top,bot) of menu_frame
top_menu_frame = Frame(menu_frame, bg='blue', width=500, height=350)
top_menu_frame.grid_propagate(0)

bot_menu_frame = Frame(menu_frame, bg='green', width=500, height=50)
bot_menu_frame.grid_propagate(0)

top_menu_frame.grid(row=0)
bot_menu_frame.grid(row=1)


#implementation Buttons
#button - import
menu_frame_button1 = tk.Button(top_menu_frame, text='Import EIS Measurement',
                               width=40, command=lambda: get_eis_file(menu_frame))

menu_frame_button2 = tk.Button(top_menu_frame, text='Import QMS Measurement',
                               width=40, command=lambda: get_qms_file(menu_frame))

menu_frame_button3 = tk.Button(top_menu_frame, text='EIS Measurements',
                               width=40, command=lambda: visualize_eis_data(menu_frame))

menu_frame_button4 = tk.Button(top_menu_frame, text='QMS Measurements',
                               width=40, command=lambda: visualize_qms_data(menu_frame))

menu_frame_button1.grid(padx=(100, 100), pady=10, row=0, column=0, sticky='nesw')
menu_frame_button2.grid(padx=(100, 100), pady=10, row=1, column=0, sticky='nesw')
menu_frame_button3.grid(padx=(100, 100), pady=10, row=2, column=0, sticky='nesw')
menu_frame_button4.grid(padx=(100, 100), pady=10, row=3, column=0, sticky='nesw')

menu_frame.mainloop()

