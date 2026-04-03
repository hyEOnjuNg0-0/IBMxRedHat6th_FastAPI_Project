from app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func, ForeignKey
from typing import Optional
from app.db.models.users import User
from app.db.models.cocktails import Cocktail


class Review(Base):
    __tablename__="reviews"
    review_id:Mapped[int]=mapped_column(primary_key=True, index=True)
    cocktail_id:Mapped[int]=mapped_column(ForeignKey("cocktails.cocktail_id"), nullable=False, index=True)
    title:Mapped[str]=mapped_column(String(255), nullable=False)
    description:Mapped[Optional[str]]=mapped_column(String(500), nullable=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.user_id"), nullable=False, index=True)
    created_at:Mapped[datetime]=mapped_column(
        TIMESTAMP, server_default=func.now(), nullable=False
    )

    user = relationship("User", back_populates="reviews")
    cocktail = relationship("Cocktail", back_populates="reviews")