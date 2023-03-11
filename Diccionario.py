
Datos = {}
Estado = True
registro = 0

while Estado == True:
    nombre = input(" Ingrese nombre completo ")
    correo = input ("Ingrese su correo  ")
    Datos[nombre] = correo
    Pregunta = input ( " ¿Desea agregar otro usuario? s/n ")
    if Pregunta == "s" or Pregunta == "S":
        pass
    else:
        Estado = False
        for x in Datos:
            registro = registro + 1
            print(str(registro)+ x + " su correo es " + Datos[x])
           
           
            
            
            

        



