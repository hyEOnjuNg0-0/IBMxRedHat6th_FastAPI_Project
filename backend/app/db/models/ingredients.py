from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func
from typing import Optional

#테이블 생성되는 작업
#orm타입힌트 -> 새로운 타입 힌트방식 -> Mapped => 각필드의 특정타입을 좀 더 명확히 정의가능
class Ingredient(Base):
    __tablename__="ingredients"

    ingredient_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ingredient_name: Mapped[str] =mapped_column(String(40), nullable=False)

    cocktail_ingredients = relationship("CocktailIngredient",back_populates="ingredient",cascade="all, delete")