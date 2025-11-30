from fastapi import HTTPException, status


class DBExeption(Exception):


    not_found = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Record with this data not found",
    )

    exist_name = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Record with this name already exist",
    )

    db_error = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Error Data Base",
    )