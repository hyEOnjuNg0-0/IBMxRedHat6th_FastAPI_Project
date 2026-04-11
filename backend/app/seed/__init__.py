from app.db.database import SessionLocal
from app.seed.ingredients_seed import seed_ingredients
from app.seed.cocktails_seed import seed_cocktails
from app.seed.cocktail_ingredients_seed import seed_cocktail_ingredients
from app.db.models.cocktail_ingredients import CocktailIngredient


def seed_all():
    db = SessionLocal()

    try:
        # 이미 연결 테이블 데이터가 있으면 seed 안 함
        if db.query(CocktailIngredient).count() > 0:
            return

        # 1. 재료 먼저
        seed_ingredients(db)
        db.flush()

        # 2. 칵테일
        seed_cocktails(db)
        db.flush()

        # 3. 연결 테이블 마지막
        seed_cocktail_ingredients(db)

        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


# def seed_all():
#     db = SessionLocal()

#     try:
#         seed_ingredients(db)
#         seed_cocktails(db)
#         seed_cocktail_ingredients(db)

#         db.commit()

#     finally:
#         db.close()