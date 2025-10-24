#!/usr/bin/python3

"""
Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    connection_url = (
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}"
    )
    engine = create_engine(
        connection_url,
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()
