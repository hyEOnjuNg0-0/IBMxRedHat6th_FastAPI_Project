from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Ingredient
from app.db.scheme.ingredients import IngredientCreate, IngredientUpdate
from app.db.crud import IngredientCrud
from fastapi import HTTPException

# crud는 db 쿼리, service는 비지니스 로직
class ingredientService:
    # 새 재료 등록
    @staticmethod
    async def create_ingredient(db:AsyncSession, ingredient:IngredientCreate) -> Ingredient:
        try:
            new_ingredient = await IngredientCrud.create(db, ingredient)
            await db.commit()
            await db.refresh(new_ingredient)
            return new_ingredient
        except Exception:
            await db.rollback()
            raise

    # 특정 재료 삭제
    @staticmethod
    async def delete_ingredient(db: AsyncSession, ingredient_id: int) -> Ingredient:
        ingredient = await IngredientCrud.delete(db, ingredient_id)

        if not ingredient:
            raise HTTPException(status_code=404, detail="존재하지 않는 재료")
        
        await db.commit()
        await db.refresh(ingredient)

        return ingredient

    