from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Esta libreria define una excepcion en caso que no pueda encontrar un elemento
from selenium.common.exceptions import NoSuchElementException
# proporciona la clase options que se utiliza para configurar opciones especificas del navegador
from selenium.webdriver.chrome.options import Options

# Inicializar el controlador de Selenium
c = Service(r"C:\chromedriver_win32\chromedriver.exe")
# Configurar las opciones del controlador para tomar capturas de pantalla
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana del navegador)
driver = webdriver.Chrome(service=c, options=chrome_options)

# Navegar a la página demoqa.com/radio-button
driver.get("https://demoqa.com/radio-button")

try:
    # Intentar encontrar el radio button con el valor "Yes"
    texto = driver.find_element(By.XPATH, "//p[@class='mt-3']")

    # Hacer algo con el radio button si se encuentra

    # (por ejemplo, imprimir el texto del radio button)
    print(texto.text)

except NoSuchElementException:
    # Manejar la excepción si no se encuentra el radio button
    print("El texto no esta visible")
    # Imprime pantalla con el resultado
    driver.save_screenshot(r"C:\Users\Lenovo\Desktop\Evidencia\Prueba1.png")

# Cerrar el navegador
driver.quit()
