# Modo de utilización del scriptPython
Script para automatizar consultas a la API de MELI.
Genera un archivo de LOG.
Recibe argumentos por linea de comandos.
El primer argumento corresponte al site_ID, y el o los siguientes son del seller_ID. 
Puede recibir uno o varios seller_ID al mismo tiempo

Modo de uso

1. Abrir consola y moverse hasta la carpeta donde se encuentra el proyecto.
2. Para ejecutarlo ingrese por ej: ScriptAPIMELI.py MLA 66146765.
3. Debe ingresar minimo dos parametros correspondientes al site_id y seller_id respectivamente.
	por ej:  ScriptAPIMELI.py  MLA  66146765 132961968 15096445 172753273 54152646.
4. Si lo requiere puede ingresar mas de un seller_id separados por un espacio en blanco.
5. Al finalizar la ejecucion se habra generado un archivo de LOG nuevo si aun no existe, o caso contrario se agregara informacion al archivo existente.
6. Una vez finalizada la ejecucion se muestra por consola un mensaje de finalizacion. 
7. El mismo script, esta documentado para su mejor comprensión, sobre su funcionamiento.