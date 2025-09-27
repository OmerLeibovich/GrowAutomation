from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging

def FirstPage(driver):
    try:
        checkBox_One = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='product_checkbox_8997_']"))
        )
        checkBox_One.click()
    except:
        logging.error("Failed to check Shakshuka checkBox")

    try:
        checkBox_Two = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='product_checkbox_8998_']"))
        )
        checkBox_Two.click()
    except:
        logging.error("Failed to check pita checkBox")

    try:
        checkBox_Three = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='product_checkbox_9000_']"))
        )
        checkBox_Three.click()
    except:
        logging.error("Failed to check falafel checkBox")



    try:
        itemShakshuka = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='להוספת כמות למוצר שקשוקה']"))
        )
        itemShakshuka.click()
    except:
        logging.error("Failed to increase Shakshuka by 1")
    try:
        itemPita = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='להוספת כמות למוצר פיתה']"))
        )
        itemPita.click()
    except:
        logging.error("Failed to increase pita by 1")

    try:
        itemFalafel = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='להוספת כמות למוצר פלאפל']"))
        )
        itemFalafel.click()
    except:
        logging.error("Failed to increase falafel by 1")

    try:
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "span.main-payment-content_price-value__T5lnO.main-payment-content_final-price__YNO_r"))
        )
        Price = int(price_element.text)
        assert Price == 62, f"Expected 62 but got {Price}"
        logging.info("Price assertion passed: %s", Price)

    except TimeoutException:
        logging.error("Failed to find price element within timeout")

    except ValueError:
        logging.error("Price element text is not a valid integer: %s", price_element.text)

    except AssertionError as e:
        logging.error("Assertion failed: %s", e)
    try:
        precent_17 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.main-payment-content_price-value__T5lnO.main-payment-content_vat-value__KLj1Y"))
        )
        VAT=float(precent_17.text)
        assert VAT == round(Price * 0.17, 2), f"Expected {round(Price * 0.17, 2)} but got {VAT}"
        logging.info("Price assertion passed: %s", Price)
    except TimeoutException:
        logging.error("Failed to find precent_17 within timeout")
    except ValueError:
        logging.error("Price precent_17 text is not a valid float: %s", precent_17.text)
    except AssertionError as e:
        logging.error(" Assertion failed: %s", e)

    try:
        nextPhase = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "footer-button_button-wrapper__s0Dxb"))
        )
        nextPhase.click()
    except:
        logging.error("Failed to find nextPage button")
