from sqlalchemy.orm import Session
from app.db.models.ingredients import Ingredient

def seed_ingredients(db: Session):
    if db.query(Ingredient).count() > 0:
        return

    data = [
        Ingredient(ingredient_name="Mint"),
        Ingredient(ingredient_name="Lime"),
        Ingredient(ingredient_name="Soda"),
        Ingredient(ingredient_name="Gin"),
        Ingredient(ingredient_name="Dry Vermouth"),
        Ingredient(ingredient_name="Tequila"),
        Ingredient(ingredient_name="Triple Sec"),
        Ingredient(ingredient_name="Whiskey"),
        Ingredient(ingredient_name="Sugar"),
        Ingredient(ingredient_name="Cranberry Juice"),
    ]

    db.add_all(data)