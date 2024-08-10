import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from allure_commons.types import AttachmentType
import time

# URL de prueba
url = "https://the-internet.herokuapp.com/login"

@pytest.fixture(scope="function")
def setup_browser():
    # Inicializar el WebDriver
    path = Service("C://Calidad/Drivers/chromedriver.exe")
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=path, options=options)
    # Abrir la URL de prueba y maximizar la ventana
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)  # Espera implícita
    # Proporcionar el driver a las pruebas
    yield driver

    # Cierre del navegador después de cada prueba
    driver.quit()
    print("Fin de los Tests")

def save_screenshot(driver, test_name):
    screenshot_path = f"screenshots/{test_name}.png"
    driver.save_screenshot(screenshot_path)
    return screenshot_path

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Obtener el nombre de la prueba
    test_name = item.name
    # Obtener el driver del fixture
    driver = item.funcargs.get('setup_browser')  
    # Cuando una prueba falla, tomar una captura de pantalla
    if call.excinfo is not None:
        if driver:
            # Tomar la captura de pantalla y adjuntarla al reporte de Allure
            allure.attach(driver.get_screenshot_as_png(), name=f'Screenshot_{test_name}', attachment_type=AttachmentType.PNG)
    
@allure.feature('Login Tests')
def test_login_exito(setup_browser):
    driver = setup_browser
    try:
        # Ingresar usuario y contraseña válidos
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        time.sleep(1)  # Espera para ver el texto ingresado
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        time.sleep(1)  # Espera para ver el texto ingresado
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)  # Espera para que la acción se complete
        # Verificar que el mensaje de bienvenida está presente
        welcome_message = driver.find_element(By.CSS_SELECTOR, "#flash")
        assert "You logged into a secure area!" in welcome_message.text, "El mensaje de bienvenida no se encontró."   
        print("Test de inicio de sesión exitoso completado correctamente.")

    except Exception as e:
        # Tomar la captura de pantalla si ocurre un error
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_error", attachment_type=AttachmentType.PNG)
        print(f"Error: {e}")
        raise  # Re-lanzar la excepción para que pytest la maneje

@allure.feature('Login Tests')
def test_login_fallo(setup_browser):
    driver = setup_browser
    try:
        # Ingresar usuario y contraseña inválidos
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("invaliduser")
        time.sleep(1)  # Espera para ver el texto ingresado
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("invalidpassword")
        time.sleep(1)  # Espera para ver el texto ingresado
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)  # Espera para que la acción se complete
        # Verificar que el mensaje de error está presente
        error_message = driver.find_element(By.CSS_SELECTOR, "#flash")
        assert "Your username is invalid!" in error_message.text, "El mensaje de error no se encontró." 
        print("Test de inicio de sesión fallido completado correctamente.")

    except Exception as e:
        # Tomar la captura de pantalla si ocurre un error
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_error", attachment_type=AttachmentType.PNG)
        print(f"Error: {e}")
        raise  # Re-lanzar la excepción para que pytest la maneje
