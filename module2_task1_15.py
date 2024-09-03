from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(text_link)
    link = browser.find_element(By.LINK_TEXT, text_link)
    time.sleep(5)
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Иван")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Петров")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Смоленск")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Россия")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла