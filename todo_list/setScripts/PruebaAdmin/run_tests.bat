@echo off
:menu
REM Menú de opciones
echo Seleccione una opción:
echo 1. Agregar listas
echo 2. Agregar tareas
echo 3. Eliminar listas
echo 4. Eliminar tareas
echo 5. Salir

REM Leer la opción seleccionada por el usuario
set /p option=Ingrese el número de la opción deseada:

REM Ejecutar el script de Python con la opción seleccionada
python ScriptPrueba.py %option%

REM Preguntar al usuario si desea continuar o salir
echo ¿Desea realizar otra operación? (s/n)
set /p continuar=
if /i "%continuar%"=="s" goto menu
