from sqlalchemy import Float, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from init import db


class Cupcake(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    flavor: Mapped[str] = mapped_column(Text, nullable=False)
    size: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)
    image: Mapped[str] = mapped_column(Text, default="https://tinyurl.com/demo-cupcake")

    def __init__(self, **kwargs) -> None:
        super(Cupcake, self).__init__(**kwargs)

    def serialize(self):
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }
