from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func

Base = declarative_base()

class Folder(Base):
    __tablename__ = "folders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # parent folder UUID (no foreign key restriction)
    parent_id = Column(UUID(as_uuid=True), nullable=False)


class File(Base):
    __tablename__ = "files"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # parent folder UUID (no foreign key restriction)
    parent_id = Column(UUID(as_uuid=True), nullable=False)
