from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Demo:

    # Inicializa el parametro instanciado para que pueda utilizar objeto "driver" durante su ciclo de vida
    def __init__(self, path_service):
        self.path_service = path_service
        c = Service(self.path_service)
        self.driver = webdriver.Chrome(service=c)
        self.pathlib = str(pathlib.Path().absolute())

    def get_page(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Se abrio la pagina : {}" + url)
        time.sleep(tiempo)

    def login(self, user_selector, pwd_selector, user_value, pwd_value, login_selector,
              class_car, xpath_error, tiempo):
        try:
            # Buscar elementos para realizar el login
            username = self.driver.find_element(By.ID, user_selector)
            username.send_keys(user_value)
            pwd = self.driver.find_element(By.ID, pwd_selector)
            pwd.send_keys(pwd_value)
            button = self.driver.find_element(By.ID,  login_selector)
            button.click()

            # Validamos si hay error en captura
            if user_value == "" or pwd_value == "":
                # Verificamos si se capturo toda la información
                error = WebDriverWait(self.driver, tiempo).until(ec.visibility_of_element_located((By.XPATH, xpath_error)))
                print(error.text)
                return "Error: No se capturo toda la información, " + error.text

            success = self.driver.find_element(By.CLASS_NAME, class_car)

            # Guardar una screen de prueba del ultimo pasoss
            self.driver.save_screenshot(self.pathlib + r"\login.png")

            if success is None:
                return "Login fallido"
            else:
                return "Login success"
        except Exception as ex:
            print(ex.msg)
            # Guardar una screen de prueba del ultimo pasos
            self.driver.save_screenshot(self.pathlib + r"\login.png")

            # Obtenemos el mensaje de error
            try:
                error = self.driver.find_element(By.XPATH, xpath_error)
                return error.text
            except Exception as err:
                print(err.msg)
                return "Login fallido"

    def logout(self, selector_menu, selector_link, selector_button, tiempo):
        try:
            # Buscar elementos para realizar el logout

            # Buscamos y hacemos click al menu
            menu_logout = self.driver.find_element(By.ID, selector_menu)
            menu_logout.click()

            self.driver.implicitly_wait(tiempo)

            # Buscamos y hacemos click al link para el logout
            link_logout = self.driver.find_element(By.ID, selector_link)
            link_logout.click()

            # Utilizar un Explicit Wait para elementos de forma individual y luego espera a que redireccione al login
            button_login = WebDriverWait(self.driver, tiempo).until(ec.visibility_of_element_located((By.ID, selector_button)))

            # Tomamos una screenshot de evidencia
            self.driver.save_screenshot(self.pathlib + r"\logout.png")

            if button_login is None:
                return "Logout fallido"
            else:
                return "Logout success"

        except Exception as ex:
            print(ex.msg)
            self.driver.save_screenshot(self.pathlib + r"\logout.png")
            return "Logout fallido"

    def compra(self, selector_product, link_cart, checkout, selector_first_name, selector_last_name, selector_zipcode,
               first_name, last_name, zipcode, selector_continue, xpath_error, finish, complete, time_compra):
        try:
            # Buscar elemento para agregar producto al carrito
            product = self.driver.find_element(By.ID, selector_product)
            product.click()

            # Esperamos de forma implicita para que se refresquen los elementos de la pagina
            self.driver.implicitly_wait(time_compra)

            # Buscar elemento para agregar al carrito
            cart = self.driver.find_element(By.CLASS_NAME, link_cart)
            cart.click()

            # Esperamos de forma implicita para que se refresquen los elementos de la pagina
            self.driver.implicitly_wait(time_compra)

            # Buscar elemento checkout para redirigirse a la pagina y capturar su información
            button_checkout = self.driver.find_element(By.ID, checkout)
            button_checkout.click()

            # Esperamos de forma implicita para que se refresquen los elementos de la pagina
            self.driver.implicitly_wait(time_compra)

            # Capturar la información y continuar para terminar el pago
            firstname = self.driver.find_element(By.ID, selector_first_name)
            firstname.send_keys(first_name)
            lastname = self.driver.find_element(By.ID, selector_last_name)
            lastname.send_keys(last_name)
            zip_code = self.driver.find_element(By.ID, selector_zipcode)
            zip_code.send_keys(zipcode)
            button_continue = self.driver.find_element(By.ID, selector_continue)
            button_continue.click()

            # Validamos si hay error en captura
            if first_name == "" or last_name == "" or zipcode == "":
                # Verificamos si se capturo toda la información
                error = WebDriverWait(self.driver, time_compra).until(ec.visibility_of_element_located((By.XPATH, xpath_error)))
                print(error.text)
                return "Error: No se capturo toda la información, " + error.text

            # Terminar la compra
            button_continue = self.driver.find_element(By.ID, finish)
            button_continue.click()

            # Usamos espera explicita para que se refresque el elemento y verificar que se realizo la compra
            complete_text = WebDriverWait(self.driver, time_compra).until(ec.visibility_of_element_located((By.CLASS_NAME, complete)))
            print(print(complete_text.text))

            # Tomamos una screenshot de evidencia
            self.driver.save_screenshot(self.pathlib + r"\compra.png")

            if complete_text.text is None:
                return "Compra fallida"
            else:
                return "Compra success"

        except Exception as ex:
            print(ex.msg)
            # Tomamos una screenshot de evidencia
            self.driver.save_screenshot(self.pathlib + r"\compra.png")
            return "Compra fallida " + ex.msg