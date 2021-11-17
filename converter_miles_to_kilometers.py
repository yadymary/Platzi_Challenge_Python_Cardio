''' # **Challenge 3 Datacademy @Platzi**

#**Converter from miles to kilometers**
Suppose you want to calculate the kilometers that are a certain number of miles. 
To avoid repeating this calculation, write a program in which the user indicates a number of miles and the screen displays the result converted to kilometers.
Take into account that in each mile there are 1.609344 Km

Bonus: Make the user can choose between converting miles to kilometers or kilometers to miles. **
'''
##Start YMR 05/09/2021

#Variables

#Determine Options Screen
def options():
        msg =   """
                Por favor elige la opción:
                Convertir Millas a KMs:1
                Convertir KMs a Millas:2
                """
        option = input(f'{msg}')
        cant = input('Por favor ingresa la cantidad a convertir:')
        return option, cant

#Main method
def main ():
        result= options()
        option_1= str(result[0])
        cantidad = float(result[1])
        if option_1 == '1':
            miles = str(cantidad*1.6093) 
            print("La cantidad de millas son:" + miles)           
        elif option_1 == '2':
            kms = str(cantidad/1.6093)
            print("La cantidad de KMs son:" + kms)      
        else:
            print ("Error en la selección")            

if __name__ == '__main__':
        main()

##End   YMR 05/09/2021