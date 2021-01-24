import pandas as pd
import tkinter as tk
from tkinter import Frame
from datetime import datetime
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import scipy.optimize as optimize
from scipy.optimize import fsolve, root
import pathlib
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def eis_plotter(dropdown_var, canvas, subf1):

    rootpath = pathlib.Path(__file__).parent.absolute()
    df_eis_data = pd.read_csv(str(rootpath) + '/EIS_data/CSV_data/' + dropdown_var + '.csv', delimiter='\t')

    # preview
    x_values = np.asarray(df_eis_data['Re [Ohm*cm²]'])
    y_values = np.asarray(df_eis_data['-Im [Ohm*cm²]'])

    # graph interpolation
    f = interp1d(x_values, y_values, kind='linear', fill_value="extrapolate")

    roots = fsolve(lambda x: f(x), [-100, 100])
    hfr = roots[0]
    rr = roots[1] - roots[0]


    subf1.plot(x_values, y_values, linestyle='dashed', linewidth=2, marker='s', markersize=4, label=str(dropdown_var))
    #subf1.legend(loc='upper left', bbox_to_anchor=(-0.28, 1.15), ncol=8, fontsize=8)
    subf1.set_xlabel('Re [Ohm*cm²]', labelpad=10, fontdict=dict(fontsize=12, weight='bold'))
    subf1.set_ylabel('-Im [Ohm*cm²]', labelpad=10, fontdict=dict(fontsize=12, weight='bold'))

    canvas.draw()

def visualize_eis_data(frame):

    eis_data_frame = tk.Toplevel(frame)
    eis_data_frame.title("EIS Data-Library")
    eis_data_frame.geometry("{}x{}".format(800, 600))
    eis_data_frame.maxsize(800, 600)
    eis_data_frame.config(bg="blue")
    eis_data_frame.iconbitmap('zbt_logo.ico')


    #eis_data_frame.rowconfigure(0, weight=1)

    #eis_data_frame.rowconfigure(1, weight=1)


    top_eis_data_frame = Frame(eis_data_frame, bg='green', width=800, height=50)
    # bot_eis_data_frame = Frame(eis_data_frame, bg='grey', width=800, height=700)
    top_eis_data_frame.grid_propagate(0)
    # bot_eis_data_frame.grid_propagate(0)

    top_eis_data_frame.grid(row=0, column=2)
    # bot_eis_data_frame.grid(row=1)

    rootpath = pathlib.Path(__file__).parent.absolute()
    filelist = [fname[:-4] for fname in os.listdir(str(rootpath) + '/EIS_data/CSV_data/') if fname.endswith('.csv')]

    # set startvalue and define optionmenu
    var = tk.StringVar(top_eis_data_frame)

    var.set(filelist[0])

    option = tk.OptionMenu(top_eis_data_frame, var, *filelist,
                           command=lambda _: eis_plotter(var.get(), eis_canvas, fig_ax1)
                           )

    option.grid(row=0, column=0, sticky='ew', padx=(10, 10))
    #option.pack()

    fig = Figure(figsize=(50, 50))
    grid = fig.add_gridspec(13, 18)

    fig_ax1 = fig.add_subplot(grid[:13, :18])
    fig_ax1.set_title('EIS-Data Comparison', pad=10, fontdict=dict(fontsize=16, weight='bold'))

    # fig_ax1.set_xlim([0, 20])
    # fig_ax1.set_ylim([0, 400])

    eis_canvas = FigureCanvasTkAgg(fig, master=eis_data_frame)
    #eis_canvas.get_tk_widget().grid(row=1, column=0)

    #eis_canvas.get_tk_widget().pack()

    eis_data_frame.mainloop()

def visualize_qms_data(frame):

    qms_data_frame = tk.Toplevel(frame)
    qms_data_frame.title("QMS Data-Library")
    qms_data_frame.geometry("{}x{}".format(800, 600))
    qms_data_frame.maxsize(800, 600)
    qms_data_frame.config(bg="blue")
    qms_data_frame.iconbitmap('zbt_logo.ico')

    qms_data_frame.mainloop()