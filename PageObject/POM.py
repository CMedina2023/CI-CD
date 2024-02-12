import time
import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Funciones_globales import funciones
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class base_test(unittest.TestCase):

    def setUp(self):
        c = Service(r"C:/Users/Carlos Medina/Downloads/chromedriver-win64/chromedriver.exe")
        # Configurar las opciones del controlador para tomar capturas de pantalla
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana del navegador)
        self.driver = webdriver.Chrome(service=c, options=chrome_options)

    def test1(self):
        driver = self.driver
        f = funciones(driver)
        driver.get("https://demoqa.com/")

    def test2(self):
        driver = self.driver
        f = funciones(driver)
        driver.get("https://www.google.com.mx/")

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output=r'C:/Users/Lenovo/PycharmProjects/PruebasAutomatizadas/Reportes'))
