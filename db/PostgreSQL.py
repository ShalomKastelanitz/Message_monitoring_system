from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base,relationship
from datetime import datetime

Base = declarative_base()

class Email(Base):
    __tablename__ = 'emails'
    id = Column(String, primary_key=True)
    email_address = Column(String, nullable=False)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    location = Column(JSON)
    device_info = Column(JSON)

    # קשרים לטבלאות התוכן החשוד
    hostage_content = relationship("SuspiciousHostageContent", back_populates="email")
    explosive_content = relationship("SuspiciousExplosiveContent", back_populates="email")

class SuspiciousHostageContent(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = Column(Integer, primary_key=True)
    email_id = Column(String, ForeignKey('emails.id'))
    suspicious_sentence = Column(Text)
    detected_at = Column(DateTime, default=datetime.utcnow)
    email = relationship("Email", back_populates="hostage_content")

class SuspiciousExplosiveContent(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = Column(Integer, primary_key=True)
    email_id = Column(String, ForeignKey('emails.id'))
    suspicious_sentence = Column(Text)
    detected_at = Column(DateTime, default=datetime.utcnow)
    email = relationship("Email", back_populates="explosive_content")

# הגדרת החיבור למסד הנתונים
engine = create_engine('postgresql://postgres:1234@localhost:5432/email_db4')
Base.metadata.create_all(engine)

# יצירת Session
Session = sessionmaker(bind=engine)
session = Session()

