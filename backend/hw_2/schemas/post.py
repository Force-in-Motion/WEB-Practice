from typing import Annotated, List, Optional
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel
from datetime import datetime, timezone
from schemas.comment import CommentResponse




class PostCreate(BaseModel):
    """Схема поста для создания клиентом"""

    title: Annotated[str, MinLen(5), MaxLen(255)]

    description: Annotated[str, MinLen(5)]



class PostUpdate(BaseModel):
    """Схема поста для создания клиентом"""

    title: Optional[Annotated[str, MinLen(5), MaxLen(255)]]

    description: Optional[Annotated[str, MinLen(5)]]



class PostResponse(PostCreate):
    """Схема для возврата поста клиенту"""

    id: int

    created_at: datetime = datetime.now(timezone.utc)

    comments: List[CommentResponse] = []
