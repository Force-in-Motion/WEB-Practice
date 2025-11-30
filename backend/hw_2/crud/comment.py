from backend.hw_2.schemas.post import PostResponse
from hw_2.storage import STORAGE
from hw_2.schemas.comment import CommentCreate, CommentResponse
from hw_2 import DBExeption




class CommentCrud:

    storage: list = STORAGE

    count: int = 1


    @classmethod
    async def get_all(
        cls,
        post: PostResponse,
    ) -> list[CommentResponse]:
        """
        Возвращает список коммментариев полученного поста
        :param post: конкретный пост
        :return: список коммментариев
        """

    @classmethod
    async def get_by_id(
        cls,
        post: PostResponse,
        comment_id: int,
    ) -> CommentResponse:
        """
        Возвращает конкретный комментарий, найденный по id в конкретном посте
        :param post: полученный пост
        :param comment_id: Идентификатор комментария в посте
        :return: конкретный комментарий
        """

    @classmethod
    async def add(cls, post: PostResponse) -> CommentResponse:
        """
        Добавляет комментарий в полученный пост
        :param post: конкретный пост
        :return: добавленный комментарий
        """

    @classmethod
    async def update(
        cls,
        post: PostResponse,
        new_comment_data: CommentCreate,
        comment_response: CommentResponse,
    ) -> CommentResponse:
        """
        Обновляет данные полученного комментария
        :param post: конкретный пост
        :param new_comment_data: новые данные комментария
        :param comment_response: конкретный комментарий, полученный для замены его данных
        :return: обновленный комментарий
        """

    @classmethod
    async def delete(cls, post: PostResponse, comment_id: int,) -> CommentResponse:
        """
        Удаляет конкретный комментарий из полученного поста 
        :param post: конкретный пост
        :param comment_id: конкретный комментарий
        :return: удаленный комментарий
        """


    @classmethod
    async def clear(cls) -> list:
        """
        Полностью очищает полученный пост
        :return: Пустой список
        """
