#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, json, os
from src.uni_scheduler.scheduler import Scheduler
from src.uni_scheduler.data_example import dataset_ejemplo

def main():
    parser = argparse.ArgumentParser(description="Generador de horarios universitarios")
    parser.add_argument("--semester", default="Agosto-Diciembre", choices=["Abril-Agosto","Agosto-Diciembre"], help="Semestre a usar")
    parser.add_argument("--export", action="store_true", help="Exportar Excel y PDF de alertas")
    args = parser.parse_args()

    rooms, profs, courses, assistants = dataset_ejemplo()
    s = Scheduler(args.semester, rooms, profs, courses, assistants)
    s.build()

    # Print resumen
    cursos_map = {c.code: c for c in courses}
    print("\n===== HORARIOS GENERADOS =====\n")
    for fac in sorted({c.faculty for c in courses}):
        print(f"--- {fac} ---")
        asigns = [a for a in s.assignments if cursos_map[a.course_code].faculty == fac]
        asigns_sorted = sorted(asigns, key=lambda x: (["Lunes","Martes","Miércoles","Jueves","Viernes"].index(x.slot.day), x.slot.start, x.course_code, x.group))
        for a in asigns_sorted:
            c = cursos_map[a.course_code]
            prof = "Asistente/No asignado" if a.professor_id is None else s.professors[a.professor_id].name
            from src.uni_scheduler.models import minutes_to_hhmm
            print(f"{c.name:<28} | {a.group:<6} | {a.slot.day:<10} {minutes_to_hhmm(a.slot.start)}-{minutes_to_hhmm(a.slot.end)} | {a.room_id:<10} | {prof}")
    print("\n===== ALERTAS =====")
    if not s.alerts:
        print("Sin alertas.")
    else:
        for msg in s.alerts:
            print("- ", msg)

    if args.export:
        s.export_excel("horarios.xlsx")
        s.export_pdf_alertas("alertas.pdf")
        print("\nArchivos generados: horarios.xlsx, alertas.pdf")

if __name__ == "__main__":
    main()
