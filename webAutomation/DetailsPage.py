import os
import logging
import sys
import time
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def SecondPage(driver):
    error = False
    load_dotenv()
    try:
        FullName = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "fullName"))
        )

        if os.getenv("correct_case") == "yes":
            FullName.send_keys(os.getenv("correct_fullname"))
        else:
            FullName.send_keys(os.getenv("incorrect_fullname"))

    except:
        logging.error("Failed to find fullname field")
    try:
        phone = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )
        if os.getenv("correct_case") == "yes":
            phone.send_keys(os.getenv("correct_phone"))
        else:
            phone.send_keys(os.getenv("incorrect_phone"))


    except:
        logging.error("Failed to find phone field")

    try:
        WithoutPickle = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "2934_3448"))
        )
        WithoutPickle.click()
    except:
        logging.error("Failed to find WithoutPickle CheckBox")

    try:
        WithoutFrenchFries = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "2935_3450"))
        )
        WithoutFrenchFries.click()
    except:
        logging.error("Failed to find WithoutFrenchFries CheckBox")


    try:
        prepare = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME,"2933"))
        )
        prepare.click()
    except:
        logging.error("Failed to find prepare field")

    try:
        prepareOption = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "2933_3444"))
        )
        prepareOption.click()
    except:
        logging.error("Failed to find prepareOption field")

    try:
        shipping = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "shipping"))
        )
        shipping.click()
    except:
        logging.error("Failed to find shipping field")

    time.sleep(3)

    try:
        shippingOption = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "shipping_2304"))
        )
        shippingOption.click()
    except:
        logging.error("Failed to find shippingOption field")

    try:
        Terms = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"additional-fields_checkbox-label__VEpko"))
        )
        Terms.click()
    except:
        logging.error("Failed to find terms checkBox")
    try:
        NextPage = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".footer-button_button-wrapper__s0Dxb"))
        )
        NextPage.click()
    except:
        logging.error("Failed to find nextPage Button")
    time.sleep(7)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fullName-input-error"))
        )
        logging.error("Wrong FullName")
        error = True
    except:
        logging.info("Fullname is valid")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "phone-input-error"))
        )
        logging.error("Wrong phone number")
        error = True
    except:
        logging.info("Phone number is valid")

    if error:
        sys.exit(1)







