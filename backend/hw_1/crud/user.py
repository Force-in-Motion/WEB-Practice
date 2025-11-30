from app.schemas.user import UserOut, UserIn
from app.utils.exeption import DBExeption


class Crud:

    storage: list[UserOut] = []
    count: int = 1


    @classmethod
    async def check_username(cls, username: str) -> None:
        """
        Выбрасывает исключение в случае наличия в БД полученного имени пользователя
        :param username: Имя пользователя
        :return: None
        """
        user = next((u for u in cls.storage if u.username == username), None)

        if user:
            raise DBExeption.exist_name


    @classmethod
    async def get_all_records(cls, is_active: bool = True) -> list[UserOut]:
        """
        Возвращает список кнпользователей, хранящихся в БД в зависимости от условия
        :return: список кнпользователей, хранящихся в БД
        """
        if is_active:
            return cls.storage

        return [user for user in cls.storage if user.is_active == False]


    @classmethod
    async def get_record_by_id(cls, id: int) -> UserOut:
        """
        Возвращает Конкретного кнпользователя, найденного по id
        :param id: Идентификатор объекта в БД
        :return: Объект UserOut
        """
        user = next((user for user in cls.storage if user.id == id), None)

        if not user:
            raise DBExeption.not_found

        return user


    @classmethod
    async def get_record_by_name(cls, username: str) -> UserOut:
        """
        Возвращает ККонкретного кнпользователя, найденного по имени
        :param username: Имя объекта в БД
        :return: Объект UserOut
        """
        user = next((user for user in cls.storage if user.username == username), None)

        if not user:
            raise DBExeption.not_found

        return user


    @classmethod
    async def add_record(cls, user_in: UserIn) -> UserOut:
        """
        Создает новую запись в БД
        :param user_in: Объект UserIn, полученный от пользователя
        :return: Объект UserOut, созданный в БД
        """
        await cls.check_username(user_in.username)

        user_out: UserOut = UserOut(id=cls.count, **user_in.model_dump())

        cls.storage.append(user_out)

        cls.count += 1

        return user_out


    @classmethod
    async def update_record(
        cls,
        user_in: UserIn,
        user_out: UserOut,
    ) -> UserOut:
        """
        Обновляет Объект пользователя в БД
        :param user_in: Объект UserIn, полученный от пользователя
        :param user_out: Объект UserOut, предварительно найденный по id
        :return: Объект UserOut, обновленный в БД
        """
        for key, value in user_in.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(user_out, key, value)

        return user_out


    @classmethod
    async def del_record_by_id(cls, user_out: UserOut) -> UserOut:
        """
        Удаляет Объект пользователя из БД
        :param user_out: Объект UserOut, предварительно найденный по id
        :return: Объект UserOut, удаленный из БД
        """
        cls.storage.remove(user_out)

        return user_out


    @classmethod
    async def clear_db(cls) -> list[UserOut]:
        """
        Полностью очищает БД
        :return: Пустой список
        """
        cls.storage.clear()
        cls.count = 1
        return cls.storage
