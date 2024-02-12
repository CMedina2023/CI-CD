import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones_globales import funciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Funciones2 import Demo
import pathlib

tg = 2
vacio = ""
path = str(pathlib.Path().absolute())

def test_Compra():
    c = Service(r"C:\Users\Carlos Medina\Downloads\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    f.Navegar("https://www.saucedemo.com/", tg)
    f.Texto_Mixto("ID", "user-name", "standard_user", tg)
    f.Texto_Mixto("ID", "password", "secret_sauce", tg)
    f.Click_Mixto("ID", "login-button", tg)
    f.Click_Mixto("ID", "item_0_img_link", tg)
    element = driver.find_element(By.XPATH, "//*[@id='inventory_item_container']/div/div/div[2]/div[2]")
    assert element.text == "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.", "El texto del elemento no coincide con el esperado"
    f.Click_Mixto("ID", "add-to-cart-sauce-labs-bike-light", tg)
    RemButton = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "remove-sauce-labs-bike-light")))
    f.Click_Mixto("ID", "shopping_cart_container", tg)
    texto = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
    print("Se ingresa para hacer checkout")
    f.Click_Mixto("ID", "checkout", tg)
    f.Texto_Mixto("ID", "first-name", "NombreTest", tg)
    f.Texto_Mixto("ID", "last-name", "ApellidoTest", tg)
    f.Texto_Mixto("ID", "postal-code", "80000", tg)
    f.Click_Mixto("ID", "continue", tg)
    texto = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[2]")))
    print("Se ingresa para revisar compra")
    f.Click_Mixto("ID", "finish", tg)
    try:
        # Intentar encontrar el radio button con el valor "Yes"
        texto = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2")
        print(texto.text)

    except NoSuchElementException:
        # Manejar la excepción si no se encuentra el texto
        print("No se tiene mensaje confirmación de la compra")
        # Imprime pantalla con el resultado
        driver.save_screenshot(r"C:\Evidencia\Prueba1.png")


def test_compra():
    c = Service(r"D:\Descargas\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    # Navegamos a la pagina
    f.Navegar("https://www.saucedemo.com/", tg)
    # Realizamos el login
    f.Texto_Mixto("ID", "user-name", "performance_glitch_user", 1)
    f.Texto_Mixto("ID", "password", "secret_sauce", 1)
    f.Click_Mixto("ID", "login-button", tg)
    # Agregamos un articulo al carrito
    f.Click_Mixto("ID", "add-to-cart-sauce-labs-bike-light", tg)
    driver.save_screenshot(r"C:\Evidencias\AgregarProducto.png")
    # Entramos al carrito
    f.Click_Mixto("ID", "shopping_cart_container", tg)
    driver.save_screenshot(r"C:\Evidencias\Carrito.png")
    # Hacemos checkout
    f.Click_Mixto("ID", "checkout", tg)
    # Llenamos los datos para la compra
    f.Texto_Mixto("ID", "first-name", "Ivan", 1)
    f.Texto_Mixto("ID", "last-name", "Zazueta", 1)
    f.Texto_Mixto("ID", "postal-code", "80040", 1)

    # Encontramos los campos personales a mandar en la compra
    nombre = f.Encontrar_elemento("ID", "first-name", 1)
    apellido = f.Encontrar_elemento("ID", "last-name", 1)
    postal = f.Encontrar_elemento("ID", "postal-code", 1)

    # Validamos que ningun campo vaya vacio
    assert nombre.text == vacio, "Capture el nombre"
    assert apellido.text == vacio, "Capture el apellido"
    assert postal.text == vacio, "Capture el codigo postal"

    f.Click_Mixto("ID", "continue", tg)
    driver.save_screenshot(r"C:\Evidencias\Compra.png")
    # Finalizamos la compra
    f.Click_Mixto("ID", "finish", tg)
    driver.save_screenshot(r"C:\Evidencias\Final.png")


def test_logout():
    c = Service(r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    f.Navegar("https://www.saucedemo.com/", 1)
    f.Texto_Mixto("ID", "user-name", "standard_user", 1)
    f.Texto_Mixto("ID", "password", "secret_sauce", 1)
    f.Click_Mixto("ID", "login-button", 2)
    f.Click_Mixto("ID", "add-to-cart-sauce-labs-backpack", 2)
    f.Click_Mixto("ID", "shopping_cart_container", 2)
    f.Click_Mixto("ID", "checkout", 2)

    f.Texto_Mixto("ID", "first-name", "Christian", 1)
    f.Texto_Mixto("ID", "last-name", "Flores", 1)
    f.Texto_Mixto("ID", "postal-code", "80197", 1)
    f.Click_Mixto("ID", "continue", 2)

    f.Click_Mixto("ID", "finish", 2)
    # cerrar navegador
    driver.quit()




@pytest.mark.parametrize(
    ["url_page", "time_page", "selector_name", "selector_pwd", "username", "pwd", "selector_login", "class_car", "xpath_error_login", "time_login",
     "selector_product", "link_cart", "checkout", "selector_first_name", "selector_last_name", "selector_zipcode",
     "first_name", "last_name", "zipcode", "selector_continue", "xpath_error", "finish", "complete", "time_compra"],
    [(["https://www.saucedemo.com/", 1, "user-name", "password", "standard_user", "secret_sauce", "login-button", "shopping_cart_container", "//*[@id='login_button_container']/div/form/div[3]/h3", 3,
       "add-to-cart-sauce-labs-backpack", "shopping_cart_link", "checkout", "first-name", "last-name", "postal-code",
       "Jesus Javier", "Sanchez Guerrero", "82180", "continue", "//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3",
       "finish", "complete-text", 3
    ])]

)
def test_compra(url_page, time_page, selector_name, selector_pwd, username, pwd, selector_login, class_car, xpath_error_login, time_login,
                selector_product, link_cart, checkout, selector_first_name, selector_last_name, selector_zipcode,
                first_name, last_name, zipcode, selector_continue, xpath_error, finish, complete, time_compra):
    demo = Demo(path + r"C:\chromedriver_win32\chromedriver.exe")
    demo.get_page(url_page, time_page)

    # Nos logueamos para probar el realizar una compra
    result = demo.login(selector_name, selector_pwd, username, pwd, selector_login, class_car, xpath_error_login, time_login)
    result = demo.compra(selector_product, link_cart, checkout, selector_first_name, selector_last_name, selector_zipcode,
                         first_name, last_name, zipcode, selector_continue, xpath_error, finish, complete, time_compra)
    assert result == "Compra success"


def test_compra_completa():
    c = Service(r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=c)
    f = funciones(driver)
    f.Navegar("https://www.saucedemo.com/", tg)
    f.Compra_Completa("standard_user", "secret_sauce", tg)