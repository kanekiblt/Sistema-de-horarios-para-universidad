from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Tuple
from src.uni_scheduler.scheduler import Scheduler
from src.uni_scheduler.models import Room, Professor, Course, Slot, Assignment
from src.uni_scheduler.data_example import dataset_ejemplo

app = FastAPI(title="Uni Scheduler API", version="1.0.0")

# ----- Schemas -----
class SlotOut(BaseModel):
    day: str
    start: int
    end: int

class AssignmentOut(BaseModel):
    course_code: str
    group: str
    slot: SlotOut
    room_id: str
    professor_id: Optional[str]

class RoomIn(BaseModel):
    id: str
    faculty: str
    kind: str
    capacity: int

class ProfessorIn(BaseModel):
    id: str
    name: str
    habilitado_desde_ciclo: int = 1
    disponible_labs: bool = True
    disponibilidad: Dict[str, List[Tuple[str, str]]] = {}

class CourseIn(BaseModel):
    code: str
    name: str
    faculty: str
    cycle: int
    inscritos_teorico: int
    inscritos_lab: int
    duracion_teorico_horas: int = 2
    duracion_lab_horas: int = 2
    profesor_id: Optional[str] = None

class ScheduleIn(BaseModel):
    semester: str = Field(..., description="Abril-Agosto o Agosto-Diciembre")
    rooms: List[RoomIn]
    professors: List[ProfessorIn]
    courses: List[CourseIn]
    assistants: List[str] = []

class ScheduleOut(BaseModel):
    assignments: List[AssignmentOut]
    alerts: List[str]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/sample", response_model=ScheduleIn)
def sample():
    rooms, profs, courses, assistants = dataset_ejemplo()
    return {
        "semester": "Agosto-Diciembre",
        "rooms": [r.__dict__ for r in rooms],
        "professors": [{
            "id": p.id,
            "name": p.name,
            "habilitado_desde_ciclo": p.habilitado_desde_ciclo,
            "disponible_labs": p.disponible_labs,
            "disponibilidad": p.disponibilidad,
        } for p in profs],
        "courses": [c.__dict__ for c in courses],
        "assistants": assistants,
    }

@app.post("/schedule", response_model=ScheduleOut)
def schedule(payload: ScheduleIn):
    rooms = [Room(**r.model_dump()) for r in payload.rooms]
    profs = [Professor(**p.model_dump()) for p in payload.professors]
    courses = [Course(**c.model_dump()) for c in payload.courses]
    s = Scheduler(payload.semester, rooms, profs, courses, payload.assistants)
    s.build()
    assignments = [AssignmentOut(
        course_code=a.course_code,
        group=a.group,
        slot=SlotOut(day=a.slot.day, start=a.slot.start, end=a.slot.end),
        room_id=a.room_id,
        professor_id=a.professor_id,
    ) for a in s.assignments]
    return {"assignments": assignments, "alerts": s.alerts}
