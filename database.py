from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL="postgresql://postgres:test1234@localhost:5432/fluttermusicapp"
engin=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engin)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close



