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


def read_eis_data(file):
    # read out file data (experiement specs)
    # readout file data

    # read out experiment specifications
    df_eis_specs = pd.read_csv(file, decimal=',', encoding='cp1252', error_bad_lines=False, delim_whitespace=True, index_col=False,
                               header=None, nrows=7, keep_default_na=False)

    eis_specs_date = df_eis_specs[3].values[0]
    eis_specs_time = df_eis_specs[1].values[5]
    eis_specs_datetime = datetime.strptime(eis_specs_date + ' ' + eis_specs_time, '%b,%d.%Y %H:%M:%S')

    eis_specs_voltage = df_eis_specs[1].values[2][0:-1]
    eis_specs_file = df_eis_specs[1].values[0]
    eis_specs_system = df_eis_specs[1].values[1]

    # read and format measurement data !fix with load, save, reload, columns --> to get into aspired design
    df_eis_data = pd.read_csv(file, sep='\t', decimal='.', encoding='cp1252', error_bad_lines=False, skiprows=19, index_col=False)


    df_eis_data.to_csv('temp_eis_data.txt', mode='w', header=True)

    df_eis_data_formated = pd.read_csv('temp_eis_data.txt', decimal='.', encoding='cp1252', error_bad_lines=False,
                                       delim_whitespace=True)

    df_eis_data_formated.columns = ['index', 'number', 'frequency [Hz]', 'impedance Re [Ohm]', 'impedance Im [Ohm]',
                                    'significance', 'time [s]']

    df_eis_data_formated['Re [Ohm*cm²]'] = df_eis_data_formated['impedance Re [Ohm]'].apply(lambda x: x*25)
    df_eis_data_formated['-Im [Ohm*cm²]'] = df_eis_data_formated['impedance Im [Ohm]'].apply(lambda x: x*-25)



    return df_eis_data_formated, df_eis_specs, eis_specs_datetime, eis_specs_voltage, eis_specs_file, eis_specs_system

def save_eis_data(df_eis, filename, frame, name, molarity, current):

    df_eis['Sample'] = name
    df_eis['MeOH Molarity [M]'] = molarity
    df_eis['Current [mA]'] = current*1000
    df_eis.round(4)
    print(df_eis)

    # save eis data to csv
    rootpath = pathlib.Path(__file__).parent.absolute()
    df_eis.to_csv(str(rootpath)+'/CSV_data/'+filename+'.csv', mode='w', header=True,
                  index=False, sep='\t')

    # save eis data to excel
    wb_path = str(rootpath) + '/EIS_data/eis_data_library.xlsx'
    book = load_workbook(wb_path)
    writer = pd.ExcelWriter(wb_path, engine='openpyxl')
    writer.book = book
    df_eis.to_excel(writer, sheet_name=filename, index=False)

    writer.save()
    writer.close()

    #close frame
    frame.destroy()

    # preview
    x_values = np.asarray(df_eis['Re [Ohm*cm²]'])
    y_values = np.asarray(df_eis['-Im [Ohm*cm²]'])

    # graph interpolation
    f = interp1d(x_values, y_values, kind='linear', fill_value="extrapolate")

    roots = fsolve(lambda x: f(x), [-100, 100])
    hfr = roots[0]
    rr = roots[1] - roots[0]

    plt.plot(x_values, y_values, 'rs--')
    plt.plot(x_values, f(x_values), 'k-')
    plt.title('Preview -Nyquist Plot')
    plt.xlabel('Re [Ohm*cm²]')
    plt.ylabel('-Im [Ohm*cm²]')
    plt.xticks()
    plt.axhline(0, color='black')

    table_data = [["High Frequency Resistance [Ohm*cm²]", str(round(hfr, 2))],
                  ["Reaction Resistance [Ohm*cm²]", str(round(rr, 2))]]
    table = plt.table(cellText=table_data,
                      bbox=[0.02, 0.85, 0.35, 0.1], colWidths=[.9, .1], cellLoc='right')
    #edges = 'open',
    table.auto_set_font_size(False)
    table.set_fontsize(12)

    for (row, col), cell in table.get_celld().items():
        if col == 0:
            cell.set_height(1.3)
            cell._loc = 'left'
            cell.set_text_props(ma='left', fontweight=50)
        elif col == 1:
            cell.set_height(1.3)
            cell._loc = 'right'
            cell.set_text_props(ma='right')

    plt.show()


