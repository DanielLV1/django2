import unittest
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time
import sys

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Inicializa el navegador Chrome

    def tearDown(self):
        self.driver.quit()  # Cierra el navegador después de cada prueba

    def test_open_todo_list_admin_page(self):
        self.driver.get("http://localhost:8000/")  # Abre la página de administración de la lista de tareas
        with open('DatosAcceso.csv', newline='', encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile)
            for i, row in enumerate(csvreader):
                try:
                    TitleList_value = row[0] 
                    TitleItem_value = row[1]
                    descItem_value = row[2]
                except IndexError:
                    continue  # Ignorar líneas incorrectas

                action = sys.argv[1]
                if action == "1":
                    self.agregar_lista(TitleList_value)
                elif action == "2":
                    self.agregar_tarea(TitleList_value, descItem_value)
                elif action == "3":
                    self.eliminar_listas()
                elif action == "4":
                    self.eliminar_items()
                elif action == "5":
                    self.ejecutar_todas_las_funciones(TitleList_value, descItem_value)

    def agregar_lista(self, TitleList_value):
        addList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/p/input")))
        addList.click()
        titleList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id_title']")))
        titleList.send_keys(TitleList_value)
        guardar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/form/input[2]")))
        guardar.click()

    def agregar_tarea(self, TitleList_value, descItem_value):
        selectList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/ul/li/div")))
        selectList.click()
        addItem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/p/input[1]")))
        addItem.click()
        titleItem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id_title']")))
        titleItem.send_keys(TitleList_value)
        itemDesc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id_description']")))
        itemDesc.send_keys(descItem_value)
        select_element = self.driver.find_element(By.ID, "id_todo_list")
        select = Select(select_element)
        select.select_by_visible_text(TitleList_value)
        save = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/form/input[2]")))
        save.click()
        time.sleep(3)

    def eliminar_items(self):
        try:
            selectList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/ul/li/div")))
            selectList.click()
            selectItem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/ul/li/div/div")))
            selectItem.click()
            deleteItem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/form/input[4]")))
            deleteItem.click()
            sureButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/form/input[2]")))
            sureButton.click()
        except TimeoutException:
            pass  # No se encontró ningún elemento para eliminar, puede continuar

    def eliminar_listas(self):
        selectList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/ul/li/div")))
        selectList.click()
        deleteList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/p/input[2]")))
        deleteList.click()
        sureList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/form/input[2]")))
        sureList.click()

    def ejecutar_todas_las_funciones(self, TitleList_value, descItem_value):
        self.agregar_lista(TitleList_value)
        self.agregar_tarea(TitleList_value, descItem_value)
        self.eliminar_items()
        self.eliminar_listas()
        

if __name__ == "__main__":
    unittest.main(argv=sys.argv[:1])
