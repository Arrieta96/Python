""" danilo = open('danilo.txt')
print(danilo.read())
 """

""" danilo = open('danilo.txt', 'w')

danilo.write('\nagregaremos una nueva linea a nuestro registro')

danilo.close()

x = open('danilo.txt')

print(x.read()) """

# append = a / sobreescribir 
# write = w / eliminar y escribe

import os

if os.path.exists('danilo.txt'):
    os.remove('danilo.txt')
else:
    print('El archivo no existe')

os.rmdir('micarpeta')