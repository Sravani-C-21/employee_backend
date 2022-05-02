from typing import List, Optional

from pydantic import BaseModel


class EmployeeCreateSchema(BaseModel):
    name: str
    email: Optional[str] = None

class EmployeeResponseSchema(BaseModel):
    id: int
    name: str
    email: Optional[str] = None