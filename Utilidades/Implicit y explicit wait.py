import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Permite utilizar la funcionalidad de espera explicita en selenium
from selenium.webdriver.support.ui import WebDriverWait
# Proporciona un conjunto de condiciones para realizar una espera explicita y validar que las condiciones se cumplan
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el controlador de Selenium
c = Service(r"C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=c)


# Configurar un Implicit Wait de 20 segundos (Esta espera se realiza de forma global, es decir, todos los elementos son afectados)
driver.implicitly_wait(20)

# Navegar a la página demoqa.com/checkbox
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()

yesRadio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yesRadio.click()

# Utilizar un Explicit Wait para elementos de forma individual y luego espera a que se cumpla la condicion
texto = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='mt-3']")))
print(texto.text)

# Cerrar el navegador
driver.quit()