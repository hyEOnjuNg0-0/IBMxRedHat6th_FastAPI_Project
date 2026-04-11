from sqlalchemy.orm import Session
from app.db.models.cocktail_ingredients import CocktailIngredient

def seed_cocktail_ingredients(db: Session):
    if db.query(CocktailIngredient).count() > 0:
        return

    data = [
        # (cocktail_id, ingredient_id)
        CocktailIngredient(cocktail_id=1, ingredient_id=1),
        CocktailIngredient(cocktail_id=1, ingredient_id=2),
        CocktailIngredient(cocktail_id=1, ingredient_id=3),

        CocktailIngredient(cocktail_id=2, ingredient_id=4),
        CocktailIngredient(cocktail_id=2, ingredient_id=5),

        CocktailIngredient(cocktail_id=3, ingredient_id=6),
        CocktailIngredient(cocktail_id=3, ingredient_id=7),

        CocktailIngredient(cocktail_id=4, ingredient_id=8),
        CocktailIngredient(cocktail_id=4, ingredient_id=9),

        CocktailIngredient(cocktail_id=5, ingredient_id=10),
    ]

    db.add_all(data)