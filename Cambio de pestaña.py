import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Inicializar el controlador de Selenium
c = Service(r"C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=c)

# Navegar a la página demoqa.com/browser-windows
driver.get("https://demoqa.com/browser-windows")

# Hacer clic en el botón "New Tab"
new_tab_button = driver.find_element(By.XPATH, "//button[@id='tabButton']")
new_tab_button.click()

# Obtener los identificadores de todas las pestañas abiertas
window_handles = driver.window_handles

# Cambiar al controlador de la nueva pestaña
driver.switch_to.window(window_handles[1])
time.sleep(2)
# Cerrar la nueva pestaña
driver.close()

# Cambiar de nuevo al controlador de la pestaña principal
driver.switch_to.window(window_handles[0])
time.sleep(2)

# Cerrar el navegador
driver.quit()