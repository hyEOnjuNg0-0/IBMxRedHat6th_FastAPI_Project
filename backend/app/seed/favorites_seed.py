from sqlalchemy.orm import Session
from app.db.models.favorites import Favorite

def seed_favorites(db: Session):
    if db.query(Favorite).count() > 0:
        return

    data = [
        Favorite(user_id=1, cocktail_id=1),
        Favorite(user_id=1, cocktail_id=2),
        Favorite(user_id=1, cocktail_id=3),

        Favorite(user_id=2, cocktail_id=1),
        Favorite(user_id=2, cocktail_id=4),

        Favorite(user_id=3, cocktail_id=2),
        Favorite(user_id=3, cocktail_id=5),
    ]

    db.add_all(data)