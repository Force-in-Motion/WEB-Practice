from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr


class UserOut(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    full_name: Optional[str] | None = None
    is_active: bool = True


class UserIn(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    username: str
    email: EmailStr
    full_name: Optional[str] | None = None
    is_active: bool = True
