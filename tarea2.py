'''
Autor Jose Daniel Duran Toro
Carnet: 10-10222
'''

from datetime import timedelta, datetime, time
from decimal import Decimal

class tarifa:
 def __init__(self,tarif1,tarif2):
  if(Decimal(tarif1)<0 or Decimal(tarif2)<0):
   raise ValueError("Montos inválidos.")
  self.tarif1=Decimal(tarif1) #tarifa diurna
  self.tarif2=Decimal(tarif2) #tarifa nocturna

def monto(comienza,termina,tarifaIn):
 tiempo = (termina-comienza).total_seconds()
 if(termina<comienza or tiempo<900 or tiempo>259200): #los numeros son 15 mins y 3 dias en segundos respectivamente
  raise ValueError("Fechas inválidas, diferencia inválida.")

 respuesta = Decimal('0')
 t2 = comienza
 delta = timedelta(hours=1)

 while(True):
  cruzado = ((t2.minute + ((tiempo / 60)%60)) >= 60)
  if((t2.hour >= 6 and t2.hour < 17)or(t2.hour == 17 and not cruzado)):
   respuesta+=tarifaIn.tarif1
  elif((t2.hour < 5 or t2.hour >= 18)or(t2.hour == 5 and not cruzado)):
   respuesta+=tarifaIn.tarif2
  else:
   respuesta+=(tarifaIn.tarif1 if tarifaIn.tarif1>=tarifaIn.tarif2 else tarifaIn.tarif2)
  t2+=delta
  if(tiempo<3600):
   return respuesta
  else:
   tiempo-=3600