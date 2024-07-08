import datetime as dt

t_delta = dt.timedelta(hours=9)
JST = dt.timezone(t_delta, 'JST')
now = dt.datetime.now(JST)
d = now.strftime('%Y%m')

print(type(now))