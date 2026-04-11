from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.db.crud.favorite import FavoriteCrud
from app.db.crud.cocktail import CocktailCrud
from app.db.models import Cocktail


class FavoriteService:
    # 즐겨찾기 추가
    @staticmethod
    async def add_favorite(db: AsyncSession, user_id: int, cocktail_id: int) -> bool:
        # 칵테일 존재 여부 확인
        cocktail = await CocktailCrud.get_by_id(db, cocktail_id)
        if not cocktail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="칵테일을 찾을 수 없습니다")

        # 이미 즐겨찾기 되어있는지 확인
        existing = await FavoriteCrud.get_by_user_and_cocktail(db, user_id, cocktail_id)
        if existing:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="이미 즐겨찾기에 추가된 칵테일입니다")

        try:
            await FavoriteCrud.create(db, user_id, cocktail_id)
            await db.commit()
            return True
        except Exception:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="즐겨찾기 추가에 실패했습니다")

    # 내 즐겨찾기 칵테일 목록 조회
    @staticmethod
    async def get_my_favorites(db: AsyncSession, user_id: int) -> list[Cocktail]:
        return await FavoriteCrud.get_cocktails_by_user_id(db, user_id)
