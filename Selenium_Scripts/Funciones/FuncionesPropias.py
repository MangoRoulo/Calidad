from select import select
import pytest
import time
import json
from datetime import datetime
import datetime
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
# from datetime import datetime


# Url
produccion = "https://app.colegium.cloud/"

usuario = "pormero@colegium.com"
clave = "Pop23725"

class FuncionesPropias():
    def __init__(self, driver):
        self.driver = driver

# Funciones

    # *************************************************Funciones Recurrentes*************************************************
    def inicioSesion(self, usuario=usuario, clave=clave):
        print("■■■■■-Inicio inicio sesion-■■■■■")
        self.driver.implicitly_wait(20)

        # Campos
        Email = "//input[@placeholder='ejemplo@colegium.com']"
        Contraseña = "//input[@placeholder='······']"
        BotonLogin = "//button[normalize-space()='Iniciar sesión']"
        NombreColegio = "//div[@class='contenedor']//p[@class='ml-1 mb-0 title'][normalize-space()='colegio aleman de la uniÓn']"
        NombreUsuario = "//a[@id='avatar']"
        NombreRolAdmin = "//span[@class='mb-0 sub-title']"


        self.driver.find_element(By.XPATH, Email).send_keys(str(usuario))
        time.sleep(1)   
        self.driver.find_element(By.NAME, Contraseña).send_keys(clave)
        time.sleep(1)
        self.driver.find_element(By.XPATH, BotonLogin).click()
        time.sleep(1)
       
        # Verificar que se haya iniciado sesión correctamente
        assert "Colegio Aleman De La UniÓn" in self.driver.find_element(By.XPATH, NombreColegio).text, "Colegio Erroneo"

        # Vaerificar nombre de usuario
        assert "Pablo Daniel Ormero" in self.driver.find_element(By.CSS_SELECTOR, NombreUsuario).text, "Nombre de usuario incorrecto"

        # Verificar el rol del usuario
        assert "ADMINISTRADOR" in self.driver.find_element(By.CSS_SELECTOR, NombreRolAdmin).text, "El rol no corresponden al usuario"

        
        print("■■■■■-Fin inicio sesion-■■■■■")
        time.sleep(2)

    def cerrarSesion(self):

        print("■■■■■-Inicio cerrar sesion-■■■■■")
        time.sleep(2)

        # Campos
        SimboloMenu = "//i[@class='clg clg-select-abajo']"
        CerrarSesion = "//button[normalize-space()='Cerrar Sesión']"

        # Inicio Cierre de Sesión
        # Click sobre el menu de usuario
        self.driver.find_element(By.XPATH, SimboloMenu).click()
        time.sleep(1)
        # Click en cierra de sesións
        self.driver.find_element(By.XPATH, CerrarSesion).click()
        time.sleep(3)
        # Fin Cierre de Sesión
        print("■■■■■-Fin cerrar sesion-■■■■■")
        time.sleep(2)
