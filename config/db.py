from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://사용자이름:비번@localhost:포트/hellofast")

meta = MetaData()
conn = engine.connect()