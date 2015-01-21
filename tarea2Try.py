'''
Autor Jose Daniel Duran Toro
Carnet: 10-10222
'''

from datetime import timedelta, datetime, time
from decimal import Decimal
from tarea2 import tarifa, monto

print('Ingrese fecha en formato: YYYY MM DD HH mm')
print('Ingrese fecha de inicio:')
s = input()
s = s.split(' ')
t1 = datetime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), 0, 0)
print('Ingrese fecha de final:')
s = input()
s = s.split(' ')
t2 = datetime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), 0, 0)
print('Ingrese un monto para la tarifa diurna:')
s = input()
print('Ingrese un monto para la tarifa nocturna:')
s2 = input()
m = monto(t1,t2,tarifa(s,s2))
print("El monto a pagar es: "+str(m))