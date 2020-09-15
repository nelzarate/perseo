from app.wsgi import *
from core.erp.models import Type

""" query = Type.objects.all()
print (queryssssss)
 """


""" t = Type()
t.name='senador'
t.save() """

""" t = Type.objects.get(id='4')
t.name='diputado'
t.save() 
print(t.name) """
#obj = Type.objects.filter(name__icontains='Dipu')
for i in Type.objects.filter(name__contains='a'):
    print("es asi asi" + i.name)
    print("o  k")

