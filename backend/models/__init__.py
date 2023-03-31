from database.connect_mysql import Base, engine


Base.metadata.create_all(bind=engine)
