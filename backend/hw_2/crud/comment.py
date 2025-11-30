from hw_2.schemas.comment import CommentCreate, CommentResponse, CommentUpdate
from hw_2.schemas.post import PostResponse
from hw_2.utils.exeption import DBExeption




class CommentCrud:

    post: PostResponse = None

    count: int = 1


    @classmethod
    async def get_all(cls) -> list[CommentResponse]:
        """
        Возвращает список коммментариев полученного поста
        :param post: конкретный пост
        :return: список коммментариев
        """
        return cls.post.comments


    @classmethod
    async def get_by_id(
        cls,
        comment_id: int,
    ) -> CommentResponse:
        """
        Возвращает конкретный комментарий, найденный по id в конкретном посте
        :param comment_id: Идентификатор комментария в посте
        :return: конкретный комментарий
        """
        comment = next((com for com in cls.post.comments if com.id == comment_id), None)

        if not comment:
            raise DBExeption.not_found
        
        return comment
    

    @classmethod
    async def add(cls, comment: CommentCreate) -> CommentResponse:
        """
        Добавляет комментарий в полученный пост
        :param comment: конкретный комментарий
        :return: добавленный комментарий
        """
        comment = CommentCreate(
            id=cls.count,
            **comment.model_dump()
        )

        cls.post.comments.append(comment)

        cls.count += 1

        return comment
    

    @classmethod
    async def update(
        cls,
        comment_update: CommentUpdate,
        comment: CommentResponse,
    ) -> CommentResponse:
        """
        Обновляет данные полученного комментария
        :param comment: конкретный комментарий
        :param comment_update: новые данные комментария
        :return: обновленный комментарий
        """
        for key, value in comment_update.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(comment, key, value)

        return comment


    @classmethod
    async def delete(cls, comment: CommentResponse,) -> CommentResponse:
        """
        Удаляет конкретный комментарий из полученного поста 
        :param comment: конкретный комментарий
        :return: удаленный комментарий
        """
        cls.post.comments.remove(comment)

        return comment


    @classmethod
    async def clear(cls) -> list:
        """
        Полностью очищает полученный пост от комментариев
        :return: Пустой список
        """
        return [] if cls.post.comments.clear() else cls.post.comments
