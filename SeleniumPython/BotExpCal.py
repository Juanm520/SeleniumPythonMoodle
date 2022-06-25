# -*- coding: utf-8 -*-
# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os

#Inicio del Navegador
start = webdriver.ChromeOptions()
start.add_argument('--start-maximized')
driver_path = 'C:/Users/JuanM/Desktop/codex/chromedriver102.exe'
driver = webdriver.Chrome(driver_path, chrome_options=start) 

#Inicio de Sesion en Moodle
    #Credenciales e ID del curso
User = "Juanm520@admin.com"
Pass = "Metal-Yo.!0481"
CursosID = [27]
Bimestre = "2"
Componentes = [
    "Total Cognitivo Bimestre ",
    "Total Procedimental Bimestre ",
    "Total Axiológico Bimestre ",
    "Total Actitudinal Bimestre ",
    "Total Comunicativo Bimestre "]

    #Script login y administración
driver.get("https://formarinnovar.com/moodle")

WaitPageLogin = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "password")))

input_User = driver.find_element_by_id('username')
input_Pass = driver.find_element_by_id('password')
input_User.send_keys(User)
input_Pass.send_keys(Pass)
SubmitB = driver.find_element_by_id("loginbtn")
SubmitB.click()

    #Entrar a la interfaz de exportar calificaciones del Curso.
def CursoCatTree(CursoId):
 driver.get("https://formarinnovar.com/moodle/grade/export/xls/index.php?id=" + str(CursoID))
 WebDriverWait(driver, 10)
    
def SelCategorias():
    #Deseleccionar categorias
 WebDriverWait(driver, 10)
 DeselectCats = driver.find_element_by_link_text("Seleccionar todos/ninguno")
 DeselectCats.click()
#  SelectCats = driver.find_elements_by_class_name("form-group.row..fitem.checkboxgroup1")
 driver.execute_script("window.scrollTo({ top: 0});")
 #Crea arreglo de los elementos de la clase.
 SelectCatsClass = driver.find_elements_by_class_name("form-check.d-flex")
 #filtra elementos que deseamos
 for Componente in Componentes:
    for i in range (0, len(SelectCatsClass)):
        if SelectCatsClass[i].find_element_by_tag_name('label').text == Componente + Bimestre:
            SelectCatsClass[i].find_element_by_tag_name('label').click()
            break
        


    #Seleccionar categorias correspondientes als bimestre

# for Componente in range(0,len(checkBoxsCatBim)):
#     selectCats = driver.find_element_by_link_text("Seleccionar todos/ninguno")
#  driver.find_element_by_id("menumoveafter").click()
#  Select(driver.find_element_by_id("menumoveafter")).select_by_visible_text("No calificables")
#  WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,"btn.btn-primary"))).click()

 
for CursoID in CursosID:
 CursoCatTree(CursoID)
 SelCategorias()
#  Categoria()
#  VisualCategoria()
#  print(CursoID)
# print("Lista terminada")
# driver.close()


