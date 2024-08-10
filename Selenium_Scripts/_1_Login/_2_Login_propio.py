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
Email = "/html[1]/body[1]/section[1]/div[2]/div[1]/div[1]/form[1]/div[1]/input[1]"
Password = "/html[1]/body[1]/section[1]/div[2]/div[1]/div[1]/form[1]/div[2]/input[1]"
Login = "/html[1]/body[1]/section[1]/div[2]/div[1]/div[1]/form[1]/button[1]"


# Página Web
driver.get("https://beta_inf.colegium.cloud")
driver.maximize_window()
time.sleep(2)

# Acciones
print("■■■■■-Empezar Inicio de Sesión-■■■■■")
driver.find_element(By.XPATH, Email).send_keys("pormero@colegium.com")
time.sleep(2)   
driver.find_element(By.XPATH, Password).send_keys("Pop23725")
time.sleep(2)   
driver.find_element(By.XPATH, Login).click()
time.sleep(2) 
print("■■■■■-Finalizar Inicio de Sesión-■■■■■")


# Cerrar el navegador
driver.quit()   
