from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class CocktailIngredient(Base):
    __tablename__ = "cocktail_ingredients"
    cocktailIngredient_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cocktail_id: Mapped[int] = mapped_column(ForeignKey("cocktails.cocktail_id"))
    ingredient_id: Mapped[int] = mapped_column(ForeignKey("ingredients.ingredient_id"))

    cocktail = relationship("Cocktail", back_populates="cocktail_ingredients")
    ingredient = relationship("Ingredient", back_populates="cocktail_ingredients")