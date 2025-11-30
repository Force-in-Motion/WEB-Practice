from typing import Annotated
from fastapi import APIRouter, Depends, status
from hw_2.schemas.comment import CommentCreate, CommentResponse, CommentUpdate
from hw_2.service.comm_sevice import CommentService
from hw_2.service.post_service import PostService
from hw_2.schemas.post import PostResponse

router = APIRouter(
    prefix="/posts/{post_id}/comments",
    tags=["Comments"],
)


@router.get("/", response_model=list[CommentResponse], status_code=status.HTTP_200_OK)
async def get_all_comments_from_post(
    post: Annotated[PostResponse, Depends(PostService.get_post_by_id)],
) -> list[CommentResponse]:
    """
    Обрабатывает запрос на получение списка всех комментариев конкретного поста
    :param post: конкретный пост, полученный через зависимость
    :return: Список всех комментариев поста
    """
    return await CommentService.get_all_comment(post=post)


@router.get(
    "/{comment_id}", response_model=CommentResponse, status_code=status.HTTP_200_OK
)
async def get_comment_by_id_from_post(
    post: Annotated[PostResponse, Depends(PostService.get_post_by_id)],
    comment_id: int,
) -> PostResponse:
    """
    Обрабатывает запрос на получение конкретного комментария поста
    :param post: конкретный пост, полученный через зависимость
    :param comment_id: идентификатор конкретного комментария
    :return: конкретный комментарий
    """
    return await CommentService.del_comment_by_id(
        comment_id=comment_id,
        post=post,
    )


@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment_from_post(
    post: Annotated[PostResponse, Depends(PostService.get_post_by_id)],
    comment: CommentCreate,
) -> CommentResponse:
    """
    Обрабатывает запрос на добавление нового комментария в пост
    param post: конкретный пост, полученный через зависимость
    param comment: комментарий, полученный от клиента
    :return: добавленный в пост комментарий
    """
    return await CommentService.add_comment(
        post=post,
        comment=comment,
    )


@router.put(
    "/{comment_id}", response_model=CommentResponse, status_code=status.HTTP_200_OK
)
async def update_comment_by_id_from_post(
    post: Annotated[PostResponse, Depends(PostService.get_post_by_id)],
    comment_id: int,
    comment_update: CommentUpdate,
) -> CommentResponse:
    """
    Обрабатывает запрос на обновление конкретного комментария в посте
    param post: конкретный пост, полученный через зависимость
    :return: Обновленный в посте комментарий
    """
    return await CommentService.update_comment(
        post=post,
        comment_id=comment_id,
        comment_update=comment_update,
    )


@router.delete("/", response_model=list, status_code=status.HTTP_200_OK)
async def clear_comments_from_post(
    post: Annotated[PostResponse, Depends(PostService.get_post_by_id)],
) -> list:
    """
    Полностью очищает комментарии в посте
    param post: конкретный пост, полученный через зависимость
    :return: Пустой писок
    """
    return await CommentService.clear_comments(post)


@router.delete(
    "/{comment_id}", response_model=CommentResponse, status_code=status.HTTP_200_OK
)
async def delete_comment_by_id_from_post(
    post: Annotated[PostResponse, Depends(PostService.get_post_by_id)], comment_id: int
) -> CommentResponse:
    """
    Обрабатывает запрос на удаление конкретного комментария из поста
    param post: конкретный пост, полученный через зависимость
    :return: Удаленный из поста комментарий
    """
    return await CommentService.del_comment_by_id(
        post=post,
        comment_id=comment_id,
    )
