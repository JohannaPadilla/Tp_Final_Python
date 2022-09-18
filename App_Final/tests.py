from django.test import TestCase

from App_Final.models import *

# Create your tests here.
class Autor(TestCase):

    def setUp(self):
        Autor.objects.create(nombre="Clamp", apellido="Clamp", nacionalidad="Japon")

    def test_nombre(self):
        p1 = Autor.objects.get(Autor=1)
        self.assertEqual(p1.nombre, 'Clamp')

    def test_apellido(self):
        p1 = Autor.objects.get(Autor=1)
        self.asser (p1.apellido, 'Clamp'.lower)

    def test_nacionalidad(self):
        p1 = Autor.objects.get(Autor=1)
        self.asser (p1.nacionalidad, 'Clamp'.upper)    
