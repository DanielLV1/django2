import unittest
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
import time
import sys

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Inicializa el navegador Chrome

    def tearDown(self):
        self.driver.quit()  # Cierra el navegador después de cada prueba

    def test_open_todo_list_admin_page(self):
        self.driver.get("http://127.0.0.1:8000/admin/")  # Abre la página de administración de la lista de tareas
        with open('DatosAcceso.csv', newline='', encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile)
            for i, row in enumerate(csvreader):
                try:
                    UserName = row[0]
                    Password = row[1] 
                    TitleList_value = row[2] 
                    TitleItem_value = row[3]
                    descItem_value = row[4]
                except IndexError:
                    continue  # Ignorar líneas incorrectas

                usuario=self.driver.find_element(By.XPATH, "//*[@id='id_username']")
                usuario.send_keys(UserName)
                password=self.driver.find_element(By.XPATH, "//*[@id='id_password']")
                password.send_keys(Password)
                logIn = self.driver.find_element(By.XPATH, "//*[@id='login-form']/div[3]/input")
                logIn.click()

                action = sys.argv[1]
                if action == "1":
                    self.agregar_lista(TitleList_value)
                elif action == "2":
                    self.agregar_tarea(TitleList_value, descItem_value)
                elif action == "3":
                    self.eliminar_listas()
                elif action == "4":
                    self.eliminar_items()

    def agregar_lista(self, TitleList_value):
        addList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content-main']/div[2]/table/tbody/tr[2]/td[1]/a")))
        addList.click()
        titleList = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id_title']")))
        titleList.send_keys(TitleList_value)
        guardar = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='todolist_form']/div/div/input[1]")))
        guardar.click()

    def agregar_tarea(self, TitleList_value, descItem_value):
        addItem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content-main']/div[2]/table/tbody/tr[1]/td[1]/a")))
        addItem.click()
        titleItem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id_title']")))
        titleItem.send_keys(TitleList_value)
        itemDesc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='id_description']")))
        itemDesc.send_keys(descItem_value)
        select_element = self.driver.find_element(By.ID, "id_todo_list")
        select = Select(select_element)
        select.select_by_visible_text(TitleList_value)
        save = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='todoitem_form']/div/div/input[1]")))
        save.click()
        time.sleep(3)

    def eliminar_items(self):
        self.driver.get("http://127.0.0.1:8000/admin/todo_app/todoitem/")
        element_found = False
        for i in range(1, 50):
            checkbox_value = str(i)  # Convertir el número a cadena

            # Intenta encontrar el elemento checkbox con el valor actual
            try:
                checkbox = self.driver.find_element(By.CSS_SELECTOR, f"input[type='checkbox'][value='{checkbox_value}']")
                # Si se encuentra el elemento, haz algo aquí, por ejemplo:
                selectAll = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='action-toggle']")))
                selectAll.click()
                actionSelect = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='changelist-form']/div[1]/label/select")))
                select = Select(actionSelect)
                select.select_by_value("delete_selected")
                goButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='changelist-form']/div[1]/button")))
                goButton.click()
                sureButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit' and @value='Yes, I’m sure']")))
                sureButton.click()

                time.sleep(3)
                print(f"Checkbox con el valor {checkbox_value} encontrado y marcado.")
                element_found = True
                # Puedes agregar más acciones aquí si es necesario
                break  # Sal del bucle después de encontrar el elemento
            except:
                print(f"No se encontró el checkbox con el valor {checkbox_value}.")

        # Si no se encontró ningún checkbox, imprime que no hay listas
        if not element_found:
            print("No se encontraron checkboxes en el rango del 1 al 10.")

    def eliminar_listas(self):
        self.driver.get("http://127.0.0.1:8000/admin/todo_app/todolist/")
        
        toDolist = self.driver.find_element(By.XPATH, "//*[@id='nav-sidebar']/div[2]/table/tbody/tr[2]/th/a")
        toDolist.click()

        for i in range(1, 50):
            checkbox_value = str(i)  # Convertir el número a cadena

            # Intenta encontrar el elemento checkbox con el valor actual
            try:
                checkbox = self.driver.find_element(By.CSS_SELECTOR, f"input[type='checkbox'][value='{checkbox_value}']")
                # Si se encuentra el elemento, haz algo aquí, por ejemplo:
                selectAll = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='action-toggle']")))
                selectAll.click()
                actionSelect = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='changelist-form']/div[1]/label/select")))
                select = Select(actionSelect)
                select.select_by_value("delete_selected")
                goButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='changelist-form']/div[1]/button")))
                goButton.click()
                sureButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit' and @value='Yes, I’m sure']")))
                sureButton.click()

                time.sleep(3)
                print(f"Checkbox con el valor {checkbox_value} encontrado y marcado.")
                element_found = True
                # Puedes agregar más acciones aquí si es necesario
                break  # Sal del bucle después de encontrar el elemento
            except:
                print(f"No se encontró el checkbox con el valor {checkbox_value}.")

        # Si no se encontró ningún checkbox, imprime que no hay listas
        if not element_found:
            print("No se encontraron checkboxes en el rango del 1 al 10.")


if __name__ == "__main__":
    unittest.main(argv=sys.argv[:1])
    