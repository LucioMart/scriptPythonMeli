#!/usr/bin/python
 
 #Script para generar un archivo de LOG
 #Recibe argumentos por linea de comandos.
 #El primer argumento corresponte al site_ID, 
 #y el o los siguientes son del seller_ID. 
 #Puede recibir uno o varios seller_ID al mismo tiempo
 #
 # @version 1.0
 # @author Lucio Martínez <luchoweb15@gmail.com>
 # Python 3.8.1


import requests
import json
import logging
import sys

site_ID='MLA'
seller_ID=str(179571326)

def requestsAPI(site_ID, seller_ID):
    """
    Retorna una lista con los items del seller_ID.

    Recibe como parametro el site_ID y un seller_ID,
    hace la peticion, a la api de Meli, remplazando las variable site_ID y seller_ID, por sus correspondientes
    argumentos recibidos; y retorna por cada iteracion del for 
    una lista con todos los articulos publicados por el 
    vendedor correspondiente a ese id.

    ###
    TO DO: 
    En caso de obtener una respuesta negativa, debe retornar un error
    para luego ser procesado. 

    """
    response = requests.get('https://api.mercadolibre.com/sites/'+site_ID+'/search?seller_id='+seller_ID)
    list_items_JSON = response.json()#se procesa como archivo JSON
    return list_items_JSON["results"]


logging.basicConfig(
    filename='Output_log.log', #nombre del archivo log
    filemode='a',# modo
    level=logging.INFO, #nivel
    format='[%(asctime)s] [%(levelname)s] %(message)s',#formato de salida
    datefmt="%d/%m/%Y %H:%M:%S"#formato de la fecha
)
 
#Creo un anueva lista unicamente con los seller_ID 
#que se ingresa por consola al momento de ejecutar el script
sellers=sys.argv[2:]


for id in sellers:
    #Itero sobre la lista de seller_ID.
    #Por cada elemento de la lista invoco a la funcion requestsAPI()
    #e itero sobre cada elemento de la lista que me retorna dicha funcion
    results=requestsAPI(sys.argv[1], id)
    
    for i in results:
        #Obtengo los items que necesito procesar
        a=i["id"]
        b=i["title"]
        c=i["category_id"]
        #Realizo una nueva peticion a la APIṕara obtener el 'name' 
        #que corresponde a 'category_id'
        #
        #TO DO: IMPORTANTE!!!
        #En este punto el script se torna INEFICIENTE al tener que 
        #hacer una nueva peticion por cada elemento que recibe.
        #Posible solucion:
        #Descargar el arbol de categorias en un solo requests y 
        #procesar la busqueda de 'name' de la categoria.
        #Con eso tendremos una velocidad de procesamiento mucho mayor 
        #comparado con tener que hacer un request por cada articulo.
        #
        response = requests.get('https://api.mercadolibre.com/categories/'+ c)
        name = response.json()["name"]

        #Por ultimo, se reliza la escritura del archivo de LOG
        logging.getLogger().info("\nid: %s \ntitle: %s \ncategory_id: %s \nname: %s \n", a, b, c, name)


print("script finalizado con exito")#se imprime una vez ejecutado correctamente las instrucciones anteriores.
    