def import_eis_data(frame, file):


    # implement sample_documentation_frame
    sampledoc_frame = tk.Toplevel(frame)
    sampledoc_frame.title("Additional Sample Data")
    sampledoc_frame.geometry("{}x{}".format(400, 400))
    sampledoc_frame.maxsize(400, 400)
    sampledoc_frame.config(bg="blue")
    sampledoc_frame.iconbitmap('zbt_logo.ico')


    # subframes of sampledoc_frame
    top_sampledoc_frame = Frame(sampledoc_frame, bg='lightgrey', width=400,
                                height=300)
    bot_sampledoc_frame = Frame(sampledoc_frame, bg='grey', width=400,
                                height=100)
    top_sampledoc_frame.grid_propagate(0)
    bot_sampledoc_frame.grid_propagate(0)

    top_sampledoc_frame.grid(row=0)
    bot_sampledoc_frame.grid(row=1)

    # subsubframes
    # top_left_sampledoc_frame = Frame(top_sampledoc_frame, bg='lightblue', width=300, height=350)
    # top_right_sampledoc_frame = Frame(top_sampledoc_frame, bg='lightgreen', width=500, height=350)
    # top_left_sampledoc_frame.grid_propagate(0)
    # top_right_sampledoc_frame.grid_propagate(0)

    # top_left_sampledoc_frame.grid(row=0, column=0)
    # top_right_sampledoc_frame.grid(row=0, column=1)

    df_eis, df_eis_specs, eis_datetime, eis_voltage, eis_file, eis_system = read_eis_data(file)

    # labels of entries
        # labels (date, sample ,molarity, current, voltage)
    sdf_label1 = tk.Label(top_sampledoc_frame, text='Date:', pady=10,
                          bg='lightgrey')
    sdf_label2 = tk.Label(top_sampledoc_frame, text='Sample:', pady=10,
                          bg='lightgrey')
    sdf_label3 = tk.Label(top_sampledoc_frame, text='Molarity [M]:', pady=10,
                          bg='lightgrey')
    sdf_label4 = tk.Label(top_sampledoc_frame, text='Current [A]:', pady=10,
                          bg='lightgrey')
    sdf_label5 = tk.Label(top_sampledoc_frame, text='Voltage [V]:', pady=10,
                          bg='lightgrey')

    #sdf_label6 = tk.Label(top_right_sampledoc_frame, justify='left', text=df_eis_specs)

    sdf_label7 = tk.Label(bot_sampledoc_frame, text='File:   ' + '\t' + eis_file,
                          pady=10, bg='grey')
    sdf_label8 = tk.Label(bot_sampledoc_frame, text='System: ' + '\t' +
                                                    eis_system,
                          pady=10, bg='grey')

    # label placement
    sdf_label1.grid(row=1, column=0, sticky='w', padx=(10, 10))
    sdf_label2.grid(row=2, column=0, sticky='w', padx=(10, 10))
    sdf_label3.grid(row=3, column=0, sticky='w', padx=(10, 10))
    sdf_label4.grid(row=4, column=0, sticky='w', padx=(10, 10))
    sdf_label5.grid(row=5, column=0, sticky='w', padx=(10, 10))

    #sdf_label6.grid(row=1, column=0, sticky='e')

    sdf_label7.grid(row=0, column=0, sticky='w', padx=(10, 0))
    sdf_label8.grid(row=1, column=0, sticky='w', padx=(10, 0))

    # entries for additonal documentation

        # entries (date, sample ,molarity, current, voltage)
    sdf_entry1 = tk.Entry(top_sampledoc_frame, width=30, bd=5)
    sdf_entry1.insert(0, eis_datetime)
    sdf_entry2 = tk.Entry(top_sampledoc_frame, width=30, bd=5)
    sdf_entry2.insert(0, '')
    sdf_entry3 = tk.Entry(top_sampledoc_frame, width=30, bd=5)
    sdf_entry3.insert(0, '')
    sdf_entry4 = tk.Entry(top_sampledoc_frame, width=30, bd=5)
    sdf_entry4.insert(0, '')
    sdf_entry5 = tk.Entry(top_sampledoc_frame, width=30, bd=5)
    sdf_entry5.insert(0, eis_voltage)

    sample_name = sdf_entry2.get()
    sample_molarity = sdf_entry3.get()
    sample_current = sdf_entry4.get()


        # entry placement
    sdf_entry1.grid(row=1, column=1)
    sdf_entry2.grid(row=2, column=1)
    sdf_entry3.grid(row=3, column=1)
    sdf_entry4.grid(row=4, column=1)
    sdf_entry5.grid(row=5, column=1)

    # buttons of sampledoc_frame
        # sdf_button1 --> format file and store with given additional data
    sdf_button1 = tk.Button(top_sampledoc_frame, text='OK', width=20, bd=5,
                            command=lambda: save_eis_data(df_eis, eis_file,
                                                          sampledoc_frame,
                                                          sample_name,
                                                          sample_molarity,
                                                          sample_current))
    sdf_button1.grid(row=6, column=1)


    sampledoc_frame.mainloop()


