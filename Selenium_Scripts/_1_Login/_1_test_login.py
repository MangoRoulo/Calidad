
from Funciones.common_imports import *

# Llamados
@pytest.fixture()
def limpiaFallo(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        print("■■■■■***-Limpia fallo-***■■■■■")
        # fconfiguracion.informacionFinancieraInicial()


def setup_function(function):
    # para poder usarla en todos lados. dos variables globales
    global driver, f, vglobales
    path = Service(r"C:/Drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=path)
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    # -----Llamados de Funciones y variables
    f = global_functions(driver)
    vglobales = Funciones.Funciones_Globales
    # -----Navegador
    driver.get(vglobales.produccion)
    driver.maximize_window()
    print("■■■■■-Iniciando Tests-■■■■■")


def teardown_function(function):
    print("■■■■■-Fin de los Tests-■■■■■")
    driver.close()


@pytest.mark.no_ejecutar
@allure.feature("*Flujo completo Financiero*")
@allure.severity(allure.severity_level.NORMAL)
@allure.description(u"""Realiza un flujo completo de cajero.""")
@pytest.mark.flaky(reruns=3, reruns_delay=2)
@pytest.mark.usefixtures("limpiaFallo")
def test_1_0_Flujo_completo_financiero():
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("dguarin@colegium.com")
    driver.implicitly_wait(20)
    driver.find_element(By.NAME, "pass").send_keys("abc123")
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, "//button[text()='Iniciar sesión']").click()
    time.sleep(1)
    driver.implicitly_wait(20)