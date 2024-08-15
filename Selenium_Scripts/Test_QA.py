import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from allure_commons.types import AttachmentType
import time
from _1_Login._2_Login_propio import login_propio

# URL de prueba
url = "https://app.colegium.cloud/"

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
def test_login_propio(setup_browser):
    driver = setup_browser
    
    try:

        login_propio.test_login_propio(driver)
        
    except Exception as e:
        # Tomar la captura de pantalla si ocurre un error
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_error", attachment_type=AttachmentType.PNG)
        print(f"Error: {e}")
        raise  # Re-lanzar la excepción para que pytest la maneje
