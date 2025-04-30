from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    image: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    caption: Mapped[str] = mapped_column(String(120), nullable=False)
    location: Mapped[str] = mapped_column(String(120), nullable=False)
    tags: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "image": self.image,
            "caption": self.caption,
            "location": self.location,
            "tags": self.tags,
        }
    
class Likes(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    # user who liked
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    # post liked
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    # comment liked
    comment_id: Mapped[int] = mapped_column(ForeignKey("comments.id"))


    def serialize(self):
        return {
            "user_id": self.user_id,
            "post_id": self.post_id,
            "comment_id": self.comment_id
        }
    
class Comments(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    comment: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "comment": self.comment,
        }
    
class Shares(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))


    def serialize(self):
        return {
            "user_id": self.user_id,
            "post_id": self.post_id
        }
    
class bookmarks(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))


    def serialize(self):
        return {
            "user_id": self.user_id,
            "post_id": self.post_id
        }
