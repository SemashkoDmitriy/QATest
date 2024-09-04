import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

s = 'My Name is Julia'
ss = 'Names'

if ss in s:
    print('Substring found')

index = s.find(ss)
if index != -1:
    print(f'Substring found at index {index}')
else:
    print('Substring not found')

assert ss in s, f'Подстрока "{ss}" не найдена в строке "{s}"'