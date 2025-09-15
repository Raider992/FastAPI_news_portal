from datetime import datetime

from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from sqlalchemy.dialects.postgresql import UUID

import uuid


from ..postsapp.models import Post
from db.base_class import Base

class User(Base):

    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creation_date = Column(DateTime(timezone=True), default=datetime.now)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    token = Column(String(64), nullable=True)

    post = relationship('Post', back_populates='owner', cascade='all, delete-orphan')
