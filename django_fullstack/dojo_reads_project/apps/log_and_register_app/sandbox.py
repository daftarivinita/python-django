from datetime import datetime,date, timedelta
import re

from django.db.models import aggregates
today_date = date.today()

min_age = today_date - timedelta(days=13*365)
print(type(str((min_age))))



# format_str = '%Y-%m-%d %H:%M:%S%z'
# input_date = datetime.strptime('1988-08-01 00:00:00+00:00', format_str).date()

# # calculate age
# age = today_date - input_date
# print(age.days/365)

format_str = '%Y-%m-%d %H:%M:%S%z'
datetime_obj = datetime.strptime('1988-08-01 00:00:00+00:00', format_str).date()

age_years = abs((today_date - datetime_obj)/365)
print(type(str(age_years)))
PASSWORD_REGEX=re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
if PASSWORD_REGEX.match("vinita1471"):
    print(True)
else:
    print(False)
   
