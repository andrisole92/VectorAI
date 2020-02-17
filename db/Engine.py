from sqlalchemy import create_engine


# Generating Sessions
class Engine:
    # conn string
    db_string = "postgres://postgres:@localhost:5432/vector"
    # engine
    engine = create_engine(db_string)

    @staticmethod
    def get_engine():
        # new session
        return Engine.engine

