import datetime

def format_date(date_str):
     print(date_str)
     date_obj = datetime.datetime.fromisoformat(date_str)

     date_obj = date_obj.astimezone(datetime.timezone(datetime.timedelta(hours=-3)))

     date_str = date_obj.strftime("%d-%m-%Y %H:%M:%S")

     return date_str