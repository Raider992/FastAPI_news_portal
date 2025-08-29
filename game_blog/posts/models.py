from datetime import datetime

from django.forms import IntegerField
from pygments.lexer import default
from sqlalchemy import Boolean, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, UUIDType

from ..database import Base

class Post(Base):
    __tablename__ = 'posts'

    uid = Column(UUIDType, primary_key=True)
    creation_date = Column(DateTime(timezone=True), default=datetime.now)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    owner_id = Column(UUIDType, ForeignKey('users.uid'))
    owner = relationship('User', back_populates='post')