from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class CocktailIngredient(Base):
    __tablename__ = "cocktail_ingredients"

    cocktail_id: Mapped[int] = mapped_column(
        ForeignKey("cocktails.cocktail_id"), primary_key=True
    )
    ingredient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredients.ingredients_id"), primary_key=True
    )