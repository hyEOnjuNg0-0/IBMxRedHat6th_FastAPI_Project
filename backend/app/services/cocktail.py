from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Cocktail
from app.db.scheme.cocktails import CocktailCreate, CocktailUpdate
from app.db.crud import CocktailCrud
from fastapi import HTTPException

# crud는 db 쿼리, service는 비지니스 로직
class CocktailService:
    # 전체 칵테일 목록 조회
    @staticmethod
    async def get_all_cocktails(db: AsyncSession) -> list[Cocktail]:
        cocktails = await CocktailCrud.get_all(db)

        if not cocktails:
            return []

        return cocktails
    
    # 특정 칵테일 조회
    @staticmethod
    async def get_cocktail(db:AsyncSession, cocktail_id:int) -> Cocktail:
        cocktail = await CocktailCrud.get_by_id(db, cocktail_id)
        if not cocktail:
            raise HTTPException(status_code=404, detail="존재하지 않는 칵테일")
        return cocktail
    
    # 새 칵테일 등록
    @staticmethod
    async def create_cocktail(db:AsyncSession, cocktail:CocktailCreate) -> Cocktail:
        try:
            new_cocktail = await CocktailCrud.create(db, cocktail)
            await db.commit()
            await db.refresh(new_cocktail)
            return new_cocktail
        except Exception:
            await db.rollback()
            raise

    # 특정 칵테일 정보 수정
    @staticmethod
    async def update_cocktail(db: AsyncSession, cocktail_id: int, cocktail_data: CocktailUpdate) -> Cocktail:
        cocktail = await CocktailCrud.update(db, cocktail_id, cocktail_data)

        if not cocktail:
            raise HTTPException(status_code=404, detail="존재하지 않는 칵테일")
        
        await db.commit()
        await db.refresh(cocktail)

        return cocktail

    # 특정 칵테일 삭제
    @staticmethod
    async def delete_cocktail(db: AsyncSession, cocktail_id: int) -> Cocktail:
        cocktail = await CocktailCrud.delete(db, cocktail_id)

        if not cocktail:
            raise HTTPException(status_code=404, detail="존재하지 않는 칵테일")
        
        await db.commit()

    