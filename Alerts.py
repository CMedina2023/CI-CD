# Crear de librerias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Sirve para habilitar la funcion webdriverwait que realiza una espera explicita
from selenium.webdriver.support.ui import WebDriverWait
# Habilitar la condicion de la espera explicita
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlado de seleniumm ( asegurate de tener le contralador adecuado para tu navegador)
c = Service(r"C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=c)

# Navegar a url
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

# Esperar hasta que el botón "Click for JS Alert" esté visible
btnalert = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='confirmButton']")))

# Hacer clic en el botón "Click for JS Alert"
btnalert.click()
time.sleep(4)
driver.save_screenshot(r"C:\Users\Lenovo\Desktop\Evidencia\Prueba1.png")

# Cambiar al controlador de la alerta
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
# Cancelar la alerta
alert.accept()
driver.save_screenshot(r"C:\Users\Lenovo\Desktop\Evidencia\Prueba2.png")
driver.quit()