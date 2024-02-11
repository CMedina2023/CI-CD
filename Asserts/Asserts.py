# Crear de librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Inicializar el controlado de seleniumm ( asegurate de tener le contralador adecuado para tu navegador)
c = Service(r"C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=c)

# Navegar a url
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

#Assert para validar un elemento
usuario = driver.find_element(By.ID, "user-name")
usuario.send_keys("Carlos")
# Crea un assert para validar que exista el elemento
assert driver.find_element(By.ID, "user-name"), "El elemento no está presente en la página"
contraseña = driver.find_element(By.ID, "password")
contraseña.send_keys("Prueba")
btn = driver.find_element(By.ID, "login-button")
btn.click()

#Assert para validar un texto
element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
# Se crea un assert para validar que el texto sea el esperado
assert element.text == "Epic sadface: Username and password do not match any user in this service", "El texto del elemento no coincide con el esperado"

#Cerrar navegador
driver.quit()