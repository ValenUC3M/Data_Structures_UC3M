
"""
Created on Fri Mar 13 14:06:33 2020

@author: isegura
"""
from fase1 import GestionAmazon

gst=GestionAmazon()
dataPaq=[
      
      ['132-1352234-332348','C/Coronavirus',3,28911],
      ['132-1352234-332349','C/Paz',4,28911],
      ['132-1352234-332350','C/Metro',3,28912],
      ['132-1352234-332351','C/Mar',4,28912],
      ['132-1352234-332352','C/Salvador',1,28913],
      ['132-1352234-332353','C/Brasil',5,28913],
      ['132-1352234-332354','C/Salvador',1,28913],
      ['132-1352234-332355','C/Brasil',5,28913],
      ['132-1352234-332344','C/Canovas del Castillo',53,28914],
      ['132-1352234-332347','C/Madrid',5,28914],
      ['132-1352234-332345','C/Mayor',10,28915],
      ['132-1352234-332346','C/Real',15,28915],
      ['132-1352234-000001','C/Pez',10,28916],
      ['132-1352234-000002','C/Paris',15,28917],
      ['132-1352234-000003','C/Sevilla',33,28918],
      ['132-1352234-000004','C/Jaen',15,28918]  
]
gst.cargarPedidos(dataPaq)
print('Pedidos:\t',str(gst.paquetes))
print('\n')


dataRep=[
  ['R1000001','Segura, Isabel','Activo',[28911,28912]],
  ['R1000002','Iglesias, Julio','Activo',[28911]],
  ['R1000003','Vargas, Chavela','Activo',[28912]],
  ['R1000004','Bose, Miguel','Activo',[28913,28914]],
  ['R1000005','Barrio, Paquita','Activo',[28914]],
  ['R1000006','Escudero, Juan','Activo',[28915]],
  ['R1000007','Ruíz, Juan','Activo',[28915,28916]],
  ['R1000008','Segura, David','Activo',[28917]],
  ['R1000009','Sampedro, Monica','Activo',[28918]],
  ['R1000010','Molina, Clara','Activo',[28914,28916]],
  ['R1000011','Molina, Miguel','Activo',[28917,28918]]
]
gst.cargarRepartidores(dataRep)
print('Repartidores antes de la asignación de paquetes:')
gst.mostrarRepartidores()
print('\n')

gst.asignarReparto()
print('Repartidores después de la asignación de paquetes:')
gst.mostrarRepartidores()
print('\n')
#
gst.bajaRepartidor('R1000011')
print('\n')

print('Mostramos repartidores después de borrar R1000011')

gst.mostrarRepartidores()
print('\n')

gst.reparto()

gst.mostrarRepartidores()
print('\n')

print("Entregados correctamente:",gst.entregados)
print("Incidencias",gst.incidencias)

