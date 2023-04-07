import datetime

def print_working_days(date1, date2):
    date_format = '%Y-%m-%d'
    start_date = datetime.datetime.strptime(date1, date_format)
    end_date = datetime.datetime.strptime(date2, date_format)
    delta = datetime.timedelta(days=1)
    while start_date < end_date:
        if start_date.weekday() < 5: # Monday = 0, Friday = 4
            print(start_date.strftime(date_format))
        start_date += delta


