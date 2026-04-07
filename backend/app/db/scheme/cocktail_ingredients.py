from pydantic import BaseModel

class CocktailIngredientCreate(BaseModel):
    ingredient_id: int