def import_qms_data(frame, file):

    # implement sample_documentation_frame
    sampledoc_frame = tk.Toplevel(frame)
    sampledoc_frame.title("Additional Sample Data")
    sampledoc_frame.geometry("{}x{}".format(800, 400))
    sampledoc_frame.maxsize(800, 400)
    sampledoc_frame.config(bg="lightgrey")
    sampledoc_frame.iconbitmap('zbt_logo.ico')


    # subframes of sampledoc_frame
    top_sampledoc_frame = Frame(sampledoc_frame, bg='black', width=800, height=350)
    bot_sampledoc_frame = Frame(sampledoc_frame, bg='red', width=800, height=50)
    bot_sampledoc_frame.grid_propagate(0)

    top_sampledoc_frame.grid(row=0)
    bot_sampledoc_frame.grid(row=1)

    # subsubframes
    top_left_sampledoc_frame = Frame(top_sampledoc_frame, bg='lightblue', width=300, height=350)
    top_right_sampledoc_frame = Frame(top_sampledoc_frame, bg='lightgreen', width=500, height=350)
    top_left_sampledoc_frame.grid_propagate(0)
    top_right_sampledoc_frame.grid_propagate(0)

    top_left_sampledoc_frame.grid(row=0, column=0)
    top_right_sampledoc_frame.grid(row=0, column=1)

    df_eis, df_eis_specs, eis_datetime, eis_voltage, eis_file, eis_system = read_eis_data(file)

    # labels of entries
        # labels (date, sample ,molarity, current, voltage)
    sdf_label1 = tk.Label(top_left_sampledoc_frame, text='Date:', pady=10)
    sdf_label2 = tk.Label(top_left_sampledoc_frame, text='Sample:', pady=10)
    sdf_label3 = tk.Label(top_left_sampledoc_frame, text='Molarity [M]:', pady=10)
    sdf_label4 = tk.Label(top_left_sampledoc_frame, text='Current [A]:', pady=10)
    sdf_label5 = tk.Label(top_left_sampledoc_frame, text='Voltage [V]:', pady=10)

    sdf_label6 = tk.Label(top_right_sampledoc_frame, justify='left', text=df_eis_specs)

    sdf_label7 = tk.Label(bot_sampledoc_frame, text='File: ' + eis_file, pady=10)
    sdf_label8 = tk.Label(bot_sampledoc_frame, text='System: ' + eis_system, pady=10)

        # label placement
    sdf_label1.grid(row=1, column=0, sticky='ew')
    sdf_label2.grid(row=2, column=0, sticky='ew')
    sdf_label3.grid(row=3, column=0, sticky='ew')
    sdf_label4.grid(row=4, column=0, sticky='ew')
    sdf_label5.grid(row=5, column=0, sticky='ew')

    sdf_label6.grid(row=1, column=0, sticky='e')

    sdf_label7.grid(row=0, column=0, sticky='ew')
    sdf_label8.grid(row=0, column=1, sticky='ew')

    # entries for additonal documentation

        # entries (date, sample ,molarity, current, voltage)
    sdf_entry1 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry1.insert(0, eis_datetime)
    sdf_entry2 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry2.insert(0, '')
    sdf_entry3 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry3.insert(0, '')
    sdf_entry4 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry4.insert(0, '')
    sdf_entry5 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry5.insert(0, eis_voltage)

        # entry placement
    sdf_entry1.grid(row=1, column=1)
    sdf_entry2.grid(row=2, column=1)
    sdf_entry3.grid(row=3, column=1)
    sdf_entry4.grid(row=4, column=1)
    sdf_entry5.grid(row=5, column=1)

    # buttons of sampledoc_frame
        # sdf_button1 --> format file and store with given additional data
    sdf_button1 = tk.Button(top_left_sampledoc_frame, text='OK', width=20, bd=5,
                            command=lambda: save_eis_data(df_eis, eis_file, sampledoc_frame))
    sdf_button1.grid(row=6, column=1)


    sampledoc_frame.mainloop()




