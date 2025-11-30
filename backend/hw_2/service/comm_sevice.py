from hw_2.schemas.post import PostResponse
from hw_2.schemas.comment import CommentCreate, CommentResponse, CommentUpdate
from hw_2.crud.comment import CommentCrud


class CommentService:

    @classmethod
    async def get_all_comment(
        cls,
        post: PostResponse,
    ) -> list[CommentResponse]:
        """
        Возвращает список комментариев поста
        :return: список комментариев
        """
        CommentCrud.post = post

        return await CommentCrud.get_all()

    @classmethod
    async def get_comment_by_id(
        cls,
        post: PostResponse,
        comment_id: int,
    ) -> CommentResponse:
        """
        Возвращает конкретный комментарий, найденный по id в полученном посте
        :param comment_id: Идентификатор комментария в посте
        :return: конкретный комментарий
        """
        CommentCrud.post = post

        return await CommentCrud.get_by_id(comment_id=comment_id)

    @classmethod
    async def add_comment(
        cls, post: PostResponse,
        comment: CommentCreate,
    ) -> CommentResponse:
        """
        Добавляет комментария в полученный пост
        :param post: конкретный пост
        :return: добавленный комментарий
        """
        CommentCrud.post = post

        return await CommentCrud.add(comment=comment)

    @classmethod
    async def update_comment(
        cls,
        comment_id: int,
        post: PostResponse,
        comment_update: CommentUpdate,
    ) -> CommentResponse:
        """
        Обновляет данные комментария полученного поста
        :param comment_id: идентификатор комментария
        :param post: конкретный пост
        :param comment_update: новые данные комментария, полученные от клиента
        :return: обновленный комментарий
        """
        CommentCrud.post = post

        comment = await CommentCrud.get_by_id(comment_id=comment_id)

        return await CommentCrud.update(
            comment_update=comment_update,
            comment=comment,
        )

    @classmethod
    async def del_comment_by_id(
        cls,
        comment_id: int,
        post: PostResponse,
    ) -> PostResponse:
        """
        Удаляет конкретный комментарий из поста, найденный по id
        :param comment_id: идентификатор комментария
        :param post: конкретный пост
        :return: удаленный комментарий
        """
        CommentCrud.post = post

        comment = await CommentCrud.get_by_id(comment_id=comment_id)

        return await CommentCrud.delete(comment=comment)

    @classmethod
    async def clear_comments(
        cls,
        post: PostResponse,
    ) -> list:
        """
        Полностью очищает Пост от комментариев
        :return: Пустой список
        """
        CommentCrud.post = post

        return await CommentCrud.clear()
