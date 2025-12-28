from .models import Room, Professor, Course

def dataset_ejemplo():
    rooms = [
        # Ingeniería
        Room("Ing-A101", "Ingeniería", "teorico", 60),
        Room("Ing-A102", "Ingeniería", "teorico", 60),
        Room("Ing-Lab1", "Ingeniería", "lab", 20),
        Room("Ing-Lab2", "Ingeniería", "lab", 20),
        # Ciencias
        Room("Cien-201", "Ciencias", "teorico", 60),
        Room("Cien-202", "Ciencias", "teorico", 60),
        Room("Cien-Lab5", "Ciencias", "lab", 20),
        # Letras
        Room("Let-301", "Letras", "teorico", 60),
        Room("Let-302", "Letras", "teorico", 60),
    ]

    profs = [
        Professor(
            id="p1",
            name="Prof. X",
            habilitado_desde_ciclo=3,
            disponible_labs=False,
            disponibilidad={
                "Lunes": [("07:00","12:00"), ("14:00","18:00")],
                "Martes": [("07:00","12:00")],
                "Miércoles": [("12:30","18:00")],
                "Jueves": [("07:00","12:00")],
                "Viernes": [("14:00","20:00")],
            },
        ),
        Professor(
            id="p2",
            name="Prof. Y",
            habilitado_desde_ciclo=1,
            disponible_labs=True,
            disponibilidad={
                "Lunes": [("07:00","20:00")],
                "Martes": [("07:00","20:00")],
                "Miércoles": [("07:00","20:00")],
                "Jueves": [("07:00","20:00")],
                "Viernes": [("07:00","20:00")],
            },
        ),
    ]

    courses = [
        # Caso pedido: Biología Molecular (Ciclo 4 - Ciencias) 80 teórico + 30 lab
        Course(
            code="BIO401",
            name="Biología Molecular",
            faculty="Ciencias",
            cycle=4,
            inscritos_teorico=80,
            inscritos_lab=30,
            duracion_teorico_horas=2,
            duracion_lab_horas=2,
            profesor_id="p2",
        ),
        # Otros cursos de muestra
        Course(
            code="MAT101",
            name="Cálculo I",
            faculty="Ingeniería",
            cycle=1,
            inscritos_teorico=55,
            inscritos_lab=0,
            profesor_id="p1",
        ),
        Course(
            code="FIS203",
            name="Física II",
            faculty="Ingeniería",
            cycle=3,
            inscritos_teorico=100,
            inscritos_lab=45,
            duracion_lab_horas=3,
            profesor_id="p2",
        ),
        Course(
            code="LIT202",
            name="Literatura Universal",
            faculty="Letras",
            cycle=2,
            inscritos_teorico=40,
            inscritos_lab=0,
            profesor_id="p1",
        ),
    ]

    assistants = ["asist1", "asist2"]
    return rooms, profs, courses, assistants
