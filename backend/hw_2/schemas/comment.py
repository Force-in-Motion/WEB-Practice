from typing import Annotated, Optional
from annotated_types import MinLen
from pydantic import BaseModel
from datetime import datetime, timezone




class CommentCreate(BaseModel):
    """ Схема комменатария для создания клиентом"""

    text: Annotated[str, MinLen(5)]



class CommentUpdate(BaseModel):
    """ Схема комменатария для создания клиентом"""

    text: Optional[Annotated[str, MinLen(5)]]



class CommentResponse(CommentCreate):
    """ Схема для возврата клиенту """

    id: int

    created_at: datetime = datetime.now(timezone.utc)