"""La salida del programa debería ser:
    
    Pedidos:         132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0,
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0,
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0,
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0,
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0,
                132-1352234-000001 C/Pez 10 28916 0,
                132-1352234-000002 C/Paris 15 28917 0,
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0


Repartidores antes de la asignación de paquetes:
Repartidor: R1000005, Barrio, Paquita, Activo, Zonas: 28914,

Repartidor: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914,

Repartidor: R1000006, Escudero, Juan, Activo, Zonas: 28915,

Repartidor: R1000002, Iglesias, Julio, Activo, Zonas: 28911,

Repartidor: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916,

Repartidor: R1000011, Molina, Miguel, Activo, Zonas: 28917, 28918,

Repartidor: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

Repartidor: R1000009, Sampedro, Monica, Activo, Zonas: 28918,

Repartidor: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912,

Repartidor: R1000008, Segura, David, Activo, Zonas: 28917,

Repartidor: R1000003, Vargas, Chavela, Activo, Zonas: 28912



Repartidores después de la asignación de paquetes:
Repartidor: R1000005, Barrio, Paquita, Activo, Zonas: 28914
        Paquetes:
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0,

Repartidor: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914
        Paquetes:
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0,

Repartidor: R1000006, Escudero, Juan, Activo, Zonas: 28915
        Paquetes:
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0,

Repartidor: R1000002, Iglesias, Julio, Activo, Zonas: 28911
        Paquetes:
                132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0,

Repartidor: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916
        Paquetes:
                132-1352234-000001 C/Pez 10 28916 0,

Repartidor: R1000011, Molina, Miguel, Activo, Zonas: 28917, 28918
        Paquetes:
                132-1352234-000002 C/Paris 15 28917 0,
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0,

Repartidor: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

Repartidor: R1000009, Sampedro, Monica, Activo, Zonas: 28918,

Repartidor: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912
        Paquetes:
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0,

Repartidor: R1000008, Segura, David, Activo, Zonas: 28917,

Repartidor: R1000003, Vargas, Chavela, Activo, Zonas: 28912



vamos a dar de baja: R1000011
reasignado paquete  132-1352234-000002  a: R1000008
reasignado paquete  132-1352234-000003  a: R1000009
reasignado paquete  132-1352234-000004  a: R1000009


Mostramos repartidores después de borrar R1000011
Repartidor: R1000005, Barrio, Paquita, Activo, Zonas: 28914
        Paquetes:
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0,

Repartidor: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914
        Paquetes:
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0,

Repartidor: R1000006, Escudero, Juan, Activo, Zonas: 28915
        Paquetes:
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0,

Repartidor: R1000002, Iglesias, Julio, Activo, Zonas: 28911
        Paquetes:
                132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0,

Repartidor: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916
        Paquetes:
                132-1352234-000001 C/Pez 10 28916 0,

Repartidor: R1000011, Molina, Miguel, No activo, Zonas: 28917, 28918,

Repartidor: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

Repartidor: R1000009, Sampedro, Monica, Activo, Zonas: 28918
        Paquetes:
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0,

Repartidor: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912
        Paquetes:
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0,

Repartidor: R1000008, Segura, David, Activo, Zonas: 28917
        Paquetes:
                132-1352234-000002 C/Paris 15 28917 0,

Repartidor: R1000003, Vargas, Chavela, Activo, Zonas: 28912


#Esta parte puede cambiar porque la entrega o no de un paquete es aleatorio

procesando reparto de: 
Repartidor: R1000005, Barrio, Paquita, Activo, Zonas: 28914
        Paquetes:
                132-1352234-332344 C/Canovas del Castillo 53 28914 0,
                132-1352234-332347 C/Madrid 5 28914 0


Paquete a entregar... 132-1352234-332344 C/Canovas del Castillo 53 28914 0
No se ha podido entregar: 132-1352234-332344  repartidor por: R1000005  intentos: 1
Paquete a entregar... 132-1352234-332347 C/Madrid 5 28914 0
No se ha podido entregar: 132-1352234-332347  repartidor por: R1000005  intentos: 1
Paquete a entregar... 132-1352234-332344 C/Canovas del Castillo 53 28914 1
Entregado: 132-1352234-332344  entregado por: R1000005  al intento: 1
Paquete a entregar... 132-1352234-332347 C/Madrid 5 28914 1
No se ha podido entregar: 132-1352234-332347  repartidor por: R1000005  intentos: 2
Paquete a entregar... 132-1352234-332347 C/Madrid 5 28914 2
Incidencia del paquete: 132-1352234-332347  repartidor por: R1000005  intentos: 3

procesando reparto de: 
Repartidor: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914
        Paquetes:
                132-1352234-332352 C/Salvador 1 28913 0,
                132-1352234-332353 C/Brasil 5 28913 0,
                132-1352234-332354 C/Salvador 1 28913 0,
                132-1352234-332355 C/Brasil 5 28913 0


Paquete a entregar... 132-1352234-332352 C/Salvador 1 28913 0
No se ha podido entregar: 132-1352234-332352  repartidor por: R1000004  intentos: 1
Paquete a entregar... 132-1352234-332353 C/Brasil 5 28913 0
Entregado: 132-1352234-332353  entregado por: R1000004  al intento: 0
Paquete a entregar... 132-1352234-332354 C/Salvador 1 28913 0
Entregado: 132-1352234-332354  entregado por: R1000004  al intento: 0
Paquete a entregar... 132-1352234-332355 C/Brasil 5 28913 0
No se ha podido entregar: 132-1352234-332355  repartidor por: R1000004  intentos: 1
Paquete a entregar... 132-1352234-332352 C/Salvador 1 28913 1
Entregado: 132-1352234-332352  entregado por: R1000004  al intento: 1
Paquete a entregar... 132-1352234-332355 C/Brasil 5 28913 1
Entregado: 132-1352234-332355  entregado por: R1000004  al intento: 1

procesando reparto de: 
Repartidor: R1000006, Escudero, Juan, Activo, Zonas: 28915
        Paquetes:
                132-1352234-332345 C/Mayor 10 28915 0,
                132-1352234-332346 C/Real 15 28915 0


Paquete a entregar... 132-1352234-332345 C/Mayor 10 28915 0
Entregado: 132-1352234-332345  entregado por: R1000006  al intento: 0
Paquete a entregar... 132-1352234-332346 C/Real 15 28915 0
No se ha podido entregar: 132-1352234-332346  repartidor por: R1000006  intentos: 1
Paquete a entregar... 132-1352234-332346 C/Real 15 28915 1
No se ha podido entregar: 132-1352234-332346  repartidor por: R1000006  intentos: 2
Paquete a entregar... 132-1352234-332346 C/Real 15 28915 2
Incidencia del paquete: 132-1352234-332346  repartidor por: R1000006  intentos: 3

procesando reparto de: 
Repartidor: R1000002, Iglesias, Julio, Activo, Zonas: 28911
        Paquetes:
                132-1352234-332348 C/Coronavirus 3 28911 0,
                132-1352234-332349 C/Paz 4 28911 0


Paquete a entregar... 132-1352234-332348 C/Coronavirus 3 28911 0
Entregado: 132-1352234-332348  entregado por: R1000002  al intento: 0
Paquete a entregar... 132-1352234-332349 C/Paz 4 28911 0
Entregado: 132-1352234-332349  entregado por: R1000002  al intento: 0

procesando reparto de: 
Repartidor: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916
        Paquetes:
                132-1352234-000001 C/Pez 10 28916 0


Paquete a entregar... 132-1352234-000001 C/Pez 10 28916 0
No se ha podido entregar: 132-1352234-000001  repartidor por: R1000010  intentos: 1
Paquete a entregar... 132-1352234-000001 C/Pez 10 28916 1
No se ha podido entregar: 132-1352234-000001  repartidor por: R1000010  intentos: 2
Paquete a entregar... 132-1352234-000001 C/Pez 10 28916 2
Incidencia del paquete: 132-1352234-000001  repartidor por: R1000010  intentos: 3
R1000011 no está activo

.
R1000007 no tiene paquetes a repartir.



procesando reparto de: 
Repartidor: R1000009, Sampedro, Monica, Activo, Zonas: 28918
        Paquetes:
                132-1352234-000003 C/Sevilla 33 28918 0,
                132-1352234-000004 C/Jaen 15 28918 0


Paquete a entregar... 132-1352234-000003 C/Sevilla 33 28918 0
No se ha podido entregar: 132-1352234-000003  repartidor por: R1000009  intentos: 1
Paquete a entregar... 132-1352234-000004 C/Jaen 15 28918 0
Entregado: 132-1352234-000004  entregado por: R1000009  al intento: 0
Paquete a entregar... 132-1352234-000003 C/Sevilla 33 28918 1
No se ha podido entregar: 132-1352234-000003  repartidor por: R1000009  intentos: 2
Paquete a entregar... 132-1352234-000003 C/Sevilla 33 28918 2
Entregado: 132-1352234-000003  entregado por: R1000009  al intento: 2

procesando reparto de: 
Repartidor: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912
        Paquetes:
                132-1352234-332350 C/Metro 3 28912 0,
                132-1352234-332351 C/Mar 4 28912 0


Paquete a entregar... 132-1352234-332350 C/Metro 3 28912 0
No se ha podido entregar: 132-1352234-332350  repartidor por: R1000001  intentos: 1
Paquete a entregar... 132-1352234-332351 C/Mar 4 28912 0
No se ha podido entregar: 132-1352234-332351  repartidor por: R1000001  intentos: 1
Paquete a entregar... 132-1352234-332350 C/Metro 3 28912 1
Entregado: 132-1352234-332350  entregado por: R1000001  al intento: 1
Paquete a entregar... 132-1352234-332351 C/Mar 4 28912 1
No se ha podido entregar: 132-1352234-332351  repartidor por: R1000001  intentos: 2
Paquete a entregar... 132-1352234-332351 C/Mar 4 28912 2
Entregado: 132-1352234-332351  entregado por: R1000001  al intento: 2

procesando reparto de: 
Repartidor: R1000008, Segura, David, Activo, Zonas: 28917
        Paquetes:
                132-1352234-000002 C/Paris 15 28917 0


Paquete a entregar... 132-1352234-000002 C/Paris 15 28917 0
Entregado: 132-1352234-000002  entregado por: R1000008  al intento: 0
R1000003 no tiene paquetes a repartir.


Repartidor: R1000005, Barrio, Paquita, Activo, Zonas: 28914,

Repartidor: R1000004, Bose, Miguel, Activo, Zonas: 28913, 28914,

Repartidor: R1000006, Escudero, Juan, Activo, Zonas: 28915,

Repartidor: R1000002, Iglesias, Julio, Activo, Zonas: 28911,

Repartidor: R1000010, Molina, Clara, Activo, Zonas: 28914, 28916,

Repartidor: R1000011, Molina, Miguel, No activo, Zonas: 28917, 28918,

Repartidor: R1000007, Ruíz, Juan, Activo, Zonas: 28915, 28916,

Repartidor: R1000009, Sampedro, Monica, Activo, Zonas: 28918,

Repartidor: R1000001, Segura Bedmar, Isabel, Activo, Zonas: 28911, 28912,

Repartidor: R1000008, Segura, David, Activo, Zonas: 28917,

Repartidor: R1000003, Vargas, Chavela, Activo, Zonas: 28912



Entregados correctamente: R1000005 132-1352234-332344,
                R1000004 132-1352234-332353,
                R1000004 132-1352234-332354,
                R1000004 132-1352234-332352,
                R1000004 132-1352234-332355,
                R1000006 132-1352234-332345,
                R1000002 132-1352234-332348,
                R1000002 132-1352234-332349,
                R1000009 132-1352234-000004,
                R1000009 132-1352234-000003,
                R1000001 132-1352234-332350,
                R1000001 132-1352234-332351,
                R1000008 132-1352234-000002
Incidencias 132-1352234-332347 R1000005 superado número intentos,
                132-1352234-332346 R1000006 superado número intentos,
                132-1352234-000001 R1000010 superado número intentos
    
    """
