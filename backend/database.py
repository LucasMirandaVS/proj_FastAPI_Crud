from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# motor do banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()