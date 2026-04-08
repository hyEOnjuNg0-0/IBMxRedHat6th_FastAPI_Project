from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class CocktailIngredient(Base):
    __tablename__ = "cocktail_ingredients"
    cocktail_id: Mapped[int] = mapped_column(ForeignKey("cocktails.cocktail_id"), primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.ingredient_id"), primary_key=True)

    cocktail = relationship("Cocktail", back_populates="cocktail_ingredients")
    ingredient = relationship("Ingredient", back_populates="cocktail_ingredients")