from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Ingredient
from app.db.scheme.ingredients import IngredientCreate

class IngredientCrud:
    # 재료 추가
    @staticmethod
    async def create(db:AsyncSession, ingredient:IngredientCreate) -> Ingredient:
        new_ingredient = Ingredient(**ingredient.model_dump())
        db.add(new_ingredient)
        await db.flush()
        return new_ingredient
    
    # 재료 삭제
    @staticmethod
    async def delete(db: AsyncSession, ingredient_id: int) -> Ingredient | None:
        ingredient = await db.get(Ingredient, ingredient_id)

        if not ingredient:
            return None

        await db.delete(ingredient)
        await db.flush()
        return ingredient