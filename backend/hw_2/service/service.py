from backend.hw_2.schemas.post import PostCreate, PostResponse, PostUpdate
from hw_2.storage import STORAGE
from hw_2.crud.post import PostCrud
from hw_2.utils.exeption import DBExeption


class DBService:


    @classmethod
    async def get_all_posts(cls) -> list[PostResponse]:
        """
        Возвращает список постов из БД
        :return: список постов
        """
        return await PostCrud.get_all()


    @classmethod
    async def get_post_by_id(
        cls,
        post_id: int,
    ) -> PostResponse:
        """
        Возвращает конкретный пост, найденный по id в БД
        :param post_id: Идентификатор поста в БД
        :return: конкретный пост
        """
        return await PostCrud.get_by_id(post_id=post_id)


    @classmethod
    async def add_post(
        cls,
        post: PostCreate,
    ) -> PostResponse:
        """
        Добавляет пост в БД
        :param post: конкретный пост
        :return: добавленный пост
        """
        return await PostCrud.add(post=post)


    @classmethod
    async def update_post(
        cls,
        post_id: int,
        post_update: PostUpdate,
    ) -> PostResponse:
        """
        Обновляет данные полученного поста
        :param post_create: новые данные поста, полученный от клиента
        :param post_response: конкретный пост, найденный в БД
        :return: обновленный пост
        """
        post = await PostCrud.get_by_id(post_id=post_id)

        return await PostCrud.update(
            post_update=post_update,
            post=post,
        )


    @classmethod
    async def del_post_by_id(
        cls,
        post_id: int,
    ) -> PostResponse:
        """
        Удаляет полученный пост из БД
        :param post: конкретный пост
        :return: удаленный пост
        """
        post = await PostCrud.get_by_id(post_id=post_id)

        return await PostCrud.delete(post=post)


    @classmethod
    async def clear_storage(cls) -> list:
        """
        Полностью очищает БД
        :return: Пустой список
        """
        return await PostCrud.clear()