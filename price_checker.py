from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path
URL = 'https://www.amazon.com/Intel-i5-12600KF-Desktop-Processor-Unlocked/dp/B09FXFJW2F/?_encoding=UTF8&pd_rd_w=G28nJ&content-id=amzn1.sym.8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_p=8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_r=AVKVESDMB0HKX97CTNB4&pd_rd_wg=Xj0Ga&pd_rd_r=7443b95c-ee96-44a0-bfac-b6de26834c1b&ref_=pd_gw_ci_mcx_mi'
class Browser():
	driver = path.dirname(path.realpath(__name__)) + '/chromedriver'
	def __init__(self):
		self.browser = webdriver.Chrome(self.driver)
		self.opened = False

	def open(self, item):
		self.browser.get(item.url)
		if not self.opened:
			self.opened = True

	def getPrice(self, item):
		if not self.opened:
			self.open(item)
		ID = 'corePrice_feature_div' 
		price = self.browser.find_element(By.ID, ID).text[1:-2]
		try:
			price = int(price)
			item.setPrice(price)
		except:
			pass
		return price

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
