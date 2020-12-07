import pandas as pd
import tkinter as tk
from tkinter import Frame
from datetime import datetime


def read_eis_data(file):
    # read out file data (experiement specs)
    # readout file data

    # read out experiment specifications
    df_eis_specs = pd.read_csv(file, decimal=',', encoding='cp1252',
                               error_bad_lines=False, delim_whitespace=True,
                               index_col=False, header=None, nrows=7,
                               keep_default_na=False,
                               names=['data', 'value#1', 'value#2', 'value#3'])

    # read and format measurement data !fix with load, save, reload, columns --> to get into aspired design
    df_eis_data = pd.read_csv(file, sep='\t', decimal=',', encoding='cp1252', error_bad_lines=False, skiprows=19, index_col=False)

    # df_eis_specs.to_csv('temp_eis_specs.txt', mode='w', header=True)
    #
    # df_eis_specs_formated = pd.read_csv('temp_eis_specs.txt', decimal=',', encoding='cp1252', error_bad_lines=False,
    #                                    delim_whitespace=True)
    #
    # print(df_eis_specs_formated)

    df_eis_data.to_csv('temp_eis_data.txt', mode='w', header=True)

    df_eis_data_formated = pd.read_csv('temp_eis_data.txt', decimal=',', encoding='cp1252', error_bad_lines=False,
                                       delim_whitespace=True)

    df_eis_data_formated.columns = ['index', 'number', 'frequency [Hz]', 'impedance Re [Ohm]', 'impedance Im [Ohm]',
                                    'significance', 'time [s]']

    print(df_eis_specs)
    # filename
    eis_specs_filename = df_eis_specs['value#1'].values[0]
    # specification
    eis_specs_spec = df_eis_specs['value#1'].values[1]
    # date
    eis_specs_date = df_eis_specs['value#3'].values[0]
    # time
    eis_specs_time = df_eis_specs['value#1'].values[5]
    # voltage
    eis_specs_voltage = df_eis_specs['value#1'].values[2]

    eis_specs_date_time = eis_specs_date + ' ' + eis_specs_time
    eis_specs_datetime = datetime.strptime(eis_specs_date_time,
                                           '%b,%d.%Y %H:%M:%S')

    return df_eis_specs, eis_specs_filename, eis_specs_spec, eis_specs_datetime, \
           eis_specs_voltage


def format_eis_data(file):
    # readout file data
    df_input = pd.read_csv(file, decimal=',', encoding='cp1252',
                           error_bad_lines=False, delim_whitespace=True)

    # df_input = df_input.drop(range(0, 12))
    df_input.columns = ['index', 'number', 'frequency [Hz]', 'impedance Re [Ohm]', 'impedance Im [Ohm]', 'significance',
                        'time [s]']


    print(len(df_input.columns))
    print(df_input)


def import_eis_data(frame, file):


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

    df, filename, spec, datetime, voltage = read_eis_data(file)


    # labels of entries
        # labels (date, sample ,molarity, current, voltage)
    sdf_label1 = tk.Label(top_left_sampledoc_frame, text='Date:', pady=10)
    sdf_label2 = tk.Label(top_left_sampledoc_frame, text='Sample:', pady=10)
    sdf_label3 = tk.Label(top_left_sampledoc_frame, text='Molarity [M]:',
                          pady=10)
    sdf_label4 = tk.Label(top_left_sampledoc_frame, text='Current [A]:',
                          pady=10)
    sdf_label5 = tk.Label(top_left_sampledoc_frame, text='Voltage [V]:',
                          pady=10)

    sdf_label6 = tk.Label(top_right_sampledoc_frame, justify='left', text=df)


    sdf_label7 = tk.Label(bot_sampledoc_frame, text='File: ' + filename,
                          pady=10)
    sdf_label8 = tk.Label(bot_sampledoc_frame, text='Specs: ' + spec,
                          pady=10)

        # label placement
    sdf_label1.grid(row=1, column=0, sticky='ew')
    sdf_label2.grid(row=2, column=0, sticky='ew')
    sdf_label3.grid(row=3, column=0, sticky='ew')
    sdf_label4.grid(row=4, column=0, sticky='ew')
    sdf_label5.grid(row=5, column=0, sticky='ew')

    sdf_label6.grid(row=1, column=0, sticky='e')

    sdf_label7.grid(row=1, column=0, sticky='ew')
    sdf_label8.grid(row=1, column=1, sticky='ew')



    # entries for additonal documentation

        # entries (date, sample ,molarity, current, voltage)
    sdf_entry1 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry1.insert(0, datetime)
    sdf_entry2 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry2.insert(0, '')
    sdf_entry3 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry3.insert(0, '')
    sdf_entry4 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry4.insert(0, '')
    sdf_entry5 = tk.Entry(top_left_sampledoc_frame, width=30, bd=5)
    sdf_entry5.insert(0, voltage)

        # entry placement
    sdf_entry1.grid(row=1, column=1)
    sdf_entry2.grid(row=2, column=1)
    sdf_entry3.grid(row=3, column=1)
    sdf_entry4.grid(row=4, column=1)
    sdf_entry5.grid(row=5, column=1)

    # buttons of sampledoc_frame
        # sdf_button1 --> format file and store with given additional data
    sdf_button1 = tk.Button(top_left_sampledoc_frame, text='OK', width=20, bd=5, command=lambda: format_eis_data(file))
    sdf_button1.grid(row=6, column=1)

    sampledoc_frame.mainloop()


    #save formated data to new txt file
    #new_file_name = file[:-4] + '_formated.txt'
    #df_input.to_csv(new_file_name, mode='a', header=False)

    # df_input2 = pd.read_csv(new_file_name, sep=r'\s*', decimal=',', encoding='cp1252',
    #                        error_bad_lines=False, header=None)



