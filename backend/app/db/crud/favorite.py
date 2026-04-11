from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Favorite, Cocktail
from fastapi import HTTPException

class FavoriteCrud:
    # 특정 즐겨찾기 조회 (존재 여부 확인용)
    @staticmethod
    async def get_by_user_and_cocktail(db: AsyncSession, user_id: int, cocktail_id: int) -> Favorite | None:
        result = await db.execute(
            select(Favorite).filter(Favorite.user_id == user_id, Favorite.cocktail_id == cocktail_id)
        )
        return result.scalar_one_or_none()

    # 즐겨찾기 추가
    @staticmethod
    async def create(db: AsyncSession, user_id: int, cocktail_id: int) -> Favorite:
        # 중복 체크
        existing = await db.get(Favorite,
            {
                "user_id": user_id,
                "cocktail_id": cocktail_id,
            }
        )

        if existing:
            raise HTTPException(status_code=409, detail="이미 즐겨찾기 된 칵테일입니다")
        
        new_favorite = Favorite(user_id=user_id, cocktail_id=cocktail_id)
        db.add(new_favorite)
        await db.flush()
        return new_favorite

    # 즐겨찾기 삭제
    @staticmethod
    async def delete(db: AsyncSession, favorite: Favorite) -> None:
        if not favorite:
            return None
        
        await db.delete(favorite)
        await db.flush()

    # 사용자 별 즐겨찾기 칵테일 목록 조회
    @staticmethod
    async def get_favorites_by_user_id(db: AsyncSession, user_id: int) -> list[Cocktail]:
        result = await db.execute(
            select(Cocktail)
            .join(Favorite, Favorite.cocktail_id == Cocktail.cocktail_id)
            .filter(Favorite.user_id == user_id)
        )
        return result.scalars().all()
