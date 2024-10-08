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

        #Confirnmación de pagina colegium
        assert "Colegium" in driver.title, "Título incorrecto de la página"
        time.sleep(3)

        # Ingresar usuario y contraseña
        driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys("pormero@colegium.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[1]/div[1]/form[1]/div[2]/input[1]").send_keys("Pop23725")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        # Verificar que se haya iniciado sesión correctamente
        assert "Colegio Aleman De La UniÓn" in driver.find_element(By.XPATH, "//div[@class='contenedor']//p[@class='ml-1 mb-0 title']").text, "Colegio Erroneo"

        # Vaerificar nombre de usuario
        assert "Pablo Daniel Ormero" in driver.find_element(By.CSS_SELECTOR, "p[class='mb-0 title").text, "Nombre de usuario incorrecto"

        # Verificar el rol del usuario
        assert "ADMINISTRADOR" in driver.find_element(By.CSS_SELECTOR, "span[class='mb-0 sub-title']").text, "El rol no corresponden al usuario"
        
    except Exception as e:
        # Tomar la captura de pantalla si ocurre un error
        allure.attach(driver.get_screenshot_as_png(), name="screenshot_error", attachment_type=AttachmentType.PNG)
        print(f"Error: {e}")
        raise  # Re-lanzar la excepción para que pytest la maneje
