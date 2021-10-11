from django.test import TestCase
from config.wsgi import *
from core.models import Type, Employee

#LISTAR

##select * from TABLA;
# query = Type.objects.all()
# print(query)

#INSERTAR
# t=Type()
# t.name = 'Aliado'
# t.save()

# #EDICION
# t = Type.objects.get(id=1)
# print(t.name)
# t.name = 'Prueba2'
# t.save()
# print(t.name)

# #ELIMINACION
#
# t = Type.objects.get(id=1)
# t.delete()
# print(t.name)

# #PRUEBA CON try catch
# try:
#     t = Type.objects.get(id=1)
#     t.name = 'Accion'
#     t.save()
# except Exception as e:
#     print(e)

#LISTAR
obj = Type.objects.filter(name__contains='Pre') #tal cual
print(obj)

obj = Type.objects.filter(name__icontains='pre') #cualquiere
print(obj)

obj = Type.objects.filter(name__endswith='a') #que termine en
print(obj)
obj = Type.objects.filter(name__in = ['Presidente','Alle'])#exactament igual
print(obj)
print(obj.count() )
obj = Type.objects.filter(name__contains = ['e']).query #exactament igual
print(obj)

emp = Employee.objects.filter(type_id=1)
print(emp)
