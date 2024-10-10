import requests
from bs4 import BeautifulSoup


url = "https://dockerlabs.es/"

#Analizamos la pagina 
respuesta = requests.get(url)

if respuesta.status_code == 200: 
    print("La pagina se ha cargado correctamente")
    #Analizamos el contenido de la pagina
    soup = BeautifulSoup(respuesta.text, 'html.parser')

    #Buscamos los elementos que tengan el atributo onclick
    maquinas = soup.find_all('div', onclick = True)

    # Encontrar el nombre de la maquina
    for maquina in maquinas:
        #Obtenemos el texto del atributo onclick
        onclick_text = maquina['onclick']
        #Obtenemos el nombre de la maquina
        nombre_maquina = onclick_text.split("'")[1]
        #Obtenemos la dificultad de la maquina
        dificultad_maquina = onclick_text.split("'")[3]
        #Obtenemos el autor de la maquina
        autor_maquina = onclick_text.split("'")[7]
        print(f"Nombre: {nombre_maquina}, Dificultad: {dificultad_maquina}, Autor: {autor_maquina}")

else: 
    print(f"Hubo un error con la pagina {respuesta.status_code}")