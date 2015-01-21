import unittest
from datetime import timedelta, datetime, time
from decimal import Decimal
from tarea2 import tarifa, monto

class TestSequenceFunctions(unittest.TestCase):

 def test_tarifaConstruction(self):
  t = tarifa('0','0')
  self.assertEqual(t.tarif1,Decimal('0'))
  self.assertEqual(t.tarif2,Decimal('0'))

 def test_tarifaConstruction2(self):
  t = tarifa('0.51951281652','0.5619165198235')
  self.assertEqual(t.tarif1,Decimal('0.51951281652'))
  self.assertEqual(t.tarif2,Decimal('0.5619165198235'))

 def test_tarifaConstruction3(self):
  t = tarifa('234.51951281652','342.5619165198235')
  self.assertEqual(t.tarif1,Decimal('234.51951281652'))
  self.assertEqual(t.tarif2,Decimal('342.5619165198235'))

 def test_tarifaConstruction4(self):
  t = tarifa('84926542654864254104504.51951281652','4589406511089610218974089.5619165198235')
  self.assertEqual(t.tarif1,Decimal('84926542654864254104504.51951281652'))
  self.assertEqual(t.tarif2,Decimal('4589406511089610218974089.5619165198235'))

 def test_tarifaRaises(self):
  self.assertRaises(ValueError,tarifa,'-1','0')

 def test_tarifaRaises2(self):
  self.assertRaises(ValueError,tarifa,'0','-1')

 def test_tarifaRaises3(self):
  self.assertRaises(ValueError,tarifa,'-1','-1')

 def test_tarifaRaises4(self):
  self.assertRaises(ValueError,tarifa,'-0.000000000000000000000000000000000000000000001','0')

 def test_tarifaRaises5(self):
  self.assertRaises(ValueError,tarifa,'0','-99999999999999999999999999999999999999999999999')

 def test_estacionamientoGratis(self):
  fecha1 = datetime(2009, 1, 24, 15, 1, 24, 78915)
  fecha2 = datetime(2009, 1, 27, 15, 1, 24, 78915)
  tarif = tarifa('0','0')
  self.assertEqual(monto(fecha1,fecha2,tarif),0)

 def test_estGratis15min(self):
  fecha1 = datetime(2009, 1, 24, 15, 0, 24, 78915)
  fecha2 = datetime(2009, 1, 24, 15, 15, 24, 78915)
  tarif = tarifa('0','0')
  self.assertEqual(monto(fecha1,fecha2,tarif),0)

 def test_estGratis16min(self):
  fecha1 = datetime(2009, 1, 24, 15, 0, 24, 78915)
  fecha2 = datetime(2009, 1, 24, 15, 16, 24, 78915)
  tarif = tarifa('0','0')
  self.assertEqual(monto(fecha1,fecha2,tarif),0)

 def test_estGratis14min(self):
  fecha1 = datetime(2009, 1, 24, 15, 0, 24, 78915)
  fecha2 = datetime(2009, 1, 24, 15, 14, 24, 78915)
  tarif = tarifa('0','0')
  self.assertRaises(ValueError,monto,fecha1,fecha2,tarif)

 def test_estGratisNegDia(self):
  fecha1 = datetime(2009, 1, 24, 15, 0, 0, 0)
  fecha2 = datetime(2009, 1, 23, 15, 15, 0, 0)
  tarif = tarifa('0','0')
  self.assertRaises(ValueError,monto,fecha1,fecha2,tarif)

 def test_estGratis72h(self):
  fecha1 = datetime(2009, 1, 24, 15, 0, 0, 0)
  fecha2 = datetime(2009, 1, 27, 15, 0, 0, 0)
  tarif = tarifa('0','0')
  self.assertEqual(monto(fecha1,fecha2,tarif),0)

 def test_estGratis72hMenos1min(self):
  fecha1 = datetime(2009, 1, 24, 15, 0, 0, 0)
  fecha2 = datetime(2009, 1, 27, 14, 59, 0, 0)
  tarif = tarifa('0','0')
  self.assertEqual(monto(fecha1,fecha2,tarif),0)

 def test_estGratis72h1min(self):
  fecha1 = datetime(2009, 1, 24, 15, 0, 0, 0)
  fecha2 = datetime(2009, 1, 27, 15, 1, 0, 0)
  tarif = tarifa('0','0')
  self.assertRaises(ValueError,monto,fecha1,fecha2,tarif)

 def test_est1h0am(self):
  fecha1 = datetime(2009, 1, 24, 0, 0, 0, 0)
  fecha2 = datetime(2009, 1, 24, 0, 59, 0, 0)
  tarif = tarifa('0','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),1)

 def test_est2h0am(self):
  fecha1 = datetime(2009, 1, 24, 0, 0, 0, 0)
  fecha2 = datetime(2009, 1, 24, 1, 0, 0, 0)
  tarif = tarifa('0','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),2)

 #ya no se que nombre seguir poniendole a las funciones

 def test_est1(self):
  fecha1 = datetime(2009, 1, 24, 0, 45, 0, 0)
  fecha2 = datetime(2009, 1, 24, 1, 0, 0, 0)
  tarif = tarifa('0','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),1)

 def test_est2(self):
  fecha1 = datetime(2009, 1, 24, 0, 50, 0, 0)
  fecha2 = datetime(2009, 1, 24, 1, 5, 0, 0)
  tarif = tarifa('0','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),1)

 def test_est3(self):
  fecha1 = datetime(2009, 1, 24, 5, 50, 0, 0)
  fecha2 = datetime(2009, 1, 24, 6, 5, 0, 0)
  tarif = tarifa('1','2')
  self.assertEqual(monto(fecha1,fecha2,tarif),2)

 def test_est4(self):
  fecha1 = datetime(2009, 1, 24, 5, 0, 0, 0)
  fecha2 = datetime(2009, 1, 24, 6, 0, 0, 0)
  tarif = tarifa('1','2')
  self.assertEqual(monto(fecha1,fecha2,tarif),3)

 def test_est5(self):
  fecha1 = datetime(2009, 1, 24, 4, 59, 0, 0)
  fecha2 = datetime(2009, 1, 24, 6, 0, 0, 0)
  tarif = tarifa('1','2')
  self.assertEqual(monto(fecha1,fecha2,tarif),4)

 def test_est6(self):
  fecha1 = datetime(2009, 1, 24, 4, 59, 0, 0)
  fecha2 = datetime(2009, 1, 24, 6, 59, 0, 0)
  tarif = tarifa('1','2')
  self.assertEqual(monto(fecha1,fecha2,tarif),5)

 def test_est7(self):
  fecha1 = datetime(2009, 1, 24, 4, 59, 0, 0)
  fecha2 = datetime(2009, 1, 24, 6, 0, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),3)

 def test_est8(self):
  fecha1 = datetime(2009, 1, 24, 5, 0, 0, 0)
  fecha2 = datetime(2009, 1, 24, 5, 59, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),1)

 def test_est9(self):
  fecha1 = datetime(2009, 1, 24, 0, 0, 0, 0)
  fecha2 = datetime(2009, 1, 27, 0, 0, 0, 0)
  tarif = tarifa('1','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),73)

 def test_est9(self):
  fecha1 = datetime(2009, 1, 24, 0, 0, 0, 0)
  fecha2 = datetime(2009, 1, 27, 0, 0, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),109)

 def test_est10(self):
  fecha1 = datetime(2009, 1, 24, 5, 45, 0, 0)
  fecha2 = datetime(2009, 1, 24, 6, 15, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),2)

 def test_est11(self):
  fecha1 = datetime(2009, 1, 24, 5, 15, 0, 0)
  fecha2 = datetime(2009, 1, 24, 5, 45, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),1)

 def test_est12(self):
  fecha1 = datetime(2009, 1, 24, 0, 0, 0, 0)
  fecha2 = datetime(2009, 1, 26, 23, 59, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),108)

 def test_est13(self):
  fecha1 = datetime(2009, 1, 24, 17, 15, 0, 0)
  fecha2 = datetime(2009, 1, 24, 17, 45, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),2)

 def test_est14(self):
  fecha1 = datetime(2009, 1, 24, 17, 45, 0, 0)
  fecha2 = datetime(2009, 1, 24, 18, 14, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),2)

 def test_est15(self):
  fecha1 = datetime(2009, 1, 24, 18, 0, 0, 0)
  fecha2 = datetime(2009, 1, 24, 18, 15, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),1)

 def test_est16(self):
  fecha1 = datetime(2009, 1, 24, 23, 45, 0, 0)
  fecha2 = datetime(2009, 1, 25, 0, 15, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),1)

 def test_est17(self):
  fecha1 = datetime(2009, 1, 24, 23, 45, 0, 0)
  fecha2 = datetime(2009, 1, 25, 0, 15, 0, 0)
  tarif = tarifa('2','1.6298498')
  self.assertEqual(monto(fecha1,fecha2,tarif),Decimal('1.6298498'))

 def test_est19(self):
  fecha1 = datetime(2009, 1, 24, 23, 45, 0, 0)
  fecha2 = datetime(2009, 1, 25, 0, 50, 0, 0)
  tarif = tarifa('2','1.25')
  self.assertEqual(monto(fecha1,fecha2,tarif),Decimal('2.5'))

 def test_est18(self):
  fecha1 = datetime(2009, 1, 24, 0, 0, 0, 0)
  fecha2 = datetime(2009, 1, 24, 8, 0, 0, 0)
  tarif = tarifa('2','1')
  self.assertEqual(monto(fecha1,fecha2,tarif),12)

#nota: el programa se construyo pensando que si la entrada es a las 4am y la salida a las 5am, se cobran dos horas porque se considera que la segunda hora empezo a correr, este es un detalle de implementacion

if __name__ == '__main__':
    unittest.main()