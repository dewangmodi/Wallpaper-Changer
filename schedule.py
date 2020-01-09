""" For easy testing of whether cron is correctly configured or not
r = open('a.txt','w')
r.write('Working well!')
r.close()
"""

try:
	import sys
	import json
	import functions
	import datetime
	from main import load_json,change_now,write_json


	today = datetime.date.today()
	config = load_json('config.json')
	record = load_json('record.json')
	last_date = datetime.datetime.strptime(record['last_update'],"%d/%m/%Y").date()
	if today-last_date>=datetime.timedelta(days=int(config['frequency'])):
		change_now(config,record)
		record['last_update'] = today.strftime("%d/%m/%Y")
		record_str = json.dumps(record)
		write_json(record,'record.json')

except Exception as e:
	r = open('exception.txt','a')
	today = datetime.date.today()
	r.write(today.strftime("%d/%m/%Y"))
	r.write(" =====> ")
	r.write(str(e))
	r.close()
