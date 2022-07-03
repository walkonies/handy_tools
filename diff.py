import os
import sys
from tools import getTime

'''
This program helps to find changes in two files
Given two files, this program determines what is added
and what is removed, saves data in text file, and 
outputs to termnal 
'''

def getDiff(f1, f2):
	time = getTime()
	new_file = 'txt/diff-'+time+'.txt'
	os.system(f'diff -u {f1} {f2} >> {new_file}')
	return new_file

def readDiff(text_file):
    rem = []
    added = []
    lines = []
    with open(text_file,'r') as f:
            lines = f.readlines()
    for line in lines:
            first = line[0]
            if first  == '-':
                    rem.append(line)
            elif first == '+':
                    added.append(line)
    return (added, rem)

def showDiff(added, rem):
	print('****ADDED****')
	for elem in added:
		print(elem.strip())
	print('\n****REMOVED****')
	for elem in rem:
		print(elem.strip())

def main():
	if len(sys.argv) > 2:
		f1 = sys.argv[1]
		f2 = sys.argv[2]
	else:
		f1, f2 = input('Files: ').split()

	diff = getDiff(f1,f2)
	added, rem = readDiff(diff)
	showDiff(added,rem)

if __name__ == '__main__':
	main()