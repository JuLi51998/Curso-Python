#VARIABLES

#Variable tipo string
my_variable = "Mi variable de tipo string" 
print(my_variable)

#Variable tipo entero
my_int_variable = 3 
print(my_int_variable)

#Transformacion de tipo de variable
my_int_str_variable = str(my_int_variable) 
print(my_int_str_variable)
print(type(my_int_str_variable))

#Variable de tipo bolean
my_bool_variable = False 
print(my_bool_variable)


#Contatenacion de variables
print(my_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_int_variable)

#Funciones del sistema
print(len(my_variable)) #len() cuenta la cantidad de caracteres

#Variables en una sola linea
name, surname, alias, edad = "Julian", "Gomez", "Juli", 23
print("Me llamo",name, surname, "tengo", edad, "y mi apodo es", alias)

#Inputs
""""
name = input("cual es tu nombre:")
age = input("cual es tu edad?:")
print(name)
print(age)
"""


#Cambiar tipo de dato
name = 123
age = "Ana"
print(name)
print(age)

#Forzar tipo de dato
address: str = "Mi direccion"
address = 32

print(type(address))