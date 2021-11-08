from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api import deps


router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_user_list(
        *,
        user_list: schemas.UserList = Depends(deps.get_user_list)):
    """
    Fetch user list.
    """
    return user_list
