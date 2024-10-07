from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# DATABASE_URL="postgresql://postgres:test1234@localhost:5432/fluttermusicapp"
DATABASE_URL="postgresql://render_example_q167_user:1YoSQ50RhpjigXrhXClvfrkGpc6ccBOT@dpg-cs1oh45ds78s73b7umb0-a.singapore-postgres.render.com/render_example_q167"
engin=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engin)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close



