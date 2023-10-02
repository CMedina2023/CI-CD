from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
driver.maximize_window()
driver.implicitly_wait(5)

# Busca el iframe dentro de la pagina
iframe = driver.find_element(By.ID, "frame1")

# Cambia el contexto al iframe utilizando el método switch_to.frame() y pasando el elemento iframe.
driver.switch_to.frame(iframe)
driver.save_screenshot(r"C:\Users\Lenovo\Desktop\Evidencia\Prueba1.png")
texto = driver.find_element(By.ID, "sampleHeading")
assert texto.text == "This is a sample page", "No se encontro el texto"

# Al final la interaccion podremos regresar a la pagina principal de la siguiente manera
driver.switch_to.default_content()

#Cierra navegador
driver.quit()