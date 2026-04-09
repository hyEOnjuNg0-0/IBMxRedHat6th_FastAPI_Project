from sqlalchemy.orm import Session
from app.db.models.users import User

def seed_users(db: Session):
    if db.query(User).count() > 0:
        return

    users = [
        User(
            username="user1",
            email="user1@test.com",
            password="1234"
        ),
        User(
            username="user2",
            email="user2@test.com",
            password="1234"
        ),
        User(
            username="user3",
            email="user3@test.com",
            password="1234"
        ),
    ]

    db.add_all(users)