import pandas as pd
from datetime import datetime

file = 'C:/Users/Julian/Desktop/Homeoffice_20201201/20201127_dmfc_protonly/MSR/20201106_dmfc_cathode.dat'

df_qms_specs = pd.read_csv(file, decimal=',', encoding='cp1252', error_bad_lines=False, delim_whitespace=True,
                               index_col=False, header=None, skiprows=2, nrows=5, keep_default_na=False)


# qms_filename = df_qms_specs[5].values[0].split('\\')[-1][:-1]
# print(qms_filename)

qms_filename = file.split('/')[-1][:-4]
qms_specs_date = df_qms_specs[12].values[0]
qms_specs_time = df_qms_specs[13].values[0]

qms_specs_datetime = datetime.strptime(qms_specs_date + ' ' + qms_specs_time, '%Y-0%m-%d %H\'%M\'%S.isi')

    # read and format measurement data !fix with load, save, reload, columns --> to get into aspired design
df_qms_data = pd.read_csv(file, sep='\t', decimal='.', encoding='cp1252', error_bad_lines=False, skiprows=7,
                              index_col=False)


