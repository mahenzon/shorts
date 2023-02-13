from datetime import datetime, timedelta

date_time = datetime(2022, 2, 26, 13, 37)
print(date_time)

two_days = timedelta(days=2)
print(date_time + two_days)

date_time = datetime(2020, 2, 26, 13, 37)
four_days = timedelta(days=4)
print(date_time + four_days)
