from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    button_count = len(browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket'))
    time.sleep(30)
    assert button_count > 0, "button not found"


