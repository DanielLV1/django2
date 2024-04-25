Pasos para iniciar aplicacion django y pruebas automatizadas


1. Instalar Python (ultima version) 3.12.3 https://www.python.org/downloads/release/python-3123/
2. Instalar GIT https://git-scm.com/download/win
3. Instalar visual studio code
4. Ingresar a visual studio code, clonar repositorio por medio del siguiente link https://github.com/DanielLV1/django2.git
5. ingresar a cmd e ir a la ruta del repositorio ej: C:\django2\todo_list
7. Configurar entorno virtual usando el comando python -m venv venv
6. Iniciar el entorno virtual con el siguiente comando venv\Scripts\activate.bat
7. Instalar django con el siguiente comando python -m pip install django=="3.2.9"
8. Instalar selenium con el siguiente comando python -m pip install selenium
9. iniciar servidor con el siguiente comando python manage.py runserver
10. Instalar google chrome (No importa la version)
11. Para ingresar a la app usar el siguiente enlace http://localhost:8000/
12. Para ingresar a la plataforma admin usar el siguiente enlace: http://127.0.0.1:8000/admin/   Credenciales:
user: kronner pass: Nicolas321

Instrucciones pruebas automatizadas

PruebasAdmin
Aqui se prueba la plataforma administrativa para verificar que elimina, agrega y modifica las tareas y listas

1. Ingresar a la carpeta setScripts ingresar a PruebaAdmin
2. Abrir el archivo run_tests
3. Digitar el modulo o accion a probar: 
IMPORTANTE: si se desea utilizar eliminar listas o tareas, antes usar agregar listas, agregar tareas,
en caso de no existir el script saldra Ok sin realizar una opcion

El archivo DatosAcceso funciona de manera que se pueden modificar los datos a ingresar sin ingresar al codigo. 

el orden de las filas es el siguiente: usuario, contraseña, titulo de lista, titulo de tarea, descripcion de tarea

No modificar las credenciales de usuario y contraseña

PruebasApp

Aqui se prueba la aplicacion, para verificar que elimina, agrega y modifica las tareas y listas

1. Ingresar a la carpeta setScripts ingresar a PruebaApp
2. Abrir el archivo run_tests
3. Digitar el modulo o accion a probar: 
IMPORTANTE: si se desea utilizar eliminar listas o tareas, antes usar agregar listas, agregar tareas,
en caso de no existir el script saldra Ok sin realizar una opcion

El archivo DatosAcceso funciona de manera que se pueden modificar los datos a ingresar sin ingresar al codigo. 

el orden de las filas es el siguiente: titulo de lista, titulo de tarea, descripcion de tarea

En este archivo run se puede probar la aplicacion completamente para asi aprobar su prueba de aceptacion. 

