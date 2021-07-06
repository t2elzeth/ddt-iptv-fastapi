from pydantic import BaseModel


class RetrieveSingleShow(BaseModel):
    id: int
    title: str
    rating: int
    type: str
    description: str
    genre: str
