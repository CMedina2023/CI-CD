import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones_globales import funciones


# devuelve un conjunto de datos de prueba que se utilizarán para ejecutar la prueba varias veces con diferentes valores
def get_Data():
    return {
        "Primera",
        "Segunda",
        "Tercero",
    }


# se utiliza el decorador @pytest.mark.parametrize() para parametrizar la función test_1 con el argumento "buscar"
@pytest.mark.parametrize("buscar", get_Data())
def test_1(buscar):
    c = Service(r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    f.Navegar("https://demo.seleniumeasy.com/basic-first-form-demo.html", 1)
    f.Texto_Mixto("xpath", "//input[contains(@id,'user-message')]", buscar, 1)
    f.Click_Mixto("xpath", "(//button[@type='button'])[2]", 2)
    driver.save_screenshot(r"C:\Users\Lenovo\Desktop\Evidencia\Prueba1.png")
