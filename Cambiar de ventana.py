import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Inicializar el controlador de Selenium
c = Service(r"C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=c)

# Navegar a la página demoqa.com/browser-windows
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

# Hacer clic en el botón "New Window"
new_window_button = driver.find_element(By.ID, "windowButton")
new_window_button.click()

# Obtener los identificadores de todas las ventanas abiertas
window_handles = driver.window_handles
time.sleep(2)

# Cambiar al controlador de la nueva ventana
driver.switch_to.window(window_handles[1])
driver.maximize_window()
time.sleep(2)
# Cerrar la nueva ventana
driver.close()

# Cambiar de nuevo al controlador de la ventana principal
driver.switch_to.window(window_handles[0])
time.sleep(2)

# Cerrar el navegador
driver.quit()