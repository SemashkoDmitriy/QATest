import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = x_element1.text
    x_element2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = x_element2.text
    y = int(x1)+int(x2)
    print(y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(y))  # ищем элемент с текстом "Python"
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла