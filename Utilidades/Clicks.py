import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana del navegador)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_double_click(driver):
    driver.get("https://demoqa.com/buttons")

    # Localizar el botón para double click
    double_click_button = driver.find_element(By.ID, "doubleClickBtn")

    # Realizar double click en el botón
    action_chains = ActionChains(driver)
    action_chains.double_click(double_click_button).perform()

    # Verificar el mensaje de éxito después del double click
    success_message = driver.find_element(By.ID, "doubleClickMessage")
    assert success_message.text == "You have done a double click"
    driver.save_screenshot(r'C:\Users\Lenovo\Desktop\Evidencia\Prueba1.png')


def test_right_click_me(driver):
    driver.get("https://demoqa.com/buttons")

    # Localizar el botón "Right click me"
    right_click_me_button = driver.find_element(By.ID, "rightClickBtn")

    # Realizar clic derecho en el botón
    action_chains = ActionChains(driver)
    action_chains.context_click(right_click_me_button).perform()

    # Verificar el mensaje de éxito después del clic derecho
    success_message = driver.find_element(By.ID, "rightClickMessage")
    assert success_message.text == "You have done a right click"
    driver.save_screenshot(r'C:\Users\Lenovo\Desktop\Evidencia\Prueba3.png')