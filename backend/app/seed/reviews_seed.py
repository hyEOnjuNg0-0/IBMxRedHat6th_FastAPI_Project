from sqlalchemy.orm import Session
from app.db.models.reviews import Review

def seed_reviews(db: Session):
    if db.query(Review).count() > 0:
        return

    data = [
        Review(
            cocktail_id=1,
            user_id=1,
            title="상큼하고 시원함",
            description="민트 향이 너무 좋고 여름에 딱이에요"
        ),
        Review(
            cocktail_id=1,
            user_id=2,
            title="괜찮은데 살짝 셔요",
            description="라임이 좀 강한 느낌"
        ),
        Review(
            cocktail_id=2,
            user_id=1,
            title="깔끔한 맛",
            description="드라이해서 좋았어요"
        ),
        Review(
            cocktail_id=3,
            user_id=3,
            title="데킬라 최고",
            description="마가리타는 역시 최고"
        ),
        Review(
            cocktail_id=4,
            user_id=2,
            title="클래식 그 자체",
            description="올드패션드는 항상 옳다"
        ),
    ]

    db.add_all(data)