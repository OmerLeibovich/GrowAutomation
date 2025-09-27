import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

def FillPaymentDetails(driver):
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Gr0W8-credit-iframe"))
    )
    driver.switch_to.frame(iframe)
    time.sleep(2)
    try:
        CardNumber = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "cardNumber"))
        )
        CardNumber.send_keys("4580458045804580")
    except:
        logging.error("Failed to find cardNumber field")

    time.sleep(2)

    try:
        expYear = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "expYear"))
        )
        expYear.click()
        year = Select(expYear)
        year.select_by_value("30")
    except:
        logging.error("Failed to find expYear field")

    time.sleep(2)

    try:
        expMonth = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "expMonth"))
        )
        expMonth.click()
        month = Select(expMonth)
        month.select_by_value("03")
    except:
        logging.error("Failed to find expMonth field")

    time.sleep(2)

    try:
        cvv = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "cvv"))
        )
        cvv.send_keys("123")
    except:
        logging.error("Failed to find cvv field")

    time.sleep(2)

    try:
        SubmitButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "submit-btn"))
        )
        SubmitButton.click()
    except:
        logging.error("Failed to find SubmitButton")
