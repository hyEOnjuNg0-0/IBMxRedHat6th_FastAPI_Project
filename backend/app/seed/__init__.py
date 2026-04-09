from app.db.database import SessionLocal
from app.seed.users_seed import seed_users
from app.seed.ingredients_seed import seed_ingredients
from app.seed.cocktails_seed import seed_cocktails
from app.seed.cocktail_ingredients_seed import seed_cocktail_ingredients
from app.seed.favorites_seed import seed_favorites
from app.seed.reviews_seed import seed_reviews

def seed_all():
    db = SessionLocal()

    try:
        seed_users(db)
        seed_ingredients(db)
        seed_cocktails(db)
        seed_cocktail_ingredients(db)
        seed_favorites(db)
        seed_reviews(db)

        db.commit()

    finally:
        db.close()