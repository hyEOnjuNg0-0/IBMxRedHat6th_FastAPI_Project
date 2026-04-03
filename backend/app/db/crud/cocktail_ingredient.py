from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import CocktailIngredient, Ingredient
from app.db.scheme.cocktail_ingredients import CocktailIngredientCreate

class CocktailIngredientCrud:
    # 특정 칵테일 모든 재료 정보 조회
    @staticmethod
    async def get_ingredients_by_cocktail_id(db: AsyncSession, cocktail_id: int) -> list[Ingredient]:
        join = (select(Ingredient)
                .join(CocktailIngredient, CocktailIngredient.ingredient_id == Ingredient.id)
                .where(CocktailIngredient.cocktail_id == cocktail_id))
        result = await db.execute(join)
        return result.scalars().all()

    # 특정 칵테일 재료 추가
    @staticmethod
    async def create(db:AsyncSession, ingredient:CocktailIngredientCreate) -> CocktailIngredient:
        new_ingredient = CocktailIngredient(**ingredient.model_dump())
        db.add(new_ingredient)
        await db.flush()
        return new_ingredient
    
    # 특정 칵테일 재료 제거
    @staticmethod
    async def delete(db: AsyncSession, ingredient_id: int) -> CocktailIngredient | None:
        ingredient = await db.get(CocktailIngredient, ingredient_id)

        if not ingredient:
            return None

        await db.delete(ingredient)
        await db.flush()
        return ingredient