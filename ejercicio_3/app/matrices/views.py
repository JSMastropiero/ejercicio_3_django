# Create your views here.

import random
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Matriz


def generar_matriz(request):
    if request.method == 'POST':
        try:
            filas = int(request.POST.get('filas'))
            columnas = int(request.POST.get('columnas'))
            if filas <= 0 or columnas <= 0:
                return HttpResponse("El número de filas y columnas debe ser un entero positivo.", status=400)
        except ValueError:
            return HttpResponse("El número de filas y columnas debe ser un entero positivo.", status=400)

        matriz = [[random.randint(1, 1000) for _ in range(columnas)] for _ in range(filas)]
        matriz_json = json.dumps(matriz)
        matriz_instancia = Matriz.objects.create(filas=filas, columnas=columnas, matriz_original=matriz_json)
        return redirect('ver_matriz', matriz_id=matriz_instancia.id)
    return render(request, 'matrices/generar_matriz.html')

def ver_matriz(request, matriz_id):
    matriz_instancia = Matriz.objects.get(id=matriz_id)
    matriz = json.loads(matriz_instancia.matriz_original)
    context = {
        'matriz': matriz,
        'matriz_id': matriz_id
    }
    return render(request, 'matrices/ver_matriz.html', context)

def ordenar_matriz(request, matriz_id):
    matriz_instancia = Matriz.objects.get(id=matriz_id)
    matriz = json.loads(matriz_instancia.matriz_original)
    lista_plana = [item for sublist in matriz for item in sublist]
    lista_ordenada = ordenar_lista(lista_plana)
    matriz_ordenada = [lista_ordenada[i:i + matriz_instancia.columnas] for i in range(0, len(lista_ordenada), matriz_instancia.columnas)]
    context = {
        'matriz': matriz_ordenada,
        'matriz_id': matriz_id
    }
    return render(request, 'matrices/matriz_ordenada.html', context)

def espejar_matriz(request, matriz_id):
    matriz_instancia = Matriz.objects.get(id=matriz_id)
    matriz = json.loads(matriz_instancia.matriz_original)
    lista_plana = [item for sublist in matriz for item in sublist]
    lista_ordenada = ordenar_lista(lista_plana)
    matriz_ordenada = [lista_ordenada[i:i + matriz_instancia.columnas] for i in range(0, len(lista_ordenada), matriz_instancia.columnas)]
    matriz_espejo = matriz_ordenada[::-1]
    matriz_espejo = [fila[::-1] for fila in matriz_espejo]
    matriz_final_json = json.dumps(matriz_espejo)
    matriz_instancia.matriz_final = matriz_final_json
    matriz_instancia.save()
    context = {
        'matriz': matriz_espejo,
        'matriz_id': matriz_id
    }
    return render(request, 'matrices/matriz_final.html', context)

def ordenar_lista(lista):
    # Implementación del algoritmo de ordenamiento 
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def listar_matrices(request):
    matrices = Matriz.objects.all().order_by('creado_el')
    context = {
        'matrices': matrices
    }
    return render(request, 'matrices/listar_matrices.html', context)
