try:
 num = int('3a')
 print ('no_existe')
except NameError:
 print ('La variable no existe')
except ValueError:
 print ('El valor no es un numero')