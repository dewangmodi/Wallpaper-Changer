import sys
import json
import functions
import datetime
import os

CATEGORIES = ['bing','brainy']

def load_json(filename):
	dirname = os.path.dirname(__file__)
	filepath = os.path.join(dirname, filename)
	reader = open(filepath)
	content = reader.read()
	reader.close()
	return json.loads(content)

def write_json(dictionary,filename):
	dirname = os.path.dirname(__file__)
	filepath = os.path.join(dirname, filename)
	dict_str = json.dumps(dictionary)
	writer = open(filepath,'w')
	writer.write(dict_str)
	writer.close()


def display_menu():
	x = input("\nMain Menu\n(Enter the number before a choice to choose it)\n1 - Change Wallpaper Now!\n2 - Change Config file\n3 - View Config file\nEnter your choice : ")
	return int(x)


def change_now(config,record):

	if config['category']=='bing':

		if record['file_count']==config['max_file_count']:

			record['file_count'] = 0

		functions.bing_daily_wallpaper(config['location'],record['file_count'])

	elif config['category']=='brainy':
		if record['file_count']==config['max_file_count']:

			record['file_count'] = 0

		functions.brainy_quotes(config['location'],record['file_count'])

	
	functions.change_wallpaper(config['location'],record['file_count'])
	record['file_count'] += 1
	record['last_update'] = datetime.date.today().strftime("%d/%m/%Y")
	record_str = json.dumps(record)
	
	write_json(record,'record.json')

def view_config(config):

	print("The configurations are : ")
	print("Category : ",config["category"])
	print("Location : ",config['location'])
	print("Max File Count : ",config['max_file_count'])
	print("Frequency of Updating : ",config['frequency'])

def update_config(config):
	
	view_config(config)
	choice = input("Would you like to update the config file? (y/n) : ")
	if (choice=='n') or (choice=='N'):
		return

	category = input('Enter the preferred category :\n1. Bing\n2. Brainy Quotes \nEnter your choice [1-2] : ')
	location = input('Enter a path where wallpapers are to be stored : ')
	file_count = input('Enter max. number of wallpapers to store : ')
	frequency = input('Enter number of days after which wallpaper is to be changed : ')
	config["category"] = CATEGORIES[int(category)-1]
	config["location"] = location
	config['max_file_count'] = file_count
	config['frequency'] = frequency
	config_str = json.dumps(config)
	write_json(config,'config.json')

def main():

	choice = display_menu()
	config = load_json('config.json')
	record = load_json('record.json')
	if choice==1:
		change_now(config,record)

	elif choice==2:
		update_config(config)

	elif choice==3:
		view_config(config)

	else:
		return



if __name__ == '__main__':
	main()
