from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Tuple

DAYS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
START_MINUTES = 7 * 60
END_MINUTES = 20 * 60
SLOT = 30

def minutes_to_hhmm(m: int) -> str:
    h = m // 60
    mi = m % 60
    return f"{h:02d}:{mi:02d}"

def hhmm_to_minutes(hhmm: str) -> int:
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m

@dataclass
class Room:
    id: str
    faculty: str   # Ingeniería / Ciencias / Letras
    kind: str      # "teorico" | "lab"
    capacity: int

@dataclass
class Professor:
    id: str
    name: str
    habilitado_desde_ciclo: int = 1
    disponible_labs: bool = True
    disponibilidad: Dict[str, List[Tuple[str, str]]] = field(default_factory=dict)
    # ejemplo: {"Lunes": [("07:00","12:00"), ("14:00","18:00")]}

@dataclass
class Course:
    code: str
    name: str
    faculty: str
    cycle: int
    inscritos_teorico: int
    inscritos_lab: int
    duracion_teorico_horas: int = 2
    duracion_lab_horas: int = 2
    profesor_id: Optional[str] = None

@dataclass
class Slot:
    day: str
    start: int
    end: int
    def overlaps(self, other: "Slot") -> bool:
        return self.day == other.day and not (self.end <= other.start or other.end <= self.start)
    def duration_hours(self) -> float:
        return (self.end - self.start) / 60.0
    def __str__(self):
        return f"{self.day} {minutes_to_hhmm(self.start)}-{minutes_to_hhmm(self.end)}"

@dataclass
class Assignment:
    course_code: str
    group: str
    slot: Slot
    room_id: str
    professor_id: Optional[str]
