from selenium import  webdriver
import pyautogui
from time import sleep

#Ler dados da pessoa

nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
idade = str(input('Digite sua idade: '))
email = str(input('Digite seu email: '))
senha = str(input('Digite a senha a ser cadastrada '))
sexo = str(input('Sexo =[M/F] '))


pyautogui.PAUSE = 1.5
navegador = webdriver.Chrome(executable_path=r'chromedriver.exe')
navegador.get('https://www.facebook.com/')
sleep(1.5)
navegador.find_element_by_css_selector('._42ft._4jy0._6lti._4jy6._4jy2.selected._51sy').click()
sleep(1)
pyautogui.write(nome)
pyautogui.press('enter')
pyautogui.write(sobrenome)
pyautogui.press('enter')
sleep(0.5)
pyautogui.write(email)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
pyautogui.write(email)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
sleep(0.5)
pyautogui.write(senha)
pyautogui.press('enter')
pyautogui.write(idade)
pyautogui.press('enter')
sleep(1)
if sexo[0].upper() == 'M':
    pyautogui.press('right')
else:
    pyautogui.press('right')
    pyautogui.press('left')
navegador.find_element_by_name('websubmit').click()