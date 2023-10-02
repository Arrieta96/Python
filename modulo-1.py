import modulos as xs
from camelcase import CamelCase

print(xs.mascotas)
xs.saludo('Danillo')


c = CamelCase()
s = 'esta oracion necesita CamelCase'

camelcased = c.hump(s)
print(camelcased)


""" print(modulos.mascotas)
modulos.saludo('Danillo Callupe Arrieta') """


