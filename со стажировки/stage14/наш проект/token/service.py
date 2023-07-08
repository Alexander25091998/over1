from data import Token
from sqlalchemy.orm import Session


def create_token(token_limit: int, db: Session):
    token = Token(token_limit=token_limit, token_count=0)
    db.add(token)
    db.commit()
    db.refresh(token)
    return token


def use(token_id: int, db: Session):
    token = db.query(Token).filter(Token.id == token_id).first()
    if token.token_count < token.token_limit:
        token.token_count = token.token_count + 1
        db.add(token)
        db.commit()
        db.refresh(token)
        return token
    else:
        return {
            'message': 'Лимит токена исчерпан'
        }


def get_all(db: Session):
    return db.query(Token).all()

