
import subprocess
import os
import sys

def runCommand(cmd):
	'''
	Run command and return results -> str[]
	!! RUNS COMMAND IN NEW WINDOW !! 
	'''
	results = subprocess.run(cmd, stdout=subprocess.PIPE, text=True).stdout.strip()

	if results.find('\n') >= 0:
		results = results.strip().split('\n')

	return results

def removeAll(rem, arr):
	while(rem in arr):
		arr.pop(arr.index(rem))

def getNames(items):
	names = []
	for i in items:
		elem = i.split(' ')

		removeAll('',elem)
			
		name = elem[-1]
		names.append(name)
	return names


def getDates(items):
	dates = []
	for i in items:
		elem = i.split(' ')

		removeAll('',elem)
		
		date = elem[5] + elem[6]
		dates.append(date)
	return dates

def checkDup(items):
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


def main():
	# use python3 clips.py {dir}
	if len(sys.argv) < 2:
		print('Useage: python3 rename.py {dir}')
		dir = input("Directory: ")
	else:
		dir =' '.join(sys.argv[1:])

	cmd = f'ls -l {dir}'
	os.system(cmd)

	items = runCommand(cmd)
	print(items)
	items.pop(0)
	items.pop()

	names = getNames(items)
	dates = getDates(items)
	dates = checkDup(dates)

	ext = input("Ext: ")
	if '.' not in ext:
		ext = '.txt'

	for old, new in zip(names, dates):
		cmd = f'mv {old} {new}.{ext}'
		runCommand(cmd)

	print('Rename complete!')

if __name__ == '__main__':
	main()
