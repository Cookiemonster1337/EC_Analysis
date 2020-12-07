
from datetime import datetime

eis_specs_date = 'NOV,27.2020'
eis_specs_time = '14:33:06'
eis_specs_datetime = eis_specs_date + ' ' + eis_specs_time
print(eis_specs_datetime)


date_object = datetime.strptime(eis_specs_datetime, '%b,%d.%Y %H:%M:%S')

print(date_object)