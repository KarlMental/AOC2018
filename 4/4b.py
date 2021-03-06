from datetime import datetime, timedelta

with open('input.txt', 'r') as f:
    data = f.read().split('\n')

def rationalize_timestamps(diary):
	for i, row in enumerate(diary):
		if row[0].hour > 1:
			diary[i][0] += timedelta(days=1)
			diary[i][0] = diary[i][0].replace(hour=0, minute=0)
		if row[0].hour == 0 and  row[1][0] == '#':
			diary[i][0] = diary[i][0].replace(hour=0, minute=0)
	return diary

data = [[datetime.strptime(row[row.find("[")+1:row.find("]")], "%Y-%m-%d %H:%M"), row[row.find("]")+8:]] for row in data]
data = sorted(rationalize_timestamps(data))

schedules = {}

for row in data:
	if row[1][0] == '#':
		guard = row[1].split(' ')[0]
		if guard in schedules.keys():
			schedules[guard].append([0 for i in range(60)])
		else:
			schedules[guard] = [[0 for i in range(60)]]
	elif row[1] == 'asleep':
		for minute in range(row[0].minute, 60):
			schedules[guard][-1][minute] = 1
	elif row[1] == 'up':
		for minute in range(row[0].minute, 60):
			schedules[guard][-1][minute] = 0

guard_stats = {}

for key, value in schedules.items():
	summa = sum([sum(day) for day in value])
	count_list = [0 for i in range(60)]
	for day in value:
		for minute, value in enumerate(day):
			count_list[minute] += value
	guard_stats[key] = {'summa': None, 'type_value': None, 'schedule_sum': count_list}
	guard_stats[key]['summa'] = summa
	guard_stats[key]['type_value'] = count_list.index(max(count_list))

match = ['noguard', 0, 0]
print(guard_stats)
for key, value in guard_stats.items():
	for minute, sleep_sum in enumerate(guard_stats[key]['schedule_sum']):
		if sleep_sum > match[1]:
			match = [key, sleep_sum, minute]
print(match)
print(int(match[0][1:])*match[2])
