from typing import Annotated, Optional
from fastapi import APIRouter, Depends, status
from app.crud.user import Crud
from app.schemas.user import UserIn, UserOut


router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def get_all_users(is_active: bool = True) -> list[UserOut]:
    """
    Обрабатывает запрос на получение списка пользователей согласно условия
    :param is_active: Позволяет определить условие выдачи результата ( все пользователи / те, которые не активны )
    :return: Список пользователей согласно условию
    """
    return await Crud.get_all_records(is_active)


@router.get("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_out: Annotated[UserOut, Depends(Crud.get_record_by_id)],
) -> UserOut:
    """
    Обрабатывает запрос на получение конкретного пользователя по его id
    :param user_out: Схема пользователя для возврата клиенту, полученная Через зависимость
    :return: Конкретного пользователя
    """
    return user_out


@router.get("/by-name/{name}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user_by_name(
    user_out: Annotated[UserOut, Depends(Crud.get_record_by_name)],
) -> UserOut:
    """
    Обрабатывает запрос на получение конкретного пользователя по его name
    :param user_out: Схема пользователя для возврата клиенту, полученная Через зависимость
    :return: Конкретного пользователя
    """
    return user_out


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserIn) -> UserOut:
    """
    Обрабатывает запрос на добавление пользователя в БД
    :param user_out: Схема пользователя для возврата клиенту, полученная Через зависимость после добавления в БД
    :return: добавленного в БД пользователя
    """
    return await Crud.add_record(user_in=user_in)


@router.put("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_user_by_id(
    user_in: UserIn,
    user_out: Annotated[UserOut, Depends(Crud.get_record_by_id)],
) -> UserOut:
    """
    Обрабатывает запрос на обновление конкретного пользователя в БД
    :param user_in: Схема пользователя, полученная от клиента
    :param user_out: Схема пользователя для возврата клиенту, полученная Через зависимость после обновления в БД
    :return: Обновленного в БД пользователя
    """
    return await Crud.update_record(
        user_in=user_in,
        user_out=user_out,
    )


@router.delete("/", response_model=list, status_code=status.HTTP_200_OK)
async def clear_users(
    list_user_out: Annotated[list, Depends(Crud.clear_db)],
) -> list:
    """
    Полностью очищает БД
    :return: Список
    """
    return list_user_out


@router.delete("/{id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def delete_user_by_id(
    user_out: Annotated[UserOut, Depends(Crud.get_record_by_id)],
) -> UserOut:
    """
    Обрабатывает запрос на удаление конкретного пользователя из БД
    :param user_out: Схема пользователя для возврата клиенту, полученная Через зависимость после удаления из БД
    :return: Удаленную из БД книгу
    """
    return await Crud.del_record_by_id(user_out=user_out)
