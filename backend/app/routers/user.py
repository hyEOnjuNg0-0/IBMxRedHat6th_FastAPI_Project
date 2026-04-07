from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.scheme.users import UserRead, UserLogin, UserCreate, UserUpdate
from app.services import UserService
from app.core.auth import set_auth_cookies, get_user_id

router = APIRouter(prefix="/users", tags=["User"])

'''회원 가입'''
@router.post("", response_model=UserRead)
async def signup(user:UserCreate, db: AsyncSession=Depends(get_db)):
    db_user = await UserService.signup(db, user)
    return db_user

'''로그인(JWT 토큰 발급)'''
@router.post("/login", response_model=UserRead)
async def login(user:UserLogin, response:Response, db: AsyncSession=Depends(get_db)):
    result = await UserService.login(db, user)
    db_user, access_token, refresh_token = result
    set_auth_cookies(response, access_token, refresh_token)
    return db_user

'''내 정보 조회'''
@router.get("/me", response_model=UserRead)
async def get_user(user_id:int = Depends(get_user_id), db: AsyncSession = Depends(get_db)):
    return await UserService.get_user_by_id(db, user_id)

'''내 정보 수정'''
@router.put("/me", response_model=UserRead)
async def update_user(user:UserUpdate, user_id:int = Depends(get_user_id), db: AsyncSession = Depends(get_db)):
    return await UserService.update_user(db, user_id, user)

'''JWT 토큰 쿠키 삭제'''
@router.post("/logout", response_model=bool)
async def logout(response:Response):
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    return True