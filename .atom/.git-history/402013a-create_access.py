from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import models
from os.path import expanduser
home = expanduser("~")

db_engine = create_engine('sqlite:////' + home + '/.portal.db')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=db_engine))
base_db = declarative_base()
base_db.query = db_session.query_property()

access = models.Access('All Access', 'inf.interns')
db_session.add(access)
db_session.commit()

print models.Access.query.all()

db_session.remove()