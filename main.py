class Materia:
    def __init__(self, materia, profesores=[]):
        self.__materia__ = materia
        self.__profesores__ = profesores
        self.__alumnos__ = []

    def obtener_profesores(self):
        return self.__profesores__
    
    def cambiar_nombre(self, materia):
        self.__materia__ = materia

    def obtener_materia(self):
        return self.__materia__

    def obtener_lista_de_estudiantes_de_la_materia(self, materia):     #en vez de la funcion --> obtener_alumnos(self)
        return self.__alumnos__                                        #obtengo una lista de los alumno que van a esa materia.
    
    def agregar_alumnos_a_materia(self ,estudiante):
        self.__alumnos__.append(estudiante)


class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__

class Alumno:
    def __init__(self, estudiante, materia, nota):
        self.__estudiante__ = estudiante
        self.__materia__ = materia
        self.__nota__ = nota






     