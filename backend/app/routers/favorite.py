from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.scheme.cocktails import CocktailListRead
from app.services.favorite import FavoriteService
from app.core.auth import get_user_id

router = APIRouter(tags=["Favorite"])

'''즐겨찾기 추가'''
@router.post("/cocktails/{cocktail_id}/favorites", response_model=bool)
async def add_favorite(cocktail_id: int, user_id: int = Depends(get_user_id), db: AsyncSession = Depends(get_db)):
    return await FavoriteService.add_favorite(db, user_id, cocktail_id)

'''내 즐겨찾기 칵테일 목록 조회'''
@router.get("/users/me/favorites", response_model=list[CocktailListRead])
async def get_my_favorites(user_id: int = Depends(get_user_id), db: AsyncSession = Depends(get_db)):
    return await FavoriteService.get_my_favorites(db, user_id)
