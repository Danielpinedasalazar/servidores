from typing import Iterable, List
from sqlalchemy.orm import Session
from . import models, schemas


def create_many_items(
    db: Session, payloads: Iterable[schemas.ItemCreate]
) -> List[models.Item]:
    items: list[models.Item] = []
    for p in payloads:
        item = models.Item(
            name=p.name,
            price=p.price,
            created_at=p.created_at,
        )
        db.add(item)
        items.append(item)
    db.commit()
    for i in items:
        db.refresh(i)
    return items


def list_items(db: Session) -> list[models.Item]:
    return db.query(models.Item).order_by(models.Item.id.asc()).all()
