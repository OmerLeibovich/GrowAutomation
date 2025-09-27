from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

def ChoosePayOption(driver):
    try:
        Visa = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Gr0W8-payment-btn.Gr0W8-show"))
        )
        Visa.click()
    except:
        logging.error("Failed to find visa option")

