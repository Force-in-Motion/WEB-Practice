from typing import Annotated
from fastapi import APIRouter, Depends, status
from backend.hw_2.service.post_service import PostService
from hw_2.schemas.post import PostResponse

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=list[PostResponse], status_code=status.HTTP_200_OK)
async def get_all_posts(
    posts: Annotated[list[PostResponse], Depends(PostService.get_all_posts)],
) -> list[PostResponse]:
    """
    Обрабатывает запрос на получение списка всех постов из БД
    :return: Список всех постов из БД 
    """
    return posts


@router.get("/{id}", response_model=PostResponse, status_code=status.HTTP_200_OK)
async def get_post_by_id(
    post: Annotated[PostResponse, Depends(PostService.get_post_by_id)],
) -> PostResponse:
    """
    Обрабатывает запрос на получение конкретного поста по его id
    :param post: конкретный пост, полученный через зависимость
    :return: онкретный пост
    """
    return post


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: Annotated[PostResponse, Depends(PostService.add_post)],
) -> PostResponse:
    """
    Обрабатывает запрос на добавление поста в БД
    :param post: добаленный пост, созданный через зависимость
    :return: добавленный в БД пост
    """
    return post


@router.put("/{id}", response_model=PostResponse, status_code=status.HTTP_200_OK)
async def update_post_by_id(
    post: Annotated[PostResponse, Depends(PostService.update_post)],
) -> PostResponse:
    """
    Обрабатывает запрос на обновление конкретного поста в БД
    :param post: конкретный пост, обновленный через зависимость
    :return: Обновленный в БД пост
    """
    return post


@router.delete("/", response_model=list, status_code=status.HTTP_200_OK)
async def clear_posts(
    posts: Annotated[list, Depends(PostService.clear_storage)],
) -> list:
    """
    Полностью очищает БД
    :return: Список
    """
    return posts


@router.delete("/{id}", response_model=PostResponse, status_code=status.HTTP_200_OK)
async def delete_book_by_id(
    post: Annotated[PostResponse, Depends(PostService.del_post_by_id)],
) -> PostResponse:
    """
    Обрабатывает запрос на удаление конкретного поста из БД
    :param post: онкретный пост, удаленный через зависимость
    :return: Удаленный из БД пост
    """
    return post
