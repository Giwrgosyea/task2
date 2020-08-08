from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine, event


import os.path
# Paths
DIRNAME = os.path.dirname(__file__)
ROOT_PATH = os.path.normpath(os.path.join(DIRNAME))
STATIC_PATH = os.path.join(DIRNAME, 'static')
TEMPLATE_PATH = os.path.join(DIRNAME, 'templates')
# ConfigDB
CONFIGDB_PATH = "%s/deploy/requests.db" % (ROOT_PATH,)
print(CONFIGDB_PATH)
CONFIGDB_ENGINE = "sqlite:///%s" % (CONFIGDB_PATH,)
# import base64
# import uuid
# COOKIE_SECRET = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
COOKIE_SECRET = b'xyRTvZpRSUyk8/9/McQAvsQPB4Rqv0w9mBtIpH9lf1o='


DEBUG = True
ENGINE = create_engine(CONFIGDB_ENGINE, pool_recycle=6000)

def on_connect(conn, record):
	conn.execute('pragma foreign_keys=ON')



event.listen(ENGINE, 'connect', on_connect)
SESSION_FACTORY = sessionmaker(autoflush=True,bind=ENGINE,expire_on_commit=False)
Session = scoped_session(SESSION_FACTORY)
Base = declarative_base()



class TblReqs(Base):
    __tablename__ = 'request'
    
    id = Column(Integer, primary_key = True)
    request = Column(String(255))
    time = Column(String(255))

  


Base.metadata.create_all(ENGINE)