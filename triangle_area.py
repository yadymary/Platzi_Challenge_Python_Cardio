'''# **Challenge 1 Datacademy @Platzi**

#**Area of a Triangle**
It is time to put that knowledge into practice. The area of a triangle is described as follows: A = (b * h) / 2.
Write a program that takes the base and the height as parameters and calculates the area of the triangle.

** Bonus: the program must determine if the triangle is isosceles, equilateral or scalene. ** 
'''

##Start YMR 05/09/2021

#Cálculo del área del triángulo
def calculo_area (base, altura):
    return round ((base * altura /2), 2)

#Clasificación triángulo
def clasificacion (base, lado_a, lado_b): 
    resultado = ""
    if base == lado_a and lado_a == lado_b:
        resultado = "Equilátero"
    elif base == lado_a or base == lado_b or lado_a == lado_b:
        resultado = "Isósceles"
    else: 
       resultado = "Escaleno"
    return resultado

#Método Principal
def main ():

    #Inputs
    base   = float(input('Por favor digite la longitud de la base del triángulo en cm: '))
    altura = float(input('Por favor digite la longitud de la altura del triángulo en cm: '))
    lado_a = float(input('Por favor digite la longitud del lado A del triángulo en cm: '))
    lado_b = float(input('Por favor digite la longitud del lado B del triángulo en cm: '))

    #Prints
    result_area          = str (calculo_area (base, altura))
    result_clasificacion = str (clasificacion (base, lado_a, lado_b))
    print ( "Tomando como referencia los datos ingresados El área del triángulo es:" + result_area + " cm²" )
    print ( "Tomando como referencia los datos ingresados El triángulo es:" + result_clasificacion)
  
if __name__ == '__main__':
    main()

##End YMR 05/09/2021