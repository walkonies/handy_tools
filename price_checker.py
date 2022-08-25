from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path
import threading
import time
from tools import readCSV

driver = path.dirname(path.realpath(__name__)) + '/chromedriver'

class Browser():
	def __init__(self, driver = None):
		self.Chrome = False
		if driver:
			self.browser = webdriver.Chrome(driver)
			self.Chrome = True
		else:
			self.browser = webdriver.Safari()

	def open(self, item):
		self.browser.get(item.url)
	def getPrice(self, item):
		self.open(item)
		if self.Chrome:
			price = self.getChromePrice()
		else:
			price = self.getSafariPrice()
		item.setPrice(price)
		return price
	def getChromePrice(self):
		ID = 'corePrice_feature_div'
		by = By.ID
		price = self.browser.find_element(by, ID).text[1:-2]
		try:
			price = int(price)
			item.setPrice(price)
		except:
			pass
		return price
	def getSafariPrice(self):
		ID = 'a-price-whole'
		by = By.CLASS_NAME
		price = self.browser.find_element(by, ID).text[:-1]
		try:
			price = int(price)
			item.setPrice(price)
		except:
			pass
		return price
	def execute(self, job):
		return self.getPrice(job)

class Item():
	def __init__(self, item, url):
		self.name = item
		self.url = url
		self.price = None
	def setPrice(self, p):
		self.price = p
	def getPrice(self):
		if self.price:
			return self.price
		return '??'
	def getName(self):
		return self.name
	def __str__(self):
		return f'{self.getName()} - ${self.getPrice()}'

class Job(threading.Thread):
	def __init__(self, id, driver, jobs):
		super().__init__()
		self.id = id
		self.driver = driver
		self.jobs = jobs
		self.output = []
	def run(self):
		t = time.time()
		jobs = self.jobs
		print(f'[{self.id}] -> Job Running...')
		if type(jobs) == list:
			for i, job in enumerate(jobs):
				out = self.driver.execute(job)
				self.output.append(out)
				print(f'[{self.id}] -> Job [{i+1}] of [{len(jobs)}]')
		else:
			out = self.driver.execute(jobs)
			self.output.append(out)
		print(f'[{self.id}] -> Job Complete {time.time()-t:.2f}s')

def getNumJobs(size):
	num_jobs = min(size-1,5)
	while size%num_jobs != 0:
		num_jobs-=1
		if num_jobs == 0:
			num_jobs = 1
			break
	return num_jobs
def getItems(data):
	items = []
	size = len(data['date'])
	for i in range(size):
		name = data['name'][i]
		url = data['url'][i]
		item = Item(name, url)
		items.append(item)
	return items

def partition(size, parts):
	p = []
	for i in range(parts):
		start = i*(size//parts)
		end = (i+1)*size//parts
		p.append((start,end))
	return p



def test():
	data = readCSV('txt/amazon_list.csv')
	items = getItems(data)
	size = len(items)
	num_jobs = getNumJobs(size)
	p_indx = partition(size, num_jobs)
	print(p_indx)
	
	jobs = [Job(i, Browser(driver), p_items[i]) for i in range(num_jobs)]
		
	for j in jobs:
		j.start()
	for j in jobs:
		j.join()
	for i in items:
		print(i)

def main():
	
	
	test()

	



if __name__ == '__main__':
	main()