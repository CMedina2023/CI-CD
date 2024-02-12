import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class funciones():
    # Inicializa el parametro instanciado para que pueda utilizar objeto "driver" durante su ciclo de vida
    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Se abrio la pagina : {}" + Url)
        t = time.sleep(Tiempo)
        return t

    def Texto_Mixto(self, tipo, elemento, texto, Tiempo):
        if tipo == "xpath":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, elemento)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.XPATH, value=elemento)
                var.clear()
                var.send_keys(texto)
                print("Escribiendo en el campo {} el texto {} -> ".format(elemento, texto))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + elemento)
        elif tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, elemento)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.ID, value=elemento)
                var.clear()
                var.send_keys(texto)
                print("Escribiendo en el campo {} el texto {} -> ".format(elemento, texto))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + elemento)

    def Click_Mixto(self, tipo, selector, Tiempo):
        if tipo == "xpath":
            try:
                var = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.XPATH, value=selector)
                var.click()
                print("Damos click en el campo {} ".format(selector))
                t =time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
        elif tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.ID, value=selector)
                var.click()
                print("Damos click en el campo {} ".format(selector))
                t =time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)

    def Encontrar_elemento(self, tipo, selector, Tiempo):
        if tipo == "xpath":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.XPATH, value=selector)
                print("Elemento encontrado {}".format(selector))
                t = time.sleep(Tiempo)
                return var
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
        elif tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.ID, value=selector)
                print("Elemento encontrado {}".format(selector))
                return var
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)

    def Compra_Completa(self, User, Pass, Tiempo):
        # Login
        usuario = self.driver.find_element(By.ID, "user-name")
        usuario.send_keys(User)
        contra = self.driver.find_element(By.ID, "password")
        contra.send_keys(Pass)

        boton = self.driver.find_element(By.ID, "login-button")
        boton.click()

        t = time.sleep(Tiempo)

        # Seleccionar Articulo
        try:
            boton = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
            boton.click()
            t = time.sleep(Tiempo)
        except NoSuchElementException:
            print("No se encontro el articulo")

        try:
            boton2 = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")
            boton2.click()
            t = time.sleep(Tiempo)
        except NoSuchElementException:
            print("No se encontro el carrito")

        try:
            boto3 = self.driver.find_element(By.ID, "checkout")
            boto3.click()
            t = time.sleep(Tiempo)
        except NoSuchElementException:
            print("No se encontro el boton de pago")

        print("Termino")
