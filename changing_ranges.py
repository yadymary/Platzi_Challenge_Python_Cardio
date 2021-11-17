''' # **Challenge 5 Datacademy @Platzi**

#**Changing Ranges**

For this final challenge let's play with numbers. In your program, ask the user to enter 3 numbers: a lower limit, an upper limit and a comparison limit.
If your comparison number is in the range of the two limits, print it on screen.
In case of being below the lower or higher than the upper one, also show it on the screen and ask to enter another number to repeat the process.

'''
##Start YMR 05/09/2021

def comparison(number_l_lower,number_l_higher, number_l_comparison):

        if number_l_comparison >= number_l_lower and number_l_comparison <= number_l_lower:
                print ('El número de comparación:' + str(number_l_comparison) + 'ingresado se encuentra en el rango de los límites ingresados')
        else:
                print ('El número de comparación:' + str(number_l_comparison) + ' no se encuentra en el rango de los límites ingresados')
                def options()
def options():
        number_l_lower = float(input('Por favor ingrese el número límite inferior: ' ))
        number_l_higher     = float(input('Por favor ingrese el número límite superior: ' ))
        number_l_comparison = float(input('Por favor ingrese el número límite comparación: '))
        def comparison(number_l_lower,number_l_higher, number_l_comparison)

#Main method    
def main ():
    
    options()
  
if __name__ == '__main__':
    main()

##End   YMR 05/09/2021
