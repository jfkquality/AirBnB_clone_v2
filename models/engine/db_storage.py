from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

# imports from model Classes
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)


        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):  #JFK added =none
        dic = {}
        if cls is None:
            query = self.__session.query(
                User,
                State,
                City,
                Amenity,
                Place,
                Review
            )
        else:
            query = self.__session.query(cls)
        for a in query:
            key = "{}.{}".format(type(a).__name__, a.id)  # JFK: removed <> around {}
            value = a
            dic[key] = value
        return dic

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sessionista = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        Session = scoped_session(sessionista)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute."""
        self.__session.remove()
