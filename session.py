from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://lenatester:Password1!@192.168.1.45:5432/test')

__session = sessionmaker(engine)

session: Session = __session()
