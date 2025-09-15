from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import datetime
import uuid

from sqlalchemy_utils import UUIDType
from db.base_class import Base


class Post(Base):
    uid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    content = Column(String)
    owner_uid = Column(UUIDType, ForeignKey("user.uid", ondelete='CASCADE'))
    owner = relationship("User", back_populates="post")
