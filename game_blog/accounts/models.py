from datetime import datetime

from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, UUIDType

from ..database import Base

class User(Base):
    __tablename__= 'users'

    uid = Column(UUIDType, primary_key=True)
    creation_date = Column(DateTime(timezone=True), default=datetime.now)
    email = Column(EmailType)
    username = Column(String, unique=True)
    is_active = Column(Boolean, default=True)

    post = relationship('Post', back_populates='owner')