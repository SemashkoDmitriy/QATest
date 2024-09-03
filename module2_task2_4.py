import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("Значение people radio: ", people_checked)
    assert people_checked is not None, "People radio не выбран в качестве значения по умолчанию"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None, "Robots radio выбран в качестве значения по умолчанию"

    field_answer = browser.find_element(By.ID, "answer")
    field_answer.send_keys(y)
    check_b = browser.find_element(By.ID, "robotCheckbox")
    check_b.click()
    browser.execute_script("window.scrollBy(0, 100);")
    radio_b = browser.find_element(By.ID, "robotsRule")
    radio_b.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла