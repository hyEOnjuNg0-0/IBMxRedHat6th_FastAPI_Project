from sqlalchemy.orm import Session
from app.db.models.cocktails import Cocktail

def seed_cocktails(db: Session):
    if db.query(Cocktail).count() > 0:
        return

    cocktails = [
        Cocktail(
            cocktail_name="Mojito",
            cocktail_base="Rum",
            cocktail_detail="민트와 라임이 들어간 상큼하고 시원한 칵테일"
        ),
        Cocktail(
            cocktail_name="Martini",
            cocktail_base="Gin",
            cocktail_detail="드라이하고 깔끔한 클래식 칵테일"
        ),
        Cocktail(
            cocktail_name="Margarita",
            cocktail_base="Tequila",
            cocktail_detail="데킬라와 트리플 섹으로 만드는 상큼한 칵테일"
        ),
        Cocktail(
            cocktail_name="Old Fashioned",
            cocktail_base="Whiskey",
            cocktail_detail="클래식한 올드패션드, 설탕과 비터로 맛을 낸 칵테일"
        ),
        Cocktail(
            cocktail_name="Cosmopolitan",
            cocktail_base="Vodka",
            cocktail_detail="크랜베리 주스와 라임으로 상큼하게 즐기는 칵테일"
        ),
    ]

    db.add_all(cocktails)