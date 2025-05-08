#Codigo para una calculadora utilizando el framework Kivy

#imports
from cProfile import label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


#variables globales
numeros=['0','1','2','3','4','5','6','7','8','9']
operadores = ['+','-','*','/']
listaoperadores = []

#Funciones
def suma(resultado, num1:int, num2:int):
    resultado = num1 + num2
    return resultado

def resta(resultado,num1:int, num2:int):
    resultado = num1 - num2
    return resultado
def multiplicacion(resultado,num1:int, num2:int):
    resultado =  num1 * num2
    return resultado

def division(resultado,num1:int, num2:int):
    resultado = num1 / num2
    return resultado

#Funcion que obtiene lo ingresado por el usuario y lo divide en lista de operadores y numeros
def obtenerlista(entrada:str):
    listaoperadores = []
    listanumeros = []
    numero_actual = ''
    
    for i in range (len(entrada)):
        if entrada[i] in operadores:
            listanumeros.append(numero_actual)
            numero_actual = ''
            listaoperadores.append(entrada[i])
        elif entrada[i] in numeros:
            numero_actual += entrada[i]
    if numero_actual != '':
        listanumeros.append(numero_actual)
        
    return listanumeros, listaoperadores

#Funcion que obtiene el resultado de la operacion estilo calculadora
def obtenerresultado(listanumeros,listaoperadores):
    resultado=0
    i=0
    while i < len(listaoperadores):
        if listaoperadores[i] == '*':
            resultado= multiplicacion(resultado,int(listanumeros[i]),int(listanumeros[i+1]))
            listanumeros[i+1] = resultado
            listanumeros.pop(i)
            listaoperadores.pop(i)
        elif listaoperadores[i] == '/':
            resultado= division(resultado,int(listanumeros[i]),int(listanumeros[i+1]))
            listanumeros[i+1] = resultado
            listanumeros.pop(i)
            listaoperadores.pop(i)
        else:
            i += 1
    i=0
    while i < len(listaoperadores):
        if listaoperadores[i] == '+':
            resultado= suma(resultado,int(listanumeros[i]),int(listanumeros[i+1]))
            listanumeros[i+1] = resultado
            listanumeros.pop(i)
            listaoperadores.pop(i)
        elif listaoperadores[i] == '-':
            resultado= resta(resultado,int(listanumeros[i]),int(listanumeros[i+1]))
            listanumeros[i+1] = resultado
            listanumeros.pop(i)
            listaoperadores.pop(i)
        else:
            i += 1
    return listanumeros[0]

#definicion de la interfaz grafica
class grid(GridLayout):
     def __init__(self, **kwargs):
        super(grid, self).__init__(**kwargs)
        self.entrada = ""
        
     def clearresultado(self):
         self.entrada = ""
         self.ids.resultado_label.text = ""

     def agregarEntrada(self,texto):
        self.entrada += texto
        self.ids.resultado_label.text = f"{self.entrada}"  # Actualiza el texto del Label
        return self.entrada
     
     def llamarresultado(self):
        listanumeros, listaoperadores = obtenerlista(self.entrada)
        resultado = obtenerresultado(listanumeros, listaoperadores)
        self.ids.resultado_label.text = f"{resultado}"
        self.entrada = ""  # Limpiar la entrada después del resultado
        return resultado

class Calculadora(App):
    def build(self):
        return grid()

if __name__ == '__main__':
    Calculadora().run()
