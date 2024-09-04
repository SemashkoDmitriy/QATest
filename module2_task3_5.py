import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def reg(link):
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Иван")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Петров")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("mail@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text


class TestRegistration(unittest.TestCase):


    def test_registration1(self):
        link = "http://suninjuly.github.io/registration2.html"

        self.assertEqual("Congratulations! You have successfully registered!", reg(link),
                         "Что-то не так с регистрацией")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration1.html"

        self.assertEqual("Congratulations! You have successfully registered!", reg(link),
                         "Что-то не так с регистрацией")

    # def test_reg2(self):
    #     self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

