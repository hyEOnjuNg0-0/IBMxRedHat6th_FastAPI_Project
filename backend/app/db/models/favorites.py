from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Favorite(Base):
    __tablename__ = "favorites"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), primary_key=True)
    cocktail_id: Mapped[int] = mapped_column(ForeignKey("cocktails.cocktail_id"), primary_key=True)

    user = relationship("User", back_populates="favorites")
    cocktail = relationship("Cocktail", back_populates="favorites")