from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from backend.database import Base


class CollegeCutoff(Base):

    __tablename__ = "college_cutoffs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    college_name = Column(
        String(255)
    )

    branch = Column(
        String(255)
    )

    category = Column(
        String(50)
    )

    cap1_cutoff = Column(
        Float
    )


class CollegeLocation(Base):

    __tablename__ = "college_locations"

    college_name = Column(
        String(255),
        primary_key=True
    )

    location = Column(
        String(100)
    )


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100)
    )

    email = Column(
        String(100),
        unique=True
    )

    password = Column(
        String(255)
    )

    role = Column(
        String(20),
        default="user"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    last_login = Column(
        DateTime,
        nullable=True
)

    is_active = Column(
        String(10),
        default="true"
)
    

class SearchHistory(Base):

    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer)

    percentage = Column(Float)

    category = Column(String(50))

    gender = Column(String(20))

    branch = Column(String(100))

    location = Column(String(100))

    searched_at = Column(DateTime)


class FavoriteCollege(Base):

    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer)

    college_name = Column(String(255))

    branch = Column(String(255))

    category = Column(String(50))

    cutoff = Column(Float)

    location = Column(String(255))

    saved_at = Column(DateTime)