from django.shortcuts import render
import random
from django.http import JsonResponse
from django.http import HttpResponse
import json

import serial, time

 
#arduino = serial.Serial('COM3', 9600)
arduino = "hola"
# Abre la conexión con el Arduino (ajusta el puerto COM o /dev/ttyUSB0)


# Create your views here.
def hola(request):

    #print("enviando datos a arduino")
    return render(request, "index.html")  # vuelve a la página principal


    

def hola_mesa(request):

    #arduino = serial.Serial('COM4', 9600)  # en Linux: '/dev/ttyUSB0'
    #time.sleep(1)
    #arduino.write(b'salir')  # Enviar al Arduino
    return render(request, "menu_principal.html")

def mover_mesa(request):
    #return render(request, "mover_mesa.html")
    if request.method == 'POST':
        accion = request.POST.get('accion')  # "ON" o "OFF"
        if accion:
            #arduino = serial.Serial('COM4', 9600)  # en Linux: '/dev/ttyUSB0'
            #time.sleep(1)
            #arduino.write(accion.encode())  # Enviar al Arduino
            #print("enviando datos a arduino")
            return render(request, 'mover_mesa.html')  # vuelve a la página principal
    else:
        #return HttpResponse("Método no permitido", status=405)
        #arduino = serial.Serial('COM4', 9600)  # en Linux: '/dev/ttyUSB0'
        #time.sleep(1)
        #arduino.write(b'mover_mesa')  # Enviar al Arduino
        return render(request, "mover_mesa.html")

def reproducir_sismo(request):
    #return render(request, "reproducir_sismo.html")

    if request.method == 'POST':
        accion = request.POST.get('accion')  # "ON" o "OFF"
        if accion:
            #arduino = serial.Serial('COM4', 9600)  # en Linux: '/dev/ttyUSB0'
            #time.sleep(1)
            arduino.write(accion.encode())  # Enviar al Arduino
            #print("enviando datos a arduino")
        return render(request, 'reproducir_sismo.html')  # vuelve a la página principal
    else:
        #return HttpResponse("Método no permitido", status=405)
        #arduino = serial.Serial('COM4', 9600)  # en Linux: '/dev/ttyUSB0'
        #time.sleep(1)
        arduino.write(b'reproducir_sismo')  # Enviar al Arduino
        return render(request, "reproducir_sismo.html")

def crear_sismo(request):
    #return render(request, "crear_sismo.html")
    if request.method == 'POST':
        accion = request.POST.get('accion')  # "ON" o "OFF"
        if accion:
            #arduino = serial.Serial('COM4', 9600)  # en Linux: '/dev/ttyUSB0'
            #time.sleep(1)
            arduino.write(accion.encode())  # Enviar al Arduino
            #print("enviando datos a arduino")
        return render(request, 'crear_sismo.html')  # vuelve a la página principal
    else:
        #return HttpResponse("Método no permitido", status=405)
          # en Linux: '/dev/ttyUSB0'
        #time.sleep(1)
        arduino.write(b'crear_sismo')  # Enviar al Arduino
        return render(request, "crear_sismo.html")


def documentacion(request):
    return render(request, "documentacion.html")



'''
def obtener_info(request):
    if arduino.in_waiting > 0:
        linea = arduino.readline().decode().strip()  # Lee la línea completa
        try:
            datos = json.loads(linea)  # Convierte de JSON a diccionario
        except json.JSONDecodeError:
            datos = {"error": "Formato JSON inválido", "raw": linea}
    else:
        datos = {"distancia_ejex": 0, "aceleracion_ejex": 0, "aceleracion_ejey": 0, "aceleracion_ejez": 0}

    return JsonResponse(datos)
'''

def obtener_info(request):
    if request.method == "POST":
        valor = request.POST.get('valor')
        #valor_slider = str(data.get("valor"))  # Valor del input range
        print("valor recibido", valor)
        # Enviar el valor al Arduino

        arduino.write((valor + "\n").encode())
            
    
        # Esperar la respuesta
        time.sleep(0.1)
        
        if arduino.in_waiting > 0:
            print("------------------------------------------")
            
            linea = arduino.readline().decode().strip()  # Lee la línea completa
            try:
                datos = json.loads(linea)  # Convierte de JSON a diccionario
                
            except json.JSONDecodeError:
                datos = {"error": "Formato JSON inválido", "raw": linea}
                
        else:
            datos = {"distancia_ejex": 0, "aceleracion_ejex": 0, "aceleracion_ejey": 0, "aceleracion_ejez": 0}

    return JsonResponse(datos)

    #return JsonResponse(datos)

def dato_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            valor = data.get('valor')

            if valor is None:
                return JsonResponse({'error': 'No se recibió ningún valor'}, status=400)

            # Enviar dato al Arduino
            arduino.write(f"{valor}\n".encode())

            # Esperar breve tiempo a que Arduino responda
            #time.sleep(0.01)

            while arduino.in_waiting > 0:
                respuesta_arduino = arduino.readline().decode('utf-8').strip()
            '''
            # Leer respuesta del Arduino
            if arduino.in_waiting > 0:
                respuesta_arduino = arduino.readline().decode('utf-8').strip()
            else:
                respuesta_arduino = "No hubo respuesta del Arduino"
            '''
            return JsonResponse({
                'status': 'OK',
                'valor_enviado': valor,
                'respuesta_arduino': respuesta_arduino
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)