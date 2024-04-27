import unittest
from main import Materia, Profesor, Alumno
    
class TestMateriaProfesor(unittest.TestCase):

    def setUp(self):
        self.nombre =  'Daniel'
        self.cargo = 'Titular'
        self.legajo = 1234
        self.profe1 = Profesor(self.nombre,self.cargo,self.legajo)
        self.profe2 = Profesor('Elio','Ayudante', 2341)

        self.mat1 = 'Computacion'
        self.profe = self.nombre
        self.materia1 = Materia(self.mat1, [self.profe])

        self.mat2 = 'Programacion'
        self.profes = ['yo','vos','el']
        self.materia2 = Materia(self.mat2, self.profes)

        self.alumno1 = Alumno('Maxi','Computacion',90)
        self.alumno2 = Alumno('Marc','Computacion',70)

        
        

    def test_constructor_Profesor(self):
        
        self.assertEqual(self.profe1.obtener_nombre(), self.nombre)
        self.assertEqual(self.profe1.obtener_cargo(), self.cargo)
        self.assertEqual(self.profe1.obtener_legajo(), self.legajo)

        self.assertEqual(self.profe2.obtener_nombre(), 'Elio')
        self.assertEqual(self.profe2.obtener_cargo(), 'Ayudante')
        self.assertEqual(self.profe2.obtener_legajo(), 2341)

    def test_constructor_Materia(self):
        self.assertEqual(self.materia1.obtener_materia(),self.mat1)
        self.assertEqual(self.materia1.obtener_profesores(), [self.profe])

    def test_obtener_profesores(self):
        self.assertEqual(self.materia1.obtener_profesores(), [self.profe])

    def test_cambiar_nombre_de_materia(self):
        self.materia1.cambiar_nombre('Fisica')
        self.assertEqual(self.materia1.obtener_materia(), 'Fisica') 
    
    def test_constructor_Alumno(self):
        self.assertEqual(self.alumno1.__estudiante__, 'Maxi')
        self.assertEqual(self.alumno1.__materia__, 'Computacion')
        self.assertEqual(self.alumno1.__nota__, 90)

    def test_obtener_lista_de_estudiantes_de_la_materia_vacia(self):
        self.assertEqual(self.materia1.obtener_lista_de_estudiantes_de_la_materia(self.mat1), [])
        self.assertEqual(self.materia2.obtener_lista_de_estudiantes_de_la_materia(self.mat2), [])

    def test_agregar_alumno_a_materia(self):
        self.materia1.agregar_alumnos_a_materia(self.alumno1.__estudiante__)
        self.assertEqual(self.materia1.obtener_lista_de_estudiantes_de_la_materia(self.materia1),['Maxi'])

    def test_agregar_alumnos_a_materia(self):
        self.materia1.agregar_alumnos_a_materia(self.alumno1.__estudiante__)
        self.materia1.agregar_alumnos_a_materia(self.alumno2.__estudiante__)
        self.assertEqual(self.materia1.obtener_lista_de_estudiantes_de_la_materia(self.materia1),['Maxi','Marc'])
        


if __name__ == "__main__":
    unittest.main()

