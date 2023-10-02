from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Funciones_globales import funciones


tg = 2


def test_1():
    c = Service(r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    f.Navegar("https://demoqa.com/", tg)
    f.Click_Mixto("xpath", "//*[@id='app']/div/div/div[2]/div/div[2]/div/div[2]/svg", tg)


def test_mixto():
    c = Service(r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    f.Navegar("https://demoqa.com/text-box", tg)
    f.Texto_Mixto("id", "//*[@id='userName']", "Carlos", tg)


def test_navegar():
    c = Service(r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    f.Navegar("https://demoqa.com/radio-button", tg)


def test_2():
    c = Service(r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    # f.Navegar utiliza el objeto y la funcion perteneciente a ese objeto
    f.Navegar("https://www.google.com.mx/", 4)
    f.Texto_Mixto("xpath", "//textarea[@id='APjFqb']", "Hola", 5)
