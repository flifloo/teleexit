from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from bot import config


db = config.get("db")
args = {"pool_pre_ping": True, "pool_recycle": 3600}
if not db.startswith("sqlite:"):
    args.update({"pool_size": 0, "max_overflow": -1})
engine = create_engine(db, **args)
Session = sessionmaker(bind=engine)
Base = declarative_base()
from db.User import User
Base.metadata.create_all(engine)
