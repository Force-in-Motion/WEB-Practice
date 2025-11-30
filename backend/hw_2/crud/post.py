from backend.hw_2.schemas.post import PostCreate, PostResponse, PostUpdate
from hw_2.storage import STORAGE
from hw_2.utils.exeption import DBExeption 




class PostCrud:

    storage: list = STORAGE

    count: int = 1


    @classmethod
    async def get_all(cls) -> list[PostResponse]:
        """
        Возвращает список постов из БД
        :return: список постов
        """


    @classmethod
    async def get_by_id(
        cls,
        post_id: int,
    ) -> PostResponse:
        """
        Возвращает конкретный пост, найденный по id в БД
        :param post_id: Идентификатор поста в БД
        :return: конкретный пост
        """


    @classmethod
    async def add(cls, post: PostCreate) -> PostResponse:
        """
        Добавляет пост в БД
        :param post: конкретный пост
        :return: добавленный пост
        """


    @classmethod
    async def update(
        cls,
        post_update: PostUpdate,
        post: PostResponse,
    ) -> PostResponse:
        """
        Обновляет данные полученного поста
        :param post_create: новые данные поста, полученный от клиента
        :param post_response: конкретный пост, найденный в БД
        :return: обновленный пост
        """


    @classmethod
    async def delete(
        cls,
        post: PostResponse,
    ) -> PostResponse:
        """
        Удаляет полученный пост из БД
        :param post: конкретный пост
        :return: удаленный пост
        """


    @classmethod
    async def clear(cls) -> list:
        """
        Полностью очищает БД
        :return: Пустой список
        """
