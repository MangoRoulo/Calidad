# Paquetes importados
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Inciio de Chrome
# path = Service("C:\Users\steve\OneDrive\Desktop\Python\Drivers\chromedriver-win64\chromedriver.exe")
path = Service(r"C:\Users\steve\OneDrive\Desktop\Python\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=path)
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

# Campos

# Página Web
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

# Acciones

# Cerrar el navegador
driver.quit()   
