from pydantic import BaseModel


class ShowSingleUser(BaseModel):
    id: int
    email: str
    is_active: bool
    is_staff: bool
    is_superuser: bool


class CreateUser(BaseModel):
    email: str
    password: str


class PatchUser(BaseModel):
    email: str
    is_active: bool
