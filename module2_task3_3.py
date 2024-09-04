import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def test_substring(full_string, substring):
    assert substring in full_string, f'Подстрока "{substring}" не найдена в строке "{full_string}"'

s = "My Name is Julia"
ss = "Name"
test_substring(s,ss)