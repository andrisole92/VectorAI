from sqlalchemy import create_engine


# Generating Sessions
class Engine:
    # conn string
    db_string = "postgres://postgres:@localhost:5432/vector"
    # db_string = "postgres://postgres:postgrespassword@159.203.2.190:5432/postgres"

    # engine
    engine = create_engine(db_string)

    @staticmethod
    def get_engine():
        # new session
        return Engine.engine

