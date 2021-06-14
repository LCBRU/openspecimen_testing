from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from pathlib import Path

Base = declarative_base()

DATABASE_PATH = r'sqlite:////home/richard/OpenSpecimenTest/db.sqlite'

class CollectionProtocol(Base):
    __tablename__ = 'collection_protocol'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), index=True)
    href = Column(String)
    completed = Column(Boolean(), default=False)


class Participant(Base):
    __tablename__ = 'participant'

    id = Column(Integer, primary_key=True)
    collection_protocol_id = Column(Integer, ForeignKey(CollectionProtocol.id))
    collection_protocol = relationship(CollectionProtocol)   
    ppid = Column(String(100))
    has_error = Column(Boolean(), default=False)
    completed = Column(Boolean(), default=False)


class Sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    participant_id = Column(Integer, ForeignKey(Participant.id))
    participant = relationship(Participant)
    href = Column(String(1000))
    name = Column(String(100))
    has_error = Column(Boolean(), default=False)
    completed = Column(Boolean(), default=False)


def init_database():

    existing = Path(DATABASE_PATH).exists()

    engine = create_engine(DATABASE_PATH)

    if not existing:
        Base.metadata.create_all(engine)

    return sessionmaker(bind=engine)()
