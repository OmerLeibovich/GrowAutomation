import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from InitLog import init_log
from ChooseItemsPage import FirstPage
from DetailsPage import SecondPage
from ChoosePayOption import ChoosePayOption
from FillPaymentDetails import  FillPaymentDetails
init_log()
logging.info("script start")
service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
options.service = service

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://sandbox.grow.link/6f340bc4d18a0bcb559914d970ac2870-MTE4NjI")

FirstPage(driver)
logging.info("passed firstPage")

SecondPage(driver)
logging.info("passed secondPage")

ChoosePayOption(driver)
logging.info("Visa payment option selected")

FillPaymentDetails(driver)
logging.info("complete fill payment details")

logging.info("script end")

time.sleep(100)


