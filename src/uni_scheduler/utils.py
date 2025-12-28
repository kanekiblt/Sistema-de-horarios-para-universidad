from typing import List
from .models import Slot, DAYS, START_MINUTES, END_MINUTES, SLOT, hhmm_to_minutes, minutes_to_hhmm

def generar_candidatos(duracion_horas: int) -> List[Slot]:
    delta = duracion_horas * 60
    slots: List[Slot] = []
    for d in DAYS:
        t = START_MINUTES
        while t + delta <= END_MINUTES:
            slots.append(Slot(d, t, t + delta))
            t += SLOT
    return slots

def profesor_disponible(prof, slot: Slot) -> bool:
    if slot.day not in prof.disponibilidad:
        return False
    for (ini, fin) in prof.disponibilidad[slot.day]:
        s = hhmm_to_minutes(ini)
        e = hhmm_to_minutes(fin)
        if s <= slot.start and slot.end <= e:
            return True
    return False
