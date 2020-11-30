import pandas as pd

def import_eis_data(frame, file):

    #readout file data
    df_input = pd.read_csv(file, decimal=',', encoding='cp1252',
                           error_bad_lines=False, delim_whitespace=True)

    #df_input = df_input.drop(range(0, 12))
    df_input.columns = ['index', 'number', 'frequency [Hz]', 'impedance Re [Ohm]', 'impedance Im [Ohm]', 'significance', 'time [s]']

    #save formated data to new txt file
    #new_file_name = file[:-4] + '_formated.txt'
    #df_input.to_csv(new_file_name, mode='a', header=False)

    # df_input2 = pd.read_csv(new_file_name, sep=r'\s*', decimal=',', encoding='cp1252',
    #                        error_bad_lines=False, header=None)

    print(len(df_input.columns))
    print(df_input)

