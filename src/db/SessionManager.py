from sqlalchemy.orm import sessionmaker


# Generating Sessions
from src.db import Engine


class SessionManager:
    # session factory
    Session = sessionmaker(bind=Engine.get_engine())

    @staticmethod
    def get_session():
        # new session
        return SessionManager.Session()


