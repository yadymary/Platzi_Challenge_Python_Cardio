''' # **Challenge 4 Datacademy @Platzi**

#**Volumes Calculator**
Let's continue with elementary mathematics so as not to lose the habit and challenge our skills. Write a program where you apply the different mathematical formulas to calculate the volume of a cylinder.
Remember that the base of the cylinder is a circle and you will need to calculate its area. Apply the formulas in your program receiving data like height and radius.
Bonus: add other geometric figures to your program so that the user can choose which one to calculate.

'''
##Start YMR 05/09/2021

#Import Mathematical functions
import math

#Formulas
def cylinder_volume(h, r):
    return round(math.pi * h * r**2, 2)

def cone_volume(h, r):
    return round((1 / 3) * math.pi * r**2 * h, 2)

def sphere_volume(r):
    return round((4/3) * math.pi * r**3, 2)

def cube_volume(a):
    return round(a**3)
    
#Select options figures
def options():
        msg =   """
                Por favor elige la figura para calcular el volumen:
                Cilindro:1
                Cono:2
                Esfera:3
                Cubo:4
               """
        option = input(f'{msg}')
        return option

#Main method
def main ():
        select_option= options()
        
        if select_option == '1':
                h = float(input('Por favor ingrese la altura en cm del cilindro: '))
                r = float(input('Por favor ingrese el radio  en cm del cilindro: '))
                volume = str(cylinder_volume(h, r))
                print ('El volumen del cilindro es: ' + volume + 'cm³')
                       
        elif select_option == '2':
                h = float(input('Por favor ingrese la altura en cm del cono: '))
                r = float(input('Por favor ingrese el radio  en cm del cono: '))
                volume = str(cone_volume(h, r))
                print ('El volumen del cono es: ' + volume + 'cm³')

        elif select_option == '3':
                r = float(input('Por favor ingrese el radio en cm de la esfera: '))
                volume = str(sphere_volume(r))
                print ('El volumen de la esfera es: ' + volume + 'cm³')

        elif select_option == '4': 
                a = float(input('Por favor ingrese la medida del un lado en cm del cubo: '))
                volume = str(cube_volume(a))
                print ('El volumen del cubo es: ' + volume + 'cm³')
        else:
           print('⚠ Por favor ingrese una opción correcta.')            

if __name__ == '__main__':
        main()

##End   YMR 05/09/2021