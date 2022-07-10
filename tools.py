import os
import sys
import math
import time
import subprocess
import webbrowser
import random
import collections  # Plans to use Counter() !! 
from tqdm import tqdm

'''
##Systems##
'''
EROS = 'a_w366@eros.cs.txstate.edu'
FRONTERA = 'a_w366@frontera.tacc.utexas.edu'


def main():
	'''
	Run tests here
	'''
	print(runCommand('pwd')[0])
	files = runCommand('ls')
	printList(files)
	
	for file in files:
		if getFileExt(file) == 'txt':
			printList(readFile(file))
		else:
			print(getFileExt(file))


'''
##WHERE AM I?##
'''
dir_path = os.path.dirname(os.path.realpath(__name__))
'''
##WHERE THE FILE FROM?##
'''
file_path = os.path.dirname(os.path.realpath(__file__))
'''
##WEB TOOLS##
'''

HIST = '/Users/Walker/Documents/Code/Python/Tools/search_engine_history.txt'

def websearch(query):
	'''
	Open new browser window with given query
	'''
	web = formatSearch(query)
	webbrowser.open_new(web)
	log_info = f'{timeStamp()} : {web}' 
	log(HIST, log_info)

def formatSearch(website):
	'''
	Format google search -> str::URL
	'''
	root = 'https://www.google.com/search?q='

	if website == 'youtube':
		return 'https://www.youtube.com/'

	website = root + website.replace(' ','+')
	return website

def getHistory():
	'''
	Get last 10 logs of search engine history 
	'''
	history = readFile(HIST)

	num_items = 10 if len(history) > 9 else len(history) 
	start = -1
	temp_hist = subList(history, start, start - num_items)

	printColl(temp_hist)

			
'''
##COLLECTION / PRINT TOOLS##
'''
LETTERS = [chr(x) for x in range(ord('a'), ord('z')+1)]

def removeAll(rem, arr):
	'''
	removes all instances of {rem} in place in list
	'''
	while(rem in arr):
		arr.pop(arr.index(rem))

def makeUnique(items):
	'''
	creates new list with renamed duplicates
	'''
	no_dup = []
	for elem in items:
		if elem not in no_dup:
			no_dup.append(elem)
		else:
			elem+='-0'
			while(elem in no_dup):
				num = int(elem[-1])
				num += 1
				elem = elem[:-1] + str(num)
			no_dup.append(elem)
	return no_dup

def countLetters(words):
	'''
	returns count of letters
	param: list or string
	return: dict
	'''
	
	count = {letter: 0 for letter in LETTERS}

	if type(words) == list:
		words = ''.join(words)

	words = words.replace(' ','')

	for let in words.lower():
		count[let] += 1

	return count

def randomLet():
	'''
	returns random letter -> chr
	'''
	return  random.choose(LETTERS)

def makeList():
	'''
	input -> List
	'''
	words = []
	while True:
		words.append(input())
		if words[-1] == 'q':
			words.pop(-1)
			printList(words)
			return words
def subList(ls, start, end):
	'''
	Create and return sublist with start and end indicies  -> List 
	'''
	new_ls = []
	step = -1 if start < 0 else 1
	for i in range(start, end+1, step):
		new_ls.append(ls[i])
	return new_ls


def printList(lst, sep=', '):
	'''
	Print pretty list
	'''
	num_items = len(lst)
	print(f'items : {num_items}')


	for i, elem in enumerate(lst):
		if i == 0:
			print(f'[{elem}', end=sep)
		elif i == num_items-1:
			print(f'{elem}]')
		else:
			print(elem, end=sep)

def printColl(col):
	'''
	Print collection of items with new line
	'''
	printList(col, sep='\n')

def printLocals(locals, show_all=False):
	'''
	locals() Print local variables
	'''
	char_per_line = 60

	for key, val in locals.items():
		if not key[:2] == '__':
			if len(str(val)) > char_per_line and not show_all:
				print(f'{key} = {str(val)[:char_per_line]}...')
			else:
				print(f'{key} = {val}')


'''
##FILE TOOLS##
'''

def getFileExt(file):
	'''
	Return 
	'''
	ext = file.split('.')
	return ext[-1] if len(ext) > 1 else ext

def readFile(file):
	'''
	.txt -> str[]
	'''

	with open(file, 'r') as f:
		lines = [line.strip() for line in f.readlines()]
		for i in tqdm(range(len(lines)),desc=f'Reading...'):
			pass

	return lines

def log(file, data):
	'''
	Append data to .txt
	'''
	with open(file, 'a')as f:
		write(f,data)

def makeTxt(data):
	'''
	List -> .txt
	'''
	file = f'{dir_path}/{getTime()}.txt'
	with open (file, 'w') as f:
		write(f,data)

	print(f'Writing to file "{file}"... ')
	# open file
	os.system(f'open {file}')
	return file

def write(f, data):
	'''
	Write data to open file
	'''
	if type(data) == str or type(data) == int:
		f.write(str(data))
		f.write('\n')
	else:
		for elem in data:
			f.write(str(elem))
			f.write('\n')

def readCSV(file):
	'''
	Read CSV file and return dict with lists as values
	'''
	data = {}
	sep = ','
	with open(file, 'r') as f:
		headers = f.readline().strip().split(sep)
		file_data = f.read().split('\n')

	for header in headers:
		data[header] = list()
	for line in file_data:
		d = line.split(sep)
		for col, elem in zip(headers, d):
			data[col].append(elem)
	return data

'''
##TIME TOOLS##
'''

def getTime():
	'''
	Current time year-month-day-hour-minute -> str
	'''
	return time.strftime("%Y_%m_%d_%H:%M", time.localtime())

def timeStamp():
	'''
	Current time day-day-mon-year-hour-minute -> str
	'''
	return time.strftime("%a, %d %b %Y %H:%M", time.localtime())


'''
##SYSTEM / OS TOOLS##
'''

def login(sys):
	'''
	SSH login to remote system
	'''
	os.system(f'ssh {sys}')

IP_LOG = '/Users/Walker/Documents/Code/Python/Tools/IP.txt'

def logIP():
	'''
	Logs IP address to IP.txt
	'''
	file = IP_LOG
	ip_address = getIP()
	data = f'{timeStamp()} : {ip_address}'
	log(file, data)

def getIP():
	'''
	Return current IP address -> str
	'''

	# Run ifconfig, filter for broadcast, save to clipboard
	os.system('ifconfig | grep broadcast | pbcopy')
	results = runCommand('pbpaste')

	if results:
		return results.split()[1]
	else:
		return 'No IP address found'

def clip(data):
	'''
	Clip data to clipboard (CMD + C)
	'''
	cmd = f'echo {data} | pbcopy'
	os.system(cmd)

def sendFile(file):
	'''
	Send file from host to school ssh
	'''
	address = EROS
	destination = '/home/Students/a_w366'

	cmd = f'scp {file} {address}:{destination}'

	os.system(cmd)

def clear():
	'''
	Clear terminal
	'''
	os.system('clear')

def runCommand(cmd):
	'''
	Run command and return results -> str[]
	!! RUNS COMMAND IN NEW WINDOW !! 
	'''
	results = subprocess.run(cmd, stdout=subprocess.PIPE, text=True).stdout.strip()

	if results.find('\n') >= 0:
		results = results.split('\n')

	return results


if __name__ == '__main__':
	main()