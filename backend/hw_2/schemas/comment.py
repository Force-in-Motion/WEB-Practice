from typing import Annotated
from annotated_types import MinLen
from pydantic import BaseModel
from datetime import datetime, timezone




class CommentCreate(BaseModel):
    """ Схема комменатария для создания клиентом"""

    text: Annotated[str, MinLen(5)]

    created_at: datetime = datetime.now(timezone.utc)


class CommentResponse(CommentCreate):
    """ Схема для возврата клиенту """

    id: int
