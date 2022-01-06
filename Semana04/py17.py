import datetime
import pytz

d = datetime.date(2016, 9, 24)
print(d)


tday = datetime.date.today()
print(tday)
print(tday.day)
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

tdelta = datetime.timedelta(hours=12)


bday = datetime.date(2022, 3, 22)

till_bday = bday - tday
print(till_bday)
print(till_bday.days)



t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

# dt = datetime.datetime.today()
# dtnow = datetime.datetime.now()
# print(dir(datetime.datetime))
# print(dt)
# print(dtnow)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, 1000)
print(dt)
print(dt.time)
print(dt.year)
print(dir(dt))

dt_today = datetime.datetime.today()
dtnow = datetime.datetime.now()
dtutcnow = datetime.datetime.utcnow()
print(dt_today, 'aaaaaaaaaaa', dtnow, 'aaaaaaaaaaa', dtutcnow)




dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)


dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow2)


dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

for tz in pytz.all_timezones:
	print(tz)


dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)


dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
