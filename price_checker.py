from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path
URL = 'https://www.amazon.com/Intel-i5-12600KF-Desktop-Processor-Unlocked/dp/B09FXFJW2F/?_encoding=UTF8&pd_rd_w=G28nJ&content-id=amzn1.sym.8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_p=8cf3b8ef-6a74-45dc-9f0d-6409eb523603&pf_rd_r=AVKVESDMB0HKX97CTNB4&pd_rd_wg=Xj0Ga&pd_rd_r=7443b95c-ee96-44a0-bfac-b6de26834c1b&ref_=pd_gw_ci_mcx_mi'
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
			self.getChromePrice()
		else:
			self.getSafariPrice()

	def getChromePrice(self):
		ID = 'corePrice_feature_div'
		by = By.ID
		price = self.browser.find_element(by, ID).text[1:-2]
		try:
			price = int(price)
			item.setPrice(price)
		except:
			pass
		print(price)
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
		print(type(price))
		return price

class Item():
	def __init__(self, item, url):
		self.name = item
		self.url = url
		self.price = None
	def setPrice(self, p):
		self.price = p
		print('price =',p)
	def getPrice(self):
		if self.price:
			return self.price
		return '??'
	def getName(self):
		return self.name
	def __str__(self):
		return f'{self.getName()} - ${self.getPrice()}'

def main():
	driver = path.dirname(path.realpath(__name__)) + '/chromedriver'
	b = Browser()
	ssd = Item('ssd', 'https://www.amazon.com/dp/B08V7GT6F3/?coliid=I3NYUVEK83KWIE&colid=1LAJEQL0430W6&psc=1&ref_=gv_vv_lig_pi_dp')
	i5 = Item('i5 CPU', 'https://www.amazon.com/dp/B09FXFJW2F/?coliid=I1F3G29H9WS1UD&colid=1LAJEQL0430W6&psc=1&ref_=gv_ov_lig_pi_dp')
	b.getPrice(ssd)
	b.getPrice(i5)
	print(ssd,i5)


if __name__ == '__main__':
	main()