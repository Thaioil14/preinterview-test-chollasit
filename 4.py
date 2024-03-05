from datetime import datetime

x = input("Date x = ")
y = input("Date y = ")
m = input("Date m = ")

def between_dates(date_x, date_y, date_m):
    return date_x < date_m < date_y or date_y < date_m < date_x

date_x = datetime.strptime(x, "%d/%m/%Y")
date_y = datetime.strptime(y, "%d/%m/%Y")
date_m = datetime.strptime(m, "%d/%m/%Y")
days_difference = (date_m - date_x).days
if between_dates(date_x, date_y, date_m):
    print("true,","{} Days".format(days_difference))
else:
    print("false,","{} Days".format(days_difference))



