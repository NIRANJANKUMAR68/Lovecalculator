from sqlalchemy import create_engine,Integer,Column,String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database
DATABASE_URL = "sqlite:///./love.db"

# Create Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
engine.connect()
# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base Class
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class Love(Base):
    __tablename__ = "love"

    id = Column(Integer, primary_key=True, index=True)
    name1 = Column(String)
    name2 = Column(String)
    percentage = Column(Integer)
Base.metadata.create_all(bind=engine)