from app.db.database import SessionLocal
from app.seed.ingredients_seed import seed_ingredients
from app.seed.cocktails_seed import seed_cocktails
from app.seed.cocktail_ingredients_seed import seed_cocktail_ingredients


def seed_all():
    db = SessionLocal()

    try:
        seed_ingredients(db)
        seed_cocktails(db)
        seed_cocktail_ingredients(db)

        db.commit()

    finally:
        db.close()