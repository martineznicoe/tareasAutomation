# Una escuela tiene alumnos, cuyas características son:

# *Nombre
# *Apellido
# *Nota Matematica
# *Nota Lengua
# *Nota geografía
# *Promedio

# -Los alumnos pueden dar exámenes.

# La escuela también tiene profesores que tienen las siguientes características:

# *Nombre
# *Apellido
# *Materia que enseña

# -Los profesores toman exámenes y le dan al alumno una nota.

# Se deben cargar distintos alumnos y profesores, 
# que los alumnos den exámenes que toman los profesores y que el resultado sea una nota. 
# El alumno siempre debe tener un promedio (al principio las tres notas son 0).

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Alumno(Persona):
    def __init__(self, nombre, apellido, nota_matematica, nota_lengua, nota_geografia, promedio):
        Persona.__init__(self, nombre, apellido)
        self.nota_matematica = nota_matematica
        self.nota_lengua = nota_lengua
        self.nota_geografia = nota_geografia
        self.promedio = promedio
    
    #def examen():

class Profesor(Persona):
    def __init__(self, nombre, apellido, materia):
        Persona.__init__(self, nombre, apellido)
        self.materia = materia

    #def tomar_examen():
    

