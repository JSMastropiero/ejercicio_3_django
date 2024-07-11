# Generador de Matrices

Esta aplicación genera matrices de números enteros aleatorios, los ordena y los espeja. 

Utiliza python y django como framework.

## Requisitos

- Docker
- Docker Compose

## Instalación

# Clonar el repositorio

Para clonar el repositorio, ejecuta el siguiente comando:

```bash
git clone https://github.com/JSMastropiero/ejercicio_3_django.git

cd ejercicio_3_django/ejercicio_3




docker-compose build
docker-compose up

Para revisar las matrices generadas y guardadas en la base de datos se puede hacer mediante el panel de administracióin de django.

Abrir una nueva terminal en la carpeta raiz del proyecto ejecutar el comando de docker: 

docker-compose exec web python app/manage.py createsuperuser

Seguir las instrucciones de la terminal y una vez creado ingresar al admin.

localhost:8000/admin

---------------------------------------------------------------------

## código original sin ser implementado en django ni conectado a la base de datos.

import random

def generar_matriz(filas, columnas):
    """
    Genera una matriz de números enteros aleatorios entre 1 y 1000.
    """
    # Verificar que las filas y columnas sean mayores a 0
    if filas <= 0 or columnas <= 0:
        print("El número de filas y columnas debe ser un entero positivo.")
        return None

    # Crear la matriz con números aleatorios entre 1 y 1000
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            numero_aleatorio = random.randint(1, 1000)
            fila.append(numero_aleatorio)
        matriz.append(fila)
    
    return matriz



def ordenar_matriz(matriz):
    """
    Ordena una matriz transformándola en una lista plana, ordenando la lista,
    y reconstruyendo la matriz ordenada.
    """
    filas = len(matriz)  # Obtiene la cantidad de filas de la matriz
    columnas = len(matriz[0]) if filas > 0 else 0  # Obtiene la cantidad de columnas de la matriz

    # Convertir la matriz en una lista plana
    lista_plana = []
    for sublist in matriz:
        for item in sublist:
            lista_plana.append(item)

    # Ordenar la lista plana
    lista_ordenada = ordenar_lista(lista_plana)

    # Reconstruir la matriz ordenada a partir de la lista plana ordenada
    matriz_ordenada = []
    for i in range(0, len(lista_ordenada), columnas):
        fila = []
        for j in range(columnas):
            fila.append(lista_ordenada[i + j])
        matriz_ordenada.append(fila)
    
    return matriz_ordenada

def espejar_matriz(matriz):
    """
    Espeja una matriz, invirtiendo las filas y las columnas.
    """
    filas = len(matriz)  # Obtiene la cantidad de filas de la matriz
    columnas = len(matriz[0]) if filas > 0 else 0  # Obtiene la cantidad de columnas de la matriz

    # Espejar la matriz (invertir filas y columnas)
    matriz_espejo = []
    for fila in matriz[::-1]:  # Invierte el orden de las filas
        nueva_fila = []
        for item in fila[::-1]:  # Invierte el orden de los elementos dentro de cada fila
            nueva_fila.append(item)
        matriz_espejo.append(nueva_fila)

    return matriz_espejo
  
def ordenar_lista(lista):
    """
    Ordena los números enteros de la lista plana.
    """
    n = len(lista)  # Obtiene la longitud de la lista
    # Bucle externo: controla la cantidad de pasadas necesarias
    for i in range(n):
        # Bucle interno: recorre la lista desde el principio hasta n-i-1
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente, los intercambia
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Ejemplo de uso
filas, columnas = 5, 3

# Generar matriz
matriz_original = generar_matriz(filas, columnas)
if matriz_original:
    print("Matriz Original:")
    # Imprime la matriz en formato de fila.
    for fila in matriz_original:
        print(fila)

    # Ordenar matriz
    matriz_ordenada = ordenar_matriz(matriz_original)
    print("\nMatriz Ordenada:")
    for fila in matriz_ordenada:
        print(fila)

    # Espejar matriz
    matriz_espejada = espejar_matriz(matriz_ordenada)
    print("\nMatriz Espejada:")
    for fila in matriz_espejada:
        print(fila)
