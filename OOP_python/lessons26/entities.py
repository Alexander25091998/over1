from dataclasses import dataclass, field

ADMIN_ACCES = 'ADMIN_ACCES'
SRUDENT_ACCES = 'SRUDENT_ACCES'


@dataclass(frozen=True)
class Student:
    name: str
    password: str
    role: str = SRUDENT_ACCES
    marks: list = field(default_factory=list)