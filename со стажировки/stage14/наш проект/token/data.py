from sqlalchemy import Integer, Column
from database import Base


class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)
    token_limit = Column(Integer)
    token_count = Column(Integer)
