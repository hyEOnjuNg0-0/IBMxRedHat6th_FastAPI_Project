from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import CocktailIngredient, Ingredient
from fastapi import HTTPException

class CocktailIngredientCrud:
    # 특정 칵테일 모든 재료 정보 조회
    @staticmethod
    async def get_ingredients_by_cocktail_id(
        db: AsyncSession,
        cocktail_id: int
    ) -> list[Ingredient]:
        query = (
            select(Ingredient)
            .join(
                CocktailIngredient,
                CocktailIngredient.ingredient_id == Ingredient.ingredient_id
            )
            .where(CocktailIngredient.cocktail_id == cocktail_id)
        )

        result = await db.execute(query)
        return result.scalars().all()


    # 칵테일에 재료 추가
    @staticmethod
    async def create(
        db: AsyncSession,
        cocktail_id: int,
        ingredient_id: int) -> CocktailIngredient:
        # 중복 체크
        existing = await db.get(
            CocktailIngredient,
            {
                "cocktail_id": cocktail_id,
                "ingredient_id": ingredient_id
            }
        )

        if existing:
            raise HTTPException(status_code=409, detail="이미 해당 칵테일에 등록된 재료입니다")

        new_ingredient = CocktailIngredient(
            cocktail_id=cocktail_id,
            ingredient_id=ingredient_id
        )

        db.add(new_ingredient)
        await db.flush()
        return new_ingredient
    

    # 특정 칵테일 재료 제거
    @staticmethod
    async def delete(db: AsyncSession, cocktail_id: int, ingredient_id: int) -> CocktailIngredient | None:
        ingredient = await db.get(CocktailIngredient, 
                                  {"cocktail_id": cocktail_id, "ingredient_id": ingredient_id})

        if not ingredient:
            return None

        await db.delete(ingredient)
        await db.flush()
        return ingredient