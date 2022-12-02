import datetime
 


year=input('Please enter year: ')
month=input('Please enter month: ')
day=input('Please enter day: ')

today = datetime.date(int(year), int(month), int(day))

one_week = datetime.timedelta(days=7)

print(today)

for x in range(16):
	today = today + one_week
	print(today)
